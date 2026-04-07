# VM-Series Firewall Bootstrap Guide (Azure) -- Choose Your Path

Pick your deployment scenario and follow the tailored path. Each branch gives you only the steps relevant to your chosen method.

> **See also:** [AWS Guide](../aws/branching-guide.md) | [GCP Guide](../gcp/branching-guide.md)

---

## Table of Contents

1. [Prerequisites Checklist](#prerequisites-checklist-all-methods)
2. [Method 1: Panorama Licensing Plugin](#method-1-panorama-licensing-plugin)
3. [Method 2: Simple Custom Data Bootstrap](#method-2-simple-custom-data-bootstrap)
4. [Method 3: Azure File Share Basic Bootstrap with init-cfg and authcode](#method-3-azure-file-share-basic-bootstrap-with-init-cfg-and-authcode)
5. [Method 4: Azure File Share Full Bootstrap with bootstrap.xml](#method-4-azure-file-share-full-bootstrap-with-bootstrapxml)

---

## Prerequisites Checklist (All Methods)

Complete all applicable items before bootstrapping. Each section includes setup instructions.

1. [ ] [**1 Software NGFW Credit Pool**](#activate-software-ngfw-credits) — activated and funded ([Activate Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-credits))
2. [ ] [**2 Deployment Profile**](#create-a-deployment-profile) — created with auth code ([Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series))
3. [ ] [**3 Device Group**](#create-a-device-group-on-panorama) — created on Panorama ([Manage Device Groups](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-device-groups))
4. [ ] [**4 Template Stack**](#create-a-template-stack-on-panorama) — created on Panorama ([Manage Templates and Template Stacks](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-templates-and-template-stacks))
5. [ ] [**5 Auth Code**](#obtain-the-auth-code) — obtained for bootstrap definitions ([Manage a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/manage-a-deployment-profile))
6. [ ] [**6 Auto-Registration PIN ID & PIN Value**](#generate-auto-registration-pin-id-and-pin-value) — generated for device certificates ([Install a Device Certificate](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/install-a-device-certificate-on-the-vm-series-firewall))
7. [ ] [**7 Backhaul Connectivity to Panorama**](#establish-backhaul-connectivity-to-panorama) — ExpressRoute, VPN, or VNet peering established
8. [ ] [**8 Network Security Groups (NSGs)**](#configure-network-security-groups-nsgs) — Panorama ports and management access configured ([Ports Used for Panorama](https://docs.paloaltonetworks.com/pan-os/11-0/pan-os-admin/firewall-administration/reference-port-number-usage/ports-used-for-panorama))
9. [ ] [**9 Azure Marketplace Subscription**](#accept-the-azure-marketplace-subscription) — accepted for your license model
10. [ ] [**10 VM-Series Azure Image**](#discover-the-vm-series-azure-image) — identified for your region
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
   - **Profile Name** — e.g., `azure-prod`
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
2. Create a base template first (if none exist): click **Add**, name it (e.g., `TPL-BASE-AZURE`), click **OK**.
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
- **Azure ExpressRoute** — dedicated private connection from your data center to Azure
- **Point-to-Point VPN (IPsec)** — site-to-site VPN tunnel to the VNet

**If Panorama is in Azure:**
- **VNet Peering** — direct peering between the firewall VNet and the Panorama VNet
- **Azure Virtual WAN / vHub** — attach both VNets to a shared Virtual WAN hub and configure route tables

> Verify routing end-to-end. The firewall management subnet must have a route to Panorama, and Panorama must have a return route. Test with `nc -zv <panorama-ip> 3978` from a VM in the management subnet before deploying.

### Configure Network Security Groups (NSGs)

Apply to **all** management subnets where firewalls will be deployed. For the full list of ports, see [Ports Used for Panorama](https://docs.paloaltonetworks.com/pan-os/11-0/pan-os-admin/firewall-administration/reference-port-number-usage/ports-used-for-panorama).

**Panorama communication (required for all Panorama-managed methods):**

| Direction | Port | Purpose |
|---|---|---|
| Outbound to Panorama | TCP 3978 | Device registration and config sync |
| Outbound to Panorama | TCP 28443 | Panorama-to-device communication (PAN-OS 8.1+) |
| Inbound from Panorama | TCP 3978 | Panorama-initiated connections |
| Inbound from Panorama | TCP 28443 | Panorama-initiated connections |

**Management access (UI/SSH to firewalls):**

| Direction | Port | Purpose |
|---|---|---|
| Inbound from mgmt subnets | TCP 443 | Web UI (HTTPS) |
| Inbound from mgmt subnets | TCP 22 | SSH access |

> Ensure the Panorama-side NSGs also allow inbound from firewall management subnets on 3978 and 28443. For VM Scale Sets, pre-configure rules on all subnets across availability zones.

### Accept the Azure Marketplace Subscription

You must accept the Azure Marketplace terms before deploying VM-Series instances. This is a one-time action per Azure subscription per plan.

**Via Azure Portal:**

1. Navigate to the [Azure Marketplace — Palo Alto VM-Series](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/MarketplaceOffersBlade/searchQuery/palo%20alto%20vm-series).
2. Select the **VM-Series Next-Generation Firewall** listing (publisher: Palo Alto Networks).
3. Choose your plan (BYOL, Bundle 1, or Bundle 2) and click **Create**.
4. Accept the terms on the first page of the deployment wizard. You do not need to complete the deployment.

**Via Azure CLI:**

Accept terms for each plan you intend to use:

```bash
# BYOL
az vm image terms accept \
  --publisher paloaltonetworksgx \
  --offer vmseries-flex \
  --plan byol

# Bundle 1 (PAYG)
az vm image terms accept \
  --publisher paloaltonetworksgx \
  --offer vmseries-flex \
  --plan bundle1

# Bundle 2 (PAYG)
az vm image terms accept \
  --publisher paloaltonetworksgx \
  --offer vmseries-flex \
  --plan bundle2
```

Check if terms have already been accepted:

```bash
az vm image terms show \
  --publisher paloaltonetworksgx \
  --offer vmseries-flex \
  --plan byol \
  --query 'accepted'
```

### Discover the VM-Series Azure Image

```bash
# List all available VM-Series Flex images
az vm image list \
  --publisher paloaltonetworksgx \
  --offer vmseries-flex \
  --all \
  --output table

# List images for a specific plan (e.g., BYOL)
az vm image list \
  --publisher paloaltonetworksgx \
  --offer vmseries-flex \
  --sku byol \
  --all \
  --output table
```

Common plans: BYOL = `byol` | Bundle 1 = `bundle1` | Bundle 2 = `bundle2`

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
  |           +-- YES --> Method 4: Azure File Share full bootstrap with bootstrap.xml
  |           |
  |           +-- NO: Do you want to avoid Azure File Shares?
  |                 |
  |                 +-- YES --> Method 2: Simple Custom Data Bootstrap
  |                 |
  |                 +-- NO --> Method 3: Azure File Share basic bootstrap
  |
  +-- NO (using SCM): --> SCM Bootstrap Variant
```

---

## Method 1: Panorama Licensing Plugin

> **Palo Alto Docs:** [Use Panorama-Based Software Firewall License Management](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/use-panorama-based-software-firewall-license-management)

This is the recommended method for production and auto-scaling environments. Panorama handles licensing automatically.

> **Internet Access:** This method does **not** require the firewalls to have direct internet access via the management interface -- Panorama handles all licensing on their behalf. However, Panorama itself **must** have direct internet access to reach `updates.paloaltonetworks.com`.

> **PAYG Note:** If you are using a PAYG (pay-as-you-go) license from the Azure Marketplace, you do **not** need the SW Firewall License plugin. PAYG firewalls are licensed directly through the marketplace. Skip to Method 2 for PAYG deployments.

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
3. Enter a **Name** for the bootstrap definition (e.g., `bsd-azure-prod`).
4. Enter the **Auth Code** from your [deployment profile](#create-a-deployment-profile) (format: `D1234567`).
5. Optionally enter a **Description**.
6. Click **OK**.

> Each bootstrap definition maps to a single deployment profile auth code. Create a separate bootstrap definition for each deployment profile.

### Step 3: Configure a License Manager

1. Go to **Panorama > SW Firewall License > License Managers**.
2. Click **Add** and configure:
   - **Name** — e.g., `lm-azure-prod`
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
custom_data = base64encode(join(";", [
  # ── Minimum required values ──────────────────────────────────────
  "plugin-op-commands=panorama-licensing-mode-on",
  "auth-key=YOUR-AUTH-KEY-HERE",
  "panorama-server=YOUR-PANORAMA-SERVER-1-HERE",
  "dgname=YOUR-DG-HERE",
  "tplname=YOUR-STACK-HERE",

  # ── Optional: secondary Panorama ─────────────────────────────────
  "panorama-server-2=YOUR-PANORAMA-2-SERVER-HERE",

  # ── Optional: DHCP settings ──────────────────────────────────────
  "dhcp-send-hostname=yes",
  "dhcp-send-client-id=yes",
  "dhcp-accept-server-hostname=yes",
  "dhcp-accept-server-domain=yes",

  # ── Optional (best practice): device certificate auto-registration
  "vm-series-auto-registration-pin-id=YOUR-PIN-ID-HERE",
  "vm-series-auto-registration-pin-value=YOUR-PIN-VALUE-HERE",
]))
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

Key points:
- Azure does not use `mgmt-interface-swap` -- the management interface is always the first interface
- Do **not** include `authcodes` or `vm-auth-key` when using this method

### Step 5b: Custom Data Alternative

```
plugin-op-commands=panorama-licensing-mode-on;auth-key=YOUR-AUTH-KEY-HERE;panorama-server=YOUR-PANORAMA-SERVER-1-HERE;panorama-server-2=YOUR-PANORAMA-2-SERVER-HERE;dgname=YOUR-DG-HERE;tplname=YOUR-STACK-HERE;dhcp-send-hostname=yes;dhcp-send-client-id=yes;dhcp-accept-server-hostname=yes;dhcp-accept-server-domain=yes;vm-series-auto-registration-pin-id=YOUR-PIN-ID-HERE;vm-series-auto-registration-pin-value=YOUR-PIN-VALUE-HERE
```

> **Rule:** No spaces around `=` signs. Use semicolons as delimiters.

**Important:** Do NOT include `authcodes` or `vm-auth-key` with this method. The plugin-generated `auth-key` replaces both.

**Skip to:** [Verification](#verification)

---

## Method 2: Simple Custom Data Bootstrap

**Best for:** Quick one-off deployments, dev/test environments, getting a firewall up fast.

**Why this method:** No Azure File Share, no storage account access key management, no bootstrap file structure. Everything is in custom data.

> **Internet Access:** This method **requires** the firewall management interfaces to have direct internet access to reach `updates.paloaltonetworks.com` for licensing. This can be accomplished via a **NAT gateway** (preferred) or with a public IP on the management interface (not recommended -- if a public IP is used, ensure the management interface NSG is locked down as tightly as possible).

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
custom_data = base64encode(join(";", [
  # ── Minimum required values ──────────────────────────────────────
  "authcodes=D1234567",
  "vm-auth-key=YOUR-VM-AUTH-KEY-HERE",
  "panorama-server=YOUR-PANORAMA-SERVER-1-HERE",
  "dgname=YOUR-DG-HERE",
  "tplname=YOUR-STACK-HERE",

  # ── Optional: secondary Panorama ─────────────────────────────────
  "panorama-server-2=YOUR-PANORAMA-2-SERVER-HERE",

  # ── Optional: DHCP settings ──────────────────────────────────────
  "dhcp-send-hostname=yes",
  "dhcp-send-client-id=yes",
  "dhcp-accept-server-hostname=yes",
  "dhcp-accept-server-domain=yes",

  # ── Optional (best practice): device certificate auto-registration
  "vm-series-auto-registration-pin-id=YOUR-PIN-ID-HERE",
  "vm-series-auto-registration-pin-value=YOUR-PIN-VALUE-HERE",
]))
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

### Step 2b: Custom Data Alternative

```
authcodes=D1234567;vm-auth-key=YOUR-VM-AUTH-KEY-HERE;panorama-server=YOUR-PANORAMA-SERVER-1-HERE;dgname=YOUR-DG-HERE;tplname=YOUR-STACK-HERE;panorama-server-2=YOUR-PANORAMA-2-SERVER-HERE;dhcp-send-hostname=yes;dhcp-send-client-id=yes;dhcp-accept-server-hostname=yes;dhcp-accept-server-domain=yes;vm-series-auto-registration-pin-id=YOUR-PIN-ID-HERE;vm-series-auto-registration-pin-value=YOUR-PIN-VALUE-HERE
```

> **Rule:** No spaces around `=` signs. Use semicolons as delimiters.

**Skip to:** [Verification](#verification)

---

## Method 3: Azure File Share Basic Bootstrap with init-cfg and authcode

**Best for:** Environments that need a structured bootstrap package but do not need to bundle PAN-OS software or content updates.

**Why this method:** More organized than custom data, supports teams that manage bootstrap files in version control, but avoids the complexity of bundling large binary files.

> **Internet Access:** This method **requires** the firewall management interfaces to have direct internet access to reach `updates.paloaltonetworks.com` for licensing. This can be accomplished via a **NAT gateway** (preferred) or with a public IP on the management interface (not recommended -- if a public IP is used, ensure the management interface NSG is locked down as tightly as possible).

### Azure File Share Directory Structure

The bootstrap Azure File Share requires the following five directories. All five **must** exist, even if empty -- the firewall checks for this structure during bootstrap and will fail if any directory is missing.

```
<storage-account>/<file-share>/
  config/
  content/
  license/
  plugins/
  software/
```

#### Creating the Storage Account, File Share, and Directory Structure

```bash
# Create a resource group (if needed)
az group create \
  --name your-bootstrap-rg \
  --location eastus

# Create the storage account
az storage account create \
  --name yourstorageaccount \
  --resource-group your-bootstrap-rg \
  --location eastus \
  --sku Standard_LRS

# Create the file share
az storage share create \
  --name bootstrap \
  --account-name yourstorageaccount

# Create the required directory structure
az storage directory create --share-name bootstrap --name config --account-name yourstorageaccount
az storage directory create --share-name bootstrap --name content --account-name yourstorageaccount
az storage directory create --share-name bootstrap --name license --account-name yourstorageaccount
az storage directory create --share-name bootstrap --name plugins --account-name yourstorageaccount
az storage directory create --share-name bootstrap --name software --account-name yourstorageaccount
```

Alternatively, create the storage account and file share through the [Azure Portal](https://portal.azure.com).

> **Important:** Azure VM-Series bootstraps from an **Azure File Share** (SMB), not Blob Storage containers. Ensure you create a File Share, not a Blob container.

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
dns-primary=168.63.129.16
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
| `dns-primary` | Primary DNS server | `168.63.129.16` |
| `vm-series-auto-registration-pin-id` | PIN ID for device certificate auto-registration | `YOUR-PIN-ID-HERE` |
| `vm-series-auto-registration-pin-value` | PIN value for device certificate auto-registration | `YOUR-PIN-VALUE-HERE` |

### Create the authcodes File

Place in `/license/authcodes`:

> **Important:** The file is named `authcodes` with **no file extension** -- not `authcodes.txt`, not `authcodes.key`. The firewall expects this exact filename. The file must be plain text with no trailing whitespace or blank lines.

```
D1234567
```

#### Upload Files to the File Share

```bash
# Upload init-cfg.txt to the config directory
az storage file upload \
  --share-name bootstrap \
  --source init-cfg.txt \
  --path config/init-cfg.txt \
  --account-name yourstorageaccount

# Upload authcodes to the license directory
az storage file upload \
  --share-name bootstrap \
  --source authcodes \
  --path license/authcodes \
  --account-name yourstorageaccount
```

> **Palo Alto Docs:** [Prepare the Bootstrap Package](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package)

### Get the Storage Account Access Key

The VM-Series firewall needs the storage account access key to authenticate to the Azure File Share during bootstrap.

```bash
az storage account keys list \
  --resource-group your-bootstrap-rg \
  --account-name yourstorageaccount \
  --output table
```

Copy the value of `key1` -- this is used as the `access-key` bootstrap parameter.

> **Alternative: Managed Identity** — Instead of using an access key, you can assign a **Managed Identity** to the VM with the **Storage File Data SMB Share Reader** role on the storage account. However, for Azure File Share-based bootstrap, the access key method is the standard approach.

### Point the Instance to the File Share

In custom data:

```
storage-account=yourstorageaccount;access-key=YOUR-ACCESS-KEY;file-share=bootstrap;share-directory=
```

**Terraform example:**

```hcl
custom_data = base64encode(
  "storage-account=yourstorageaccount;access-key=YOUR-ACCESS-KEY;file-share=bootstrap;share-directory="
)
```

**Skip to:** [Verification](#verification)

---

## Method 4: Azure File Share Full Bootstrap with bootstrap.xml

**Best for:** Standalone firewalls, air-gapped deployments, zero-touch provisioning where the firewall must boot fully configured without Panorama or SCM.

**Why this method:** The `bootstrap.xml` is a full VM-Series configuration file -- the firewall applies it on first boot, including interfaces, security policies, NAT rules, and routing. This method is generally **not used** when Panorama or SCM are managing the firewalls, since those platforms push configuration after bootstrap.

> **Internet Access:** This method **requires** the firewall management interfaces to have direct internet access to reach `updates.paloaltonetworks.com` for licensing. This can be accomplished via a **NAT gateway** (preferred) or with a public IP on the management interface (not recommended -- if a public IP is used, ensure the management interface NSG is locked down as tightly as possible).

### Azure File Share Directory Structure

Same as Method 3. All five directories must exist. See [Method 3](#method-3-azure-file-share-basic-bootstrap-with-init-cfg-and-authcode) for Azure CLI commands to create the storage account, file share, and directory structure.

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

### Get the Storage Account Access Key

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

> **Warning:** When using a configuration from another firewall as a seed, the following values will almost certainly differ if the new firewall is in a different region, availability zone, or resource group:
>
> - **Management interface IP address** (`ip-address`, `netmask`, `default-gateway`) -- these are environment-specific
> - **Default routes and gateway IPs** -- vary by VNet/subnet
> - **Interface IP addresses** -- dataplane interface IPs tied to the specific subnet
> - **DNS server addresses** -- may differ between environments
> - **Hostname** -- should be unique per firewall
> - **Zone and interface mappings** -- verify they match the new network topology
>
> Review and update these values in the `bootstrap.xml` before placing it in the Azure File Share. Deploying with incorrect network values will result in an unreachable firewall.

#### Upload bootstrap.xml to the File Share

```bash
az storage file upload \
  --share-name bootstrap \
  --source bootstrap.xml \
  --path config/bootstrap.xml \
  --account-name yourstorageaccount
```

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
custom_data = base64encode(join(";", [
  "panorama-server=cloud",
  "dgname=scm_folder_name",
  "dhcp-send-hostname=yes",
  "dhcp-send-client-id=yes",
  "dhcp-accept-server-hostname=yes",
  "dhcp-accept-server-domain=yes",
  "plugin-op-commands=advance-routing:enable",
  "vm-series-auto-registration-pin-id=YOUR-PIN-ID-HERE",
  "vm-series-auto-registration-pin-value=YOUR-PIN-VALUE-HERE",
  "authcodes=D1234567",
]))
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
| Firewall stuck at `192.168.1.1` | Bootstrap failed, reverted to factory defaults | Check `init-cfg.txt` syntax (no spaces around `=`), verify Azure File Share access |
| "Boot image error" | File Share not found or access key incorrect | Test access: `az storage file list --share-name bootstrap --account-name yourstorageaccount --output table` |
| "No bootstrap config file" | `init-cfg.txt` missing from `/config` | Verify directory structure; all 5 dirs must exist |
| "Bad or no parameters for mandatory networking" | Malformed `init-cfg.txt` | Check for spaces, missing `type` field, or incomplete static IP config |
| "Failed to install license key using authcode" | Invalid/expired auth code | Verify in the Customer Support Portal |
| "Failed content update commits" | Content version incompatible with PAN-OS | Use the minimum content version for your target PAN-OS version |
| Firewall boots but does not appear in Panorama | Network connectivity or expired VM auth key | Verify firewall can reach Panorama on port 3978; check key expiration |

### Detailed Troubleshooting Steps

1. **Read the bootstrap log:** `debug logview component bts_details`
2. **Test Azure File Share access independently:** Verify from the Azure CLI: `az storage file list --share-name bootstrap --account-name yourstorageaccount --output table`
3. **Validate init-cfg.txt:** Open in a hex editor to check for BOM markers or Windows line endings that may cause issues.
4. **Verify Panorama readiness:** The Device Group and Template Stack must exist before the firewall attempts to register.
5. **Check boot diagnostics:** In the Azure Portal, navigate to the VM and check **Help > Boot diagnostics** for serial console output.
6. **Check VM auth key expiration:** On Panorama: `request bootstrap vm-auth-key show`
7. **Verify custom data:** In the Azure Portal, navigate to the VM and check **Settings > Extensions + applications** or review the custom data under **Export template** to confirm the bootstrap string was passed correctly.
8. **Check storage account access key:** Ensure the access key in the custom data matches the current key. Keys can be rotated, which invalidates previously used keys:
   ```bash
   az storage account keys list \
     --resource-group your-bootstrap-rg \
     --account-name yourstorageaccount \
     --output table
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
