<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/migrate-from-panorama-to-strata-cloud-manager -->
<!-- Fetched: 2026-03-31T18:30:12.493111+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: scm, migration, panorama -->

# Migrate from Panorama to Strata Cloud Manager

 

 
 
 
 
 
 

 

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
                            
                                    Strata Cloud Manager Prerequisites](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html)
 

 
 

**[Next
                                
                                    Onboard to Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html)
 

 

---

 
 
 















 

# Migrate from Panorama to Strata Cloud Manager



 Learn about migrating your Prisma Access or NGFW deployments from Panorama to Strata
 Cloud Manager using the automated migration workflow.



 
 






















 

- 
- 

- [Strata
                                                Cloud Manager Essentials or Pro](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)
- [Ensure
                                                that your NGFWs meet the prerequisites for cloud
                                                management](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-prerequisites.html)

- [Prisma Access](https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license)
- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW (Managed by Panorama)Prisma Access (Managed by Panorama) | Migrating NGFWs: license
                                Migrating Prisma Access:
                                            licenseTo begin the migration from Prisma Access (Managed by
                                            Panorama) to Prisma Access (Managed by Strata Cloud
                                            Manager), reach out to your Palo Alto Networks account
                                            team |



 Migration from Panorama to Strata Cloud Manager is now available for both Prisma
 Access and NGFW Panorama configurations, allowing you the benefits of cloud
 management and shared configuration management in the cloud environment. The
 migration process addresses considerations such as configuration preservation and
 policy continuity.

 For NGFW deployments, you can follow this workflow to review configuration
 compatibility, even if you're not yet ready to migrate. You can decide to trim or
 accept any features that aren't supported or are partially supported for Strata
 Cloud Manager configuration management. During migration, Strata Cloud Manger
 converts Panorama device group hierarchies into corresponding Strata Cloud Manager
 folder structures, and converts Panorama templates and template stacks into reusable
 snippets.

 For Prisma Access deployments, migrations focus on preserving your remote access
 infrastructure, mobile user configurations, and site-to-site connectivity while
 transitioning management oversight to Strata Cloud Manager.

 
