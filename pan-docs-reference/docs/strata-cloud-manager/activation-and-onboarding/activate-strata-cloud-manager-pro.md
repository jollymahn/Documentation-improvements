<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro -->
<!-- Fetched: 2026-04-01T01:59:22.295074+00:00 -->
<!-- Project: scm -->
<!-- Tags: scm, activation, pro -->

# Activate Strata Cloud Manager Pro

 

 
 
 
 
 
 

 

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
                            
                                    Activate Strata Cloud Manager Essentials](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-essentials.html)
 

 
 

**[Next
                                
                                    Upgrade to Strata Cloud Manager Pro, from Strata Cloud Manager Essentials](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/upgrade-to-strata-cloud-manager-pro.html)
 

 

---

 
 
 















 

# Activate Strata Cloud Manager Pro



 Learn about how to activate Strata Cloud Manager Pro which provides advanced features
 beyond the Essentials license.



 
 
 **Important**: We are rolling out this new, unified activation experience in
 stages. For supported SASE products, you may see the new activation console now, or
 you maybe directed to use the Hub for activation until the update reaches your
 tenant.
























 

- [Software NGFW
                                            Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- 

- [Strata Cloud Manager Pro](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)
[your licenses remain
                                        supported](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager.html)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW, including those funded by Prisma Access | If you began using Strata Cloud Manager before this licensing
                                    tiers was introduced, . |


Strata Cloud Manager Pro provides advanced features beyond the Essentials
 license. Unlike the Essentials version, it includes the Strata Logging Service and
 provides one year of log retention. For details about device models support, see [Device Model Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility).

When your Strata Cloud Manager Pro license expires, the Strata Cloud Manager instance
 will revert to Strata Cloud Manager Essentials licensing tier. Upon license expiration
 for other subscriptions, some continue to function in a limited capacity, and others
 stop operating completely. See [what happens when each subscription
            expires](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/subscriptions/what-happens-when-licenses-expire).

- [NGFW](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-ngfw.html#activate-strata-cloud-manager-pro-for-ngfw)
- [Prisma Access](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-prisma-access.html#activate-strata-cloud-manager-pro-prisma-access)
- [VM-Series with Software NGFW
                        Credits](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-vm-series-with-software-ngfw-credits.html#activate-vm-series-with-software-ngfw-credits)
- [ELA](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-ela.html#ela)
- [ESA Pro](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro/activate-esa.html#esa)

















 

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





















 

# Activate Strata Cloud Manager Pro for Prisma Access



 Learn about how to activate Strata Cloud Manager Pro for Prisma Access.



 
 All [Prisma Access license types](https://docs.paloaltonetworks.com/prisma-access/administration/activate-your-prisma-access-license) include access
 to Strata Cloud Manager, and all Prisma Access deployments can leverage Strata Cloud
 Manager for visibility features – like Command Center and Activity Insights – and
 [Autonomous DEM](https://docs.paloaltonetworks.com/autonomous-dem) monitoring. 

 Additionally, can optionally choose to use Strata Cloud Manager for your [Prisma Access configuration management](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/how-to-manage-prisma-access);
 your other option is to use Panorama for configuration management. In both cases,
 you'll be guided to activate Strata Cloud Manager Pro during your Prisma Access
 license activation:

 
- [Activate Prisma Access, with Strata Cloud
                        Manager configuration management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation)
- [Activate Prisma Access, with Panorama
                        configuration management](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/panorama-managed-prisma-access-and-add-ons-license-activation)

 






















 

# Activate Strata Cloud Manager Pro for VM-Series with Software NGFW Credits



 Learn about how to activate Strata Cloud Manager Pro for VM-Series with Software NGFW
 Credits.



 
 You can manage VM-Series firewalls funded by Software NGFW Credits using Strata Cloud
 Manager, enabling seamless access to advanced management and monitoring features
 through Strata Cloud Manager Pro activation. 

 Strata Cloud Manager supports management of both standalone VM-Series firewalls and
 Panorama-managed VM-Series deployments, offering a comprehensive solution for
 overseeing multiple environments:

 
- [Activate Strata Cloud Manager Pro for
                        VM-Series](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/software-ngfw-credits-activation#task-vm-flex-aiops)
- [Activate Strata Cloud Manager Pro for
                        Panorama Managed VM-Series](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/software-ngfw-credits-activation#task-aiops-panorama-credits)

 






















 

# Activate Strata Cloud Manager Pro with the Enterprise License Agreement



 Learn about how to activate Strata Cloud Manager Pro for Enterprise License Agreement
 users.



 
 This task shows how to activate Enterprise License Agreement (ELA) for Strata Cloud
 Manager. The add-on for ELA is a consumption model for large enterprises to assign
 subscriptions in bulk to assets purchased from Palo Alto Networks. 

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

 
 
 You can activate multiple Strata Cloud Manager Pro tenants using the same license
 for devices belonging to the same support accounts. To do this, navigate to the
 Tenant Management to [create new tenants](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants). Then, go to the
 Subscriptions & Add-ons, search for your
 subscription, click Activate Cloud Tenant that will
 redirect you to the activation page. Choose the same TSG on the activation page
 that you used initially.

 

1.  Use one of the following activation methods.
 
  - Log in to 
 [Activation Console](https://apps.paloaltonetworks.com/hub) and select ELA Activation Strata Cloud Manager.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
  - Log into the Customer Support Portal and activate from License ManagementLicenses, and then click ELA-Ngfw
 Activation.

 

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
6.  Wait for Strata Cloud Manager and Strata Logging Service to initialize and for
 Activation Status for both to show Complete.
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
 
  1. Log in to the 
 [Activation Console](https://apps.paloaltonetworks.com/hub) and select Common Services > Device
 Associations.

  2. **Associate Products**.

  3. In the Licensed Products selection column, select
 Strata Cloud Manager.

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





















 

# Activate Strata Cloud Manager Pro with the Enterprise Support Agreement



 Learn about how to activate Strata Cloud Manager Pro for NGFW with the Enterprise
 Support Agreement.



 
 The Palo Alto Networks Enterprise Support Agreement (ESA) Pro includes
 Strata Cloud Manager Pro for NGFW. ESA Pro provides a streamlined solution for a
 consistent support experience across your existing assets and anticipated purchases.
 This enterprise program enables organizations to maximize savings and benefits as
 they scale up, making it an ideal choice for customers with large, expanding
 firewall deployments. 

 This task shows how to activate ESA Pro for Strata Cloud Manager. You can
 start the ESA Pro activation process from the 
 Activation Console or Customer Support Portal as
 described below.

 

1.  Use one of the following activation methods:
 
  - Log in to 
 [Activation Console](https://apps.paloaltonetworks.com/hub) and select ESA Activation Strata Cloud Manager.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
  - Log in to the Customer Support Portal. In the left side-panel, go to
 License Management, and then, under
 Licenses, select Activate
 Enterprise Agreement.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

 

2.  Create a New tenant where you will activate the Strata
 Cloud Manager instance. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

3.  Select a Region where you want to deploy Strata Cloud
 Manager. See the [supported regions for Strata Cloud
                        Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/regions-aiops-for-ngfw).
 A Strata Cloud Manager Pro license includes [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview) with one
 year of log retention.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

4.  Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
 CIE instance to identify and verify all users across your infrastructure.
5.  Agree to the Terms and Conditions, and
 Activate. 
6.  Wait for Strata Cloud Manager and Strata Logging Service to initialize and for
 Activation Status for both to show Complete.
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
 
  1. Log in to the 
 Activation Console and select
 Common Services > Device
 Associations.

  2. **Associate Products**.

  3. In the Licensed Products selection column, select
 Strata Cloud Manager.

  4. Select devices and **Save**.

 

9.  [Enable telemetry on the devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics).
 Strata Cloud Manager assesses the health of the devices in your deployment by
 analyzing telemetry data that your PAN-OS devices send to Strata Logging
 Service. To send this data, you must have enabled device telemetry on your
 devices.
 
 
 Beginning with PAN-OS 12.1.2, 11.1.11, 11.2.8,
 10.2.17, and later releases, the [telemetry auto-enablement feature](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview)
 configures telemetry to be enabled by default on your devices. Upon
 onboarding a new device (Panorama or firewall), telemetry is automatically
 enabled with settings centrally controlled through Strata Cloud Manager or
 
 Activation Console. 

 

10.  Log in to Strata Cloud Manager by clicking on its icon in the 
 [Activation Console](https://apps.paloaltonetworks.com/hub).