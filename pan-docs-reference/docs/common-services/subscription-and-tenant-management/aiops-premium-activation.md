<!-- Source: https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/aiops-premium-activation -->
<!-- Fetched: 2026-04-01T01:59:14.252952+00:00 -->
<!-- Project: scm -->
<!-- Tags: aiops, activation -->

# Activate AIOps Premium



 



 Learn about AIOps Premium activation.



 
 






















 

- 
- 

- 

| Where Can I Use
                                This? | What Do I Need? |
| --- | --- |
| From email activation linkCommercial deployments | Customer Support Portal account |



 [Strata Cloud Manager](https://docs.paloaltonetworks.com/cloud-management) provides unified management and
 operations only for NGFWs using the AIOps for NGFW Premium license.

 
- Continue to use the AIOps for NGFW Free app for the NGFWs onboarded
 to AIOps for NGFW Free. For more information, see [Activate AIOps for NGFW Free](https://docs.paloaltonetworks.com/ngfw/getting-started/activate-aiops-for-ngfw).
- To activate AIOps for NGFW with the add-on Enterprise License
 Agreement (ELA), see [activate an add-on enterprise license
                        agreement](/content/techdocs/en_US/common-services/subscription-and-tenant-management/enterprise-license-agreement-add-on-activation.html). 
- To activate AIOps for NGFW with a Software NGFW Credits License
 Agreement, see [activate a software NGFW credits license
                        agreement](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/vm-flex-license-activation/activate-vm-flex-license#task-vm-flex-aiops.html).

 The AIOps for NGFW Premium (use the Strata Cloud Manager app) license is
 supported only in a single tenant environment with paid Strata Logging Service. For information about support for firewalls and AIOps
 for NGFW license type combinations, see [Firewall and License Type Compatibility](https://docs.paloaltonetworks.com/common-services/device-associations/firewall-and-license-type-compatibility#aiops-for-ngfw-firewall-and-license-type-compatibility). 

 
 
 Strata Cloud Manager is now available, featuring two licensing tiers: Strata
 Cloud Manager Essentials and Strata Cloud Manager Pro. This unified structure
 streamlines the deployment of network security offerings, including AIOps for
 NGFW, Autonomous Digital Experience Management (ADEM), cloud management
 functionality, and Strata Logging Service. See [Strata Cloud Manager License](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html).

 
- [First time activation - one CSP
                            account](/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation/activate-aiops-premium-first-time-one-csp.html#aiops-premium-one-csp)

- [First time activation - multiple CSP accounts](/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation/activate-aiops-premium-first-time-multiple-csp.html#aiops-premium-multiple-csp)

- [Return visit
                        activation](/content/techdocs/en_US/common-services/subscription-and-tenant-management/aiops-premium-activation/activate-aiops-premium-repeat-visits.html#aiops-premium-return)

 
















 

# First time AIOps for NGFW Premium Activation - One Customer Support Portal
        Account



 



 Learn how to activate your AIOps for NGFW Premium application for the
 first time if you have only one Customer Support Portal account.



 
 If you have only one Customer Support Portal account, follow these steps for first
 time CASB-X activation. 

 

1.  After you receive an email from Palo Alto Networks identifying the AIOps for NGFW Premium license you're activating, click the email link to
 begin the activation process. 
2.  Because you have only one Customer Support Portal account associated with your
 username, the Customer Support Account is
 prepopulated.
3.  Allocate the product to the Recipient. 
  1.  The name provided matches your Customer Support Portal account for
 convenience. You can use the name provided or change it.

4.  Select a Region where you want to deploy your product. 
 The following are [supported regions](https://docs.paloaltonetworks.com/ngfw/aiops/about/regions-aiops-for-ngfw). If you first
 activate AIOps for NGFW Premium for Strata Cloud Manager in
 a [region that isn't supported](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations) for
 Prisma Access, it's allowed because there are no dependencies
 with Prisma Access.

 However, if you later want to activate Prisma Access in the same
 region as the original AIOps for NGFW Premium region, it's not an
 available option. For hybrid customers, you will have to wait until the same
 region is supported by both AIOps for NGFW Premium and Prisma Access.

 Since Prisma Access (Managed by Strata Cloud Manager) is not yet supported in all regions, the
 following AIOps for NGFW Premium region will map to a different
 region when using Strata Cloud Manager to manage the firewall.

 Strata Cloud Manager Singapore is mapped to by the following AIOps for NGFW Premium region:

 
  - singapore
  - taiwan
  - korea
  - indonesia

 Strata Cloud Manager Germany is mapped to by the following AIOps for NGFW Premium region:

 
  - Germany
  - Europe
  - Switzerland
  - Israel
  - France
  - Spain
  - Italy
  - Poland
  - Qatar

 Strata Cloud Manager America is mapped to by the following AIOps for NGFW Premium region:

 
  - Americas
  - Canada

 

5.  Add Strata Logging Service.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
  1.  Select a Strata Logging Service instance for storing your
 logs.
  2.  Enter the amount of data log storage.
  3.  The region is grayed out, but is autopopulated with the same region
 that you used for Strata Logging Service. 

6.  Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
 CIE instance to identify and verify all users across your infrastructure.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
7.  The web interface shows if you have Prisma Access and NGFW available
 in this tenant where you can apply AIOps for NGFW Premium.
8.  **Agree to the terms and conditions**, and **Activate**. 
 A single default tenant is autocreated behind the scenes, and the product is
 activated in the tenant.

 
 
 This tenant, and any others created by this Customer Support Portal
 account, will have the  Superuser role.

 

9.  Common ServicesProducts displays the status of the activation, such as
 initializing or
 complete.
10.  After the status is Complete, you must go to the Common ServicesDevice Associations tab to select the devices and add the firewall or Panorama
 appliance to your tenant. See [Associate Devices with a Tenant](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant). 
 
 
 If the status isn't
 Complete, you can't add your devices
 yet.

 

11.  Launch Strata Cloud Manager with AIOps for NGFW Premium license from one
 of the following options.
 
  - Click the Strata Cloud Manager tile in the [hub](https://apps.paloaltonetworks.com/hub).
  - Launch from Common ServicesProducts or from SettingsProducts.

 

12.  Get started with [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
13.  (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
14.  (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).





















 

# First time AIOps for NGFW Premium Activation - Multiple Customer Support
        Portal Account



 



 Learn how to activate your AIOps for NGFW Premium application for the
 first time if you have multiple Customer Support Portal accounts.



 
 If you have multiple Customer Support Portal accounts, follow these steps for first
 time AIOps for NGFW Premium activation. 

 

1.  After you receive an email from Palo Alto Networks identifying the AIOps for NGFW Premium license you're activating, click the email link to
 begin the activation process. 
2.  If you have multiple Customer Support Portal accounts, choose the
 Customer Support Account number that you want to use. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

3.  Allocate the product to the Recipient of your choice. 
 You can allocate your entire license to one recipient or you can share it
 with multiple recipients in a tenant hierarchy. [What is a tenant?](/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html)

 

  1.  If you need just one tenant, use or rename the tenant provided. The
 name provided matches your Customer Support Portal account for
 convenience.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  2.  (Optional) This step applies if you are a managed security
 service provider (MSSP), a distributed enterprise customer, or need
 multiple tenants. After you create the first tenant, you can
 Allocate to subtenant and use or rename the
 tenant provided. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

 A subscription gets allocated on a tenant or a sub-tenant. This step
 is for choosing a tenant where you want to allocate a license, not
 for building a complete tenant hierarchy. You can create only a
 tenant and subtenant here, and you can choose to allocate a license
 to that subtenant. 

 After activation, you can build out your tenant hierarchy as needed
 through [tenant management](/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html). You can create your
 tenant hierarchy to reflect your existing organizational structure.
 You can also consider [identity and access
                                    inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when creating the hierarchy, in addition to
 [tenant hierarchy limits](/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).

 

  3.  Select Done.

4.  Select a Region where you want to deploy your product. 
 The following are [supported regions](https://docs.paloaltonetworks.com/ngfw/aiops/about/regions-aiops-for-ngfw). If you first
 activate AIOps for NGFW Premium for Strata Cloud Manager in
 a [region that isn't supported](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations) for
 Prisma Access, it's allowed because there are no dependencies
 with Prisma Access.

 However, if you later want to activate Prisma Access in the same
 region as the original AIOps for NGFW Premium region, it's not an
 available option. For hybrid customers, you will have to wait until the same
 region is supported by both AIOps for NGFW Premium and Prisma Access.

 Since Prisma Access (Managed by Strata Cloud Manager) is not yet supported in all regions, the
 following AIOps for NGFW Premium region will map to a different
 region when using Strata Cloud Manager to manage the firewall.

 Strata Cloud Manager Singapore is mapped to by the following AIOps for NGFW Premium region:

 
  - singapore
  - taiwan
  - korea
  - indonesia

 Strata Cloud Manager Germany is mapped to by the following AIOps for NGFW Premium region:

 
  - Germany
  - Europe
  - Switzerland
  - Israel
  - France
  - Spain
  - Italy
  - Poland
  - Qatar

 Strata Cloud Manager America is mapped to by the following AIOps for NGFW Premium region:

 
  - Americas
  - Canada

 

5.  Add Strata Logging Service.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
  1.  Select a Strata Logging Service instance.
  2.  Enter the amount of data log storage.
  3.  The region is grayed out, but is autopopulated with the same region
 that you used for Strata Logging Service. 

6.  Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
 CIE instance to identify and verify all users across your infrastructure.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
7.  **Agree to the terms and conditions**, and **Activate**. 
 
 
 This tenant, and any others created by this Customer Support Portal
 account, will have the  Superuser role.

 

8.  Common ServicesProducts displays the status of the activation, such as
 initializing or
 complete.
9.  After the status is Complete, you must go to the Common ServicesDevice Associations tab to select the devices and add the firewall or Panorama
 appliance to your tenant. See [Associate Devices with a Tenant](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant). 
 
 
 If the status isn't
 Complete, you can't add your devices
 yet.

 

10.  Launch Strata Cloud Manager with AIOps for NGFW Premium license from one
 of the following options.
 
  - Click the Strata Cloud Manager tile in the [hub](https://apps.paloaltonetworks.com/hub).
  - Launch from Common ServicesProducts or from SettingsProducts.

 

11.  Get started with [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
12.  (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
13.  (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).





















 

# Return Visit AIOPs Premium Activation



 



 Learn how to activate your AIOPs Premium for repeat visits.



 
 Follow these steps if you have already completed first time activation, you have
 already created your tenant hierarchy through [Identity & AccessTenants](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-single-tenant-transition) or [tenant management](/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants.html), and you are returning to activate
 another product in your existing hierarchy. 

 

1.  Choose the Customer Support Account number that you want
 to use to activate. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

2.  Allocate the subscription to the Recipient tenant of
 your choice. 
 You can hover over each tenant to see which apps you already activated.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

3.  Select a Region for the physical location to process
 your data. 
 The following are [supported regions](https://docs.paloaltonetworks.com/ngfw/aiops/about/regions-aiops-for-ngfw). If you first
 activate AIOps for NGFW Premium for Strata Cloud Manager in
 a [region that isn't supported](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/list-of-prisma-access-locations) for
 Prisma Access, it's allowed because there are no dependencies
 with Prisma Access.

 However, if you later want to activate Prisma Access in the same
 region as the original AIOps for NGFW Premium region, it's not an
 available option. For hybrid customers, you will have to wait until the same
 region is supported by both AIOps for NGFW Premium and Prisma Access.

 Since Prisma Access (Managed by Strata Cloud Manager) is not yet supported in all regions, the
 following AIOps for NGFW Premium region will map to a different
 region when using Strata Cloud Manager to manage the firewall.

 Strata Cloud Manager Singapore is mapped to by the following AIOps for NGFW Premium region:

 
  - singapore
  - taiwan
  - korea
  - indonesia

 Strata Cloud Manager Germany is mapped to by the following AIOps for NGFW Premium region:

 
  - Germany
  - Europe
  - Switzerland
  - Israel
  - France
  - Spain
  - Italy
  - Poland
  - Qatar

 Strata Cloud Manager America is mapped to by the following AIOps for NGFW Premium region:

 
  - Americas
  - Canada

 

4.  Add Strata Logging Service.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
  1.  Select an Strata Logging Service instance.
  2.  Enter the amount of data log storage.
  3.  The region is grayed out, but is autopopulated with the same region
 that you used for Strata Logging Service. 

5.  Select [Cloud Identity Engine](https://docs.paloaltonetworks.com/cloud-identity) or create a new
 CIE instance to identify and verify all users across your infrastructure.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
6.  **Agree to the terms and conditions**, and **Activate**. 
 
 
 This tenant, and any others created by this Customer Support Portal
 account, will have the  Superuser role.

 

7.  Common ServicesProducts displays the status of the activation, such as
 initializing or
 complete.
8.  After the status is Complete, you must go to the Common ServicesDevice Associations tab to select the devices and add the firewall or Panorama
 appliance to your tenant. See [Associate Devices with a Tenant](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant). 
 
 
 If the status isn't
 Complete, you can't add your devices
 yet.

 

9.  Launch Strata Cloud Manager with AIOps for NGFW Premium license from one
 of the following options.
 
  - Click the Strata Cloud Manager tile in the [hub](https://apps.paloaltonetworks.com/hub).
  - Launch from Common ServicesProducts or from SettingsProducts.

 

10.  Get started with [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw).
11.  (Optional) [Manage your product](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products) from Strata Cloud Manager.
12.  (Optional) [Manage identity and access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access).