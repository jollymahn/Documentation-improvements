<!-- Source: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/migrate-prisma-access-from-panorama-to-strata-cloud-manager -->
<!-- Fetched: 2026-04-01T01:59:34.717430+00:00 -->
<!-- Project: scm -->
<!-- Tags: prisma-access, migration, panorama -->

# Migrate Prisma Access from Panorama to Strata Cloud Manager

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Prisma Access Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Release Notes
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 
 Select a Document
 
 **
 
 
 
  - 6.1 Preferred and Innovation
 
  - 6.0 Preferred and Innovation
 
  - 5.2 Preferred and Innovation
 
  - 5.1 Preferred and Innovation
 
  - 5.0 Preferred and Innovation
 
  - 4.2 Preferred
 
  - 4.1 Preferred
 
  - 4.0 Preferred
 
  - 3.2 Preferred and Innovation
 

 

 

 

 
 

 
 
- 
 
 
 
 
 

 Activation & Onboarding
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Administration
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 
 Select a Document
 
 **
 
 
 
  - 4.0 & Later
 
  - Prisma Access China
 

 

 

 

 
 

 
 
- 
 
 
 
 
 

 Integrations
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Incidents & Alerts
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 

 

 

 

 

 
 
 
---

 
 
 **

[Previous
                            
                                    Prisma Access Insights APIs](/content/techdocs/en_US/prisma-access/administration/prisma-access-overview/prisma-access-apis/monitor-prisma-access-apis.html)
 

 
 

**[Next
                                
                                    Check Logging Status, Routing, and EDL Information](/content/techdocs/en_US/prisma-access/administration/prisma-access-overview/trobleshooting-commands.html)
 

 

---

 
 
 















 

# Migrate Prisma Access from Panorama to Strata Cloud Manager



 Migrate your Prisma Access deployment from Panorama to Strata Cloud
 Manager.



 
 






















 

- 

