<!-- Source: https://docs.paloaltonetworks.com/ai-runtime-security/administration/discover-your-cloud-resources -->
<!-- Fetched: 2026-03-31T18:59:38.586488+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: scm, cloud-discovery -->

# Discover Your Cloud Resources

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Prisma AIRS Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Activation & Onboarding
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Administration
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 AI Model Security
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 AI Red Teaming
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Release Notes
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 

 

 

 

 

 
 
 
---

 
 
 **

[Previous
                            
                                    AI Models on Public Clouds Support](/content/techdocs/en_US/ai-runtime-security/administration/ai-models-public-clouds-support.html)
 

 
 

**[Next
                                
                                    Analyze Risk in Network Traffic](/content/techdocs/en_US/ai-runtime-security/administration/discover-your-cloud-resources/ai-traffic-network-risk-analysis.html)
 

 

---

 
 
 















 

# Discover Your Cloud Resources



 



 Get a unified view of all the discovered cloud resources in Strata Cloud Manager.



 






















 

- 

- [Onboard and Activate a Cloud
                                        Account in Strata Cloud Manager](https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/onboard-and-activate-cloud-account-in-scm)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| Cloud assets discovery in Strata Cloud Manager |  |


Gain comprehensive real-time visibility into your cloud infrastructure by
 discovering and analyzing assets protected by Prisma AIRS AI
 Runtime: Network intercept and VM-Series firewalls. The discovery
 dashboard displays threats, network traffic, and protection status across both firewall
 platforms when onboarded through Strata Cloud Manager.

**Key Assets Discovered**

- Virtual Machine (VM) workloads.
- Clusters and containers.
- Serverless workloads: For Azure functions and AWS Lambda functions, you can
 discover and analyze serverless workloads.Prerequisite for serverless
 discovery:
  - For Azure: A **Reader role** for your cloud account.
  - For AWS: IAM permissions to list, describe Lambda functions, and
 retrieve tags associated with functions.

- AI and non AI applications, AI models, and AI data.
- Network traffic.

**Important Notes on Discovery**

- Strata Cloud Manager doesn't detect or manage VM-Series firewall
 deployed outside of the Prisma AIRS AI Runtime onboarding
 workflow.
- While the discovery service updates continuously, please note that deleted cloud
 assets may continue to appear in the discovery UI for approximately 24 hours
 after deletion from the cloud environment.

**Analyzing Discovered Assets**

Navigate to Insights Prisma AIRS Prisma AIRS AI Runtime: Network intercept to see a list of protected and unprotected cloud assets, including
 applications, risky endpoints, user applications, AI models, and internet endpoints.

The discovery helps you analyze both AI and non-AI security traffic flow logs
 and threat logs, enabling you to identify and correlate malicious threats with the
 identified cloud assets. You can view threats detected from both platforms, analyze
 network traffic flows, and understand which applications are secured by each firewall
 type.

For detailed analysis, see [Analyze Risk in Network Traffic](/content/techdocs/en_US/ai-runtime-security/administration/discover-your-cloud-resources/ai-traffic-network-risk-analysis.html).

**Strata Cloud Manager Command Center**

The [Dashboard: AI Runtime Security](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/ai-runtime-security) provides
 actionable insights into all cloud assets in your onboarded cloud account. It classifies
 and prioritizes security issues based on threat urgency and risk categories, such as
 vulnerability detection and prompt injection attacks. The discovery of assets is
 classified into the **operational** and **security** views.

.
 
 

 

- The **Operational** view displays all cloud assets: application
 workloads, application users, and AI models. The view also shows the
 bidirectional communication flows between:
  - User to application

  - Application to the AI model

  - Application to the internet, and

  - Application to application.

- The **Security** view highlights the threat landscape with
 security issues prioritized by urgency and risk type.

Based on the security analysis from the security view, you can add Prisma AIRS AI Runtime: Network intercept or VM-Series firewall by selecting the "+" icon on the dashboard.

