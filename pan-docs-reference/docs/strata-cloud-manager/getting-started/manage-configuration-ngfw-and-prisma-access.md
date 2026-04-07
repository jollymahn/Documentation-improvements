<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/manage-configuration-ngfw-and-prisma-access -->
<!-- Fetched: 2026-04-01T01:59:38.783430+00:00 -->
<!-- Project: scm -->
<!-- Tags: scm, config-management -->

# Configuration:
        NGFW and Prisma Access

 

 
 
 
 
 
 

 

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
                            
                                    Configuration: Onboarding with Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/configuration-onboarding.html)
 

 
 

**[Next
                                
                                    Configuration: Overview](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/configuration-overview.html)
 

 

---

 
 
 















 

# Configuration:
        NGFW and Prisma Access



 Strata Cloud Manager enables you to configure and enforce a shared security
 policy across your NGFWs and Prisma Access. 



 
 






















 

- 
- [Software NGFW
                                            Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)

- [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/administration/your-prisma-access-license)
- [AIOps for NGFW Premium](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-free-and-premium-features)
- [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)
- [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)
[license(s)](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview/whats-supported)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| Prisma Access (Managed by Panorama or Strata Cloud Manager)NGFW, including those funded by | Each of these licenses include access to Strata Cloud Manager:
                                
                                → The features and capabilities available to you in Strata Cloud Manager depend on which  you are
                                    using. |



 Go to ConfigurationNGFW and Prisma Access to get started.

 
 
 

 

 Strata Cloud Manager enables you to configure a security policy that is shared
 across your NGFWs and Prisma Access.

 
- [Set up
                        Prisma Access, your NGFWs, or both](/content/techdocs/en_US/strata-cloud-manager/getting-started/overview/get-started.html) with Strata Cloud Manager
- [Set up folders](/content/techdocs/en_US/strata-cloud-manager/getting-started/folder-management.html) to group NGFWs that require similar settings. Prisma
 Access folders are predefined, and enable you to target configuration based on
 deployment type: mobile users, remote networks, service connections.
- Set the [Manage: Configuration Scope](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scope.html) you want to work in. You can configure settings that will
 apply globally, across both your NGFWs and Prisma Access environment, and can
 also target configuration to specific NGFWs or Prisma Access deployments based
 on [folders](/content/techdocs/en_US/strata-cloud-manager/getting-started/folder-management.html).
- Use [Configuration: Snippets](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/configuration-overview/snippets.html) to
 standardize a common base configuration for a set of NGFWs or deployments.
 Snippets enable you to quickly onboard new devices, users, or locations with a
 known good configuration and reduce the time required to onboard a new
 device.
- Start building the following your Security policy rules and share it across your
 NGFWs and Prisma Access using the management features
 described above.
  - [Security Services](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/security-services.html)
  - [Network Policies](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/network-policies.html)
  - [Identity Services](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/identity-services.html)
  - [Objects](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/objects.html)
  - [Device Settings](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/device-settings.html)
  - [Global Settings](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/global-settings.html)