- [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| Prisma Access (Managed by Panorama) | licenseTo begin the migration from Prisma Access (Managed by Panorama) to Prisma Access (Managed by Strata Cloud Manager), reach out to your Palo Alto
                                            Networks account team. |



 If you have an existing Prisma Access (Managed by Panorama) deployment and want to migrate to Strata Cloud Manager for configuration management, Palo Alto Networks offers an
 in-product workflow that lets you migrate your existing Prisma Access
 configuration to Prisma Access (Managed by Strata Cloud Manager).
 
 To enable migration
 workflow, contact your Palo Alto Networks account team.

 Managing your Prisma Access configuration using Strata Cloud Manager instead of
 Panorama can offer you benefits such as:

 
- Continuous [best practice assessments](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview/built-in-best-practices)
- Secure default configurations
- Machine learning (ML)-based configuration optimization
- Streamlined web security workflows
- An interactive visual summary ([Command Center](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/command-center)) that helps you to
 assess the health, security, and efficiency of the network 
- Intuitive [workflows](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/workflows) for complex tasks
- Simple and secure [management APIs](https://pan.dev/access/api/prisma-access-config/)
- Cloud-native architecture provides scalability, resilience, and global
 reach
- No hardware to manage or software to maintain

 



 















 

## Prepare to Migrate to Prisma Access (Managed by Strata Cloud Manager)



 Before you start your migration, you should be aware
 of the minimum software requirements and the types of Prisma Access (Managed by Panorama)
 deployments you can migrate. 
- **When to Migrate**—Don’t perform your upgrade during a dataplane or
 infrastructure upgrade. Check your [upgrade preferences](/content/techdocs/en_US/prisma-access/administration/prisma-access-releases-and-upgrades/use-the-prisma-access-app-to-get-upgrade-alerts-and-updates.html) to
 see if you have an upcoming dataplane upgrade.
- **One-Way Migration from Panorama to Prisma Access (Managed by Strata Cloud Manager)**—You can only
 migrate from a Prisma Access (Managed by Panorama) to a Prisma Access (Managed by Strata Cloud Manager) deployment.
 After you migrate to Strata Cloud Manager, you can’t return to managing
 your Prisma Access deployment using Panorama. 
- **Minimum Panorama Version**—A minimum Panorama version of 10.0 is
 required. 
- **Required Panorama and Strata Cloud Manager Administrator Roles**—Be
 sure that you have Superuser administrative roles for [Panorama](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-overview/role-based-access-control/administrative-roles) and [Strata Cloud Manager](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions). Before you
 begin the migration process, you export an .xml configuration file from
 Panorama, and the user exporting the file must have an administrative role
 of Superuser, and the user doing the migration in Strata Cloud Manager must
 also be a Superuser. 
- **Licensing Requirements**—A valid Prisma Access
 license is required. 
- **Cloud Identity Engine**—You must have [integrated the Directory Sync
                            component](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-user-based-policy/integrate-cloud-identity-engine-with-prisma-access/integrate-cloud-identity-engine-with-prisma-access-panorama#integrate-cloud-identity-engine-with-prisma-access-panorama) of the Cloud Identity Engine with the current Prisma Access (Managed by Panorama) tenant before migrating.
- **Unsupported Functionalities**—The migration program does not support
 the following Prisma Access functionalities:
  - [Data Filtering](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/security-profiles/set-up-data-filtering) (as an
 alternative, use [Enterprise DLP](https://docs.paloaltonetworks.com/enterprise-dlp))
  - [FedRAMP](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-requirements) deployments
  - [IoT Security](https://docs.paloaltonetworks.com/iot)
  - [Multitenant](/content/techdocs/en_US/prisma-access/administration/manage-multiple-tenants-in-prisma-access.html)
 deployments
  - [SSH Proxy](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/decryption/decryption-concepts/ssh-proxy)
  - Separate authentication for GlobalProtect™ portals and gateways

- **Prisma SD-WAN and Prisma Access Migrations**—If you migrate a Prisma
 Access and a [Prisma SD-WAN](https://docs.paloaltonetworks.com/prisma-sd-wan) deployment, Prisma Access and Prisma SD-WAN must share the same
 tenant service group ID ([TSG ID](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)).
- Config Diff Issues—When you run the config diff
 during the migration, ignore any diffs that show the following object names
 because they don't affect your configuration:
  - Clientless-vpn crypto-settings

  - Hip-profiles rename 

  - Mobile-user-redundancy 

  - Exclude-video-traffic








 















 

## Migrate Your Prisma Access (Managed by Panorama) Deployment to Strata Cloud Manager



 To migrate your Prisma Access (Managed by Panorama) to a Prisma Access (Managed by Strata Cloud Manager) deployment, complete the following steps.At a high level,
 you: 

1. Make sure that you have successfully pushed the latest configuration to Prisma Access, have saved the latest configuration, and have exported an
 .xml configuration file from the Panorama that manages Prisma Access.
 The user exporting this file in Panorama must have an [administrative role](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-overview/role-based-access-control/administrative-roles) of
 Superuser. 

2. Start the migration program from Strata Cloud Manager. 
3. Check the configuration differences (diffs) between the Panorama
 configuration and the migrated Strata Cloud Manager configuration. 
4. Resolve the diffs and complete the migration.

1.  Prepare your Panorama for the migration. 
  1.  Log in to the Panorama that manages Prisma Access with an [administrative role](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-overview/role-based-access-control/administrative-roles) of
 Superuser. 
  2.  (Optional) If you have configured a custom [Master Key](/content/techdocs/en_US/prisma-access/administration/prisma-access-setup/set-up-prisma-access/set-up-prisma-access-panorama.html) for your Panorama
 and for Prisma Access, make a note of it.If your deployment uses the default Master Key, this step isn't
 required.

  3.  Make sure that your current Panorama configuration is up to date
 and you have committed and pushed all your changes to Panorama and
 to Prisma Access by going to CommitCommit & Push and Preview Changes.
  4.  (Optional) Check the diffs between the running config and
 the candidate config and determine whether you want to push those
 changes. If you want to commit and push the changes, Edit
 Selections and select the Prisma Access
 components you want to push in the Push
 Scope. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  5.  (Optional) Commit and Push your
 changes.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  6.  Go to PanoramaSetupOperations and Export named Panorama configuration
 snapshot.
 This .xml file is required to upload to Strata Cloud Manager
 during the migration process. **Don't upload a techsupport file
 or any other file except an .xml configuration file.
 **
 
 The user exporting this file in Panorama must have an
 [administrative
                                                role](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-overview/role-based-access-control/administrative-roles) of Superuser. 

 

  7.  Select the running-config.xml configuration
 file and OK.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

2.  Log in to Strata Cloud Manager as an administrator with a [Superuser role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) and go to
 ConfigurationNGFW and Prisma Access.The migration program detects that you have a Panorama managed deployment.
 

3.  Start Migration.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

4.  The migration program asks you to make sure that your configuration is up
 to date and shows you the last user who updated it. After you have verified
 that this configuration has the latest changes, select Confirmed
 they are up to date and click
 Next.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

5.  Select the Panorama configuration .xml file you downloaded in an earlier
 step by dragging and dropping it or Choose File.
 
6.  Input your Master Key, or if you did not create a
 custom [master key](/content/techdocs/en_US/prisma-access/administration/prisma-access-setup/set-up-prisma-access/set-up-prisma-access-panorama.html), ask Strata Cloud Manager
 to use the Default one and click
 Next. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 The migration program begins. 

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 Wait for all the steps to complete. 

 

7.  If, during migration, the program indicates that it encountered an unsupported configuration, you can Trim the above
 configurations and proceed or Cancel
 migration.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 Some unsupported configurations (such as a multitenant configuration)
 cancel the migration and the migration program can't resolve the issue;
 in this case, Cancel Migration. 

 

8.  After migration completes, click Next.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

9.  If the migration program made changes, review them in the final
 confirmation screen.
 The migration program might make changes to your configuration to account
 for differences in the Panorama and the Strata Cloud Manager
 configuration or to fix unsupported functionality. If changes are
 required, the migration program shows those changes in a diff view with
 the new lines in green and the deleted lines in red. 

 
 
 Ignore any diffs that show the following object names; they don't
 affect your configuration:

  - Clientless-vpn crypto-settings

  - Hip-profiles rename 

  - Mobile-user-redundancy 

  - Exclude-video-traffic

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

10.  (Optional) Make changes to the diffs. Any changes you make are not committed to your configuration until you
 complete the migration and push your changes to Strata Cloud Manager. 

  1.  Navigate to the area in the Prisma Access configuration where
 you found the diffs and make changes to the configuration. For the example in the previous step, the migration program made a
 change to Backbone Routing (from
 no-asymmetric-routing to
 asymmetric-routing-only). To change this
 setting back to your original configuration, go to 
 ConfigurationNGFW and Prisma AccessConfiguration ScopePrisma AccessService ConnectionsAdvanced Settings and change the Backbone
 Routing configuration to Disable
 Asymmetric Routing for Service Connections.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

  2.  (Optional) To keep track of your changes,
 Acknowledge them as you complete
 them.While not required, it can be useful to acknowledge each change as
 you make them, so you can keep track of them.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

  3.  Continue to review the changes and make changes and acknowledge
 them. 

11.  (Optional) If you have made any changes to the configuration,
 Regenerate Diffs to see the updated diffs. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

12.  Complete Migration. 
 While not required, you can also Acknowledge your
 changes. 

 **After you Complete Migration, you can't go back
 to a Panorama managed deployment and your deployment permanently
 uses Strata Cloud Manager for its management.**

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

13.  (Optional) Go to Configuration Page to see
 your migrated configuration. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 Your migrated deployment displays. 

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

14.  Push ConfigPush to apply your migrated configuration changes. 
 This Push operation ensures that your migration has successfully
 completed and that Prisma Access has applied all changes to your
 migrated configuration.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

15.  Make a note of any messages you received during the Push operation and, if
 you see any issues, make changes to your configuration as required.