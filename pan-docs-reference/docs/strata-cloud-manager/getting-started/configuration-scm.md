<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm -->
<!-- Fetched: 2026-03-31T18:44:52.763844+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: scm, regions, config -->

# Configuration: Strata Cloud Manager

 

 
 
 
 
 
 

 

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
                            
                                    Log Viewer: Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/getting-started/log-viewer.html)
 

 
 

**[Next
                                
                                    Configuration: Onboarding with Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/configuration-onboarding.html)
 

 

---

 
 
 















 

# Configuration: Strata Cloud Manager



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



 Strata Cloud Manager enables you to configure a security policy that is shared
 across your NGFWs and Prisma Access. Continue on here to set up the following.

 
 
 

 

 
- Onboarding is the process of integrating your existing [NGFWs and Prisma Access](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access.html) into Strata
 Cloud Manager for management, visibility, or both. You can manage NGFWs
 directly through Strata Cloud Manager along with Prisma Access deployments,
 or connect your Panorama instance to Strata Cloud Manager to gain
 visibility.
- [Discovery](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/discovery.html) is where you can start critical and recommended
 actions you can take to improve security posture or optimize your
 configuration management, as soon as they're available to you.
- Enhance security for both managed and unmanaged devices using [Prisma Access Browser](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-prisma-access-browser.html). Prisma Access
 Browser provides a natively integrated enterprise browser that extends
 protection to unmanaged devices, helping safeguard business applications and
 data by implementing security directly within the browser.
- Manage your organization's shadow IT risks, secure [SaaS
                            applications](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/objects/saas-application-management.html) from cloud threats, and ensure compliance across all
 SaaS applications.
- Enforce your organization's data security standards and stop the loss of
 sensitive data across mobile users and remote networks using [Enterprise Data Loss Prevention](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-enterprise-dlp.html).
- [App Acceleration](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/activity-insights-app-acceleration.html) directly addresses
 the causes of poor app performance and acts in real-time to mitigate them,
 dramatically improving the user experience for Prisma Access GlobalProtect
 and Remote Network users.
- [ZTNA Connector](/content/techdocs/en_US/strata-cloud-manager/getting-started/insights-scm/monitor-data-centers/monitor-data-centers-ztna-connectors.html) provides a simple
 solution to onboard private applications to Prisma Access, while enabling
 true least privilege access using Zero Trust Network Access principles.
- [Push
                            configuration](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/operations.html) changes, review the configuration push history to
 your deployments, compare the configuration versions or revert to an earlier
 version.
- Customize [security posture](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/security-posture.html) checks for your deployment to
 maximize relevant recommendations.
- Set up branch sites, data center, configure policies, CloudBlades, manage
 resources, monitor uses and permissions in[Prisma SD-WAN](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-prisma-sd-wan.html) using Strata Cloud Manager.