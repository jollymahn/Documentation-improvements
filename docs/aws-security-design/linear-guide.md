# Securing Applications in AWS — Deployment Guide

A linear, step-by-step guide to deploying Palo Alto Networks VM-Series firewalls on AWS using the centralized security VPC architecture. Covers prerequisites, Panorama or SCM management deployment, GWLB-based inspection, and traffic flow configuration.

> **Source:** Based on the Palo Alto Networks Reference Architecture — *Securing Applications in AWS: Design Guide* and *Panorama on AWS: Deployment Guide*

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Panorama Deployment](#panorama-deployment)
3. [Security VPC and GWLB](#security-vpc-and-gwlb)
4. [Traffic Flow Configuration](#traffic-flow-configuration)
5. [Verification](#verification)

---

## Prerequisites

Complete all items before beginning the deployment. The checklist is divided into four categories: common licensing, Panorama management path, SCM management path, and AWS account readiness. Complete the common items first, then follow the path for your chosen management platform.

### Common — Licensing & Certificates

These steps are required regardless of whether you manage firewalls with Panorama or Strata Cloud Manager.

1. [ ] [**Software NGFW Credit Pool**](#1-activate-software-ngfw-credits) — activated and funded
2. [ ] [**Deployment Profile**](#2-create-a-deployment-profile) — created with auth code, vCPU, and subscription selections
3. [ ] [**Auth Code**](#3-obtain-the-auth-code) — copied from deployment profile for bootstrap definitions
4. [ ] [**Auto-Registration PIN**](#4-generate-auto-registration-pin) — PIN ID and PIN Value generated for device certificates

### Panorama Management Path

Complete these steps if you are using Panorama to manage your VM-Series firewalls.

5. [ ] [**Licensing API Key**](#5-set-the-licensing-api-key-on-panorama) — set on Panorama for automatic license deactivation
6. [ ] [**Panorama Deployment Mode**](#6-verify-panorama-deployment-mode) — Panorama must be in Panorama mode for logging
7. [ ] [**Device Group**](#7-create-a-device-group-on-panorama) — created on Panorama
8. [ ] [**Template Stack**](#8-create-a-template-stack-on-panorama) — created on Panorama
9. [ ] [**Backhaul Connectivity**](#9-establish-backhaul-connectivity-to-panorama) — Direct Connect, VPN, TGW, or VPC peering established
10. [ ] [**Panorama Security Groups**](#10-configure-panorama-security-groups) — ports 3978, 28443, 443, 22 configured

### SCM Management Path

Complete these steps if you are using Strata Cloud Manager to manage your VM-Series firewalls.

11. [ ] [**Strata Cloud Manager (SCM)**](#11-activate-strata-cloud-manager) — provisioned with NGFW Management flag enabled
12. [ ] [**Strata Logging Service (SLS)**](#12-activate-strata-logging-service) — provisioned for centralized log collection

### AWS Account & Environment Readiness

13. [ ] [**AWS Account & IAM**](#13-aws-account-and-iam-prerequisites) — console and CLI access with sufficient permissions
14. [ ] [**Deployment IAM Account**](#14-create-a-deployment-iam-account) — programmatic access for Terraform provisioning
15. [ ] [**AWS Marketplace Subscription**](#15-accept-the-aws-marketplace-subscription) — accepted for your license model (BYOL or PAYG)
16. [ ] [**VM-Series AMI**](#16-discover-the-vm-series-ami) — identified for your target region
17. [ ] [**Network Connectivity**](#17-verify-network-connectivity) — management interface can reach Panorama and licensing servers
18. [ ] [**Deployment Environment**](#18-set-up-the-deployment-environment) — Terraform, Git, AWS CLI installed
19. [ ] [**Remote State Backend**](#19-configure-remote-state-backend) — S3 bucket and DynamoDB table for Terraform state

---

### 1. Activate Software NGFW Credits

> **Palo Alto Docs:** [Activate Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-credits)

Before creating deployment profiles or licensing firewalls, you need an active credit pool.

1. Log in to the [Palo Alto Networks Customer Support Portal](https://support.paloaltonetworks.com).
2. Navigate to **Assets > Software NGFW Credits**.
3. Locate your credit pool authorization code (provided in your purchase order).
4. Click **Activate** and enter the auth code to fund the credit pool.
5. Verify the credit pool shows available credits for your desired VM-Series model and subscription tier.

> **Note:** Credit pools are shared across your account. Each firewall deployment consumes credits based on the vCPU count and subscriptions defined in the deployment profile.

### 2. Create a Deployment Profile

> **Palo Alto Docs:** [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) | [Manage a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/manage-a-deployment-profile)

The deployment profile defines the firewall model, vCPU allocation, and subscriptions that each bootstrapped firewall will receive.

1. In the Customer Support Portal, navigate to **Assets > Software NGFW Credits**.
2. Select your credit pool and click **Create Deployment Profile**.
3. Configure the profile:
   - **Profile Name** — descriptive name (e.g., `aws-gwlb-prod`)
   - **Firewall Model** — select the VM-Series model (e.g., VM-300, VM-500)
   - **vCPU Count** — number of vCPUs to allocate
   - **Subscriptions** — select Threat Prevention, WildFire, URL Filtering, DNS Security, etc.
   - **Token Count** — number of firewalls this profile can license (set based on expected fleet size)
4. Click **Create** to generate the deployment profile.
5. Note the **auth code** generated for this profile — you will need it for the bootstrap definition on Panorama.

> **Note:** Deployment profiles are defined by **licensing tier and vCPU count**, not by region, cloud, or individual firewall. Multiple firewalls with the same licensing requirements and vCPU allocation can share a single deployment profile. Group profiles by function and vCPU count (e.g., one profile for all 4-vCPU inspection firewalls, another for 8-vCPU firewalls with different subscriptions).

### 3. Obtain the Auth Code

> **Palo Alto Docs:** [Manage a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/manage-a-deployment-profile)

The auth code links the deployment profile to the licensing plugin on Panorama.

1. In the Customer Support Portal, navigate to **Assets > Software NGFW Credits > Deployment Profiles**.
2. Locate the deployment profile you created in the previous step.
3. Copy the **Auth Code** (format: `D1234567`).
4. This auth code is used when creating the Bootstrap Definition in Panorama (**Panorama > SW Firewall License > Bootstrap Definitions**).

### 4. Generate Auto-Registration PIN

> **Palo Alto Docs:** [Install a Device Certificate on the VM-Series Firewall](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/install-a-device-certificate-on-the-vm-series-firewall)

The PIN ID and PIN Value allow the VM-Series firewall to automatically pull a device certificate from the Palo Alto Networks licensing server during bootstrap.

1. Log in to the [Customer Support Portal](https://support.paloaltonetworks.com).
2. Navigate to **Products > VM-Series Auth-Codes** (or **Assets > VM-Series Deployment**).
3. Click **Generate OTP** (One-Time Password) or **Create Registration PIN**.
4. The portal generates two values:
   - **PIN ID** — a UUID format string (e.g., `81a75f2a-4de0-4f0e-959f-f31b5df06814`)
   - **PIN Value** — a hex string (e.g., `7059943c5565454db6b83cdcd305f338`)
5. Copy both values. These are used in bootstrap parameters as:
   - `vm-series-auto-registration-pin-id`
   - `vm-series-auto-registration-pin-value`

> **Note:** Without a valid PIN, the firewall cannot fetch a device certificate and will fail to authenticate with the licensing infrastructure.

### 5. Set the Licensing API Key on Panorama

> **Panorama only** | **Palo Alto Docs:** [Install a License Deactivation API Key](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/licensing-api/install-a-license-deactivation-api-key)

The licensing API key allows Panorama to communicate with the Palo Alto Networks licensing server for automatic license allocation and deactivation.

1. Obtain the API key from the [Customer Support Portal](https://support.paloaltonetworks.com) under **Assets > Licensing API**.
2. SSH into Panorama and run:
   ```
   request license api-key set key <key>
   ```
3. Verify the key is set:
   ```
   request license api-key show
   ```

> **Note:** This key is required for the Panorama SW Firewall License plugin. Without it, the licensing plugin cannot allocate or reclaim licenses from the credit pool.

### 6. Verify Panorama Deployment Mode

> **Panorama only**

Panorama must be running in **Panorama mode** to handle both policy management and log collection from managed firewalls. If Panorama is in Management Only mode, it will not collect logs.

*Detailed instructions to follow.*

### 7. Create a Device Group on Panorama

> **Panorama only** | **Palo Alto Docs:** [Manage Device Groups](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-device-groups)

The Device Group holds security policies, objects, and rules that are pushed to managed firewalls.

1. Log in to Panorama.
2. Navigate to **Panorama > Device Groups**.
3. Click **Add** and configure:
   - **Name** — e.g., `DG-AWS-SECURITY` (this is the value used in `dgname`)
   - **Description** — optional
4. Click **OK**.
5. **Commit** the change to Panorama (**Commit > Commit to Panorama**).

> **Important:** The Device Group must exist on Panorama *before* the firewall attempts to bootstrap. If the firewall connects and cannot find its assigned Device Group, registration will fail.

### 8. Create a Template Stack on Panorama

> **Panorama only** | **Palo Alto Docs:** [Manage Templates and Template Stacks](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-templates-and-template-stacks)

The Template Stack holds network, device, and system-level configuration that is pushed to managed firewalls.

1. In Panorama, navigate to **Panorama > Templates**.
2. Create a base template first (if none exist): click **Add**, name it (e.g., `TPL-BASE-AWS`), click **OK**.
3. Click **Add Stack** and configure:
   - **Name** — e.g., `STACK-AWS-SECURITY` (this is the value used in `tplname`)
   - **Templates** — add your base template(s) to the stack
4. Click **OK**.
5. **Commit** the change to Panorama.

### 9. Establish Backhaul Connectivity to Panorama

> **Panorama only**

The firewall management interfaces must have a network path to Panorama. Choose the appropriate connectivity method based on where Panorama is deployed.

**If Panorama is on-premises:**
- **AWS Direct Connect** — dedicated private connection from your data center to AWS
- **Point-to-Point VPN (IPsec)** — site-to-site VPN tunnel from your data center to the VPC

**If Panorama is in AWS:**
- **AWS Transit Gateway (TGW)** — attach both VPCs to a shared TGW and configure route tables
- **VPC Peering** — create a direct peering connection between the firewall VPC and the Panorama VPC

> **Important:** Verify routing is in place end-to-end. The firewall management subnet must have a route to the Panorama management IP, and Panorama must have a return route. Test with `nc -zv <panorama-ip> 3978` from an instance in the firewall management subnet before deploying.

### 10. Configure Panorama Security Groups

> **Panorama only**

Create security groups that allow the required traffic between the firewall management subnets and Panorama.

> For the full list of ports, see [Ports Used for Panorama](https://docs.paloaltonetworks.com/pan-os/11-0/pan-os-admin/firewall-administration/reference-port-number-usage/ports-used-for-panorama).

**Panorama Communication (required for all Panorama-managed methods):**

| Direction | Protocol | Port | Source | Destination | Purpose |
|---|---|---|---|---|---|
| Outbound | TCP | 3978 | Firewall mgmt subnet(s) | Panorama IP(s) | Device registration and config sync |
| Outbound | TCP | 28443 | Firewall mgmt subnet(s) | Panorama IP(s) | Panorama-to-device communication |
| Inbound | TCP | 3978 | Panorama IP(s) | Firewall mgmt subnet(s) | Panorama-initiated connections |
| Inbound | TCP | 28443 | Panorama IP(s) | Firewall mgmt subnet(s) | Panorama-initiated connections |

**Management Access (required for UI/SSH access):**

| Direction | Protocol | Port | Source | Destination | Purpose |
|---|---|---|---|---|---|
| Inbound | TCP | 443 | Admin workstation(s) | Firewall mgmt subnet(s) | Web UI (HTTPS) |
| Inbound | TCP | 22 | Admin workstation(s) | Firewall mgmt subnet(s) | SSH access |

> **Note:** Apply these rules to every management subnet across all availability zones where firewalls will be deployed. Ensure the Panorama-side security groups also allow inbound from firewall management subnets on ports 3978 and 28443.

### 11. Activate Strata Cloud Manager

> **SCM only** | **Palo Alto Docs:** [Activate Strata Cloud Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activate-strata-cloud-manager)

Strata Cloud Manager (SCM) provides centralized cloud-delivered management for VM-Series firewalls. SCM can be used as an alternative to Panorama for managing your firewall fleet.

1. Log in to the [Palo Alto Networks Hub](https://apps.paloaltonetworks.com).
2. Navigate to **Strata Cloud Manager** and complete the activation wizard.
3. Ensure the **NGFW Management** flag is enabled in SCM settings.

> **Warning:** The NGFW Management flag enablement can take approximately 2 days after initial request. Plan accordingly and do not wait until the day of deployment to request this.

### 12. Activate Strata Logging Service

> **SCM only** | **Palo Alto Docs:** [Activate Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/getting-started/activate)

Strata Logging Service (SLS) centralizes log collection and analysis from your VM-Series firewalls and enables cloud-delivered security analytics.

1. In the [Palo Alto Networks Hub](https://apps.paloaltonetworks.com), navigate to **Strata Logging Service**.
2. Complete the activation process and note your SLS region.
3. Verify the service shows as **Active** in the Hub.

### 13. AWS Account and IAM Prerequisites

Proper cloud authentication and permissions are critical for Terraform to provision resources.

1. **Console & CLI Authentication** — Ensure you can authenticate to the AWS account via both the AWS Console and the AWS CLI.
2. **IAM Permissions** — The authenticated user or role must have Admin privileges or an equivalent role capable of creating:
   - Virtual Private Clouds (VPCs), subnets, route tables
   - EC2 instances, network interfaces, Elastic IPs
   - Load balancers (ALB, NLB, GWLB), GWLB endpoints
   - IAM users, roles, and policies
   - S3 buckets for Terraform state
   - Transit Gateway and TGW attachments

### 14. Create a Deployment IAM Account

Terraform requires a dedicated programmatic account for provisioning resources. This account typically requires Administrator or equivalent rights for the initial deployment due to the wide range of resources created.

1. In the AWS Console, navigate to **IAM > Users > Add users**.
2. Set a username (e.g., `terraform-pan-deploy`).
3. Select **Programmatic access** to generate an Access Key and Secret Key.
4. Attach the **AdministratorAccess** policy (or a scoped policy covering the resources listed above).
5. **Copy and securely store** the Access Key ID and Secret Access Key.

Configure the credentials for Terraform:

```bash
# Option 1: Environment variables (recommended for CI/CD)
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-west-2"

# Option 2: AWS credentials file
aws configure --profile pan-deploy
```

> **Note:** This scope can be reviewed and reduced after a successful initial deployment. For production, consider using an IAM role attached to an EC2 instance (Instance Profile) instead of static credentials — no secret keys need to be stored.

### 15. Accept the AWS Marketplace Subscription

You must accept the AWS Marketplace subscription before launching VM-Series instances. This is a one-time action per AWS account per product listing.

**Via AWS Console:**

1. Navigate to the VM-Series marketplace listing for your license model:
   - [VM-Series BYOL](https://aws.amazon.com/marketplace/pp/prodview-ccnrlwz6ppf2g)
   - [VM-Series Bundle 1 (PAYG)](https://aws.amazon.com/marketplace/pp/prodview-ezv4dt2bfo4v2)
   - [VM-Series Bundle 2 (PAYG)](https://aws.amazon.com/marketplace/pp/prodview-d46mpctnlm2qk)
2. Click **Continue to Subscribe**.
3. Review pricing and click **Accept Terms**.

**Via AWS CLI (check status):**

```bash
# Check if you've already accepted the terms for BYOL
aws ec2 describe-images \
  --owners aws-marketplace \
  --filters "Name=product-code,Values=6njl1pau431dv1qxipg63mvah" \
  --query 'Images[0].ImageId' \
  --output text \
  --region us-west-2
```

> **Note:** If the CLI returns an image ID, your subscription is active. If it returns `None` or an error, accept the terms via the console links above. AWS Marketplace subscriptions cannot be accepted via the CLI.

### 16. Discover the VM-Series AMI

Find the latest VM-Series image for your target region:

```bash
# List available VM-Series BYOL AMIs in us-west-2
aws ec2 describe-images \
  --owners aws-marketplace \
  --filters "Name=product-code,Values=6njl1pau431dv1qxipg63mvah" \
             "Name=state,Values=available" \
  --query 'Images | sort_by(@, &CreationDate) | [-5:].{Name:Name, ImageId:ImageId, Created:CreationDate}' \
  --output table \
  --region us-west-2

# For PAYG (bundle2) images, use product code: hd44w1chf26uv4p52cdynb2o
```

**Common product codes:**

| License Model | Product Code |
|---|---|
| BYOL | `6njl1pau431dv1qxipg63mvah` |
| Bundle 1 (PAYG) | `e9yfvyj3uag5uo5j2hjikv74n` |
| Bundle 2 (PAYG) | `hd44w1chf26uv4p52cdynb2o` |

### 17. Verify Network Connectivity

The firewall management interface requires outbound access to:

| Destination | Port | Purpose |
|---|---|---|
| Panorama management IP | TCP 3978, 28443 | Device registration and management |
| `updates.paloaltonetworks.com` | TCP 443 | License activation and device certificate retrieval |
| DNS resolver | UDP 53 | DNS resolution |
| Strata Logging Service region endpoint | TCP 443 | Log forwarding (if using SLS) |

> **Important:** If the management subnet is private (no IGW), ensure a NAT Gateway or VPC endpoint is available for outbound HTTPS to `updates.paloaltonetworks.com`. Without this, license activation and device certificate retrieval will fail.

### 18. Set Up the Deployment Environment

Install the required tooling on your deployment machine (local workstation, bastion host, or CloudShell).

**Required tools:**

| Tool | Purpose | Install Link |
|---|---|---|
| Terraform CLI | Infrastructure provisioning | [terraform.io/downloads](https://www.terraform.io/downloads) |
| Git | Source code management | [git-scm.com](https://git-scm.com/downloads) |
| AWS CLI | AWS service management | [aws.amazon.com/cli](https://aws.amazon.com/cli/) |
| Code editor | Configuration editing | [VS Code](https://code.visualstudio.com/) (recommended) |

**AWS CloudShell (easiest method):**

AWS CloudShell automatically assumes the IAM permissions of the authenticated console user. It is the fastest way to get started.

1. Open CloudShell from the AWS Console.
2. Install Terraform (if not already present):
   ```bash
   sudo yum install -y yum-utils
   sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
   sudo yum -y install terraform
   ```
3. Clone your Terraform repository:
   ```bash
   git clone https://your-repo-url.git
   cd your-repo-directory
   ```

**Local or bastion host:**

1. Install Terraform, Git, and AWS CLI using the links above.
2. Configure AWS credentials (see [step 14](#14-create-a-deployment-iam-account)).
3. Verify connectivity:
   ```bash
   aws sts get-caller-identity
   terraform -v
   ```

### 19. Configure Remote State Backend

A remote state backend is critical for team collaboration and state locking. For AWS, use an S3 bucket with a DynamoDB table.

**Create the backend resources:**

1. Create an S3 bucket with versioning enabled:
   ```bash
   aws s3api create-bucket \
     --bucket pan-tf-state-bucket \
     --region us-west-2 \
     --create-bucket-configuration LocationConstraint=us-west-2

   aws s3api put-bucket-versioning \
     --bucket pan-tf-state-bucket \
     --versioning-configuration Status=Enabled
   ```

2. Create a DynamoDB table for state locking:
   ```bash
   aws dynamodb create-table \
     --table-name pan-tf-statelocks \
     --attribute-definitions AttributeName=LockID,AttributeType=S \
     --key-schema AttributeName=LockID,KeyType=HASH \
     --billing-mode PAY_PER_REQUEST \
     --region us-west-2
   ```

**Add the backend configuration to your Terraform code:**

Create or update `backend.tf`:

```hcl
terraform {
  backend "s3" {
    bucket         = "pan-tf-state-bucket"
    key            = "pan-vmseries/aws/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "pan-tf-statelocks"
    encrypt        = true
  }
}
```

> **Note:** The S3 bucket and DynamoDB table must exist before running `terraform init`. Replace the bucket name, key path, and region with your organization's values.

---

*Prerequisites complete. Proceed to [Panorama Deployment](#panorama-deployment) to begin the deployment.*
