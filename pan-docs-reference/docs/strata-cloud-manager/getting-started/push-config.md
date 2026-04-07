<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/operations/push-config -->
<!-- Fetched: 2026-03-31T18:59:35.873933+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: scm, config, push -->

# Configuration:
        Push Config

 

 
 
 
 
 
 

 

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
                            
                                    Configuration: Operations](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/operations.html)
 

 
 

**[Next
                                
                                    Configuration: Push Status](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/operations/push-status.html)
 

 

---

 
 
 















 

# Configuration:
        Push Config



 How to use Strata Cloud Manager to push configuration changes to your NGFWs and
 Prisma Access.



 
 






















 

- 

**

- [Software NGFW
                                            Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)

- 

  - 
  - 
  - [Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)
  - [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)

- [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions)
- 

| Where Can I Use
                                This? | What Do I Need? |
| --- | --- |
| Where Can I Use
                                This? | What Do I Need? |
| Prisma Access(with Strata Cloud Manager or Panorama
                                                configuration management)NGFW, including those funded by | Each of these licenses include access to Strata Cloud Manager:Prisma AccessAIOps for NGFW Premium license (use the Strata Cloud Manager app) or AIOps for NGFW Free (use the AIOps for NGFW Free app)A  that has
                                        permission to view the dashboardPrisma SD-WAN license for pushing
                                        configurations to Other Services |


After you make configuration changes and are ready to activate them, you must push the changes to
 your firewalls. You have the option to push all configuration changes or to select
 specific administrators to include in the push. Pushing changes from all
 administrators is required for your first configuration push. You can choose which
 configuration changes you want to push to Prisma Access:

 
- **Mobile Users — GlobalProtect**

Push [Global Protect](https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma/prisma-access/prisma-access-cloud-managed-admin/secure-mobile-users-with-prisma-access/globalprotect-app.html#id2c19e575-0c09-4353-8ca1-48c5136ed8a3) updates to Prisma
 Access.

- **Mobile Users — Explicit Proxy**

Push [Explicit Proxy](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/secure-mobile-users-with-prisma-access/explicit-proxy.html) updates to Prisma
 Access.

- **Remote Networks**

Push [Remote Networks](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/secure-remote-networks-with-prisma-access.html) updates to Prisma
 Access.

- **Service Connections**

Push [Service Connection](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/prisma-access-service-connections.html) updates to
 Prisma Access.

 You can push a configuration while another configuration push is taking place. Prisma
 Access applies configuration changes in the order you submit them.

 In the event a configuration is pushed in error, or a change causes network or
 security disruption, you can revert the Prisma Access configuration to the most
 recent running Prisma Access configuration. This allows you to revert the Prisma
 Access configuration back to a running configuration you know is functional and does
 not compromise your network security. You do not have the option to select a
 specific running configuration. Prisma Access automatically selects the last known
 running configuration and reverts to it.

 
 
 Pushing a Log Forwarding Profile configured for
 Management Plane logs updates the DeviceLog Settings on the firewall, whereas Data Plane profiles update specific
 policy rules.

1.  Log in to Strata Cloud Manager.
2.  Make configuration changes as needed.
3.  Push Config and Push your
configuration changes.
 
 Alternatively, you can select ConfigurationOperationsPush Config.

 
 

 
 In the Push
 Config dialog box, you can Ignore Security Check
 Failures. This feature allows you to continue with push
 operations even when certain checks would block the process. If you leave
 the check box unchecked (the default setting), and a best practice check
 with a “block” action fails, Strata Cloud Manager stops the push.

 In the Push Config dialog box,
 you can select Other Services to push configuration
 changes to external Palo Alto Networks services like Prisma SD-WAN
 Controllers or Branch Security for Prisma SD-WAN ION devices associated with
 your CSP account. Use the Push Scope to target
 configuration changes to some or all of the external services.

 
 
 You can Ignore Security Check Failures only if
 your [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions) includes the **Override
 Security Check Block Action** permission.

4.  (Optional) Add New Filter.You can filter the devices displayed in the push scope by applying filters. Applying filters
 impacts only which firewalls or Prisma Access deployments are displayed in
 the push scope and has no impact on which devices you push to.

5.  Edit the Push Scope.
 Editing the push scope allows you to push targeted configuration changes to
 some or all of your firewalls or Prisma Access deployments.

 
 
 Performing a partial configuration push is not supported and you must
 push the entire Strata Cloud Manager configuration if you:

  - [Configure a new tenant](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants#add-tenants)
 and this is your first configuration push.

  - [Onboard a firewall](https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/onboard-your-devices/onboard-a-firewall) to
 Strata Cloud Manager.

  - Onboard a Prisma Access mobile users and remote users.

  - Rename or move a [folder](/content/techdocs/en_US/strata-cloud-manager/getting-started/folder-management.html) so
 that it’s nested under a different folder.

  - Move a firewall to a different folder.

  - Rename, associate, or disassociate a [snippet](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/configuration-overview/snippets.html).
 

  - Load a configuration.

  - Revert the configuration to the last pushed configuration or to a
 previous configuration version snapshot. 

 
  - Admin Scope — Select which administrator
 configuration changes to include in the push. By default, admin
 scope selects the current user, and changes made by that user are
 pushed to the selected firewalls or Prisma Access deployments.
 Selecting changes Changes from all admins
 includes all configuration changes made by all administrators.

Editing the admin scope to select specific administrators includes
 all the configuration changes made by the selected administrators.
 This option can't be used when performing your first config push.
 Selecting specific configuration changes to include in the push is
 not supported.

  - **Push Target** — Select which targets to
 include in the push. By default, the target is set to
 NGFW and Prisma Access. Selecting
 Other Services allows you to push
 configuration changes to external Palo Alto Networks services
 associated with your CSP account.

Review the push by selecting ConfigurationOperationsPush Status. Prisma SD-WAN will be listed under the device name.
 

 
 

 After you push your configuration
 changes, you can confirm the sync status on the
 Overview page.

 
 

 
  - **Push Scope** — Select the deployment types or folders you want
 to push to. When you select a deployment or folder, the
 configuration changes are pushed to all firewalls or
 deployments.

When you select a folder that contains child folders, all child
 folders and the associated firewalls or Prisma Access deployments
 are included in the push. Selecting a specific firewall or a Prisma
 Access deployment automatically selects the folder it’s associated
 with.

 

6.  Push Config and Push.Review the push targets and Push.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

7.  Review [configuration push status](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/operations/push-status.html).

 In the event a configuration is pushed in error, or a change causes network or
 security disruption, you can revert your Prisma Access configuration.

 ➡ [Restore, load, and compare configuration
                    versions](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/administer-prisma-access/configuration/config-snapshot.html)

 



 















 

## View Prisma Access Jobs



 
 You can view the Jobs history on Prisma Access to display
 details about operations that admins initiated, as well as automatic content and
 license updates. This includes any configuration commits, pushes and reverts.
 You can use the Jobs view to troubleshoot failed operations, investigate
 warnings associated with completed commits, or cancel pending commits.

 

1.  [Launch Prisma Access](https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-setup/set-up-prisma-access#task_b4d_zzh_nwb).
2.  On the top menu bar, select Push Config and view the
 Prisma Access Jobs.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

3.  Perform any of the following tasks:
 
  - **Investigate warnings or failures**—Read the entries in the
 Summary column for warning or failure details.

  - **View a commit description**—If an administrator entered a
 commit description, you can refer to the Description column to
 understand the purpose of the commit. 

  - **Check the position of an operation in the queue**—View the
 operation position and status to determine the position of the
 operation.