For detailed steps, see the [deployment workflow](https://docs.paloaltonetworks.com/ai-runtime-security/administration/deploy-ai-instances-in-public-clouds-as-a-software) for each firewall.



 















 

## Multi-Cloud Security Fabric Discovery



 Multi-Cloud Security Fabric Discovery is a powerful feature that provides a
 unified view of your cloud infrastructure and protection status across multiple
 cloud providers. It enables you to visualize your cloud network topology,
 understand the protection status of your resources, and implement automated
 firewall deployment to secure your applications.

At its core, Multi-Cloud Security Fabric Discovery scans your cloud environments
 to identify regions, VPCs, subnets, and applications. It then analyzes traffic
 patterns and security configurations to determine whether your resources are
 protected, partially protected, or unprotected. This assessment is based on
 evaluating multiple use cases including App-to-App, App-to-Model,
 App-to-Internet, and User-to-App traffic flows.

The infrastructure view provides a geographical representation of your cloud regions, showing resource distribution and protection status. You can drill down into specific regions to view detailed information about VPCs, applications, firewalls, and tunnels deployed in that region. The topology view offers a more detailed perspective, allowing you to explore the relationships between different components within your cloud infrastructure.

For each VPC, Multi-Cloud Security Fabric Discovery determines protection status
 by evaluating whether traffic is being inspected by security elements like
 firewalls. A VPC is considered protected when all of its subnets are fully
 protected for all defined use cases. When some subnets lack complete protection,
 the VPC is marked as partially protected. If no subnets have any protection
 enabled, the VPC is classified as unprotected.

Once you've identified unprotected or partially protected resources, you can use the automated deployment feature to secure your infrastructure. This process includes creating security VPCs, deploying firewall instances, setting up load balancers, and configuring the necessary routing to redirect traffic through the security infrastructure. The system supports various traffic patterns including east-west traffic within a VPC, between VPCs in the same region, across different regions, and north-south traffic to internet destinations.

To enable these capabilities, you'll need to onboard your cloud accounts to Strata Cloud Manager with appropriate permissions. The system requires both read permissions to discover your infrastructure and write permissions to implement automated security measures. The implementation follows best practices to minimize traffic disruption, making it suitable for production environments.

By leveraging Multi-Cloud Security Fabric Discovery, you gain comprehensive
 visibility into your cloud security posture and the ability to rapidly remediate
 security gaps through automated deployment, significantly reducing the
 complexity of securing multi-cloud environments.



 















 

### Deployment without Discovery



 Prisma AIRS supports *deployment without discovery*. This feature allows you
 to bypass the complexity of onboarding your cloud accounts before you deploy
 your firewall. When using deployment without discovery you don't have to
 explicitly onboard your cloud accounts, you can skip account onboarding and
 download the Terraform template (via Strata Cloud Manager) to deploy the
 firewall.

To use deployment without discovery, you'll need to know the software versions
 for each cloud type. To locate this information:
- For AWS, you’ll need to locate the AMI ID.

- For GCP, you’ll need to know the version ID.

- For Azure, you’ll need to locate the version of your
 subscription.

The sections below describe how to locate this information.

**AWS**

AWS AMI IDs for Palo Alto Networks are typically found through the AWS
 Marketplace listing in your desired AWS region, as the AMI ID can vary by
 version and region. To locate the AMI ID for your deployment, follow these steps
 directly in the AWS console:

1. Log into the [AWS Marketplace](https://aws.amazon.com/marketplace).

2. Locate your subscription for AI Runtime Security or Prisma
 AIRS. If it’s a new subscription, continue with the configuration
 process by choosing **Continue to Subscribe**.

3. In the next screen select the desired **Software Version**
 (for example, PAN-OS 11.2.9) and the **Region**. The page displays
 the specific AMI ID corresponding to that version and region. For
 example, **ami-058d263b30c1de5d2**. Refer to the[AWS documentation](https://docs.aws.amazon.com/managedservices/latest/userguide/find-ami.html) for more
 information about locating the AMI ID. 

**Azure**

For Azure deployments, you'll need to add the region and the subscription ID:
- **Region**. Add the region based on the format (specifically, the
 *programmatic name*) noted in the [list of Azure regions](https://learn.microsoft.com/en-us/azure/reliability/regions-list). For
 example, Canada Central should be added as
 canadacentral.
- **Subscription**. The subscription is the Cloud Account ID. The Azure
 software version for Prisma AIRS is a lengthy string that includes
 details about your subscription, the cloud location, and the specific
 software version number. You need to locate this version number in your
 Azure subscription. The format of the Azure software version ID differs
 based on the firewall image version. In this example, the Azure Resource
 Manager (ARM) resembles:

```
/Subscriptitralus/Publishers/paloaltonetworks/ArtifactTypes/VMImage/Offers/airs-flex/Skus/airs-byol/Versions/11.2.9

```

To locate the software version ID in Azure you’ll typically need to use the Azure
 CLI or Azure PowerShell; use the example above to locate each element in this
 list:
1. Identify the publisher, Offer, and SKU. For a Prisma AIRS image:
  1. Publisher: paloaltonetworks.
  2. Offer: airs-flex.
  3. SKU: airs-byol.

2. List available versions. You can typically use the command
 Get-AzVMImage in PowerShell, or az vm image
 list in the Azure CLI. For example:
 /Subscriptions/<SUBSCRIPTION-ID>/Providers/Microsoft.Compute/Locations/<REGION>/Publishers/paloaltonetworks/ArtifactTypes/VMImage/Offers/airs-flex/Skus/airs-byol/Versions/<SOFTWARE-VERSION>For
 example:

```
/Subscriptions/c340b753-fc41-49ff-82c0-32978c2716cd/Providers/Microsoft.Compute/Locations/northcentralus/Publishers/paloaltonetworks/ArtifactTypes/VMImage/Offers/airs-flex/Skus/airs-byol/Versions/11.2.9

```

3. Specify the location. You must specify the Azure location (in the
 provided example, northcentralus) where you intend to
 deploy the firewall.
4. Extract the version. The specific version string (for example, 11.2.9)
 can be used to construct the full path required for deployment without
 discovery.

**GCP**

To locate the version ID for GCP when using deployment without discovery for
 Prisma AIRS, you can use the gcloud CLI tool. There are three
 methods associated with this tool, depending on the resource type

The following examples represent the expected format for the GCP
 version, which resembles a URL pointing to the image in the Google Compute
 Engine public project.

For Prisma AIRS series firewalls, run the gcloud command:

```
# Define the project
IMAGE_PROJECT="<PROJECT NAME>"

# 1. Retrieve the names of the two latest images, sorted by creation time
# The output is newline-separated image names
LATEST_IMAGE_NAMES=$(gcloud compute images list \
  --project="${IMAGE_PROJECT}" \
  --filter="name~'ai-runtime-security-byol.*'" \
  --limit=2 \
  --sort-by="~creationTimestamp" \
  --format="value(name)")

echo "--- Found Latest Images ---"
echo "$LATEST_IMAGE_NAMES"
echo "---------------------------"

# 2. Loop through the found names and retrieve the full URI for each
echo "--- Retrieving Full URIs ---"
for IMAGE_NAME in ${LATEST_IMAGE_NAMES}; do
  gcloud compute images describe "${IMAGE_NAME}" \
    --project="${IMAGE_PROJECT}" \
    --format="value(selfLink)"
done
echo "--------------------------"

```
For VM Series firewalls, run the gcloud command:
 
 Prisma AIRS and VM-Series commands can be
 combined; update the IMAGE_FILTER appropriately.

```
# Define the project
IMAGE_PROJECT="paloaltonetworksgcp-public"
IMAGE_FILTER="vmseries-flex-byol.*" # Targeting the standard firewall images

# 1. Retrieve the names of the two latest images, sorted by creation time
# The output is newline-separated image names
LATEST_IMAGE_NAMES=$(gcloud compute images list \
  --project="${IMAGE_PROJECT}" \
  --filter="name~'${IMAGE_FILTER}'" \
  --limit=2 \
  --sort-by="~creationTimestamp" \
  --format="value(name)")

echo "--- Found Latest VM-Series Images (Standard BYOL) ---"
echo "$LATEST_IMAGE_NAMES"
echo "----------------------------------------------------"

# 2. Loop through the found names and retrieve the full URI for each
echo "--- Retrieving Full URIs ---"
for IMAGE_NAME in ${LATEST_IMAGE_NAMES}; do
  gcloud compute images describe "${IMAGE_NAME}" \
    --project="${IMAGE_PROJECT}" \
    --format="value(selfLink)"
done
echo "--------------------------"

```