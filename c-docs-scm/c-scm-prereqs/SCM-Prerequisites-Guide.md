# Strata Cloud Manager: Prerequisites & Onboarding Checklist

> **Purpose:** A single, process-oriented guide that walks you through everything needed to successfully onboard firewalls and Prisma Access to Strata Cloud Manager (SCM). Follow the phases in order — each builds on the previous one.
>
> **Source Documentation:** This guide consolidates content from the [official SCM prerequisites](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites) and related pages.
>
> **Companion files:**
> - [Device Onboarding Tracker (CSV)](./SCM-Onboarding-Tracker.csv) — Per-device tracking spreadsheet
> - Screenshots are referenced throughout with `[SCREENSHOT]` markers — see [Appendix B](#appendix-b-screenshot-guide) for capture instructions

---

## How to Use This Guide

Work through **Phase 1 through Phase 4** in sequence. Each phase has a checklist. Complete every required item before moving to the next phase. Optional items are marked accordingly. Once all prerequisites are met, proceed to the **[SCM Onboarding Guide](https://github.com/jollymahn/scm-onboarding-guide)**.

**Audience paths:**
- **NGFW (hardware firewalls):** All 4 phases
- **VM-Series (Software NGFW Credits):** All 4 phases (includes deployment profile creation in Phase 2)
- **Prisma Access:** Phases 1 and 2 only (certificates handled differently)

- **Panorama-managed firewalls:** All 4 phases (use Section 4.2 for certificates)

---

## Phase 1: Verify Hardware & Software Compatibility

Before anything else, confirm your devices can actually be onboarded to SCM.

### 1.1 Supported Firewall Models

Verify your hardware is on the supported list for SCM:

| Series | Supported Models |
|---|---|
| Panorama Virtual Appliances | PRA-25, PRA-100, PRA-1000 |
| VM-Series | VM-200, VM-300, VM-500, VM-600, VM-700 |
| PA-200 Series | PA-220 |
| PA-400 Series | PA-410, PA-410R, PA-440, PA-450, PA-450R, PA-460 |
| PA-800 Series | PA-820, PA-850 |
| PA-3000 Series | PA-3220, PA-3250, PA-3260, PA-3410, PA-3420, PA-3430, PA-3440 |
| PA-5000 Series | PA-5220, PA-5250, PA-5260, PA-5280, PA-5410, PA-5420, PA-5430, PA-5445, PA-5450 |
| PA-7000 Series | PA-7050, PA-7080 |

> **Compatibility reference:** [Hardware Model Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility)

> **Important restrictions:**
> - **PA-410** is not supported if the Enterprise DLP license is active
> - **Multi-vsys is NOT supported** — only single vsys configurations work with SCM

### 1.2 PAN-OS Version Requirements

- **Minimum:** PAN-OS **10.2.3** for all firewalls and Panorama
- **Recommended for auto-telemetry:** PAN-OS 10.2.17+, 11.1.11+, 11.2.8+, or 12.1.2+ (telemetry enables automatically on these versions)

### 1.3 Checklist: Hardware & Software Compatibility

- [ ] All firewalls are on the supported hardware model list
- [ ] All firewalls run **PAN-OS 10.2.3 or later**
- [ ] Confirmed **single vsys** configuration (multi-vsys not supported)

---

## Phase 2: Licensing & Account Readiness

With hardware and software confirmed, ensure you have the right licenses and accounts in place.

### 2.1 Choose Your SCM License Tier

| Feature | SCM Essentials (Free) | SCM Pro (Paid) |
|---|---|---|
| Cost | Included with NGFW / Prisma Access purchase | Paid upgrade |
| Operational Health | Basic hardware/software alerts | Advanced forecasting, RCA, Capacity Analyzer |
| Security Posture | Best Practice Analysis (BPA) | Real-time enforcement, Policy Analyzer (ML), Compliance |
| Config Management | Cloud management for NGFW/Prisma | Full capabilities |
| Strata Logging Service | Separate add-on | Included (1-year default retention) |
| ADEM | No | AI-Powered ADEM |
| In-App Support Cases | No | Yes (requires Platinum Support) |
| Strata Copilot | Yes | Yes |

> **License migration note:** As of May 8, 2025, legacy license types (AIOps for NGFW Premium, AI-Powered ADEM, Strata Logging Service sized storage) reached end-of-sale. Existing customers are being migrated automatically at no additional cost:
> - AIOps for NGFW Free → **SCM Essentials**
> - AIOps for NGFW Premium + Logging → **SCM Pro for NGFW**
> - Prisma Access + ADEM + Logging → **SCM Pro for Prisma Access**

> `[SCREENSHOT 1]` **Activation Console — Tenant Overview** — Capture: Log into the [Activation Console](https://apps.paloaltonetworks.com/hub) → navigate to **Common Services > Tenant Management**. Screenshot showing your active SCM license tier and associated products.

### 2.2 Activate & Verify License Status

1. Log in to the [Activation Console](https://apps.paloaltonetworks.com/hub)
2. Navigate to **Common Services > Tenant Management**
3. Verify your SCM license tier (Essentials or Pro) is active
4. Check that the **Activation Status** shows **Complete**
5. If using SCM Pro, confirm **Strata Logging Service** shows as included
6. If using SCM Essentials and you need logging, activate the **SLS add-on** separately

> **Warning:** The Activation Status must show **Complete** before you proceed. License provisioning can take up to **30 minutes**. If the status shows "In Progress" or "Pending," wait for it to complete before continuing — services will not function until provisioning finishes.

### 2.3 Verify Deployment Profile Association (VM-Series only)

This section applies if you are deploying VM-Series firewalls using Software NGFW Credits. It assumes you have already activated a credit pool and created a deployment profile in the Customer Support Portal. If you have not yet created a deployment profile, see [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) first.

Once your SCM license activation is complete, verify that your deployment profile is associated with the correct tenant:

1. In the [Activation Console](https://apps.paloaltonetworks.com/hub), navigate to **Common Services > Tenant Management > Deployment Profiles**
2. Locate your deployment profile (search by name or auth code starting with "D")
3. Check the **Profile Association Status**:
   - If it shows **Complete** — your profile is correctly associated. Proceed to Section 2.4.
   - If it shows **Associating** — provisioning is in progress. Wait up to 50 minutes for it to complete.
   - If your deployment profile is **not listed** — it has not been associated with this tenant yet. Follow the steps below.

#### Associate a Deployment Profile with Your Tenant

If your deployment profile does not appear under the tenant's Deployment Profiles tab:

1. Navigate to **Common Services > Subscriptions & Add-ons**
2. Look for your deployment profile under **Ready for Activation** — click **Activate Now**
   - *Alternatively:* In CSP under **Software NGFW Credits > Current Deployment Profiles**, click **Finish SetUp** next to the profile — this redirects you to the Activation Console
3. Authenticate with SSO if prompted
4. On the **Activate Subscriptions based on Deployment Profiles** page:
   - Select the **CSP account** you are subscribed to
   - Select (or create) the target **tenant** and **region**
   - Select the **deployment profile** to associate (search by name or auth code)
5. *(Optional)* Select **Additional Services** such as Cloud Identity Engine
6. Agree to Terms and Conditions → click **Activate**
7. Wait for the **Profile Association Status** to show **Complete** (provisioning takes approximately 15–50 minutes)

> **Important:** A deployment profile can only be associated with one Tenant Service Group (TSG) at a time. All deployment profiles linked to a TSG must use the same cloud subscription type — you cannot mix SCM Pro and SLS-only profiles under the same TSG.

> **Reference:** [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) | [Activate the Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-the-deployment-profile)

> **VM-Series: Not Yet Deployed?** VM-Series firewalls do not have serial numbers until they are deployed, licensed, and bootstrapped. This is why the deployment profile is important — the auth code from your deployment profile must be included in the bootstrap data so the firewall can license and register itself automatically.
>
> If your VM-Series firewalls have not been deployed yet, **skip Section 2.4 for now** — you will associate them after deployment. VM-Series firewalls using Software NGFW Credits register automatically when they boot with a valid auth code and auto-registration PIN, so they will appear in Device Associations once deployed. Hardware NGFWs should be associated at this stage.
>
> See [Step 5: VM-Series Specific Prerequisites](#step5) for bootstrap configuration details, including how to include the auth code and auto-registration PIN in your init-cfg.txt or cloud instance user data.

### 2.4 Associate Devices to Tenant

1. In the [Activation Console](https://apps.paloaltonetworks.com/hub), navigate to **Common Services > Device Associations**
2. Click **Add Devices**
3. Select all firewalls to be onboarded by their serial numbers
4. Confirm each device has an **active support license**
5. Click **Save**

> **Note:** Devices must have a valid device certificate installed **before** they will associate with the correct tenant and can be onboarded to SCM.
> - **Hardware NGFWs:** Generate an OTP and install the certificate manually or via Panorama. See [Phase 4: Install Device Certificates](#phase-4-install-device-certificates). You also need a [Customer Support Portal (CSP)](https://support.paloaltonetworks.com) account with Super User or Standard User role for OTP generation.
> - **VM-Series:** The device certificate is installed automatically during bootstrap when you include the **auto-registration PIN ID** and **PIN Value** in your init-cfg.txt or cloud instance user data. This is why the PIN is a required element in the SCM bootstrap process. See [Step 5, Section 5.4: Generate Auto-Registration PIN](#54-generate-auto-registration-pin) for details.

### 2.5 Prisma Access Requirements (if applicable)

- [ ] Panorama version **10.0 or higher** (if currently Panorama-managed)
- [ ] Account with **superuser** privileges
- [ ] Valid **Prisma Access license**
- [ ] **Cloud Identity Engine Directory Sync** integrated with Prisma Access tenant
- [ ] Understand that **migration from Panorama to SCM is one-way** — you cannot switch back

### 2.6 Checklist: Licensing & Accounts

- [ ] **Customer Support Portal (CSP) account** — You have an account at [support.paloaltonetworks.com](https://support.paloaltonetworks.com) with an appropriate role (Super User or Standard User)
- [ ] **Activation Console access** — You can log into the [Activation Console](https://apps.paloaltonetworks.com/hub) (also referred to as "the Hub")
- [ ] **SCM license activated** — Either SCM Essentials or SCM Pro is activated for your tenant, Activation Status shows **Complete**
- [ ] **Support license active** — Active support license on all devices to be onboarded
- [ ] **Strata Logging Service** — If using SCM Pro, confirm SLS is included; if using Essentials, determine if you need the SLS add-on
- [ ] *(VM-Series only)* Deployment profile associated with tenant (Profile Association Status shows **Complete**)
- [ ] **Devices associated to tenant** — All hardware firewalls are associated with the correct tenant in the Activation Console under **Common Services > Device Associations** (VM-Series: skip if not yet deployed — they auto-register on first boot)
- [ ] *(Prisma Access only)* All Prisma Access requirements confirmed

---

## Phase 3: Network & Connectivity Preparation

This is the phase most commonly missed. All these ports and FQDNs must be open **before** you attempt onboarding.

### 3.1 Required Outbound Ports

| Port | Protocol | Purpose |
|---|---|---|
| **TCP 80** | HTTP | OCSP/CRL certificate validation |
| **TCP 443** | HTTPS | SCM communication, certificates, telemetry |
| **TCP 444** | SSL | Strata Logging Service |
| **TCP 3978** | Custom | SCM management, SLS, Panorama |
| **TCP 5222-5224, 5228, 5229** | Custom | Device telemetry (PAN-OS 10.0+) |

### 3.2 Required FQDNs — Certificate Services

These must be reachable for device certificates to install and renew:

| FQDN | Port | Purpose |
|---|---|---|
| `ocsp.paloaltonetworks.com` | 80 | OCSP validation |
| `crl.paloaltonetworks.com` | 80 | Certificate revocation list |
| `ocsp.godaddy.com` | 80 | OCSP validation (alternate CA) |
| `api.paloaltonetworks.com` | 443 | API services, certificate fetch |
| `apitrusted.paloaltonetworks.com` | 443 | Trusted API endpoint |
| `certificatetrusted.paloaltonetworks.com` | 443 | Certificate services |
| `certificate.paloaltonetworks.com` | 443 | Certificate services |

### 3.3 Required FQDNs — Strata Cloud Manager

| FQDN | Port | Purpose |
|---|---|---|
| `ds-cloudmgmt.paloaltonetworks.com` | 443 | Discovery service |
| `*.{region}.ngfw.cloudmgmt.paloaltonetworks.com` | 443 | Regional SCM endpoint (see 3.5) |

### 3.4 Required FQDNs — Strata Logging Service

| FQDN | Port | Purpose |
|---|---|---|
| `*.gpcloudservice.com` | 443, 444 | Logging service endpoints |
| `lic.lc.prod.us.cs.paloaltonetworks.com` | 444 | Legacy licensing (PAN-OS 9.1.7 or earlier) |

### 3.5 Required App-IDs (if using PA firewall to secure this traffic)

| App-ID | Ports | Notes |
|---|---|---|
| `paloalto-logging-service` | 444, 3978 | Not required for telemetry-only (no SLS license) |
| `paloalto-shared-services` | 444, 3978 | Required for general connectivity |
| `panorama` | 444, 3978 | Required if content version < 8290 |
| `paloalto-device-telemetry` | 443, 5222-5224, 5228, 5229 | Telemetry (PAN-OS 10.0+) |
| `google-base` | 443, 5222-5224, 5228, 5229 | Telemetry (PAN-OS 10.0+) |

### 3.6 Regional FQDNs for Panorama CloudConnector Plugin

If using the CloudConnector plugin, Panorama must reach your region's FQDN:

| Region | FQDN |
|---|---|
| Americas | `prod.us.secure-policy.cloudmgmt.paloaltonetworks.com` |
| Australia | `prod.au.secure-policy.cloudmgmt.paloaltonetworks.com` |
| Canada | `prod.ca.secure-policy.cloudmgmt.paloaltonetworks.com` |
| Europe | `prod.eu.secure-policy.cloudmgmt.paloaltonetworks.com` |
| FedRAMP | `prod.gov.secure-policy.cloudmgmt.paloaltonetworks.com` |
| Germany | `prod.de.secure-policy.cloudmgmt.paloaltonetworks.com` |
| India | `prod.in.secure-policy.cloudmgmt.paloaltonetworks.com` |
| Japan | `prod.jp.secure-policy.cloudmgmt.paloaltonetworks.com` |
| Singapore | `prod.sg.secure-policy.cloudmgmt.paloaltonetworks.com` |
| United Kingdom | `prod.uk.secure-policy.cloudmgmt.paloaltonetworks.com` |

### 3.7 Proxy Considerations

If outbound traffic routes through a proxy:
- The proxy must support non-standard SSL ports **TCP 3978** and **TCP 444**
- CloudConnector plugin 2.2.0+ supports proxy settings configured in Panorama (requires a commit after configuration; settings take effect on the *next* commit cycle)

### 3.8 Checklist: Network Readiness

- [ ] Outbound ports **80, 443, 444, 3978** are open
- [ ] Outbound ports **5222-5224, 5228, 5229** are open (for telemetry)
- [ ] All **certificate FQDNs** (Section 3.2) are reachable
- [ ] All **SCM FQDNs** (Section 3.3) are reachable, including your regional endpoint
- [ ] All **SLS FQDNs** (Section 3.4) are reachable
- [ ] *(If using PA firewall for transit)* App-IDs from Section 3.5 are allowed in security policy
- [ ] *(If using proxy)* Proxy allows TCP 3978 and TCP 444
- [ ] **DNS servers** are configured and resolving on each firewall
- [ ] **NTP servers** are configured and syncing on each firewall

---

## Phase 4: Install Device Certificates

Device certificates authenticate your firewalls with Palo Alto cloud services. This **must** be done before onboarding.

> **Auto-install models:** PA-400, PA-1400, PA-3400, PA-5400, PA-5450, PA-5500, and PA-7500 series firewalls install the certificate automatically during initial registration. Verify the certificate is valid; if not, follow the manual process below.

> **Certificate lifetime:** 90 days, with automatic renewal 15 days before expiration.

**Choose your workflow:**
- **Standalone firewalls** (not managed by Panorama) → follow [Section 4.1](#41-standalone-firewalls-generate-otp--install-certificate)
- **Panorama-managed firewalls** → follow [Section 4.2](#42-panorama-managed-firewalls-install-certificates-via-panorama)

---

### 4.1 Standalone Firewalls: Generate OTP & Install Certificate

Use this workflow when the firewall is **not** managed by Panorama.

#### 4.1.1 Generate a One-Time Password (OTP)

The OTP is valid for **60 minutes** and allows only **one attempt**.

1. Log into [Customer Support Portal](https://support.paloaltonetworks.com)
2. Navigate to **Products > Device Certificates**
3. Click **Generate OTP**
4. Select **Generate OTP for a Next-Gen Firewall (PAN-OS)** → **Next**
5. Select your device serial number → **Generate OTP**
6. **Download** or **Copy** the OTP immediately

> `[SCREENSHOT 2a]` **CSP OTP Generation (Standalone)** — Capture: The **Products > Device Certificates** page showing the OTP generation dialog with "Generate OTP for a Next-Gen Firewall (PAN-OS)" selected and your device serial number visible.

#### 4.1.2 Configure NTP & Install the Certificate

1. Log into the firewall web interface as **Superuser**
2. **Configure NTP** (required for certificate validation):
   - Go to **Device > Setup > Services** → edit **Services**
   - Select **NTP** → enter Primary NTP server (and optional Secondary)
   - Click **OK** → **Commit**
3. **Install the certificate** (choose one method):

   **Option A — Web Interface:**
   - Go to **Device > Setup > Management > Device Certificate**
   - Click **Get certificate** → paste the OTP → **OK**

   **Option B — CLI:**
   ```
   admin> request certificate fetch otp <otp_value>
   ```

4. Refresh the page and verify **Current Device Certificate Status** shows as valid

> `[SCREENSHOT 3a]` **Certificate Status (Standalone)** — Capture: **Device > Setup > Management > Device Certificate** showing the certificate status as "Valid" with the expiration date visible.

---

### 4.2 Panorama-Managed Firewalls: Install Certificates via Panorama

Use this workflow when firewalls are managed by Panorama. This allows you to install certificates on **multiple managed firewalls at once** from the Panorama console, without needing to log into each firewall individually.

> **Reference:** [Install the Device Certificate for a Managed Firewall](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/install-the-device-certificate-for-managed-firewalls/install-the-device-certificate-for-a-managed-firewall)

#### Prerequisites (Panorama-Managed)

- **Panorama role:** Superuser (required to generate the OTP Request Token)
- **Licenses:** Device Management license and Support license on Panorama
- **CSP alignment:** Managed firewalls must belong to the **same CSP account** as Panorama
- **Outbound internet access** from each managed firewall

#### 4.2.1 Configure NTP on Panorama and Managed Firewalls

1. **On Panorama:** Go to **Panorama > Setup > Services** → select **NTP** → enter the Primary (and optional Secondary) NTP server → **OK** → **Commit** to Panorama
2. **On managed firewalls (via Template):** Go to **Device > Setup > Services** and select the appropriate **Template**
   - For multi-vsys: Select **Global** and edit **Services**
   - For single-vsys: Edit **Services**
3. Enter NTP server details → **OK** → **Commit and Push** to managed firewalls

#### 4.2.2 Generate the OTP Request Token on Panorama

1. Log into Panorama as a **Superuser**
2. Navigate to **Panorama > Managed Devices > Summary**
3. Select the managed firewalls that require a certificate
4. Select **Request OTP From CSP > Custom selected devices**
5. **Copy** the entire output in the **OTP Request Token** field

> `[SCREENSHOT 2b]` **Panorama OTP Request Token** — Capture: **Panorama > Managed Devices > Summary** showing the "Request OTP From CSP" dialog with the OTP Request Token output visible.

#### 4.2.3 Generate the OTP on CSP (Panorama-Managed)

The OTP is valid for **60 minutes** and allows only **one attempt**.

1. Log into [Customer Support Portal](https://support.paloaltonetworks.com)
2. Navigate to **Products > Device Certificates > Generate OTP**
3. Select **Generate OTP for Panorama managed firewalls** → **Next**
4. **Paste** the OTP Request Token copied from Panorama → **Generate OTP**
5. Wait a few minutes, then go to **OTP History** → **Copy to Clipboard** the generated OTP

> `[SCREENSHOT 2c]` **CSP OTP Generation (Panorama-Managed)** — Capture: The **Products > Device Certificates** page showing "Generate OTP for Panorama managed firewalls" selected, with the OTP Request Token pasted.

#### 4.2.4 Upload OTP and Install Certificates

1. In the Panorama web interface, go to **Panorama > Managed Devices > Summary**
2. Click **Upload OTP**
3. **Paste** the OTP from CSP and click **Upload**
   - You **must paste** the text — uploading a downloaded file is not supported

#### 4.2.5 Verify Installation

In Panorama, navigate to **Panorama > Managed Devices > Summary** and confirm:
- The **Device Certificate** column displays **Valid** for each firewall
- The **Device Certificate Expiry Date** shows a future date

> `[SCREENSHOT 3b]` **Certificate Status (Panorama-Managed)** — Capture: **Panorama > Managed Devices > Summary** showing the Device Certificate column as "Valid" and the expiry dates for managed firewalls.

---

### 4.3 Restoring an Expired Certificate

If the certificate shows **Expired**:

- **Standalone devices:** Generate a new OTP and repeat the standalone install steps (Section 4.1)
- **Panorama-managed devices:** Repeat the Panorama workflow (Section 4.2) — generate a new OTP Request Token, get a new OTP from CSP, and upload it
- **TPM devices** (PA-400, PA-1400, PA-3400, PA-5400 series): Use CLI without OTP:
  ```
  admin> request certificate fetch
  ```

### 4.4 Post-Certificate: WildFire Users

If using WildFire or Advanced WildFire, refresh the registration channel on **each firewall** (whether standalone or Panorama-managed):
```
admin> request wildfire registration channel public
```

### 4.5 Checklist: Device Certificates

**Standalone firewalls:**
- [ ] OTP generated from CSP (remember: 60-minute window, one attempt)
- [ ] NTP configured and committed on each firewall
- [ ] Device certificate installed successfully on each firewall
- [ ] Certificate status verified as **valid** on each firewall

**Panorama-managed firewalls:**
- [ ] Panorama Superuser access confirmed
- [ ] Managed firewalls are on the same CSP account as Panorama
- [ ] NTP configured on Panorama and pushed to managed firewalls via template
- [ ] OTP Request Token generated from **Panorama > Managed Devices > Summary**
- [ ] OTP generated from CSP using "Generate OTP for Panorama managed firewalls"
- [ ] OTP uploaded in Panorama via **Upload OTP**
- [ ] Certificate status shows **Valid** in Panorama for all managed firewalls
- [ ] Expiry dates confirmed as future dates

**Both:**
- [ ] *(WildFire users)* Registration channel refreshed on each firewall

---

## Next Step: Onboarding

Once all prerequisites in Phases 1-4 are complete, proceed to the **[SCM Onboarding Guide](https://github.com/jollymahn/scm-onboarding-guide)** for:
- Phase 5: Onboard Devices to Strata Cloud Manager (NGFW, VM-Series, Prisma Access)
- Phase 6: Post-Onboarding Setup & Automation (CloudConnector plugin, device labels, onboarding rules)
- Troubleshooting: Cloud management connectivity, telemetry, and configuration push issues

---

## Quick Reference: Prerequisites Pre-Flight Checklist

Use this as a final go/no-go before starting the onboarding process.

### Hardware & Software
- [ ] All firewall models on supported list
- [ ] PAN-OS 10.2.3+ on all devices
- [ ] Single vsys confirmed

### Accounts & Licensing
- [ ] CSP account with appropriate role
- [ ] Activation Console access confirmed
- [ ] SCM license activated, Activation Status shows **Complete**
- [ ] Active support license on all devices
- [ ] *(VM-Series)* Deployment profile associated with tenant, Profile Association Status shows **Complete**
- [ ] All devices associated with correct tenant in Activation Console

### Network
- [ ] Outbound ports open: 80, 443, 444, 3978, 5222-5224, 5228, 5229
- [ ] All required FQDNs reachable (certificate, SCM, SLS, regional)
- [ ] DNS configured on all firewalls
- [ ] NTP configured and syncing on all firewalls
- [ ] *(Proxy)* Non-standard ports 3978 and 444 allowed

### Certificates
- [ ] Device certificate installed and valid on all firewalls (standalone or Panorama-managed)

---

## Source Documentation Links

| Topic | URL |
|---|---|
| SCM Prerequisites (main page) | [Link](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites) |
| SCM Licenses and Support | [Link](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support) |
| Install Device Certificate (Standalone) | [Link](https://docs.paloaltonetworks.com/ngfw/administration/certificate-management/certificate-deployment/install-device-certificate) |
| Install Device Certificate (Panorama-Managed) | [Link](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/install-the-device-certificate-for-managed-firewalls/install-the-device-certificate-for-a-managed-firewall) |
| Ports and FQDNs (SLS) | [Link](https://docs.paloaltonetworks.com/strata-logging-service/activation-and-onboarding/planning/ports-and-fqdns) |
| VM-Series Deployment Profile | [Link](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) |
| Hardware Model Compatibility | [Link](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility) |

---

## Appendix A: Troubleshooting Prerequisites Issues

### A.1 Device Certificate Fetch Fails

| Symptom | Likely Cause | Resolution |
|---|---|---|
| "Failed to fetch device certificate" | OTP expired (>60 min) or already used | Generate a **new OTP** from CSP. Each OTP allows only one attempt. |
| Certificate fetch times out | Management interface MTU too high causing fragmentation | Lower the management interface MTU to **1374**: `set deviceconfig system setting mtu 1374` then commit and retry. |
| Certificate validation fails | System clock is wrong — SSL handshake fails | Verify NTP is configured and synced: `show ntp`. Fix NTP under **Device > Setup > Services** and commit before retrying. |
| "TPM public key match failed" | Backend mismatch on TPM-equipped models | Open a **TAC case** — the existing certificate record may need to be reset on Palo Alto's backend. |
| `otp` keyword not available in CLI | Firewall has a TPM (PA-400, PA-1400, PA-3400, PA-5400 series) | TPM devices don't need an OTP. Simply run: `request certificate fetch` |
| Cert fetch fails through proxy | Proxy blocking or not supporting required ports | Ensure proxy allows traffic to `certificate.paloaltonetworks.com` and `api.paloaltonetworks.com` on port **443**. |
| Panorama OTP Upload fails | Pasted file content instead of text, or OTP expired | You **must paste** the OTP text — uploading a downloaded file is not supported. Generate a new OTP if expired. |

**Verification commands:**
```
admin> show device-certificate status          # Check certificate state
admin> request certificate fetch otp <value>   # Install with OTP (standalone)
admin> request certificate fetch               # Install on TPM devices (no OTP needed)
admin> show ntp                                 # Verify NTP sync
```

### A.2 Connectivity & Network Validation

Use these steps to verify network readiness before attempting onboarding.

| What to Validate | How to Test | Expected Result |
|---|---|---|
| DNS resolution | `ping host ds-cloudmgmt.paloaltonetworks.com` | Resolves to an IP address |
| Certificate FQDNs | `ping host certificate.paloaltonetworks.com` | Resolves to an IP address |
| NTP sync | `show ntp` | Status shows "synced" |
| Port 443 reachable | `ping host api.paloaltonetworks.com` | Response received |
| License status | `request license info` | Shows active licenses |

### A.3 Service Route Considerations

If your firewall's **management interface** does not have internet access (common in security-hardened environments), you need to configure a **service route** so cloud traffic uses a data-plane interface instead.

1. Navigate to **Device > Setup > Services > Service Route Configuration**
2. Select **Customize**
3. For **Palo Alto Networks Services** (or specifically **Cortex Data Lake**), assign a data-plane interface/IP that has internet access
4. **Commit** and verify connectivity

> `[SCREENSHOT 7]` **Service Route Configuration** — Capture: **Device > Setup > Services > Service Route Configuration** showing customized service routes for Palo Alto Networks cloud services.

### A.4 Quick Diagnostic Command Reference

| What to Check | CLI Command |
|---|---|
| Device certificate status | `show device-certificate status` |
| NTP synchronization | `show ntp` |
| DNS resolution | `ping host ds-cloudmgmt.paloaltonetworks.com` |
| License status | `request license info` |
| Management interface MTU | `show system setting mtu` |

---

## Appendix B: Screenshot Guide

The following screenshots should be captured during the prerequisites process. They serve as documentation proof and help with troubleshooting if issues arise. Redact any sensitive information (serial numbers, tenant IDs) before sharing externally.

| ID | Location | What to Capture | When |
|---|---|---|---|
| **Screenshot 1** | CSP: **Common Services > Tenant Management** | Active SCM license tier and associated products | Phase 1 — after license activation |
| **Screenshot 2a** | CSP: **Products > Device Certificates** | OTP generation dialog with "Next-Gen Firewall (PAN-OS)" selected and device serial number visible | Phase 4 — standalone OTP generation |
| **Screenshot 2b** | Panorama: **Managed Devices > Summary** | "Request OTP From CSP" dialog showing OTP Request Token output | Phase 4 — Panorama-managed OTP request token |
| **Screenshot 2c** | CSP: **Products > Device Certificates** | OTP generation dialog with "Panorama managed firewalls" selected and OTP Request Token pasted | Phase 4 — Panorama-managed OTP generation |
| **Screenshot 3a** | Firewall: **Device > Setup > Management > Device Certificate** | Certificate status showing "Valid" with expiration date | Phase 4 — standalone certificate verification |
| **Screenshot 3b** | Panorama: **Managed Devices > Summary** | Device Certificate column showing "Valid" and expiry dates for managed firewalls | Phase 4 — Panorama-managed certificate verification |
| **Screenshot 7** | Firewall: **Device > Setup > Services > Service Route Configuration** | Custom service routes for PA cloud services (if applicable) | Troubleshooting — if management interface lacks internet |

**Capture tips:**
- Use your OS screenshot tool or browser extension
- Include the browser URL bar for web UI screenshots to confirm the correct page
- For CLI output, copy-paste the full terminal output into a text file as backup
- Save files with a naming convention: `SCM-Screenshot-[ID]-[DeviceSerial]-[Date].png`

---

## Appendix C: Accuracy Review Notes

This guide was synthesized from the official Palo Alto Networks documentation pages listed in the [Source Documentation Links](#source-documentation-links) section. The following items were cross-referenced and verified:

**Cross-reference findings:**
1. **PAN-OS minimum version** — Consistently stated as **10.2.3** across the prerequisites page, onboarding page, CloudConnector plugin page, and telemetry page.
2. **Port requirements** — Ports 443, 444, and 3978 are consistently documented across the prerequisites and SLS ports/FQDNs pages. Telemetry ports (5222-5224, 5228, 5229) are documented in both the prerequisites and SLS pages.
3. **Certificate FQDNs** — The FQDN lists match between the device certificate page and the SLS ports/FQDNs page.
4. **Supported models** — The hardware compatibility page lists models consistent with the prerequisites page, though the compatibility page includes newer PA-1400 series models not explicitly listed on the prerequisites page.
5. **Telemetry auto-enable versions** — PAN-OS 10.2.17+, 11.1.11+, 11.2.8+, and 12.1.2+ are consistently documented on the telemetry/metrics page.

**Items to verify with SMEs:**
1. The prerequisites page mentions PA-220/220R, PA-400 Series, PA-450R/455R/455R-5G, PA-500, PA-800, PA-1400, PA-3200, PA-3400, PA-5200, PA-5400, PA-5500, PA-7000, PA-7500 as supported models — but the hardware compatibility page uses slightly different model numbering (e.g., PA-3220 vs PA-3200 series). Confirm whether series-level references on the prerequisites page encompass all models listed on the compatibility page.
2. The prerequisites page mentions **PA-455R-5G** which does not appear on the hardware compatibility page. Confirm this model's SCM support status.
3. Service route configuration is not mentioned on any of the source pages but is a common requirement in hardened environments. The troubleshooting section includes this based on community knowledge — verify with official documentation.
