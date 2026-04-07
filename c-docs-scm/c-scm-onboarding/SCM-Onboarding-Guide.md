# Strata Cloud Manager: Onboarding & Post-Onboarding Guide

> **Purpose:** A step-by-step guide for onboarding firewalls and Prisma Access to Strata Cloud Manager (SCM), including post-onboarding configuration and automation. This guide picks up where the [SCM Prerequisites Guide](https://github.com/jollymahn/scm-prerequisites-guide) left off.
>
> **Before you begin:** Complete all prerequisites (Phases 1-4) in the [SCM Prerequisites Guide](https://github.com/jollymahn/scm-prerequisites-guide). All devices must have valid certificates, network connectivity, and proper licensing before onboarding.
>
> **Source Documentation:** This guide consolidates content from the [official SCM onboarding documentation](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager) and related pages.
>
> **Companion files:**
> - [Device Onboarding Tracker (CSV)](./SCM-Onboarding-Tracker.csv) — Per-device tracking spreadsheet
> - Screenshots are referenced throughout with `[SCREENSHOT]` markers — see [Appendix B](#appendix-b-screenshot-guide) for capture instructions

---

## How to Use This Guide

Work through **Phase 5 and Phase 6** in sequence. Phase numbering continues from the Prerequisites Guide to maintain a single end-to-end workflow.

**Audience paths:**
- **NGFW (hardware firewalls):** Phases 5 and 6
- **VM-Series (Software NGFW Credits):** Phases 5 and 6
- **Prisma Access:** Phase 5 only (Section 5.2)
- **Panorama CloudConnector Plugin:** Phase 6 (Section 6.1)

---

## Phase 5: Onboard Devices to Strata Cloud Manager

### 5.1 NGFW Onboarding

#### Step 1: Configure the Firewall Locally

1. Verify **DNS and NTP** are configured under **Device > Setup > Services**
2. Navigate to **Device > Setup > Management > Panorama Settings**
3. Select **Managed By Cloud Service**
4. *(PAN-OS 11.2+)* Choose communication port: Default (dedicated) or **443** (standard SSL)
5. *(Optional)* Enable **Compress Config** for faster configuration transfers
6. **Commit** changes

> `[SCREENSHOT 4]` **Panorama Settings — Cloud Service** — Capture: **Device > Setup > Management > Panorama Settings** showing "Managed By Cloud Service" selected, with port selection visible (PAN-OS 11.2+).

#### Step 2: Associate Devices in SCM

1. In SCM, go to **System Settings > Device Associations > Add Devices**
2. Select the serial numbers of firewalls to onboard
3. Associate each firewall with **Strata Cloud Manager** or **AIOps for NGFW**

> `[SCREENSHOT 5]` **Device Association** — Capture: SCM **System Settings > Device Associations** showing the "Add Devices" dialog with serial numbers selected and product association dropdown.

#### Step 3: Move to Cloud Management

1. Go to **System Settings > Device Management > Available Devices**
2. Select the firewall(s)
3. Click **Move to Cloud Management**

#### Step 4: Verify

1. In SCM, check **Cloud Managed Devices** — status should show **Success**
2. On the firewall CLI, run:
   ```
   admin> show cloud-management-status
   ```
   Confirm `Connected` shows **Yes**

> `[SCREENSHOT 6]` **Successful Onboarding** — Capture: SCM **Cloud Managed Devices** page showing device status as "Success". Also capture the CLI output of `show cloud-management-status` showing `Connected: yes`.

---

### 5.2 Prisma Access Onboarding

**For visibility only:**
- Log into the SCM tenant associated with your Prisma Access deployment — no additional steps needed

**For full management (new deployments):**
- Choose **Strata Cloud Manager** as the management interface during activation

**For migration from Panorama:**
- Use the in-product migration workflow
- **This is a one-way migration — you cannot revert to Panorama management**

---

### 5.3 Enable Telemetry

Telemetry is required for SCM to collect health data via Strata Logging Service.

**Auto-enabled versions** (no action needed):
- PAN-OS 10.2.17+, 11.1.11+, 11.2.8+, 12.1.2+

**All other versions:**
1. Register the device in CSP under **Assets > Devices**
2. Ensure device certificate is installed (see [Prerequisites Guide, Phase 4](https://github.com/jollymahn/scm-prerequisites-guide))
3. Manually enable telemetry sharing on each device

> **Expect a ~2 hour delay** before initial insights appear. Full insights for a new device may take several hours.

---

### 5.4 Checklist: Onboarding

- [ ] Firewall configured for cloud management (Panorama Settings → Managed By Cloud Service)
- [ ] Changes committed on the firewall
- [ ] Device associated with SCM in **System Settings > Device Associations**
- [ ] Device moved to cloud management in **System Settings > Device Management**
- [ ] Status shows **Success** in SCM
- [ ] CLI `show cloud-management-status` shows **Connected: Yes**
- [ ] Telemetry enabled (automatic on supported PAN-OS versions, manual on older)
- [ ] *(Prisma Access)* Logged into SCM tenant or completed migration

---

## Phase 6: Post-Onboarding Setup & Automation (Optional)

### 6.1 Panorama CloudConnector Plugin

If you use Panorama and want BPA/Policy Analyzer features in SCM:

**Requirements:**
- Panorama running PAN-OS 10.2.3+
- Valid device certificate on Panorama
- Telemetry enabled on Panorama
- AIOps for NGFW Premium or SCM Pro license (required for Policy Analyzer and BPA)

**Installation:**
1. Enable via CLI:
   ```
   admin> request plugins cloudconnector enable basic
   ```
   *(PAN-OS 11.0.1+: plugin is preinstalled)*

2. **If upgrading from AIOps plugin:** Go to **Panorama > Plugins** → **Uninstall** the AIOps plugin → ensure only CloudConnector remains → re-enable if needed

3. Allow Panorama to reach your regional FQDN (see [Prerequisites Guide, Section 3.6](https://github.com/jollymahn/scm-prerequisites-guide))

**Regional FQDNs for CloudConnector:**

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

---

### 6.2 Device Labels & Onboarding Rules (At Scale)

For environments with many devices, automate onboarding:

**Device Labels:**
- Path: **Configuration > NGFW and Prisma Access > Setup > Device Onboarding > Device Labels**
- Group devices by software version, location, role, etc.

**Onboarding Rules:**
- Match criteria: Model, Serial Number (regex), or Labels
- Actions: Auto-assign to a **Target Folder** and apply **Snippets** (standardized base configurations)
- Advanced: Enable **VPN Onboarding** (Auto VPN clusters) or **User Context Onboarding** (Cloud Identity Engine integration)

---

### 6.3 Post-Onboarding Configuration in SCM

Once devices are onboarded:
- **General Settings:** Domain name, login banners, certificates, time zones, tunnel acceleration
- **Session Settings:** Define VPN session settings and timeouts
- **Folder Management:** Organize firewalls into folders for group configuration (HA pairs must be in the same folder)
- **Interface Assignment:** Verify predefined interfaces:
  - `$eth-internet` (eth1/3) — outbound traffic
  - `$eth-local` (eth1/4) — local connections
- **Push Config:** Always perform **Push Config** from the Configuration menu to apply changes to devices

---

### 6.4 Checklist: Post-Onboarding

- [ ] *(If using Panorama)* CloudConnector plugin installed and enabled
- [ ] *(If using Panorama)* Old AIOps plugin uninstalled (if present)
- [ ] *(At scale)* Device labels created for grouping
- [ ] *(At scale)* Onboarding rules configured for automated folder/snippet assignment
- [ ] Firewalls organized into appropriate folders in SCM
- [ ] Interface assignments verified
- [ ] Initial configuration pushed to devices

---

## Appendix A: Troubleshooting Onboarding Issues

### A.1 Cloud Management Status: Not Connected

| Symptom | Likely Cause | Resolution |
|---|---|---|
| `Connected: no` — TCP status "Failed" or "Connection timed out" | Port 3978 (or 443 on PAN-OS 11.2+) blocked outbound | Verify firewall can reach the SCM endpoint on the correct port. Check transit firewall rules, proxies, and NAT. |
| `Connected: no` — DNS failure in status output | Firewall cannot resolve SCM FQDNs | Verify DNS servers under **Device > Setup > Services**. Test with `ping host ds-cloudmgmt.paloaltonetworks.com`. |
| `Connected: no` — endpoint FQDN is empty | Device not properly onboarded in SCM | Verify the device serial number is associated in **SCM > System Settings > Device Associations** and moved to cloud management. |
| "Device Not Found" in SCM | Device not associated with correct Tenant Service Group | Verify serial number is registered and associated with the correct tenant in the Palo Alto Networks Hub/CSP. |
| Status shows "Onboarded" but "Disconnected" | Device certificate missing/expired, or port 3978 blocked | Check certificate status (`show device-certificate status`) and verify port connectivity. |

**Verification commands:**
```
admin> show cloud-management-status            # Full connection status with endpoint, TCP, DNS details
admin> show device-certificate status           # Certificate state
admin> ping host <endpoint_from_status>         # Test connectivity to SCM endpoint
admin> show ntp                                  # Verify NTP sync status
```

**If everything looks correct but still won't connect:**
```
admin> debug software restart process cloud_mgr
```
Wait 5 minutes, then re-check `show cloud-management-status`.

### A.2 Telemetry Not Appearing in SCM Dashboard

| Symptom | Likely Cause | Resolution |
|---|---|---|
| No telemetry data after 2+ hours | Telemetry not enabled on the device | Check with `show device-telemetry details`. For PAN-OS versions below auto-enable thresholds, manually enable telemetry sharing. |
| Telemetry enabled but data missing | Region mismatch between telemetry and SCM/CDL instance | Check telemetry region: `show device-telemetry settings`. Ensure it matches your SCM instance region. |
| Telemetry intermittent or stale | Ports 5222-5224, 5228, 5229 blocked | Verify these telemetry ports are open outbound in addition to 443. |
| Telemetry stuck — "cannot lock /etc/subgid" in logs | Known bug in some PAN-OS 10.2.x versions — system lock file issue | On PAN-OS 10.2.11+: `delete authentication system-lock-files`. On older versions: restart management plane or contact TAC. |

**Verification commands:**
```
admin> show device-telemetry details           # Telemetry status and last upload time
admin> show device-telemetry settings          # Region and configuration
admin> request device-telemetry collect-now    # Force immediate telemetry collection
admin> less mp-log configd.log                  # Check for lock file errors
```

### A.3 Configuration Push Fails After Onboarding

| Symptom | Likely Cause | Resolution |
|---|---|---|
| Push fails immediately | Configuration conflict with local settings | Check **SCM > Configuration > Operations > Push Status** for specific error details. Resolve conflicts between SCM config and local firewall config. |
| Push hangs or times out | Connectivity issue between SCM and firewall | Verify `show cloud-management-status` shows Connected. Check for packet loss on the management path. |
| HA peer push fails | HA peers in different SCM folders | Move both HA peers to the **same folder** in SCM. HA pairs must always be in the same folder. |

### A.4 Quick Diagnostic Command Reference

| What to Check | CLI Command |
|---|---|
| Cloud management connection | `show cloud-management-status` |
| Device certificate status | `show device-certificate status` |
| NTP synchronization | `show ntp` |
| DNS resolution | `ping host ds-cloudmgmt.paloaltonetworks.com` |
| Telemetry status | `show device-telemetry details` |
| Telemetry region | `show device-telemetry settings` |
| Force telemetry upload | `request device-telemetry collect-now` |
| License status | `request license info` |
| Restart cloud management | `debug software restart process cloud_mgr` |
| Check config logs for errors | `less mp-log configd.log` |

---

## Appendix B: Screenshot Guide

The following screenshots should be captured during the onboarding process. They serve as documentation proof and help with troubleshooting if issues arise. Redact any sensitive information (serial numbers, tenant IDs) before sharing externally.

| ID | Location | What to Capture | When |
|---|---|---|---|
| **Screenshot 4** | Firewall: **Device > Setup > Management > Panorama Settings** | "Managed By Cloud Service" selected, port selection visible | Phase 5 — after local firewall config |
| **Screenshot 5** | SCM: **System Settings > Device Associations** | "Add Devices" dialog with serial numbers and product association | Phase 5 — during device association |
| **Screenshot 6** | SCM: **Cloud Managed Devices** + Firewall CLI | Device status "Success" in SCM + `show cloud-management-status` output showing `Connected: yes` | Phase 5 — after successful onboarding |

**Capture tips:**
- Use your OS screenshot tool or browser extension
- Include the browser URL bar for web UI screenshots to confirm the correct page
- For CLI output, copy-paste the full terminal output into a text file as backup
- Save files with a naming convention: `SCM-Screenshot-[ID]-[DeviceSerial]-[Date].png`

---

## Source Documentation Links

| Topic | URL |
|---|---|
| Onboard to SCM | [Link](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager) |
| CloudConnector Plugin for Panorama | [Link](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-plugin-for-panorama) |
| Device Telemetry (Metrics) | [Link](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics) |
| SCM Prerequisites Guide (companion) | [Link](https://github.com/jollymahn/scm-prerequisites-guide) |
