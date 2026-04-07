<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites -->
<!-- Fetched: 2026-03-31T18:59:41.312320+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags:  -->

# Strata Cloud Manager Prerequisites

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Strata Cloud Manager Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Activation & Onboarding
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Subscription & Tenant Management
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Getting Started
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 AIOps
 

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
                            
                                    Upgrade to Strata Cloud Manager Pro, from Strata Cloud Manager Essentials](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/upgrade-to-strata-cloud-manager-pro.html)
 

 
 

**[Next
                                
                                    Migrate from Panorama to Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-panorama-to-strata-cloud-manager.html)
 

 

---

 
 
 















 

# Strata Cloud Manager Prerequisites



 Learn about the prerequisites for Strata Cloud Manager.



 






















 

- [Software NGFW
                                            Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- 

- [AIOps for NGFW Free](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)[Strata Cloud Manager Essentials](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)

- [AIOps for NGFW Premium](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)[Strata Cloud Manager Pro](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW, including those funded by Prisma Access | One of these: or  or |


 Strata Cloud Manager offers detailed visibility and insights into your
 Next-Generation Firewalls (NGFW) and Prisma Access deployments, regardless of whether
 they are managed through Strata Cloud Manager or Panorama. To fully leverage Strata
 Cloud Manager, it's essential to meet the necessary prerequisites before you [onboard](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html) your NGFW devices or Prisma Access for configuration
 management or connect your Panorama instance to Strata Cloud Manager for visibility
 features.

The prerequisites include ensuring connectivity between your devices and Strata
 Cloud Manager, verifying software compatibility to enable full feature access,
 validating licenses to activate critical functionalities, and selecting the appropriate
 region to optimize performance and compliance. These requirements are essential for
 successfully integrating your security devices into the platform.

- [NGFW](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites/strata-cloud-manager-prerequisites-ngfw.html#strata-cloud-manager-prerequisites-ngfw)
- [Prisma Access](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites/strata-cloud-manager-prerequisites-prisma-access.html#strata-cloud-manager-prerequisites-prisma-access)

















 

# Strata Cloud Manager Prerequisites for NGFW and VM-Series Funded by
        Software NGFW Credits



 Learn about Strata Cloud Manager prerequisites for NGFWs.



 Strata Cloud Manager provides comprehensive visibility and insights for your Palo Alto
 Networks Next-Generation Firewalls (NGFW) deployments, whether managed by Strata Cloud
 Manager or Panorama. You can onboard your NGFW to Strata Cloud Manager to manage and
 gain insights. If you already have NGFWs managed by Panorama, you can connect Strata
 Cloud Manager to your Panorama using the [Panorama CloudConnector Plugin](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-plugin-for-panorama).

When preparing to onboard and manage your NGFW and VM-Series funded by software
 NGFW credits through Strata Cloud Manager, ensure that the necessary prerequisites are
 met. This section covers the essential areas for successful onboarding, including
 connectivity requirements and supported regions.

- **Cloud Management for NGFWs Onboarding Prerequisites** - Before onboarding your NGFW to Strata Cloud Manager, verify that all
 conditions for device readiness are fulfilled. This includes network configuration,
 software compatibility, and licensing requirements. Completing these steps ensures
 that your firewall can be successfully managed using Strata Cloud Manager. 
 
 To onboard VM-series funded by software NGFW credits, see [Create a Deployment Profile](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series).

- **[Device Model Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility)** -
 Device models that you can associate with Strata Cloud Manager.
- **TCP Ports and FQDNs Required for Cloud Management of NGFWs** - To enable seamless communication between the NGFW and Strata Cloud
 Manager, configure specific TCP ports and Fully Qualified Domain Names (FQDNs). 
- **[Enable Telemetry on Devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics)** -
 Enable telemetry on your NGFW to allow Strata Cloud Manager to collect necessary
 data for insights and recommendations. Strata Cloud Manager assesses the health of
 the devices in your deployment by analyzing telemetry data that your PAN-OS devices
 send to Strata Logging Service.
- **[Create Device Labels](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html)** - Use Device Labels in Strata
 Cloud Manager to automate and streamline NGFW onboarding and management
 processes.
- **[Create a Device Onboarding Rule](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html)** - Use device
 onboarding rules to automate parts of the NGFW onboarding process for Strata Cloud
 Manager. 


 















 

## Cloud Management for NGFWs Onboarding Prerequisites



 Review the requirements to onboard a Strata Cloud Manager tenant and
 firewalls to Strata Cloud Manager. 

Note that some requirements, such as PAN-OS Version, Firewall Model,
 Ports, and Services, apply to the firewall. While others, such as the Logging and
 Authentication service requirements, apply to your Customer Support Portal (CSP)
 account. 
























 

[manually install device
                                        certificates](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/certificate-management/obtain-certificates/device-certificate)

[NGFW model](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/certificate-management/obtain-certificates/device-certificate)

[hub roles](https://docs.paloaltonetworks.com/hub/hub-getting-started/manage-app-roles/available-roles)

| Prerequisite | Supported | Required? |
| --- | --- | --- |
| PAN-OS Version | (minimum)PAN-OS 10.2.3 | Yes |
| Firewall Model
                                Single vsys firewalls only
                                Multi-vsys firewalls are not supported
                                PA-410 not supported if Enterprise DLP license is
                                        active | PA-220 and PA-220R
                                PA-400 Series
                                PA-450R, PA-455R, and PA-455R-5G
                                PA-500 Series
                                PA-800 Series
                                PA-1400 Series
                                PA-3200 Series
                                PA-3400 Series
                                PA-5200 Series
                                PA-5400 Series
                                PA-5500 Series
                                PA-7000 Series
                                PA-7500
                                VM-Series | N/A |
| Device Certificates | The device certificate must be installed on NGFWs before
                                    onboarding to Strata Cloud Manager.
                                Some NGFW models automatically install the device certificate
                                    when you first register the device on the support portal. For
                                    others, you need to  before onboarding.
                                For any NGFW models with expired certificates, you must manually
                                    renew the certificates before onboarding. | Yes
                                Whether you need to manually install the device certificate
                                    before onboarding depends on your , or the
                                    status of your device certificates. |
| Ports
                                Ports are used for outbound communication from the firewall to
                                        Strata Cloud Manager and SLS | 443
                                444
                                3978 | Yes |
| Services
                                Services are used for resolution of the Strata Cloud Manager
                                    tenant, as well as software and content updates | DNS
                                NTP | Yes |
| Firewall Onboarding | AIOps for NGFW (Premium)
                                (Optional) Zero Touch Provisioning (ZTP) | Yes
                                ZTP onboarding is optional |
| Firewall Management | Strata Cloud Manager | YesAccount Administrator or App Administrator |
| Logging | Strata Logging Service | Yes |
| Data Filtering | Enterprise data loss prevention (DLP) | No |
| Routing | Advanced Routing Engine
                                Enabled by default during onboarding | Yes |
| SaaS Application Management | Next-Generation CASB | No |









 















 

## TCP Ports and FQDNs Required for Cloud Management of NGFWs



 Review the TCP ports and Fully Qualified Domain Names (FQDN) that you must enable on
 your network communication and between the Palo Alto Networks Next-Gen Firewall
 (NGFW) and Strata Cloud Manager. Communication on these TCP ports and FQDNs must
 allowed on your network to successfully manage your firewalls from Strata Cloud Manager.

- Connections to Strata Cloud Manager
- Connections to Strata Logging Service
- Connections for Firewall Certificates


 















 

### Connections to Strata Cloud Manager



 You must allow the following app, FQDNs, and TCP ports on your network to enable
 connectivity between the firewall and Strata Cloud Manager. 

The Virtus service is a device connectivity service that facilitates the
 connection between the firewall and Strata Cloud Manager. The FQDN and/or IP
 address for the region where your Strata Cloud Manager tenant is deployed must
 be allowed on your network for the firewall to successfully connect to Strata Cloud Manager. The firewall cannot connect to Strata Cloud Manager if
 the FQDN or IP address is blocked.
























 

| App-ID | TCP Port |
| --- | --- |
| panorama | 3978 |

























 

- [ocsp.paloaltonetworks.com/](http://ocsp.paloaltonetworks.com/)

- [ocsp.godaddy.com](http://ocsp.godaddy.com)

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

****

| Service | FQDN | IP Address | TCP Ports |
| --- | --- | --- | --- |
| OCSP |  | N/A | 80 |
| Virtus | Australia—*.aus.ngfw.cloudmgmt.paloaltonetworks.com | 34.151.118.202 | 3978
                                    443 |
| Canada—*.ca.ngfw.cloudmgmt.paloaltonetworks.com | 34.118.139.11 |  |  |
| E.U—*.eu.ngfw.cloudmgmt.paloaltonetworks.com | 35.246.199.57 |  |  |
| France—*.fr.ngfw.cloudmgmt.paloaltonetworks.com | 34.155.195.45 |  |  |
| India—*.in.ngfw.cloudmgmt.paloaltonetworks.com | 35.200.223.12 |  |  |
| Israel —*.il.ngfw.cloudmgmt.paloaltonetworks.com | 34.165.153.154 |  |  |
| Italy—*.it.ngfw.cloudmgmt.paloaltonetworks.com | 34.154.245.218 |  |  |
| Indonesia—*.id.ngfw.cloudmgmt.paloaltonetworks.com | 34.101.126.22 |  |  |
| Japan—*.jp.ngfw.cloudmgmt.paloaltonetworks.com | 34.146.27.93 |  |  |
| Poland—*.pl.ngfw.cloudmgmt.paloaltonetworks.com | 34.118.28.91 |  |  |
| Qatar—*.qa.ngfw.cloudmgmt.paloaltonetworks.com | 34.18.53.154 |  |  |
| Saudi Arabia—
                                        *.sa.ngfw.cloudmgmt.paloaltonetworks.com | 34.166.126.37 |  |  |
| Singapore—*.sg.ngfw.cloudmgmt.paloaltonetworks.com | 35.198.210.240 |  |  |
| South
                                        Africa—*.za.ngfw.cloudmgmt.paloaltonetworks.com | 34.35.27.12 |  |  |
| Spain—*.es.ngfw.cloudmgmt.paloaltonetworks.com | 34.175.25.27 |  |  |
| Switzerland—*.ch.ngfw.cloudmgmt.paloaltonetworks.com | 34.65.231.25 |  |  |
| U.K—*.uk.ngfw.cloudmgmt.paloaltonetworks.com | 35.246.86.14 |  |  |
| U.S.A—*.us.ngfw.cloudmgmt.paloaltonetworks.com | 34.31.195.141 |  |  |
| Discovery Service | ds-cloudmgmt.paloaltonetworks.com | N/A | 443 |









 















 

### Connections to Strata Logging Service



 You must allow the following apps, FQDNs, and TCP ports on your network to
 forward logs from the managed firewall to Strata Logging Service (SLS). For more
 details, see the [TCP Ports and FQDNs Required for](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/ports-and-fqdns) (SLS).
























 

- 

- 

[device
                                                telemetry](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/device-telemetry/device-telemetry-overview)

- 

- 

| App-ID | TCP Port |
| --- | --- |
| paloalto-shared-servicespanorama | 444
                                    3978 |
| Required if you’re sending  data to SLS.
                                    paloalto-device-telemetrygoogle-base | 443
                                    5222-5224
                                    5228
                                    5229 |

























 

- [ocsp.paloaltonetworks.com/](http://ocsp.paloaltonetworks.com/)

- [crl.paloaltonetworks.com/](http://crl.paloaltonetworks.com/)

- [ocsp.godaddy.com](http://ocsp.godaddy.com)

- [api.paloaltonetworks.com](https://api.paloaltonetworks.com)

- [apitrusted.paloaltonetworks.com](https://apitrusted.paloaltonetworks.com)

- [certificatetrusted.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com)

- [certificate.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com)

| Service | FQDN | TCP Ports |
| --- | --- | --- |
| OCSP |  | 80 |
| SLS Certificates |  | 3978 |
| Prisma Access | *.gpcloudservice.com | 443 |









 















 

### Connections for Firewall Certificates



 You must allow the following FQDNs, and TCP ports on your network to enable your
 managed firewalls to install the device certificates for Strata Cloud Manager. 
























 

- [api.paloaltonetworks.com](https://api.paloaltonetworks.com)

- [apitrusted.paloaltonetworks.com](https://apitrusted.paloaltonetworks.com)

- [certificatetrusted.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com)

- [certificate.paloaltonetworks.com](http://certificatetrusted.paloaltonetworks.com)

| Service | FQDN | TCP Ports |
| --- | --- | --- |
| API |  | 443 |
| Device Certificates |  | 443 |

































 

# Strata Cloud Manager Prerequisites for Prisma Access



 Here's what you need to know to plan your Prisma Access deployment



 Strata Cloud Manager provides comprehensive visibility and insights into all Prisma
 Access deployments, whether managed by Strata Cloud Manager or Panorama. Additionally,
 you have the option to use Strata Cloud Manager as the management interface for Prisma
 Access if needed.

During Prisma Access activation, you can choose either Strata Cloud Manager or Panorama
 as the management interface. If Panorama currently manages your Prisma Access
 deployment, you can migrate the configuration to Strata Cloud Manager for management.
 However, after migrating, you cannot switch back to Panorama.

Before onboarding Prisma Access to Strata Cloud Manager, carefully review the following
 prerequisites to ensure your existing Prisma Access deployment satisfies all necessary
 conditions for a smooth and seamless onboarding.

- **Panorama Version** - Ensure you are using Panorama version 10.0 or higher.
- **Administrative Privileges** - You need an account with superuser privileges to
 log into Strata Cloud Manager.
- **License Requirements** - Ensure you have a valid [Prisma Access license](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license).
- **Cloud Identity Engine** - Ensure that you have [integrated the Directory Sync component](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-user-based-policy/integrate-cloud-identity-engine-with-prisma-access/integrate-cloud-identity-engine-with-prisma-access-panorama#integrate-cloud-identity-engine-with-prisma-access-panorama) of
 the Cloud Identity Engine with the current Prisma Access (Managed by Panorama)
 tenant
Additionally, if you are migrating from Panorama to Strata Cloud Manager, review the
 [migration prerequisites](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/migrate-prisma-access-from-panorama-to-strata-cloud-manager?otp=task-bcj_p2w_zbc#task-bcj_p2w_zbc) to confirm whether
 your deployment is eligible for configuration migration.