- [Panorama Configuration
                        Migration](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-panorama-to-strata-cloud-manager/migrate-from-panorama-to-strata-cloud-manager-ngfw.html#migrate-from-panorama-to-strata-cloud-manager-ngfw)
- [Prisma Access Migration](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/migrate-from-panorama-to-strata-cloud-manager/migrate-from-panorama-to-strata-cloud-manager-prisma-access.html#migrate-from-panorama-to-strata-cloud-manager-prisma-access)

 
















 

# Migrate Configurations From Panorama to Strata Cloud Manager (NGFW)



 Learn about the migration process for migrating your NGFW deployments from Panorama to
 Strata Cloud Manager.



 
 You can migrate your existing NGFW configurations from Panorama to Strata Cloud
 Manager for cloud-based configuration management. 

 During the migration, Strata Cloud Manager:

 
- Copies and translates supported security policies, network configurations, and
 objects.
- Maintains existing network topology and NGFW deployments.
- Highlights areas that are partially supported or unsupported.

 
 
 Contact your Palo Alto Networks account team to enable migration workflow.

 Managing your NGFWs using[Strata Cloud Manager instead of Panorama can offer you benefits such
          as](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview) unified management for Prisma Access and NGFWs, cloud-native scalability of your
 network, and enhanced visibility.

 Strata Cloud Manager guides you through migrating your configurations with these
 key steps:

 
- Upload existing configurations — Import your current Panorama
 configurations.

- Run compatibility assessment — Identify unsupported features or
 configurations that need attention.

- Perform validation and prepare for deployment — Complete final checks before
 migration.

- Migration control — Devices and device groups can be migrated in phases,
 allowing you to migrate non-critical devices or go site-by-site.

 Review results at each step, make necessary adjustments, and verify that your
 configurations are fully compatible with Strata Cloud Manager before completing the
 migration.

 



 















 

## How Configuration Management Changes When You Move from Panorama to Strata Cloud
      Manager



 
 Panorama configuration management is based on: 
- Device Groups — Organize firewalls into hierarchical groups for security policy
 management (security rules, NAT policies, application filters).
- Templates and Template Stacks — Define network and device settings (interfaces,
 zones, routing, system settings).
- Inheritance — Device Groups inherit policies from parent groups; Template Stacks
 layer multiple templates with override capabilities.

 Strata Cloud Manager configuration management is based on:

 
- Folders — Hierarchical containers that hold both security policies AND network
 configurations.
- Snippets — Reusable configuration blocks that can be attached to folders at any
 level.
- Containers — Device-specific configuration holders for unique firewall requirements
 .

 During migration, Strata Cloud Manager converts your Panorama-based
 configuration and builds it into folders and snippets:

 






















 ********

| Panorama | Strata Cloud Manager |
| --- | --- |
| Device Groups | Folders |
| Templates & Template Stacks | Snippets |
| Policies and Profiles | Snippets |
| Shared Objects | Global folder as an attached Snippet |
| Policies in Device Groups | Policies under mapped Folder(s) |
| Objects (addresses, EDLs, etc.) | Objects under mapped Folder(s) |



 Key difference between Panorama and Strata Cloud Manager to keep in mind:

 
- Strata Cloud Manager Folders contain both network and security
 configurations, while Panorama separates these between Templates and Device Groups

- Strata Cloud Manager Folders provide more flexible inheritance with
 Snippet-based overrides versus the lower-level group overrides seen in Panorama

- Strata Cloud Manager Snippets provide a more plug-and-play approach to configurations
 compared to Panorama's Templates and Template stacks that are inherited down the
 stack.

 After migration, you manage configurations through the folder and snippet
 model. Snippet attachment order determines configuration precedence, providing granular
 control over how multiple configuration sources combine. You can also create
 device-specific containers for NGFWs requiring unique configurations outside the folder
 inheritance model.

 
 
 **Additional Resources**

Learn more about [Device Groups](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-device-groups) and [Templates](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-templates-and-template-stacks).

Learn more about [Snippets](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/configuration-overview/snippets) and [Folders](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/system-settings/system-settings-folder-management)

 








 















 

## Prepare to Migrate Your Panorama NGFW Configurations to Strata Cloud Manager



 
 Before beginning the migration, ensure you have the following items ready:

 
- Minimum Software Requirements: PAN-OS 10.2.3 or later

- [Export Panorama Configuration File](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/administer-panorama/manage-panorama-and-firewall-configuration-backups/save-and-export-panorama-and-firewall-configurations): Export the
 complete running configuration from your source Panorama instance in XML format

- [Panorama Master Key](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-the-master-key-from-panorama): Obtain the master key used for
 encryption in your Panorama configuration (if not using the default key)

- [Strata Cloud Manager Tenant](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/activate-strata-cloud-manager): Verify that your Strata
 Cloud Manager tenant is deployed, properly licensed, and operational

- [NGFW Configuration](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/troubleshooting/troubleshoot-panorama-system-issues/generate-diagnostic-files-for-panorama): Collect the last-pushed
 configuration files (Technical Support Files) from NGFWs you plan to validate
 post-migration

- [Network Topology](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-overview/centralized-firewall-configuration-and-update-management): Review your current device group
 hierarchies, template relationships, and NGFW assignments

- [Configuration Backup](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/administer-panorama/manage-panorama-and-firewall-configuration-backups): Create complete backups of your
 current Panorama and NGFW configurations as a safety measure

- [Administrative Access](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions): Ensure you have access to the
 Superuser role in both Panorama and Strata Cloud Manager.

- Migration Planning: Identify which device groups, templates, and NGFWs you
 want to migrate in your initial phase

- [Compatibility Matrix](https://docs.paloaltonetworks.com/compatibility-matrix): Understand which features may not be
 supported in Strata Cloud Manager and plan for any necessary configuration
 adjustments

- Unsupported Functionalities: Migration of configurations to Strata Cloud Manager is
 not supported if the **intrazone-default** and **interzone-default** policies
 have been overwritten at the Device Group level. If these default security rules are
 overwritten, the migration tool cannot process the Panorama configuration. You must
 remove these overwritten policies from Panorama, commit your changes, and re-export
 the running-config.xml before attempting the migration.

 








 















 

## Migrate Your Panorama NGFW Configurations to Strata Cloud Manager



 
 Migrate your NGFW configurations from Panorama to Strata Cloud Manager:

 

1.  Prepare your Panorama for the migration.
  1.  Log in to the Panorama that manages your NGFWs with an administrative account
 that is assigned the [Superuser](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-cli-quick-start/get-started-with-the-cli/give-administrators-access-to-the-cli/administrative-privileges) role.
  2.  **(Optional)** If you have configured a custom Master Key for
 Panorama, make a note of it.If your deployment uses the default Master Key, this step isn't
 required.

  3.  Ensure that your current Panorama configuration is up to date and that you have
 committed and pushed all your current changes to Panorama by going to CommitCommit & Push and Preview Changes.
  4.  **(Optional)** Check the diffs between the running configuration and
 the candidate configuration and determine whether you want to push those changes. To
 commit and push the changes, Edit Selections and select the
 NGFWs you want to push in the Push Scope.
  5.  **(Optional)**
 Commit and Push your changes.
  6.  Go to PanoramaSetupOperations and Export the named Panorama configuration
 snapshot.The .xml file is required to upload to Strata Cloud Manager during the migration
 process. Don't upload a techsupport file or any other file except an .xml
 configuration file.

  7.  Select the running-config.xml configuration file and click
 OK.

2.  Log in to Strata Cloud Manager as an administrator with a Superuser role and go to ConfigurationOnboarding.
 
 

 

 The migration program detects that you have a Panorama managed
 deployment.

 
  1. Confirm the tenant is correct.

  2. (Optional) [Create a Named Snapshot](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/config-snapshot?otp=task-uzv_3lr_vcc#task-uzv_3lr_vcc) of your running
 configuration in the event that a rollback is necessary.

 
 
 Migration should not be attempted during an Strata Cloud Manager upgrade
 window. Check your upgrade schedule to see if you have an upcoming upgrade.

 

3.  Read the migration Overview.
 
 

 

  1.  Review the management building blocks of Strata Cloud Manager:
 Folders and Snippets.
  2.  Click Next: Upload Panorama Configuration.

4.  Upload the Panorama configuration.
 
 

 
 
 

 

  1.  Select the Panorama configuration *.xml* file you downloaded in an earlier
 step by dragging and dropping it from your file explorer or selecting
 Choose File.
  2.  **(Optional)** Input your Master Key or, if
 you did not create a custom master key, use the Default
 one.
 
 

 

  3.  Click Next: Review Migration Compatibility.

 
 
 If the migration tool produces any errors that cannot
 resolve automatically, you may have a configuration that is unsupported. Click
 Cancel Migration, remove these overwritten policies from your
 Panorama configuration, re-export the configuration file, and restart the migration
 process.

 

5.  Review the configuration compatibility.
 
 

 

  1.  **(Optional)**
 Export Compatibility Summary and review your organization’s
 configuration compatibility before continuing and allowing Strata Cloud Manager to
 trim any unsupported or partially supported configurations.
 The trimming of unsupported and partially supported features avoids migrating
 features that cannot be deployed safely or securely in Strata Cloud Manager.

 This process will only impact the staged configuration for Strata Cloud Manager.
 The configurations in Panorama will remain unaffected.

 For each flagged area, you should plan to rebuild, replace, or defer those
 configurations.

 
 
 

 

  2.  Review the Unsupported Features that will be trimmed from
 your configuration during the migration.
 These features will be trimmed from your configurations and will not be staged in
 Strata Cloud Manager during the configuration migration process.

 

  3.  Review the Partially Supported Features and determine a
 resolution path.
 Identify what exactly is going to be missing from the configuration.

 You can accept the partially supported features and build a remediation plan
 post-migration or return to your Panorama configuration and clean these areas up
 before starting the migration process again.

 

  4.  Acknowledge the unsupported and partially supported
 features.
  5.  Click Next: Select Device Groups to Migrate.

 

 
 
  For those just looking to compare supported
 configurations, or if it is decided than more planning is needed, you can end the
 migration process here.

 

6.  Select the Devices or Device Groups you
 would like to migrate.
 
 
  If you are migrating NGFWs from Panorama for the first
 time, it is recommended to only migrate non-critical devices or device groups first to
 test how your configurations will be migrated to Strata Cloud Manager.

 
 
 

 
 During the migration:

 
  - Objects are imported to a Snippet and attached to the Global
 folder.

  - Policies are imported under the Folder(s) migrated by the workflow.

  - Shared Device Groups are automatically mapped to the All Firewalls
 Folder.

After selecting the devices, click Next: Map Templates to
 Folders.

 

7.  Map Templates to your newly configured
 Folders.
 
 
 

 
 You can choose between two template mapping
 options:

 
  - Auto Template Mapping: Automatically associate template
 and template stack configurations with folders after migration to snippets. This
 feature eliminates the need for manual configuration mapping and reduces the
 iterative process that you typically face during the migration workflow.

Strata Cloud Manager processes the entire Panorama configuration, even
 when you only select a subset of device groups for migration. This comprehensive
 analysis prevents issues in subsequent device group migrations; however, it may
 extend the processing time for the initial migration. 

  - Manual Template Mapping: Manually associate template and
 template stack configurations with folders after migration to snippets.

 
 
 
  - During migration, Device Groups are transformed into folders, while templates
 and template stacks are converted into configuration snippets. 
  - If two or more Device Groups reuse the same template, elevate it to a higher
 folder. If only one site requires it, keep it at the site level.

 Here is the procedure to manually associate templates:

 

  1.  Select a Device Group to reveal the
 Templates/Template Stacks used by that device group.
 
 

 

  2.  Edit the mapping to assign each
 Template/Template Stack to a
 Folder.
  3.  Elevate templates referenced in multiple places to higher folders.
 For example, if you have global template settings, mapping them to the All
 Firewalls folder establishes those settings as the source of truth for all NGFWs.
 

 

  4.  After assigning more than one Snippet to a Folder, adjust the order.
  5.  Move Up or Move Down to finalize
 the order.
  6.  Update the order.
  7.  Save the new order.
 Before moving on to the next step, ensure the following: 
    - No unassigned templates or template stacks remain.
    - Any templates referenced by multiple device groups have been elevated to the
 proper folders.

 

8.  Click Next: Prepare Migration.
 The migration process begins.

 Wait for all steps to be completed.

 
 
 If there are any issues with the migration, return to the previous steps to
 evaluate and make changes. If issues continue to persist, please contact Palo Alto
 Networks Support.

 

9.  Prepare to migrate.
  1.  Load Configuration to Strata Cloud Manager to prepare to
 migrate.
 
    1. The migration worfklow: 
      - Translates Devices and Device Groups and Templates and Template Stacks to
 Folders and Snippets using the mappings and snippets order defined by
 you.
      - Creates a Strata Cloud Manager snapshot to enable rollback of staged
 changes.
      - Checks for conflicts in existing Strata Cloud Manager configurations (name
 collisions, missing references, 31-character limits, RBAC scope).
      - Builds the staged configuration that will be in Strata Cloud Manager
 post-load.

 

  2.  Load Results and review what objects, policies, or
 snippets were created, updated, or skipped.
  3.  Review the Validation Results for any errors, warning, and
 informational messages post migration.
  4.  Click Next: Review Config Diffs.This commits the newly generated configuration to Strata Cloud Manager.

10.  Review the configuration diffs.
 
 
  When reviewing your configuration diffs, you may notice
 that secret keys or passwords appear as **Modified**. This is expected behavior.
 Because Strata Cloud Manager uses a different Master Key than your Panorama instance,
 the encrypted string representing the key changes during the translation process. The
 underlying plaintext key remains exactly the same, and no action is required.

 

  1.  In the left folder tree, expand to the Folder and select an NGFW serial number to
 be validated
  2.  Browse File and choose the TSF for the selected serial
 number.
 Uploading the TSF for the chosen NGFW will allow you to properly validating all
 the supported, partially supported, and unsupported configurations.

 Strata Cloud Manager
 categorizes configuration diffs into three groups:

 
    - Modified/Missing: Represents changes to existing
 objects during the migration process. It can be items with changed values or
 missing object references.
    - Unsupported: Represents items that cannot be migrated
 due to feature parity gaps between Panorama and Strata Cloud Manager, detected
 using predefined parity checks.
    - Informational: Represents changes where object
 functionality remains the same but names or references have been automatically
 updated to comply with Strata Cloud Manager naming conventions. For example,
 profile names.

 Be sure to look for anything that has been created, modified, or deleted.
 Configurations being trimmed should not come as a surprise. You can use the search
 functionality to locate specific configuration elements by name, object type, or
 difference category, streamlining the review process for migrations with extensive
 configuration differences.

 
 
 Because of naming conventions in Strata Cloud Manager, some long names will be
 compressed when needed.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  3.  Review the configuration diff panes.
 
    1. Green Panes: Created or added. They are present in Strata Cloud
 Manager, but not on the original device.

    2. Red Panes: Deleted or trimmed. May not be supported in Strata Cloud
 Manager, but are on the device.

    3. Yellow Panes: Modified.

 
 
  The diff view may be extensive, limited to one NGFW at a time, and
 calculated from the last pushed XML from the TSF.

 

  4.  Verify the diffs for representative devices from each pattern or site type.
  5.  (Optional)
 Export the diff results.
  6.  (Optional)Regenerate Diffs if any corrections
 have been made.
  7.  Click Next: Confirm and Finish.

11.  Confirm and finish your migration of configurations to Strata
 Cloud Manager.
 
 
 The migration tool does not onboard your NGFWs! You must still onboard your NGFWs
 to Strata Cloud Manager.

 Now that your Panorama configurations are Strata Cloud Manager, ready for device
 onboarding and pushes performed from SCM.

 With the configuration migration complete, review the available [documentation](https://docs.paloaltonetworks.com/strata-cloud-manager) for onboarding and managing NGFWs in Strata Cloud Manager.

 

  1.  Ensure the results from Steps 8 and 9 are accepted.
  2.  Confirm the migration.This officially marks the migration as complete.

  3.  (Optional) To revert the configuration to its pre-migration state at any
 point, select Revert. This initiates a rollback workflow,
 restoring Strata Cloud Manager to a Snapshot taken before the migration was
 loaded.
  4.  (Optional) To cancel the migration at any point, select
 Cancel Migration. This aborts the migration process and
 cleans up any temporary changes.








 















 

## Post-Migration



 
 After confirming the configuration migration in the tool, the configuration is staged in
 Strata Cloud Manager but has not yet been pushed to your NGFWs. The NGFWs are still
 managed by Panorama, now you must onboard them to Strata Cloud Manager to proceed with
 cloud management.

 To complete the transition to Strata Cloud Manager, you must perform pre-onboarding
 checks, [onboard your NGFWs to Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html), and execute a [configuration push](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/push-config).

 



 















 

### Onboard NGFWs to Strata Cloud Manager



 
 You must onboard your NGFWS to Strata Cloud Manager to transfer management authority
 from Panorama to the cloud. You can migrate devices in phases (for example, by device
 group or site). For detailed steps on associating devices and configuring connectivity,
 see [Onboard to Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager.html).

 **General Onboarding Guidelines**

 
- **Associate Devices:** Ensure all firewalls are associated with your Strata Cloud
 Manager tenant.
- **Move to Cloud Management:** Use the Strata Cloud Manager onboarding workflow to
 move the device to **Cloud Management**.
- **Verify Placement:** Confirm that the device shows a **Connected** status in
 Strata Cloud Manager and appears under the correct intended Folder.

 








 















 

### First Push and Validation



 
 Once devices are onboarded and connected, you must[push the staged configuration](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/push-config) from Strata Cloud
 Manager to enforce policies.

 Once you have pushed the staged configuration, validate:

 
- Commit success.
- Session health and traffic flow.
- Interface, virtual router, and HA status.
- Log forwarding to Strata Logging Service.

 
 
 Once you have validated your push, take screenshots of the connected state and
 successful push for your validation report.

 








 















 

### Rollback Readiness



 
 If critical issues arise during the pre-onboarding or onboarding phases, you can revert
 Strata Cloud Manager to its state prior to the migration.

  Use [Configuration: Config Version Snapshots](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/config-snapshot) to load
 the **pre-migration-snapshot** created by the tool. This reverts the staged Strata
 Cloud Manager configuration but does not push changes to devices.

 
































 

# Migrate from Panorama to Strata Cloud Manager (Prisma Access)



 Learn about the migration process for migrating your Prisma Access deployments from
 Panorama to Strata Cloud Manager.



 
 If you have an existing Prisma Access Deployment for which the configuration is
 managed by Panorama and want to migrate to Strata Cloud Manager for configuration
 management, Palo Alto Networks offers an in-product workflow that lets you migrate
 your existing Prisma Access configuration to Strata Cloud Manager.
 
 To enable migration workflow, you must contact your Palo
 Alto Networks account team.

 Managing your Prisma Access configuration using Strata Cloud Manager instead of
 Panorama can offer you benefits such as:

 
- Continuous [best practice assessments](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview/built-in-best-practices)
- Secure default configurations
- Machine Learning (ML)-based configuration optimization
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
- **When to Migrate**—Do not perform your upgrade during a dataplane or
 infrastructure upgrade. Check your[upgrade preferences](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-releases-and-upgrades/use-the-prisma-access-app-to-get-upgrade-alerts-and-updates) to see if you
 have an upcoming dataplane upgrade.
- **One-Way Migration from Panorama to Prisma Access (Managed by Strata Cloud Manager)**—You can only
 migrate from a Prisma Access (Managed by Panorama) to a Prisma Access (Managed by Strata Cloud Manager) deployment.
 After you migrate to Strata Cloud Manager, you cannot return to managing
 your Prisma Access deployment using Panorama. 
- **Minimum Panorama Version**—A minimum Panorama version of 10.0 is
 required. 
- **Required Administrator Role**—You must be logged in as a superuser in
 Strata Cloud Manager to begin the migration. 
- **Licensing Requirements**—A valid Prisma Access license is required. 
- **Cloud Identity Engine**—You must have [integrated the Directory Sync
                            component](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-user-based-policy/integrate-cloud-identity-engine-with-prisma-access/integrate-cloud-identity-engine-with-prisma-access-panorama#integrate-cloud-identity-engine-with-prisma-access-panorama) of the Cloud Identity Engine with the current Prisma Access (Managed by Panorama) tenant before migrating.
- **Unsupported Functionalities**—The migration program does not support
 the following Prisma Access functionalities:
  - [Data Filtering](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/security-profiles/set-up-data-filtering) (as an
 alternative, use [Enterprise DLP](https://docs.paloaltonetworks.com/enterprise-dlp))
  - [FedRAMP](https://docs.paloaltonetworks.com/fedramp/prisma-sase/fedramp-moderate-and-high-requirements) deployments
  - [IoT Security](https://docs.paloaltonetworks.com/iot)
  - [Multi-tenant](https://docs.paloaltonetworks.com/prisma-access/administration/manage-multiple-tenants-in-prisma-access)
 deployments
  - [SSH proxy](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/decryption/decryption-concepts/ssh-proxy)
  - Separate authentication for GlobalProtect portals and gateways

- **Prisma SD-WAN and Prisma Access Migrations**—If you migrate a Prisma
 Access and a [Prisma SD-WAN](https://docs.paloaltonetworks.com/prisma-sd-wan) deployment, Prisma
 Access and Prisma SD-WAN must share the same tenant service group ID ([TSG ID](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant)).
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
2. Start the migration program from Strata Cloud Manager. 
3. Check the configuration differences (diffs) between the Panorama
 configuration and the migrated Strata Cloud Manager configuration. 
4. Resolve the diffs and complete the migration.

1.  Prepare your Panorama for the migration. 
  1.  Log in to the Panorama that manages Prisma Access with an
 administrative account that is assigned the superuser role. 
  2.  (Optional) If you have configured a custom [Master Key](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-setup/set-up-prisma-access) for your
 Panorama and for Prisma Access, make a note of it.If your deployment uses the default Master Key, this step isn't
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
 snapshot.This .xml file is required to upload to Strata Cloud Manager
 during the migration process. **Don't upload a techsupport file or
 any other file except an .xml configuration file. **

  7.  Select the running-config.xml configuration
 file and OK.
 
 
 

 
 

2.  Log in to Strata Cloud Manager as an administrator with a [Superuser role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) and go to
 ManageConfigurationNGFW and Prisma AccessConfigurationNGFW and Prisma Access.The migration program detects that you have a Panorama managed deployment.
 

3.  Start Migration.
 
 
 

 
 

4.  The migration program asks you to make sure that your configuration is up
 to date and shows you the last user who updated it. After you have verified
 that this configuration has the latest changes, select Confirmed
 they are up to date and click
 Next.
 
 
 

 
 

5.  Select the Panorama configuration .xml file you downloaded in an earlier
 step by dragging and dropping it or Choose File.
 
6.  Input your Master Key, or if you did not create a
 custom [master key](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-setup/set-up-prisma-access), ask Strata Cloud Manager to use the Default one and
 click Next. 
 
 
 

 
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
 setting back to your original configuration, go to WorkflowsPrisma Access SetupService ConnectionsAdvanced Settings
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