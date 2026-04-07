<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/validate-strata-cloud-manager-onboarding -->
<!-- Fetched: 2026-03-31T18:59:35.020294+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: scm, validation -->

# Validate Strata Cloud Manager Onboarding

 

 
 
 
 
 
 

 

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
                            
                                    Onboard NGFWs using Zero Touch Provisioning (ZTP)](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ztp-ngfws.html)
 

 
 

**[Next
                                
                                    Operationalize Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/operationalize-strata-cloud-manager.html)
 

 

---

 
 
 















 

# Validate Strata Cloud Manager Onboarding



 Learn how to validate if you have successfully onboarded to Strata Cloud
 Manager.



 






















 

- [Software NGFW
                                            Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- 

- [Prisma Access](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/cloud-managed-prisma-access-and-add-ons-license-activation)

- [Strata Cloud Manager Pro](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW, including those funded by Prisma Access | One of these: |


This section provides information to help you verify the successful onboarding of NGFW
 and Prisma Access deployments. It outlines the necessary details to ensure your devices
 are properly integrated and functioning as expected after onboarding.

- [NGFW](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/validate-strata-cloud-manager-onboarding/validate-ngfw-onboarding.html#topic-5ef0de0f-aadf-4b0c-9bad-0a13963bdcca)
- [Prisma Access](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/validate-strata-cloud-manager-onboarding/validate-prisma-access-onboarding.html#validate-prisma-access-onboarding)

















 

# NGFW



 



 

## NGFW for Visibility

 After installing the [Panorama CloudConnector plugin](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-plugin-for-panorama) and
 enabling [Device Telemetry](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/device-telemetry), you need to wait for 24
 hours to see data in the Strata Cloud Manager Dashboards and Activity Insights.

## NGFW for Configuration Management

 After moving your firewalls to Strata Cloud Manager, validate the onboarding of the
 devices by verifying the following:

- **Verify the state of configuration pushes**After successful onboarding to
 Strata Cloud Manager, two configuration pushes occur by default to the
 firewall. Select ConfigurationOPERATIONS Push Status to verify that your configuration push was successful.

  1. The first push from Strata Cloud Manager automatically enables the
 Advanced Routing Engine and restarts the firewall.
  2. The second pushes the configuration from Strata Cloud Manager to the
 firewall.

- **Verify the device details in the Cloud Managed Devices**Select System SettingsDevice ManagementCloud Managed Devices and check for the serial number for the firewall that you
 just added. By default, newly onboarded firewalls are added to the **All
 Firewalls** folder.

- **Validate firewall connection**[Log in to the firewall CLI](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli) and
 verify that the firewall is successfully connected to Strata Cloud
 Manager.

- Verify that your firewall appears in the **Summary View** of Strata Cloud
 Manager [Command Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center).






















 

# Prisma Access



 



 Validate your successful onboarding by launching Strata Cloud Manager and checking for
 data in the [Command Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/activity-insights/activity-insights-overview) and [Dashboards](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/dashboards/prisma-access-usage). 

If you are using Strata Cloud Manager for visibility or have migrated the management
 interface from Panorama to Strata Cloud Manager, you will immediately see data in Strata
 Cloud Manager. However, if you installed Prisma Access with Strata Cloud Manager as the
 management interface and are in the process of configuring its features, you must
 complete the full setup to start viewing data.