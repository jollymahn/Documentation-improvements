# GlobalProtect Deployment Guide — Branching Format

**Panorama-managed GlobalProtect remote access VPN with decision-point navigation**

---

## Overview

This guide covers the same deployment as the [Linear Guide](linear-guide.md) but is organized around decision points. Expand only the sections relevant to your environment.

### Architecture

```
                    Internet
                       |
              +--------+--------+
              |   Untrust Zone  |
              |  ethernet1/1    |
              |  (Portal + GW)  |
              +--------+--------+
                       |
              +--------+--------+
              | Tunnel Interface |
              |   tunnel.1      |
              |  (VPN Zone)     |
              +--------+--------+
                       |
              +--------+--------+
              |   Trust Zone    |
              |  ethernet1/2    |
              | (Internal LAN)  |
              +--------+--------+
                       |
                 Internal Network
```

### Prerequisites

- PAN-OS Firewall running 10.1+
- Panorama managing the firewall (device group + template stack)
- Network connectivity — external interface reachable from the internet
- Authentication source — AD/LDAP or SAML IdP
- DNS record — FQDN pointing to the firewall's external IP
- Server certificate — public CA or self-signed

---

## Section 1: Infrastructure and Certificates

This section is the same regardless of your deployment choices.

### Step 1.1: Configure Interfaces

**External Interface (Portal + Gateway)**

1. In Panorama, select your **Template** > **Network > Interfaces > Ethernet**.
2. Select the external interface (e.g., `ethernet1/1`).
3. Set **Interface Type**: Layer3, **Zone**: `untrust`, assign public IP.
4. Click **OK**.

**Internal Interface**

1. Select the internal interface (e.g., `ethernet1/2`).
2. Set **Interface Type**: Layer3, **Zone**: `trust`, assign internal IP.
3. Click **OK**.

> **Warning:** Do not enable management services (HTTP, HTTPS, SSH) on the external interface.

### Step 1.2: Create the Tunnel Interface

1. Navigate to **Network > Interfaces > Tunnel**.
2. Click **Add** — interface `tunnel.1`.
3. Create a new zone `vpn-zone`, optionally assign IP `10.31.32.1/24`.
4. Click **OK**.

> **Note:** Enable **User Identification** on the VPN zone for User-ID-based policies.

### Step 1.3: Create Security Policy Rules

1. In your **Device Group** > **Policies > Security**.
2. Create rule `Allow-VPN-to-Trust`: Source `vpn-zone`, Destination `trust`, Action `Allow`.

> **Warning:** Start with `any/any` for testing, tighten before production.

### Decision Point: Certificate Type

Choose your certificate approach:

---

#### Path A: Public CA Certificate (Recommended)

Best for production — no certificate warnings for end users.

1. Navigate to **Device > Certificate Management > Certificates**.
2. Click **Generate** to create a CSR:
   - **Certificate Name**: `gp-portal-cert`
   - **Common Name**: Your portal FQDN (e.g., `vpn.company.com`)
3. Export CSR, submit to your CA.
4. Import the signed certificate, private key, and CA chain.

---

#### Path B: Self-Signed Root CA

Best for testing or managed endpoints with pre-deployed CA.

1. Navigate to **Device > Certificate Management > Certificates**.
2. Generate root CA:
   - **Certificate Name**: `GP-Root-CA`, **Common Name**: `GlobalProtect Root CA`
   - Check **Certificate Authority**
3. Generate server certificate:
   - **Certificate Name**: `gp-server-cert`
   - **Common Name**: Portal FQDN
   - **Signed By**: `GP-Root-CA`
   - Add SAN with DNS and/or IP type

> **Warning:** You must deploy the root CA to all endpoints. Otherwise users see certificate warnings and the app may fail to connect.

---

### Step 1.5: Create SSL/TLS Service Profile

1. Navigate to **Device > Certificate Management > SSL/TLS Service Profile**.
2. Click **Add**: Name `GP-SSL-Profile`, select your certificate, Min `TLSv1.2`, Max `TLSv1.3`.
3. Click **OK**.

