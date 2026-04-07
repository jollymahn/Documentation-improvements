# VM-Series Firewall Bootstrap Guide (GCP) -- Choose Your Path

Pick your deployment scenario and follow the tailored path. Each branch gives you only the steps relevant to your chosen method.

> **See also:** [AWS Guide](../aws/branching-guide.md) | [Azure Guide](../azure/branching-guide.md)

---

## Table of Contents

1. [Prerequisites Checklist](#prerequisites-checklist-all-methods)
2. [Method 1: Panorama Licensing Plugin](#method-1-panorama-licensing-plugin)
3. [Method 2: Simple Metadata Bootstrap](#method-2-simple-metadata-bootstrap)
4. [Method 3: GCS Bucket Basic Bootstrap with init-cfg and authcode](#method-3-gcs-bucket-basic-bootstrap-with-init-cfg-and-authcode)
5. [Method 4: GCS Full Bootstrap with bootstrap.xml](#method-4-gcs-full-bootstrap-with-bootstrapxml)

---

## Prerequisites Checklist (All Methods)

Complete all applicable items before bootstrapping. Each section includes setup instructions.

1. [ ] [**1 Software NGFW Credit Pool**](#activate-software-ngfw-credits) — activated and funded ([Activate Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-credits))
2. [ ] [**2 Deployment Profile**](#create-a-deployment-profile) — created with auth code ([Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series))
3. [ ] [**3 Device Group**](#create-a-device-group-on-panorama) — created on Panorama ([Manage Device Groups](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-device-groups))
4. [ ] [**4 Template Stack**](#create-a-template-stack-on-panorama) — created on Panorama ([Manage Templates and Template Stacks](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-templates-and-template-stacks))
5. [ ] [**5 Auth Code**](#obtain-the-auth-code) — obtained for bootstrap definitions ([Manage a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/manage-a-deployment-profile))
6. [ ] [**6 Auto-Registration PIN ID & PIN Value**](#generate-auto-registration-pin-id-and-pin-value) — generated for device certificates ([Install a Device Certificate](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/install-a-device-certificate-on-the-vm-series-firewall))
7. [ ] [**7 Backhaul Connectivity to Panorama**](#establish-backhaul-connectivity-to-panorama) — Cloud Interconnect, Cloud VPN, VPC Peering, or Shared VPC established
8. [ ] [**8 VPC Firewall Rules**](#configure-vpc-firewall-rules) — Panorama ports and management access configured ([Ports Used for Panorama](https://docs.paloaltonetworks.com/pan-os/11-0/pan-os-admin/firewall-administration/reference-port-number-usage/ports-used-for-panorama))
9. [ ] [**9 GCP Marketplace Subscription**](#accept-the-gcp-marketplace-subscription) — accepted for your license model
10. [ ] [**10 VM-Series GCP Image**](#discover-the-vm-series-gcp-image) — identified from Marketplace or public project
11. [ ] [**11 Network Connectivity**](#network-requirements) — management interface can reach Panorama and licensing servers
12. [ ] [**12 Licensing API Key**](#set-the-licensing-api-key-on-panorama) — set on Panorama for license deactivation ([Install a License Deactivation API Key](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/licensing-api/install-a-license-deactivation-api-key))

---

### Activate Software NGFW Credits

> **Palo Alto Docs:** [Activate Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-credits)

1. Log in to the [Customer Support Portal](https://support.paloaltonetworks.com).
2. Go to **Assets > Software NGFW Credits**.
3. Locate your credit pool auth code (from your purchase order) and click **Activate**.
4. Verify the pool shows available credits for your VM-Series model and subscription tier.

> Credits are shared across your account. Each firewall consumes credits based on vCPU count and subscriptions in its deployment profile.

### Create a Deployment Profile

> **Palo Alto Docs:** [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) | [Manage a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/manage-a-deployment-profile)

1. In the CSP, go to **Assets > Software NGFW Credits** and select your credit pool.
2. Click **Create Deployment Profile** and configure:
   - **Profile Name** — e.g., `gcp-prod`
   - **Firewall Model** — e.g., VM-300, VM-500
   - **vCPU Count** — number of vCPUs to allocate
   - **Subscriptions** — Threat Prevention, WildFire, URL Filtering, DNS Security, etc.
   - **Token Count** — number of firewalls this profile can license
3. Click **Create**. Note the generated **auth code** (format: `D1234567`) — you will need it for the bootstrap definition on Panorama.

To manage profiles later: **Assets > Software NGFW Credits > Deployment Profiles**.

> **Note:** Deployment profiles are defined by **licensing tier and vCPU count**, not by region, cloud, or individual firewall. Multiple firewalls with the same licensing requirements and vCPU allocation can share a single deployment profile — there is no need to create one per firewall. Group your deployment profiles by function and vCPU count (e.g., one profile for all 4-vCPU inspection firewalls, another for 8-vCPU firewalls with different subscriptions). You can always create additional profiles later if requirements diverge.

### Create a Device Group on Panorama

> **Palo Alto Docs:** [Manage Device Groups](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-device-groups)

1. Log in to Panorama and go to **Panorama > Device Groups**.
2. Click **Add**:
   - **Name** — e.g., `YOUR-DG-HERE` (this is your `dgname` value)
3. Click **OK**, then **Commit to Panorama**.

> The Device Group must exist *before* the firewall bootstraps. If the firewall cannot find its assigned DG, registration fails.

### Create a Template Stack on Panorama

> **Palo Alto Docs:** [Manage Templates and Template Stacks](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-templates-and-template-stacks)

1. In Panorama, go to **Panorama > Templates**.
2. Create a base template first (if none exist): click **Add**, name it (e.g., `TPL-BASE-GCP`), click **OK**.
3. Click **Add Stack**:
   - **Name** — e.g., `YOUR-STACK-HERE` (this is your `tplname` value)
   - **Templates** — add your base template(s)
4. Click **OK**, then **Commit to Panorama**.

### Obtain the Auth Code

> **Palo Alto Docs:** [Manage a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/manage-a-deployment-profile)

1. In the CSP, go to **Assets > Software NGFW Credits > Deployment Profiles**.
2. Locate your deployment profile and copy the **Auth Code**.
3. This code is entered when creating the Bootstrap Definition on Panorama (**Panorama > SW Firewall License > Bootstrap Definitions**).

### Generate Auto-Registration PIN ID and PIN Value

> **Palo Alto Docs:** [Install a Device Certificate on the VM-Series Firewall](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/install-a-device-certificate-on-the-vm-series-firewall)

The PIN allows the firewall to automatically pull a device certificate during initial boot, which is required for license activation and Panorama registration.

1. In the CSP, go to **Products > VM-Series Auth-Codes** (or **Assets > VM-Series Deployment**).
2. Click **Generate OTP** or **Create Registration PIN**.
3. Copy both values:
   - **PIN ID** — UUID format (e.g., `81a75f2a-4de0-4f0e-959f-f31b5df06814`)
   - **PIN Value** — hex string (e.g., `7059943c5565454db6b83cdcd305f338`)
4. Used as `vm-series-auto-registration-pin-id` and `vm-series-auto-registration-pin-value` in bootstrap parameters.

> Without a valid PIN, the firewall cannot fetch a device certificate and will fail to authenticate with licensing infrastructure.

### Establish Backhaul Connectivity to Panorama

The firewall management interfaces must have a network path to Panorama.

**If Panorama is on-premises:**
- **Cloud Interconnect (Dedicated)** — dedicated private connection from your data center to GCP
- **Cloud Interconnect (Partner)** — partner-facilitated private connection to GCP
- **Cloud VPN** — IPsec VPN tunnel from your data center to the VPC

**If Panorama is in GCP:**
- **VPC Peering** — direct peering between firewall VPC and Panorama VPC
- **Shared VPC** — place both the firewall and Panorama in the same Shared VPC for simplified networking

> Verify routing end-to-end. The firewall management subnet must have a route to Panorama, and Panorama must have a return route. Test with `nc -zv <panorama-ip> 3978` from an instance in the management subnet before deploying.

### Configure VPC Firewall Rules

Apply to **all** management subnets where firewalls will be deployed. For the full list of ports, see [Ports Used for Panorama](https://docs.paloaltonetworks.com/pan-os/11-0/pan-os-admin/firewall-administration/reference-port-number-usage/ports-used-for-panorama).

**Panorama communication (required for all Panorama-managed methods):**

| Direction | Port | Purpose |
|---|---|---|
| Egress to Panorama | TCP 3978 | Device registration and config sync |
| Egress to Panorama | TCP 28443 | Panorama-to-device communication (PAN-OS 8.1+) |
| Ingress from Panorama | TCP 3978 | Panorama-initiated connections |
| Ingress from Panorama | TCP 28443 | Panorama-initiated connections |

**Management access (UI/SSH to firewalls):**

| Direction | Port | Purpose |
|---|---|---|
| Ingress from mgmt subnets | TCP 443 | Web UI (HTTPS) |
| Ingress from mgmt subnets | TCP 22 | SSH access |

> Ensure the Panorama-side VPC firewall rules also allow inbound from firewall management subnets on 3978 and 28443. Use network tags (e.g., `vm-series`) to scope the rules to firewall instances. For managed instance groups, pre-configure rules on all subnets across zones.

### Accept the GCP Marketplace Subscription

You must accept the GCP Marketplace terms before launching VM-Series instances. This is a one-time action per GCP project per product listing.

**Via GCP Console:**

1. Navigate to the VM-Series marketplace listing for your license model:
   - [VM-Series Flex BYOL](https://console.cloud.google.com/marketplace/product/paloaltonetworksgcp-public/vmseries-flex-byol)
   - [VM-Series Flex Bundle 1 (PAYG)](https://console.cloud.google.com/marketplace/product/paloaltonetworksgcp-public/vmseries-flex-bundle1)
   - [VM-Series Flex Bundle 2 (PAYG)](https://console.cloud.google.com/marketplace/product/paloaltonetworksgcp-public/vmseries-flex-bundle2)
2. Click **Launch** or **Get Started**.
3. Accept the terms and conditions. You do not need to complete the deployment from the Marketplace page.

**Via gcloud CLI:**

List available VM-Series images to verify access:

```bash
# List available VM-Series BYOL images
gcloud compute images list \
  --project paloaltonetworksgcp-public \
  --filter="name~'vmseries-flex-byol'" \
  --sort-by="~creationTimestamp" \
  --limit=5 \
  --format="table(name,creationTimestamp,status)"
```

> **Note:** Unlike AWS and Azure, GCP Marketplace terms are accepted through the console. If the `gcloud compute images list` command returns images, your project has access. If it returns empty results, accept the terms via the console links above.

### Discover the VM-Series GCP Image

```bash
gcloud compute images list \
  --project paloaltonetworksgx-public \
  --filter="name~'vmseries-flex'" \
  --format="table(name, creationTimestamp)"
```

Alternatively, browse the available images through the GCP Marketplace listing for VM-Series.

### Network Requirements

The management interface needs outbound HTTPS (443) to:
- Panorama IP address(es)
- `updates.paloaltonetworks.com` (for license activation and device certificate retrieval)
- DNS resolution capability

### Set the Licensing API Key on Panorama

> **Palo Alto Docs:** [Install a License Deactivation API Key](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/licensing-api/install-a-license-deactivation-api-key)

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

> This key is required for Method 1 (Panorama Licensing Plugin). Without it, the licensing plugin cannot allocate or reclaim licenses.

---

## Choose Your Bootstrap Method

### Decision Tree

```
Do you use Panorama?
  |
  +-- YES: Do you have the SW Firewall License plugin?
  |     |
  |     +-- YES --> Method 1: Panorama Licensing Plugin (recommended)
  |     |
  |     +-- NO: Do you need full config at boot (no Panorama push)?
  |           |
  |           +-- YES --> Method 4: GCS full bootstrap with bootstrap.xml
  |           |
  |           +-- NO: Do you want to avoid GCS buckets?
  |                 |
  |                 +-- YES --> Method 2: Simple Metadata Bootstrap
  |                 |
  |                 +-- NO --> Method 3: GCS bucket basic bootstrap
  |
  +-- NO (using SCM): --> SCM Bootstrap Variant
```

---

## Method 1: Panorama Licensing Plugin

> **Palo Alto Docs:** [Use Panorama-Based Software Firewall License Management](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/use-panorama-based-software-firewall-license-management)

This is the recommended method for production and auto-scaling environments. Panorama handles licensing automatically.

> **Internet Access:** This method does **not** require the firewalls to have direct internet access via the management interface -- Panorama handles all licensing on their behalf. However, Panorama itself **must** have direct internet access to reach `updates.paloaltonetworks.com`.

> **PAYG Note:** If you are using a PAYG (pay-as-you-go) license from the cloud marketplace, you do **not** need the SW Firewall License plugin. PAYG firewalls are licensed directly through the marketplace. Skip to Method 2 for PAYG deployments.

> **NSX Note:** If you are deploying VM-Series for VMware NSX, the `sw_fw_license` plugin has a dependency on the VM-Series plugin for NSX (`vm_series`). Both plugins must be installed on Panorama. Install the VM-Series plugin for NSX first, then install `sw_fw_license`. See [Troubleshooting: Plugin IP-Tag Issues](#plugin-ip-tag-issues) if you have multiple plugins installed.

> **Azure VM-Series Plugin Note:** If you have the Azure VM-Series plugin (`azure`) installed on Panorama alongside `sw_fw_license`, ensure the Azure plugin is fully configured and in a **Registered** or **Success** state. Unconfigured plugins can block IP-tag forwarding to firewalls. See [Troubleshooting: Plugin IP-Tag Issues](#plugin-ip-tag-issues).

### Step 1: Install the SW Firewall License Plugin

1. Log in to Panorama.
2. Navigate to **Panorama > Plugins**.
3. Click **Check Now** to refresh the list of available plugins.
4. Locate `sw_fw_license` in the plugin list.
5. Click **Download** for the latest version.
6. Once downloaded, click **Install**.
7. Verify the plugin appears under **Panorama > SW Firewall License** in the left navigation.

**Requirements:**
- Panorama 10.0.0 or later
- VM-Series plugin 2.0.4 or later (if managing NSX-based firewalls)
- VM-Series firewalls running PAN-OS 9.1.0 or later
- Licensing API key already configured on Panorama (see [§12 Licensing API Key](#set-the-licensing-api-key-on-panorama))

### Step 2: Create a Bootstrap Definition

1. Go to **Panorama > SW Firewall License > Bootstrap Definitions**.
2. Click **Add**.
3. Enter a **Name** for the bootstrap definition (e.g., `bsd-gcp-prod`).
4. Enter the **Auth Code** from your [deployment profile](#create-a-deployment-profile) (format: `D1234567`).
5. Optionally enter a **Description**.
6. Click **OK**.

> Each bootstrap definition maps to a single deployment profile auth code. Create a separate bootstrap definition for each deployment profile.

### Step 3: Configure a License Manager

1. Go to **Panorama > SW Firewall License > License Managers**.
2. Click **Add** and configure:
   - **Name** — e.g., `lm-gcp-prod`
   - **Device Group** — select the device group for the firewalls
   - **Template Stack** — select the template stack
   - **Bootstrap Definition** — select the definition created in Step 2
   - **Auto Deactivate** — set the timer for automatic license reclamation (1-24 hours, or "Never")
3. Click **OK**, then **Commit to Panorama**.

### Step 4: Get the Bootstrap Parameters

1. In the **License Managers** screen, locate your license manager.
2. In the **Action** column, click **Show Bootstrap Parameters**.
3. Copy the generated values:
   - **auth-key** — the Panorama-generated authentication key
   - **plugin-op-commands** — always starts with `panorama-licensing-mode-on`

> **Important:** The `auth-key` here is generated by the licensing plugin and is **different** from a manually created VM auth key.

### Step 5a: Terraform Configuration

```hcl
metadata = {
  # ── Minimum required values ──────────────────────────────────────
  plugin-op-commands                    = "panorama-licensing-mode-on"
  auth-key                              = "YOUR-AUTH-KEY-HERE"
  panorama-server                       = "YOUR-PANORAMA-SERVER-1-HERE"
  dgname                                = "YOUR-DG-HERE"
  tplname                               = "YOUR-STACK-HERE"

  # ── Optional: secondary Panorama ─────────────────────────────────
  panorama-server-2                     = "YOUR-PANORAMA-2-SERVER-HERE"

  # ── Optional: DHCP settings ──────────────────────────────────────
  dhcp-send-hostname                    = "yes"
  dhcp-send-client-id                   = "yes"
  dhcp-accept-server-hostname           = "yes"
  dhcp-accept-server-domain             = "yes"

  # ── Optional (best practice): device certificate auto-registration
  vm-series-auto-registration-pin-id    = "YOUR-PIN-ID-HERE"
  vm-series-auto-registration-pin-value = "YOUR-PIN-VALUE-HERE"
}
```

**Minimum required values:**

| Parameter | Description |
|---|---|
| `plugin-op-commands` | Must include `panorama-licensing-mode-on` as the first command |
| `auth-key` | Generated by the licensing plugin (from Step 4), **not** a manually created VM auth key |
| `panorama-server` | IP address of the primary Panorama |
| `dgname` | Device Group name on Panorama |
| `tplname` | **Template Stack** name on Panorama (this refers to the Template Stack, **not** a Template) |

> **Important:** The `vm-series-auto-registration-pin-id` and `vm-series-auto-registration-pin-value` parameters are optional but are a **best practice** for automatically installing a device certificate on the firewall during bootstrap.

### Step 5b: gcloud Instance Metadata Alternative

```bash
gcloud compute instances create fw-prod-01 \
  --project=YOUR-PROJECT \
  --zone=us-central1-a \
  --machine-type=n2-standard-4 \
  --image=IMAGE-NAME \
  --image-project=paloaltonetworksgx-public \
  --metadata=plugin-op-commands=panorama-licensing-mode-on,auth-key=YOUR-AUTH-KEY-HERE,panorama-server=YOUR-PANORAMA-SERVER-1-HERE,panorama-server-2=YOUR-PANORAMA-2-SERVER-HERE,dgname=YOUR-DG-HERE,tplname=YOUR-STACK-HERE,dhcp-send-hostname=yes,dhcp-send-client-id=yes,dhcp-accept-server-hostname=yes,dhcp-accept-server-domain=yes,vm-series-auto-registration-pin-id=YOUR-PIN-ID-HERE,vm-series-auto-registration-pin-value=YOUR-PIN-VALUE-HERE
```

**Important:** Do NOT include `authcodes` or `vm-auth-key` with this method. The plugin-generated `auth-key` replaces both.

**Skip to:** [Verification](#verification)

---

## Method 2: Simple Metadata Bootstrap

**Best for:** Quick one-off deployments, dev/test environments, getting a firewall up fast.

**Why this method:** No GCS bucket, no service account for bucket access, no bootstrap file management. Everything is in instance metadata.

> **Internet Access:** This method **requires** the firewall management interfaces to have direct internet access to reach `updates.paloaltonetworks.com` for licensing. This can be accomplished via a **Cloud NAT gateway** (preferred) or with an external IP on the management interface (not recommended -- if an external IP is used, ensure the VPC firewall rules are locked down as tightly as possible).

### Required Information

Gather the following before proceeding:

| Information | Source | Example |
|---|---|---|
| **Auth Code** | [Deployment profile](#create-a-deployment-profile) in the Customer Support Portal | `D1234567` |
| **Panorama IP(s)** | Primary (and optional secondary) Panorama management IP | `YOUR-PANORAMA-SERVER-1-HERE` |
| **Device Group** | [Device Group](#create-a-device-group-on-panorama) name on Panorama | `YOUR-DG-HERE` |
| **Template Stack** | [Template Stack](#create-a-template-stack-on-panorama) name on Panorama (**not** a Template) | `YOUR-STACK-HERE` |

### Step 1: Generate a VM Auth Key

On Panorama CLI:

```
request bootstrap vm-auth-key generate lifetime 8760
```

Output: `VM auth key 755036225328715 generated. Expires at: 2026/03/30 12:00:00`

To view existing keys: `request bootstrap vm-auth-key show`

Key lifetime: 1-8760 hours (1 year max).

### Step 2a: Terraform Configuration

```hcl
metadata = {
  # ── Minimum required values ──────────────────────────────────────
  authcodes                             = "D1234567"
  vm-auth-key                           = "YOUR-VM-AUTH-KEY-HERE"
  panorama-server                       = "YOUR-PANORAMA-SERVER-1-HERE"
  dgname                                = "YOUR-DG-HERE"
  tplname                               = "YOUR-STACK-HERE"

  # ── Optional: secondary Panorama ─────────────────────────────────
  panorama-server-2                     = "YOUR-PANORAMA-2-SERVER-HERE"

  # ── Optional: DHCP settings ──────────────────────────────────────
  dhcp-send-hostname                    = "yes"
  dhcp-send-client-id                   = "yes"
  dhcp-accept-server-hostname           = "yes"
  dhcp-accept-server-domain             = "yes"

  # ── Optional (best practice): device certificate auto-registration
  vm-series-auto-registration-pin-id    = "YOUR-PIN-ID-HERE"
  vm-series-auto-registration-pin-value = "YOUR-PIN-VALUE-HERE"
}
```

**Minimum required values:**

| Parameter | Description |
|---|---|
| `authcodes` | Auth code from your [deployment profile](#create-a-deployment-profile) |
| `vm-auth-key` | Manually generated VM auth key from Step 1 |
| `panorama-server` | IP address of the primary Panorama |
| `dgname` | Device Group name on Panorama |
| `tplname` | **Template Stack** name on Panorama (this refers to the Template Stack, **not** a Template) |

> **Important:** The `vm-series-auto-registration-pin-id` and `vm-series-auto-registration-pin-value` parameters are optional but are a **best practice** for automatically installing a device certificate on the firewall during bootstrap.

Key differences from Method 1:
- `plugin-op-commands` does **not** include `panorama-licensing-mode-on`
- Uses `authcodes` instead of the licensing plugin auth-key
- Uses `vm-auth-key` (manually generated) instead of the plugin-generated `auth-key`

### Step 2b: gcloud Instance Metadata Alternative

```bash
gcloud compute instances create fw-prod-01 \
  --project=YOUR-PROJECT \
  --zone=us-central1-a \
  --machine-type=n2-standard-4 \
  --image=IMAGE-NAME \
  --image-project=paloaltonetworksgx-public \
  --metadata=authcodes=D1234567,vm-auth-key=YOUR-VM-AUTH-KEY-HERE,panorama-server=YOUR-PANORAMA-SERVER-1-HERE,dgname=YOUR-DG-HERE,tplname=YOUR-STACK-HERE,panorama-server-2=YOUR-PANORAMA-2-SERVER-HERE,dhcp-send-hostname=yes,dhcp-send-client-id=yes,dhcp-accept-server-hostname=yes,dhcp-accept-server-domain=yes,vm-series-auto-registration-pin-id=YOUR-PIN-ID-HERE,vm-series-auto-registration-pin-value=YOUR-PIN-VALUE-HERE
```

> **Rule:** No spaces around `=` signs. GCP metadata supports both individual key-value pairs via `--metadata` and file-based input via `--metadata-from-file`.

> **Note:** Do **not** include `panorama-licensing-mode-on` in `plugin-op-commands` for Method 2.

**Skip to:** [Verification](#verification)

---

## Method 3: GCS Bucket Basic Bootstrap with init-cfg and authcode

**Best for:** Environments that need a structured bootstrap package but do not need to bundle PAN-OS software or content updates.

**Why this method:** More organized than instance metadata, supports teams that manage bootstrap files in version control, but avoids the complexity of bundling large binary files.

> **Internet Access:** This method **requires** the firewall management interfaces to have direct internet access to reach `updates.paloaltonetworks.com` for licensing. This can be accomplished via a **Cloud NAT gateway** (preferred) or with an external IP on the management interface (not recommended -- if an external IP is used, ensure the VPC firewall rules are locked down as tightly as possible).

### GCS Bucket Directory Structure

The bootstrap GCS bucket requires the following five directories. All five **must** exist, even if empty -- the firewall checks for this structure during bootstrap and will fail if any directory is missing.

```
gs://your-bootstrap-bucket/
  config/
  content/
  license/
  plugins/
  software/
```

#### Creating the Bucket and Directory Structure

Create the GCS bucket and required directories using gsutil:

```bash
# Create the bootstrap bucket
gsutil mb gs://your-bootstrap-bucket

# Create the required directory structure
# GCS does not have true directories -- create empty marker objects to represent the folder structure
gsutil cp /dev/null gs://your-bootstrap-bucket/config/
gsutil cp /dev/null gs://your-bootstrap-bucket/content/
gsutil cp /dev/null gs://your-bootstrap-bucket/license/
gsutil cp /dev/null gs://your-bootstrap-bucket/plugins/
gsutil cp /dev/null gs://your-bootstrap-bucket/software/
```

Alternatively, create the bucket and folders through the [GCP Console](https://console.cloud.google.com/storage).

#### Directory and Required Files

| Directory | Required File(s) | File Extension | Description |
|---|---|---|---|
| `config/` | `init-cfg.txt` | `.txt` | Bootstrap configuration parameters |
| `content/` | _(empty)_ | — | Content update files (not used in this method) |
| `license/` | `authcodes` | **no extension** | License auth code(s), one per line |
| `plugins/` | _(empty)_ | — | VM-Series plugin files (not used in this method) |
| `software/` | _(empty)_ | — | PAN-OS image files (not used in this method) |

### Create init-cfg.txt

```
type=dhcp
panorama-server=YOUR-PANORAMA-SERVER-1-HERE
panorama-server-2=YOUR-PANORAMA-2-SERVER-HERE
tplname=YOUR-STACK-HERE
dgname=YOUR-DG-HERE
vm-auth-key=YOUR-VM-AUTH-KEY-HERE
hostname=fw-prod-01
dns-primary=169.254.169.254
vm-series-auto-registration-pin-id=YOUR-PIN-ID-HERE
vm-series-auto-registration-pin-value=YOUR-PIN-VALUE-HERE
```

**Syntax rules:** No spaces around `=`. One parameter per line. Use a plain text editor (no rich text).

#### Required Parameters

| Parameter | Description | Example |
|---|---|---|
| `type` | IP assignment method | `dhcp` or `static` |
| `panorama-server` | Primary Panorama IP | `YOUR-PANORAMA-SERVER-1-HERE` |
| `tplname` | Template Stack name on Panorama (**not** a Template) | `YOUR-STACK-HERE` |
| `dgname` | Device Group name on Panorama | `YOUR-DG-HERE` |
| `vm-auth-key` | VM auth key generated on Panorama | `YOUR-VM-AUTH-KEY-HERE` |

#### Optional Parameters

| Parameter | Description | Example |
|---|---|---|
| `panorama-server-2` | Secondary Panorama IP (HA pair) | `YOUR-PANORAMA-2-SERVER-HERE` |
| `hostname` | Desired firewall hostname | `fw-prod-01` |
| `dns-primary` | Primary DNS server | `169.254.169.254` |
| `vm-series-auto-registration-pin-id` | PIN ID for device certificate auto-registration | `YOUR-PIN-ID-HERE` |
| `vm-series-auto-registration-pin-value` | PIN value for device certificate auto-registration | `YOUR-PIN-VALUE-HERE` |

### Create the authcodes File

Place in `/license/authcodes`:

> **Important:** The file is named `authcodes` with **no file extension** -- not `authcodes.txt`, not `authcodes.key`. The firewall expects this exact filename. The file must be plain text with no trailing whitespace or blank lines.

```
D1234567
```

> **Palo Alto Docs:** [Prepare the Bootstrap Package](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package)

### Create a Service Account and Grant GCS Access

The VM instance needs a service account with read access to the GCS bootstrap bucket. Without this, the firewall cannot read the bootstrap files at launch.

```bash
# Create a service account for the VM-Series firewall
gcloud iam service-accounts create vmseries-bootstrap \
  --display-name="VM-Series Bootstrap Service Account"

# Grant the service account read access to the bootstrap bucket
gsutil iam ch \
  serviceAccount:vmseries-bootstrap@YOUR-PROJECT.iam.gserviceaccount.com:roles/storage.objectViewer \
  gs://your-bootstrap-bucket
```

### Point the Instance to the Bucket

In instance metadata:

```
vmseries-bootstrap-gce-storagebucket=your-bootstrap-bucket
```

> **Important:** The metadata key is `vmseries-bootstrap-gce-storagebucket` and the value is the bucket name only (without the `gs://` prefix).

**Skip to:** [Verification](#verification)

---

## Method 4: GCS Full Bootstrap with bootstrap.xml

**Best for:** Standalone firewalls, air-gapped deployments, zero-touch provisioning where the firewall must boot fully configured without Panorama or SCM.

**Why this method:** The `bootstrap.xml` is a full VM-Series configuration file -- the firewall applies it on first boot, including interfaces, security policies, NAT rules, and routing. This method is generally **not used** when Panorama or SCM are managing the firewalls, since those platforms push configuration after bootstrap.

> **Internet Access:** This method **requires** the firewall management interfaces to have direct internet access to reach `updates.paloaltonetworks.com` for licensing. This can be accomplished via a **Cloud NAT gateway** (preferred) or with an external IP on the management interface (not recommended -- if an external IP is used, ensure the VPC firewall rules are locked down as tightly as possible).

### GCS Bucket Directory Structure

Same as Method 3. All five directories must exist. See [Method 3](#method-3-gcs-bucket-basic-bootstrap-with-init-cfg-and-authcode) for gsutil commands to create the bucket and directory structure.

#### Directory and Required Files

| Directory | Required File(s) | File Extension | Description |
|---|---|---|---|
| `config/` | `init-cfg.txt`, `bootstrap.xml` | `.txt`, `.xml` | Bootstrap parameters and full firewall configuration |
| `content/` | Content update file | _(vendor filename)_ | e.g., `panupv2-all-contents-8776-8520` |
| `license/` | `authcodes` | **no extension** | License auth code(s), one per line |
| `plugins/` | VM-Series plugin _(optional)_ | _(vendor filename)_ | e.g., `PanGPS_vm-3.0.2` |
| `software/` | PAN-OS image(s) | _(vendor filename)_ | e.g., `PanOS_vm-11.1.4-h13` |

### Create init-cfg.txt

Same format as Method 3. See Method 3 for required and optional parameter tables.

### Create the authcodes File

Same as Method 3.

### Create a Service Account and Grant GCS Access

Same as Method 3.

### Launch the Instance

Same as Method 3.

### Create bootstrap.xml

The `bootstrap.xml` is a complete PAN-OS configuration file that the firewall applies on first boot. The typical approach is to export the running configuration from a known-working reference firewall and use it as a seed configuration for new deployments.

#### Exporting the Configuration from a Reference Firewall

**Option A: Using the Web UI**

1. Log in to a VM-Series firewall that has the desired configuration.
2. Navigate to **Device > Setup > Operations**.
3. Click **Export named configuration snapshot**.
4. Select `running-config.xml` and save the file.
5. Rename the downloaded file to exactly `bootstrap.xml` (case-sensitive).
6. Place it in the `config/` directory alongside `init-cfg.txt`.

**Option B: Using the API**

Generate an API key and export the running config via the XML API:

```bash
# Generate an API key
curl -k "https://<firewall-ip>/api/?type=keygen&user=admin&password=<password>"

# Export the running configuration
curl -k "https://<firewall-ip>/api/?type=export&category=configuration&key=<api-key>" -o bootstrap.xml
```

**Option C: Using the CLI**

```
scp export configuration from running-config.xml to <user>@<destination>:/path/bootstrap.xml
```

> **Palo Alto Docs:** [Create the bootstrap.xml File](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-bootstrapxml-file)

#### What to Review Before Using the Seed Config

> **Warning:** When using a configuration from another firewall as a seed, the following values will almost certainly differ if the new firewall is in a different region, zone, or project:
>
> - **Management interface IP address** (`ip-address`, `netmask`, `default-gateway`) -- these are environment-specific
> - **Default routes and gateway IPs** -- vary by VPC/subnet
> - **Interface IP addresses** -- dataplane interface IPs tied to the specific subnet
> - **DNS server addresses** -- may differ between environments
> - **Hostname** -- should be unique per firewall
> - **Zone and interface mappings** -- verify they match the new network topology
>
> Review and update these values in the `bootstrap.xml` before placing it in the GCS bucket. Deploying with incorrect network values will result in an unreachable firewall.

### Add Software and Content Files (Optional)

If you need to boot the firewall with a specific PAN-OS version or content update:

- **Software:** Place PAN-OS image files in `software/`. Include **all intermediate versions** between the factory image and your target version -- the firewall upgrades sequentially and will fail if a version is skipped.
- **Content:** Place the content update file in `content/`. Include the minimum content version required for the target PAN-OS version. A content version mismatch causes the upgrade to fail.
- **Plugins (optional):** Place a single VM-Series plugin image in `plugins/` if needed.

**Continue to:** [Verification](#verification)

---

## SCM Bootstrap Variant

**Best for:** Organizations using Strata Cloud Manager instead of on-premises Panorama. Requires PAN-OS 11.0+.

### Terraform Configuration

```hcl
metadata = {
  panorama-server                       = "cloud"
  dgname                                = "scm_folder_name"
  dhcp-send-hostname                    = "yes"
  dhcp-send-client-id                   = "yes"
  dhcp-accept-server-hostname           = "yes"
  dhcp-accept-server-domain             = "yes"
  plugin-op-commands                    = "advance-routing:enable"
  vm-series-auto-registration-pin-id    = "YOUR-PIN-ID-HERE"
  vm-series-auto-registration-pin-value = "YOUR-PIN-VALUE-HERE"
  authcodes                             = "D1234567"
}
```

Key differences:
- `panorama-server` = `"cloud"` (literal string, not an IP)
- `dgname` = SCM folder name, not a Panorama Device Group
- No `tplname`, no `auth-key`, no `vm-auth-key`

---

## Verification

These steps apply to all methods.

### CLI Verification

SSH into the firewall management interface:

```
# System status and PAN-OS version
show system info

# Running configuration
show config running

# License status
request license info

# Panorama connection
show panorama-status

# Bootstrap log details
debug logview component bts_details
```

### Panorama Verification (Methods 1, 2, 3)

1. **Panorama > Managed Devices > Summary** -- confirm the firewall appears.
2. Verify correct Device Group and Template Stack assignment.
3. For Method 1: check **Panorama > SW Firewall License > License Managers** to confirm license allocation.
4. Verification CLI on Panorama: `show plugins sw_fw_license panorama-api-requests`

### Success Criteria

- `show system info` shows the expected hostname, PAN-OS version, and operational mode
- `request license info` shows all subscriptions as active
- The firewall appears in Panorama (if applicable) under the correct Device Group and Template Stack
- For Method 4: security policies from `bootstrap.xml` are active

---

## Troubleshooting

### Quick Diagnosis

| Symptom | Likely Cause | Fix |
|---|---|---|
| Firewall stuck at `192.168.1.1` | Bootstrap failed, reverted to factory defaults | Check `init-cfg.txt` syntax (no spaces around `=`), verify GCS access |
| "Boot image error" | GCS bucket not found or service account permissions wrong | Test service account: `gsutil ls gs://your-bucket/` from a test instance |
| "No bootstrap config file" | `init-cfg.txt` missing from `/config` | Verify directory structure; all 5 dirs must exist |
| "Bad or no parameters for mandatory networking" | Malformed `init-cfg.txt` | Check for spaces, missing `type` field, or incomplete static IP config |
| "Failed to install license key using authcode" | Invalid/expired auth code | Verify in the Customer Support Portal |
| "Failed content update commits" | Content version incompatible with PAN-OS | Use the minimum content version for your target PAN-OS version |
| Firewall boots but does not appear in Panorama | Network connectivity or expired VM auth key | Verify firewall can reach Panorama on port 3978; check key expiration |

### Detailed Troubleshooting Steps

1. **Read the bootstrap log:** `debug logview component bts_details`
2. **Test GCS access independently:** Launch a test instance with the same service account and run `gsutil ls gs://your-bucket/config/`
3. **Validate init-cfg.txt:** Open in a hex editor to check for BOM markers or Windows line endings that may cause issues.
4. **Verify Panorama readiness:** The Device Group and Template Stack must exist before the firewall attempts to register.
5. **Review instance serial console output:** In the GCP Console, navigate to **Compute Engine > VM instances**, click the instance, and select **Serial port 1 (console)** under the Logs section.
6. **Check VM auth key expiration:** On Panorama: `request bootstrap vm-auth-key show`
7. **Check service account permissions:** Verify the service account has `roles/storage.objectViewer` on the GCS bucket:
   ```bash
   gsutil iam get gs://your-bootstrap-bucket
   ```
8. **Check instance metadata:** Verify metadata was applied correctly:
   ```bash
   gcloud compute instances describe fw-prod-01 \
     --zone=us-central1-a \
     --format="yaml(metadata)"
   ```

### Plugin IP-Tag Issues

If you have a standalone Panorama or two Panorama appliances in an HA pair with multiple plugins installed, plugins might not receive updated IP-tag information if one or more of the plugins is not configured. This occurs because Panorama will not forward IP-tag information to unconfigured plugins.

This issue can also occur if one or more of the Panorama plugins is not in the **Registered** or **Success** state (the positive state differs by plugin). Ensure that your plugins are in a positive state before continuing.

**Workaround 1: Uninstall unconfigured plugins**

It is recommended that you do not install a plugin that you do not plan to configure right away. If you have unconfigured plugins, uninstall them:

1. Navigate to **Panorama > Plugins**.
2. Select the unconfigured plugin and click **Uninstall**.

**Workaround 2: Unblock device push for unconfigured plugins**

Execute the following command for each unconfigured plugin on each Panorama instance to prevent Panorama from waiting to send updates:

```
request plugins dau plugin-name <plugin-name> unblock-device-push yes
```

To cancel this workaround:

```
request plugins dau plugin-name <plugin-name> unblock-device-push no
```

> **Important:** These commands are **not persistent across reboots** and must be re-executed after any Panorama restart. For Panorama in an HA pair, the commands must be executed on **each** Panorama instance.

Without this workaround, your firewalls may lose some IP-tag information, which can affect Dynamic Address Group membership and security policy enforcement.

---

## Reference Tables

### init-cfg.txt Parameters

| Parameter | Description | Required |
|---|---|---|
| `type` | `dhcp` or `static` | Yes |
| `ip-address` | Management IP | If static |
| `netmask` | Subnet mask | If static |
| `default-gateway` | Default gateway | If static |
| `hostname` | Firewall hostname | No |
| `dns-primary` | Primary DNS | No |
| `dns-secondary` | Secondary DNS | No |
| `panorama-server` | Panorama IP or `cloud` | No |
| `panorama-server-2` | Secondary Panorama IP | No |
| `tplname` | Template Stack name | For Panorama |
| `dgname` | Device Group name | For Panorama |
| `vm-auth-key` | Manual VM auth key | Methods 2-3 |
| `auth-key` | Plugin-generated key | Method 1 |
| `authcodes` | License auth code | Methods 2-4 |
| `plugin-op-commands` | Comma-separated commands | Varies |
| `vm-series-auto-registration-pin-id` | Registration PIN ID | Recommended |
| `vm-series-auto-registration-pin-value` | Registration PIN value | Recommended |
| `dhcp-send-hostname` | `yes` to send hostname | No |
| `dhcp-send-client-id` | `yes` to send client ID | No |
| `dhcp-accept-server-hostname` | `yes` to accept hostname | No |
| `dhcp-accept-server-domain` | `yes` to accept domain | No |

### plugin-op-commands Values

| Command | Purpose |
|---|---|
| `panorama-licensing-mode-on` | Enable Panorama licensing (Method 1) |
| `advance-routing:enable` | Advanced routing (PAN-OS 11.0+) |

### Bootstrap Package Directory Structure (Methods 3-4)

```
/
  config/           init-cfg.txt (required), bootstrap.xml (Method 4 only)
  content/          Content update files (Method 4) or empty
  license/          authcodes file
  software/         PAN-OS images (Method 4) or empty
  plugins/          VM-Series plugin (optional, Method 4)
```
