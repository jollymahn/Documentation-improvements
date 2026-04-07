<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-essentials -->
<!-- Fetched: 2026-04-01T01:59:21.357371+00:00 -->
<!-- Project: scm -->
<!-- Tags: scm, activation, essentials -->

# Activate Strata Cloud Manager Essentials

 

 
 
 
 
 
 

 

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
                            
                                    Activate Your Strata Cloud Manager Licenses](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager.html)
 

 
 

**[Next
                                
                                    Activate Strata Cloud Manager Pro](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager/activate-strata-cloud-manager-pro.html)
 

 

---

 
 
 















 

# Activate Strata Cloud Manager Essentials



 Learn about how to activate Strata Cloud Manager Essentials that offers configuration
 and network security lifecycle management features.



 
 
 
 **Important**: We are rolling out this new, unified activation experience in
 stages. For supported SASE products, you may see the new activation console now,
 or you maybe directed to use the Hub for activation until the update reaches
 your tenant.

 






















 

- [Software NGFW
                                            Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- 

- [Strata Cloud Manager Essentials](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)
[your licenses remain
                                        supported](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager.html)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW, including those funded by Prisma Access | If you began using Strata Cloud Manager before these licensing
                                    tiers were introduced, . |



 Strata Cloud Manager Essentials is the free tier that offers configuration
 and network security lifecycle management features to streamline operations and
 provide essential security. For details about device models support, see [Device Model Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/hardware-model-compatibility).

 You can [activate VM-Series funded by software NGFW
                    credits](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/software-ngfw-credits-activation#task-vm-flex-aiops) using the Strata Cloud Manager Essentials license tier. If you
 don’t select a [cloud subscription in the deployment
                    profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series), Strata Cloud Manager Essentials activates automatically.

 

1.  Log in to 
 [Activation Console](https://apps.paloaltonetworks.com/hub).
2.  Go to the Strata Cloud Manager Essentials activation URL: 
3. [tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) where you will activate Strata
 Cloud Manager.
4.  Select a Region where you want to deploy Strata Cloud
 Manager. See the [supported regions for Strata Cloud
                        Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/regions-aiops-for-ngfw).
 Region support varies based on whether you want to manage NGFWs, Prisma
 Access, or both simultaneously. To manage both, you must select a region
 that supports both NGFWs and Prisma Access. 

 

5.  Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
 CIE instance to identify and verify all users across your infrastructure. You
 can also skip it by selecting None. 
6.  Agree to the Terms and Conditions, and
 Activate. 
7.  Wait for Strata Cloud Manager to initialize and for Status to show Complete. 
 If you have created a new Cloud Identity Engine instance, wait for it's
 Status to show Complete.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

8.  [Associate NGFWs, Panorama, or both](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) to
 a tenant containing your Strata Cloud Manager.
 
 
 Make sure to individually associate all the
 firewalls managed by Panorama to the tenant.

 

 
  1. Navigate to Common Services > Device
 Associations. 
  2. Add Devices. 

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
  3. Select one or more firewalls or Panorama appliances and
 Save.

 

9.  If you have [Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview), you can [associate it with devices](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices). Otherwise,
 you can skip it.
 After activating Strata Cloud Manager Essentials, you can specify the
 firewalls or Panorama appliances that you want to use with Strata Logging
 Service.

 
  1. Select Common Services > Device
 Associations.

  2. **Associate Products**.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
  3. In the Products selection column, select Strata
 Logging Service.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
  4. Select devices and **Save**.

 

10.  [Enable telemetry on devices](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about-metrics). Strata
 Cloud Manager assesses the health of the devices in your deployment by analyzing
 telemetry data that your PAN-OS devices send to Strata Logging Service. To send
 this data, you must have enabled device telemetry on your devices.
 
 
 Beginning with PAN-OS 12.1.2, 11.1.11, 11.2.8,
 10.2.17, and later releases, the [telemetry auto-enablement feature](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/device-telemetry/device-telemetry-overview)
 configures telemetry to be enabled by default on your devices. Upon
 onboarding a new device (Panorama or firewall), telemetry is automatically
 enabled with settings centrally controlled through Strata Cloud Manager or
 
 Activation Console. 

 

11.  Log in to Strata Cloud Manager by clicking on its icon in the 
 Activation Console.