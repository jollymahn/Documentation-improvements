<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-ngfw -->
<!-- Fetched: 2026-03-31T18:30:15.080754+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: scm, ngfw, activation -->

# Activate Strata Cloud Manager Pro for NGFW

 

 
 
 
 
 
 

 

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

 
 

 

 

---

 
 
 















 

# Activate Strata Cloud Manager Pro for NGFW



 Learn about how to activate Strata Cloud Manager Pro for NGFW.



 
 This task shows how to activate Strata Cloud Manager Pro for NGFW. For details about
 device models support, see [Device Model Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility).

 Here are the prerequisites for NGFW:

 
- **[Cloud Management Onboarding
                            Prerequisites](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/prerequisites-for-cloud-management-onboarding)** - Before onboarding your NGFW to Strata Cloud
 Manager, verify that all conditions for device readiness are fulfilled. This
 includes network configuration, software compatibility, and licensing
 requirements. Completing these steps ensures that your firewall can be
 successfully managed using Strata Cloud Manager. 
- **[TCP Ports and FQDNs for Cloud
                            Management](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/tcp-ports-and-fqdns-required-for-cloud-management)** - To enable seamless communication between the
 NGFW and Strata Cloud Manager, configure specific TCP ports and Fully Qualified
 Domain Names (FQDNs). 

 

1.  After you receive an email from Palo Alto Networks identifying the Strata Cloud
 Manager Pro license you're activating, click the email link to begin the
 activation process. 
2.  Select Tenant where you will activate Strata Cloud
 Manager Pro. If you don't have an existing [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant), **Create New**.
3.  Select a Region where you want to deploy Strata Cloud
 Manager. See the [supported regions for Strata Cloud
                        Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/regions-aiops-for-ngfw).
 Strata Cloud Manager Pro includes [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview) with
 one year of log retention. 

 

4.  Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
 CIE instance to identify and verify all users across your infrastructure.
5.  Agree to the Terms and Conditions, and
 Activate. 
6.  Wait for Strata Cloud Manager, Cloud Identity Engine, and Strata Logging
 Service to initialize, and for Status to show Complete.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

7.  [Associate NGFWs, Panorama, or both](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) to
 a tenant containing your Strata Cloud Manager. 
 
 
 Make sure to individually associate all the
 firewalls managed by Panorama to the tenant.

 

 
  1. Navigate to Common Services > Device
 Associations. 
  2. Add Devices. 
  3. Select one or more firewalls or Panorama appliances and
 Save.

 

8.  [Associate products](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) with devices. After
 activating Strata Cloud Manager Pro, you need to specify the firewalls or
 Panorama appliances that you want to use with it.
 
  1. Navigate to Common Services > Device
 Associations.

  2. **Associate Products**.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
  3. In the Products selection column, select Strata
 Cloud Manager.

  4. Select devices and **Save**.

 

9.  [Enable telemetry on devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics). Strata
 Cloud Manager assesses the health of the devices in your deployment by analyzing
 telemetry data that your PAN-OS devices send to Strata Logging Service. To send
 this data, you must have enabled device telemetry on your devices.
 
 
 Beginning with PAN-OS 12.1.2, 11.1.11, 11.2.8,
 10.2.17, and later releases, the [telemetry auto-enablement feature](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview)
 configures telemetry to be enabled by default on your devices. Upon
 onboarding a new device (Panorama or firewall), telemetry is automatically
 enabled with settings centrally controlled through Strata Cloud Manager or
 
 Activation Console. 

 

10.  Log in to Strata Cloud Manager by clicking on its icon in the 
 Activation Console.