### Step 1.6: Commit and Verify

1. **Commit to Panorama**, then **Push to Devices**.
2. Verify: interfaces up (green), zones configured, certificates valid.

> **Success:** Green status on all interfaces, valid certificates with correct expiration dates.

---

## Section 2: Authentication

### Decision Point: Authentication Method

Choose the authentication method that matches your environment:

---

#### Path A: LDAP (Active Directory)

Best for organizations with on-premises Active Directory.

**Step 2A.1: Create LDAP Server Profile**

1. **Device > Server Profiles > LDAP** > **Add**:
   - **Profile Name**: `AD-LDAP-Profile`
   - **Server**: AD IP/FQDN, Port `389` (or `636` for LDAPS)
   - **Type**: `active-directory`
   - **Base DN**: `DC=company,DC=com`
   - **Bind DN**: `CN=svc-globalprotect,OU=Service Accounts,DC=company,DC=com`
   - **SSL**: Check for LDAPS

> **Note:** Use LDAPS (port 636) in production. Import the AD CA certificate first.

**Step 2A.2: Create Authentication Profile**

1. **Device > Authentication Profile** > **Add**:
   - **Name**: `GP-Auth-Profile`
   - **Type**: `LDAP`
   - **Server Profile**: `AD-LDAP-Profile`
   - **Login Attribute**: `sAMAccountName`
   - **User Domain**: `company`
   - **Allow List**: `all` (for testing)

**Step 2A.3: Enable Group Mapping (Optional)**

1. **Device > User Identification > Group Mapping Settings** > **Add**:
   - **Server Profile**: `AD-LDAP-Profile`
   - **Domain**: `company`
2. Add groups on the **Group Include List** tab.

---

#### Path B: SAML

Best for cloud-first organizations or SSO requirements.

**Step 2B.1: Configure Your IdP**

Create a SAML application on your IdP with:

| Setting | Value |
|---------|-------|
| **ACS URL** | `https://vpn.company.com:443/SAML20/SP/ACS` |
| **Entity ID** | `https://vpn.company.com:443/SAML20/SP` |
| **Name ID Format** | Email or username |

Download the **IdP Metadata XML** file.

**Step 2B.2: Import IdP Metadata**

1. **Device > Server Profiles > SAML Identity Provider** > **Import**.
2. Upload the IdP metadata XML.
3. Verify: IdP ID, SSO URL, and certificate are populated.
4. **Max Clock Skew**: `60` seconds.

**Step 2B.3: Create SAML Authentication Profile**

1. **Device > Authentication Profile** > **Add**:
   - **Name**: `GP-SAML-Auth-Profile`
   - **Type**: `SAML`
   - **IdP Server Profile**: Select imported profile
   - **Username Attribute**: As configured on IdP
   - **User Group Attribute**: `groups`
   - **Allow List**: `all`

---

#### Path C: RADIUS

Best for environments with existing RADIUS infrastructure.

**Step 2C.1: Create RADIUS Server Profile**

1. **Device > Server Profiles > RADIUS** > **Add**:
   - **Profile Name**: `RADIUS-Profile`
   - **Server**: RADIUS server IP
   - **Port**: `1812` (authentication)
   - **Secret**: Shared secret
   - **Timeout**: `30` seconds
   - **Retries**: `3`

**Step 2C.2: Create Authentication Profile**

1. **Device > Authentication Profile** > **Add**:
   - **Name**: `GP-RADIUS-Auth-Profile`
   - **Type**: `RADIUS`
   - **Server Profile**: `RADIUS-Profile`
   - **Allow List**: `all`

---

### Step 2.4: Commit and Verify

1. **Commit to Panorama**, then **Push to Devices**.
2. For LDAP: Check connection status in server profile.
3. For SAML: Verify metadata imported with valid certificate.

> **Success:** Server profile shows successful connection or valid metadata.

---

## Section 3: Gateway Configuration

### Step 3.1: Add the Gateway

1. **Network > GlobalProtect > Gateways** > **Add**.
2. **General** tab:
   - **Name**: `GP-External-Gateway`
   - **Interface**: `ethernet1/1`
   - **IPv4 Address**: Select IP
   - **SSL/TLS Service Profile**: `GP-SSL-Profile`

