<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/configuration-onboarding -->
<!-- Fetched: 2026-03-31T18:44:57.103508+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: scm, onboarding -->

# Configuration: Onboarding with Strata Cloud Manager

 

 
 
 
 
 
 

 

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
                            
                                    Configuration: Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm.html)
 

 
 

**[Next
                                
                                    Configuration: NGFW and Prisma Access](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access.html)
 

 

---

 
 
 















 

# Configuration: Onboarding with Strata Cloud Manager



 Get started with securing your network environment with Strata Cloud Manager's
 intuitive onboarding guides.



 






















 

- [Software NGFW
                                    Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- 

- [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)

- [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)
- [AIOps for NGFW Premium](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-free-and-premium-features)[Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW, including those funded by Prisma Access (Managed by Strata Cloud Manager) | One of these:
                            
                                        license or |


Go to ConfigurationOnboarding to get started with securing your network environment with Strata Cloud
 Manager's intuitive onboarding guides, designed to walk you through essential security
 configurations.

## Migration Catalog

 The Migration Catalog feature simplifies and streamlines the process of
 migrating configurations to Strata Cloud Manager. As organizations evolve their
 network security infrastructure, they must migrate existing configurations from
 various platforms to Strata Cloud Manager. Migration Catalog provides a unified
 approach and a consistent user experience for these migrations.

Migration Catalog acts as a central hub where administrators can access all
 migration-related workflows. This consolidated approach eliminates the need to
 navigate different sections of Strata Cloud Manager to find specific migration
 tools. Each migration option is presented as a tile, which provides information
 about the workflow steps and prerequisites for a successful migration.

Currently, the catalog supports [Panorama-managed NGFW migration](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/migrate-from-panorama-to-strata-cloud-manager). The
 migration path follows a standardized workflow-based user experience, which makes it
 intuitive for you to progress through the migration process regardless of the source
 platform.

Before you use Migration Catalog, understand your current environment's
 configuration and ensure you meet the prerequisites for your specific migration
 scenario. The catalog displays the last access timestamp for each migration option,
 which helps you track your migration activities over time.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

## Initial Configuration

 Go to ConfigurationOnboarding to get started with onboarding your Prima Access or NGFW
 deployments.

The initial Prisma Access and NGFW onboarding workflow provides a simplified
 experience for new Prisma Access or NGFW deployments. This guided workflow quickly
 deploys and configures various Prisma Access and NGFW components, including mobile
 users and private applications, significantly reducing deployment time.

**Prerequisites**

Before onboarding mobile users, ensure that you have the following licenses:
- Prisma Access license for mobile users.
- Strata Logging Service license with adequate firewall storage
 capacity.
- If mobile users connect to other networks, you will need either the Zero
 Trust Network Access (ZTNA) or Enterprise Edition Prisma Access license,
 which provides the corporate access node (CAN) necessary to connect.

 
 

 

- **Onboard Users**Use the following onboarding workflows when setting
 up Prisma Access for the first time. After saving your configuration and
 completing the setup, you can further modify your Prisma Access
 deployment through the Prisma Access web interface.

  - **[Onboarding Workflow for
                                            Prisma Access GlobalProtect
                                        Deployments](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-globalprotect-deployments)**Secure mobile users using
 GlobalProtect, or use a hybrid deployment with GlobalProtect
 and Explicit Proxy in Proxy Mode or Tunnel and Proxy
 Mode.

  - [Onboarding Workflow for
                                        Prisma Access Explicit Proxy Deployments](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-explicit-proxy-deployments)Secure
 mobile users by redirecting browser traffic to Prisma Access
 through Explicit Proxy for secure access.

  - [Onboarding Workflow for
                                        Prisma Access Browser](https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-access-browser-onboarding)Extend SASE capabilities and
 create a secure workspace using a natively integrated
 enterprise browser.

- **Onboard Connectivity to Private Apps**Provide secure access to
 private applications for mobile and remote site users using one of the
 workflows:

  - **[Onboarding Workflow for
                                        Prisma Access ZTNA Connector](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-ztna-connector)**The Zero Trust
 Network Access (ZTNA) Connector securely connects Prisma Access
 to your organization's private applications. It automatically
 establishes secure tunnels for mobile and branch users,
 eliminating the need for manual IPSec or routing configurations
 to data centers, public clouds, or partner networks.

  - **[Onboarding Workflow for
                                        Prisma Access Service Connection](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/onboard-prisma-access/onboarding-workflow-for-service-connections)**Service
 connections enable access to internal resources (for example,
 those at data centers or headquarters). If your license includes
 it, service connections also act as an interconnect between
 internal resources, agent-based mobile users, and branch site
 users.

- **Onboard Branch Sites**Establish secure connectivity for branch
 offices, branch gateways, and remote sites.

  - [Onboarding Workflow for
                                    Site-Based Remote Networks](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/onboard-prisma-access/onboard-a-site-based-remote-network)
 Quickly onboard branch sites using Prisma Access remote networks
 to provide consistent, best-in-class security to all users and
 devices.

  - [Onboard Prisma SD-WAN Branch
                                    Sites to Prisma Access](https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-native-integrations/onboard-branch-sites-to-prisma-access)Connect Prisma SD-WAN branch
 sites to Prisma Access for consistent security and
 connectivity.