### Step 3.2: Configure Authentication

1. **Authentication** tab > **Add**:
   - **Name**: `default-auth`, **OS**: `Any`
   - **Authentication Profile**: Your auth profile

### Step 3.3: Configure Tunnel Settings

1. **Agent** tab > **Tunnel Settings**:
   - Check **Tunnel Mode**
   - **Tunnel Interface**: `tunnel.1`
   - Check **Enable IPSec**
2. **Timeout Settings**:
   - **Login Lifetime**: `30` days
   - **Inactivity Logout**: `3` hours

### Step 3.4: Configure IP Pool and DNS

1. **Agent** tab > **Tunnel Settings > Network Settings**:
   - **IP Pool**: `10.31.32.2-10.31.32.254`
   - **DNS Server**: `10.0.1.10`
   - **DNS Suffix**: `company.com`

### Decision Point: Tunnel Mode

---

#### Path A: Full Tunnel

All traffic routes through the VPN. Maximum security, higher bandwidth usage.

1. Leave **Access Route** empty (all traffic goes through VPN).
2. Click **OK**.

---

#### Path B: Split Tunnel — Route-Based

Only specified network traffic routes through VPN. Reduces bandwidth.

1. Under **Access Route**, click **Add**:
   - Add internal networks: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`
2. Click **OK**.

---

#### Path C: Split Tunnel — Domain/Application-Based

Route traffic based on destination domain or application type.

1. Under **Client Settings**, click **Add** > name `default-config`.
2. On the **Split Tunnel** tab:
   - **Include**: Add networks for VPN
   - **Exclude**: Add networks to bypass (e.g., video conferencing)
   - **Domain**: Add specific domains to route through VPN
3. Click **OK**.

> **PAN Docs:** [Split Tunnel Traffic](https://docs.paloaltonetworks.com/globalprotect/administration/globalprotect-gateways/split-tunnel-traffic-on-globalprotect-gateways) | [Domain and Application Split Tunnel](https://docs.paloaltonetworks.com/globalprotect/administration/globalprotect-gateways/split-tunnel-traffic-on-globalprotect-gateways/configure-a-split-tunnel-based-on-the-domain-and-application)

---

### Step 3.6: Commit and Verify

1. **Commit to Panorama**, then **Push to Devices**.
2. Check gateway status: **Network > GlobalProtect > Gateways** — green indicator.
3. CLI verification:

```
show global-protect-gateway name GP-External-Gateway
```

> **Success:** Gateway status shows `Running`.

---

## Section 4: Portal Configuration

### Step 4.1: Add the Portal

1. **Network > GlobalProtect > Portals** > **Add**.
2. **General** tab:
   - **Name**: `GP-Portal`
   - **Interface**: `ethernet1/1` (same as gateway)
   - **IPv4 Address**: Same IP as gateway
   - **SSL/TLS Service Profile**: `GP-SSL-Profile`

### Step 4.2: Configure Portal Authentication

1. **Authentication** tab > **Add**:
   - **Name**: `default-portal-auth`, **OS**: `Any`
   - **Authentication Profile**: Same as gateway

### Step 4.3: Configure Agent Settings

1. **Agent** tab > **Add**: Name `default-agent-config`.
2. **Authentication** tab:
   - **Save User Credentials**: `Save Username and Password`
   - **Authentication Override**: Enable cookie-based auth, lifetime `24` hours
3. **Config Selection Criteria**: OS `Any`, User `Any`.

### Step 4.4: Configure Gateway List

1. **External** tab under **Gateways** > **Add**:
   - **Name**: `GP-External-Gateway`
   - **Address**: `vpn.company.com`
   - **Priority**: `Highest`

### Decision Point: Connection Method

---

#### Path A: Always On (Recommended for Enterprise)

VPN connects automatically at user login and stays connected.

1. **App** tab:
   - **Connect Method**: `User-Logon (Always On)`
   - **Disable GlobalProtect App**: `No`
   - **Allow user to change portal address**: `No`

---

#### Path B: On-Demand

Users manually connect when they need VPN access.

1. **App** tab:
   - **Connect Method**: `On-Demand`
   - **Disable GlobalProtect App**: `Allow with Passcode` (optional)

---

#### Path C: Pre-Logon then On-Demand

Machine-level tunnel before user login, then user controls connection.

1. **App** tab:
   - **Connect Method**: `Pre-logon then On-Demand`
2. Requires machine certificate deployment — see [Pre-Logon Configuration](https://docs.paloaltonetworks.com/globalprotect/administration/globalprotect-quick-configs/remote-access-vpn-with-pre-logon).

---

### Step 4.6: Commit and Verify

1. **Commit to Panorama**, then **Push to Devices**.
2. Check: **Network > GlobalProtect > Portals** — green indicator.
3. Test: Navigate to `https://vpn.company.com` — portal login page should load.

> **Success:** Portal login page loads, accepts credentials, and offers app download.

---

## Section 5: App Deployment and Testing

### Decision Point: Deployment Method

---

#### Path A: Portal Download (Simplest)

1. Navigate to `https://vpn.company.com`.
2. Log in and download the installer for your OS.
3. Install and connect.

---

#### Path B: Host on Portal (Managed)

1. In Panorama: **Device > GlobalProtect Client** > **Download** > **Activate**.
2. Users connecting to the portal are automatically offered the download.

---

#### Path C: Enterprise Deployment (MDM/GPO)

**Windows (MSI via Group Policy or SCCM)**
```
msiexec /i GlobalProtect64.msi /quiet PORTAL=vpn.company.com
```

**macOS (MDM)**
- Deploy `.pkg` via Jamf, Mosyle, or other MDM.
- Pre-approve system extension via MDM configuration profile.

**Linux**
```
# Debian/Ubuntu
sudo dpkg -i GlobalProtect_UI_deb-*.deb

# RHEL/CentOS
sudo rpm -ivh GlobalProtect_UI_rpm-*.rpm
```

---

### Step 5.3: Connect and Test

1. Open GlobalProtect app.
2. Enter portal: `vpn.company.com`
3. Authenticate.
4. Verify: Status `Connected`, assigned IP from pool, gateway name displayed.

### Step 5.4: End-to-End Verification

**From the endpoint:**
```
ping 10.0.1.10                    # Internal server
nslookup server.company.com       # DNS resolution
```

**From the firewall CLI:**
```
show global-protect-gateway current-user gateway GP-External-Gateway
```

**In Panorama:**
- **Monitor > Logs > Traffic** — filter source zone `vpn-zone`
- Verify username, policy match, and application identification

> **Success:** App connects, gets IP from pool, accesses internal resources. Logs show correct user, zone, and policies.

---

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| App cannot reach portal | DNS or firewall blocking | Verify DNS resolution and port 443 is open |
| Certificate error | CN/SAN mismatch | Ensure cert CN or SAN matches portal FQDN |
| Authentication fails | Wrong profile or server unreachable | Check server profile connectivity |
| Connected but no access | Missing routes or policies | Verify access routes and security policies |
| Slow performance | Full tunnel | Consider split tunnel |
| Frequent disconnections | Timeout too short | Increase gateway timeout values |

### CLI Commands

```
show global-protect-gateway name GP-External-Gateway
show global-protect-gateway current-user gateway GP-External-Gateway
show global-protect-portal name GP-Portal
show global-protect-gateway statistics gateway GP-External-Gateway
debug global-protect-gateway log-level gateway GP-External-Gateway level debug
```

### Log Locations

| Source | Location |
|--------|----------|
| Firewall System | Monitor > Logs > System (filter `globalprotect`) |
| Firewall Auth | Monitor > Logs > Authentication |
| Windows | `C:\Program Files\Palo Alto Networks\GlobalProtect\PanGPS.log` |
| macOS | `/Library/Logs/PaloAltoNetworks/GlobalProtect/PanGPS.log` |
| Linux | `/opt/paloaltonetworks/globalprotect/PanGPS.log` |
