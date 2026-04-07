<!-- Source: https://docs.paloaltonetworks.com/cloud-management/administration/manage-configuration-ngfw-and-prisma-access/configuration-scope/snippets -->
<!-- Fetched: 2026-04-01T01:59:10.099948+00:00 -->
<!-- Project: scm -->
<!-- Tags: cloud-management, config, snippets -->

# Configuration:
        Snippets

 

 
 
 
 
 
 

 

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
                            
                                    Configuration: Overview](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/configuration-overview.html)
 

 
 

**[Next
                                
                                    Configuration: Variables](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/configuration-overview/variables.html)
 

 

---

 
 
 















 

# Configuration:
        Snippets



 Use snippets to group configurations that you can quickly push to your firewalls or
 deployments.



 






















 

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


Use snippets to group configurations that you can quickly push to
 your firewalls or deployments.

A snippet is a configuration object, which can't fit into
 a hierarchy, or grouping of configuration objects, that you can associate with a folder,
 deployment, or device. Snippets are used to standardize a common base configuration for
 a set of firewalls or deployments allowing you to quickly onboard new devices with a
 known good configuration and reducing the time required to onboard a new device. For
 example, you can onboard a new firewall in a remote branch office. You can associate a
 set of snippets that contain all of the required network and policy rule configurations
 with the folder the new firewall belongs to. This reduces the time required to set up
 the firewall to protect the remote branch office.

Snippet associations have a top-down priority in the
 event of conflicting object values. Rules with duplicate names are not allowed, and
 validation fails during the creation of a snippet with the same name in any folder or
 while associating a snippet to a folder if the snippet with the same name is already
 associated.

This means that if the first and the last associated snippets have different
 values for the same object, the value from the first snippet is inherited by the device
 or deployment. Additionally, all configurations inherited from a snippet can be
 overridden at the child folder, deployment, or device level.

Within a [folder hierarchy](/content/techdocs/en_US/strata-cloud-manager/getting-started/folder-management.html), a snippet might
 only be associated one time within any folder hierarchy. This means that a snippet can’t
 be associated with both a folder and the folder nested under it. However, you can
 associate the same snippet with different folders or folders nested under different
 folders. Snippets that are already associated with a folder in the folder hierarchy are
 grayed out so they can’t be used more than once where
 applicable.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

 















 

## Snippet Classification



 
- Predefined: All Strata Cloud Manager users can access these snippets to quickly
 set up new firewalls and deployments with best practice configurations.
- Local: These editable snippets are created within the tenant and can't share
 them with other subscriber tenants. Local snippets can be shared. After sharing
 the local snippet, it will change to Published snippets
- Published: Trusted subscriber tenants have access to these shared snippets,
 which can't be deleted, but can be cloned and updated.
- Subscribed: These snippets, shared by the publisher tenant, can be cloned by
 users but can't be edited.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 








 















 

## Cross-Scope References Using Snippets



 This feature allows you to reference any common configurations or objects attached to
 a global scope and push it to Prisma Access and NGFW firewalls. These shared objects
 and configurations within the global scope are available to all the snippets. A
 snippet associated with the global scope is considered as a global snippet. Objects
 defined within these snippets attached to the global scope, can be referenced across
 any snippets in the configuration.

For example, you can create a snippet named Global Variable to consolidate variables
 and attach it to a Global scope. This ensures easy referencing and availability
 across all other snippets in the configuration. Similarly, you can effectively
 manage custom URL categories for access policy rules, threat prevention profiles,
 zones, addresses, and other objects representing standard network segments.








 















 

## Create a Snippet



 
 Create and associate a snippet with a folder, deployment, or device to apply a
 common base configuration to a group of devices. You can associate as many
 snippets with a folder, deployment, or device as needed.

 Snippets can be modified and reassociated with any folder, deployment, or device
 at any time after creation. 

 Custom snippets that are no longer in use can be deleted. 

 

1.  Log in to Strata Cloud Manager.
2.  Select ConfigurationNGFW and Prisma AccessOverview and expand the Configuration Scope to
 view the Snippets.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

3.  Add
 Snippet.
  1.  Enter a descriptive Name for the
 snippet.
  2.  (Optional) Provide a Description.
  3.  (Optional) Assign one or more Labels.
 You can select existing labels or create a new one by typing the
 desired label.

 

  4.  Create the snippet.Newly created snippets appear under Local
 snippets. After publishing, they move to
 Published snippets.

 
 
 

 

 

4.  Configure your snippet.
 You are now in the Configuration Scope for the
 snippet. All configurations made here apply only to this snippet.

 Review the snippet Overview for detailed
 information, including the number of variables, creation and update
 details, and associated folders, deployments, and devices.

 

5.  Add Subscriber Tenants:
  1.  Add Subscriber.
 
 
 

 
 

  2.  Select the Tenant Name and
 Save.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  3.  Click the Tenant Name link to edit
 subscriber tenant properties for shared snippets, controlling
 snippet management during disassociation.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

 
    - The Do not delete from subscriber
 tenant option is checked by default.
      - When this option is checked, snippets cannot be
 deleted from the subscriber, even without
 associations.
      - When unchecked, snippets without folder associations
 can be deleted from the subscriber. Deleting the
 subscriber will not remove the snippets.

    - Save your changes.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

 

  4.  Select the Tenant Name, and
 Publish.Choose Validate before update for a
 pre-update validation check on the subscriber before applying
 changes. If the validation fails, an error message appears. If the
 validation succeeds, publisher request is sent to the
 subscriber.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  5.  The Status column shows Snippet
 Successfully Published to Subscriber Tenant.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  6.  The published snippet appears under
 Subscribed. Use the 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 refresh icon if the
 subscribed snippet doesn't appear immediately.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

6.  To delete a subscribed snippet, select the Tenant
 Name and Delete Subscriber.The deleted subscriber tenant will be removed and will not appear under
 Subscribed.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

7.  Associate a snippet.
  1.  Select ConfigurationNGFW and Prisma AccessOverview and expand the Configuration
 Scope to view the Config
 Tree.
  2.  Select the folder, deployment, or device you want to associate the
 snippet with.
  3.  Edit the Config Snippet.
  4.  Add the snippets that you want to associate and order them as
 needed.
 If you're associating a snippet to the global scope, it becomes
 referenceable and available to all the other snippets in the
 configuration. All the snippets will be able to reference the
 objects you have in the snippet attached to the global
 folder.

 

  5.  Close.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

8.  Push Config to [push your configuration
                            changes](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/operations/push-config.html) to your network.







 















 

## Modify a Snippet



 
 Modify your snippet configurations, details, and associations.

 Custom snippets no longer associated with a folder,
 deployment, or device can be deleted. 

 

1.  Log in to Strata Cloud Manager.
2.  Select ConfigurationNGFW and Prisma AccessOverview and expand the Configuration Scope to view the
 Snippets.
3.  Select the snippet you want to modify.
 After you select a snippet, you’re redirected to the snippet
 Overview.

 

4.  (Optional) Edit the snippet to modify the
 Name, Description, or to
 change or assign additional Labels. Enable or disable
 Pause Update to see the configuration diffs and
 decide to accept the change. 
5.  Edit the Snippet Associations to reassociate the
 snippet with a different folder, deployment, or device or to associate the
 snippet with additional folders, deployments, or devices.
 Exit the snippet reassociation screen to apply the changes.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

6.  Make any changes to the snippet configuration as needed.
7.  Push Config.







 















 

## Delete a Snippet



 
 Delete your custom snippets to keep your configurations organized. Snippets must
 be unassociated with any firewalls, folders, or deployments before they are able
 to be deleted. Deleting predefined snippets is not supported. 

 

1.  Log in to Strata Cloud Manager.
2.  Select ConfigurationNGFW and Prisma AccessOverview and expand the Configuration Scope to
 view the Snippets.
3.  Click the three vertical dots of the custom snippet you want to
 delete.
 
 

 

4.  Delete the snippet.
 
 
 Snippets currently associated with folders, deployments, or devices
 can't be deleted. First edit the Snippet
 Associations to remove all existing associations
 before it can be deleted.

 








 















 

## Clone a Snippet



 
 If you want to use an existing snippet as a template for a new snippet, you can
 easily clone it so you do not have to configure a new object.

 Cloned snippets are not associated with any devices, folders, or deployments,
 allowing you to customize them freely without having to disassociate them before
 you begin your configurations.

 

1.  Log in to Strata Cloud Manager.
2.  Select ConfigurationNGFW and Prisma AccessOverview and expand the Configuration Scope to
 view the Snippets.
3.  Click the three vertical dots of the custom snippet you want to
 clone.
4.  Clone the snippet.
  1.  (Optional) Give the cloned snippet a new name.








 















 

## Share a Snippet Configuration



 
 This feature provides a unique and flexible method for sharing common
 configurations across any tenants including in a multitenant environment. You
 can save and manage various configurations as snippets, easily sharing them
 across tenants under a customer account. This capability provides considerable
 flexibility and control in managing shared configurations across different
 tenant environments.

 Additionally, this feature supports centralizing configuration management for
 common scenarios among tenants and overseeing global configurations within a
 multibusiness unit setup.

 In this framework, the publisher tenant shares snippets with the subscriber
 tenant, while the subscriber tenant receives snippets from the publisher
 tenant.

 

1.  Log in to Strata Cloud Manager.
2.  On the publisher tenant, select ConfigurationNGFW and Prisma AccessOverview, select the Global configuration
 scope.
3.  **Establish Trust Between the Tenants**: Establish a connection between
 the subscriber and publisher tenants to enable the sharing of
 snippets.
 
  1. Click Subscriber Tenant under
 Trusted Tenants for Snippet Sharing.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

  2. Add Subscriber Tenant.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

  3. Enter the TSG ID to add as a subscriber
 tenant, and Check TSG ID. This ensures
 prevention of randomly generated TSG or serialized TSG-based
 attacks. Upon successful validation, a confirmation message
 indicates that the TSD ID has been verified.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

  4. Next: Generate Pre Shared Key.Copy the
 generated PSK. You will enter this PSK when validating the
 publisher tenant in step 4.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

 

4.  Go to subscriber tenant, select ConfigurationNGFW and Prisma AccessOverview and set the configuration scope to
 Global.
 
  1. The Publisher Tenants status under
 Trusted Tenants for Snippet Sharing shows
 as Pending.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

  2. Click Publisher Tenants and Enter
 Pre Shared Key generated in the previous step, and
 Validate the subscriber tenant.After
 successful validation, a message confirms the tenant as trusted,
 establishing trust between the subscriber and publisher
 tenants.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

 

5.  Publish a Snippet to a subscriber tenant.
 
  1. Create and associate the snippet with a folder.Newly created
 snippets are available under Local
 snippets.

    - The Overview tab shows snippet
 details such as name, description, creation time (when
 the snippet was loaded on the subscriber side), last
 updated time, and labels details.Creation time on
 Subscriber also reflects the same time as that of
 Publisher. It denotes the time when the snippet was
 created.

    - The Subscriber Tenants tab shows
 the tenant name, published version on the tenant, last
 published date, and publish status.
      - Click Published Version
 to review configuration changes.
      - Before publishing a snippet to a tenant,
 Add Subscriber and
 Save it.

    - The Version Snapshots gives a
 history of your snippet configuration. In this screen,
 you can compare configuration snapshots with your
 candidate configuration, and Save Version
 Snapshot or Load
 an earlier configuration snapshot as your candidate.
 Click the Version number to view
 the configuration differences.
    - The Audit History provides an
 audit trail of all actions initiated by the
 administrator. It logs details such as the published
 version number, changes made, the owner of the change,
 the date and time of the change, and specifics of the
 change.

  2. On the Subscriber Tenant tab, select the
 tenant name and Publish.This sends publish
 request to the subscriber tenant. In the
 Status column indicates that Snippet
 Successfully published to subscriber and the snippet will be
 available under Published snippets.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

 

6.  Verify on the subscriber tenant.
 
  1. Go to OverviewConfiguration ScopeSnippets, and select the snippet under
 Subscribed snippets.You're redirected
 to the snippet Overview which shows
 details such as the publisher tenant's name, description, TSG
 ID, snippet creation time, last updated time, labels, and pause
 update details.

With pause update enabled, user has the
 option to Validate Before Update on Publisher before loading the
 latest version.

 

7.  Delete the trust.
 
 
 Subscribed snippets associated with folders or firewalls can only be
 cloned and can't be deleted.

 

 With snippet sharing hardening, now we have option to select how we want
 to manage the deletion of snippets on Subscriber. So, while adding a
 Subscriber tenant, we have option to select/unselect "Do Not Delete"
 When no associations, so if subscribed snippet has associations, even
 with "Do Not Delete" disabled, snippet will not be deleted.

 

 
  1. Go to subscriber or publisher tenant.
  2. Click Subscriber Tenant under
 Trusted Tenants for Snippet
 Sharing.

  3. Select the Tenant Name, and Delete
 Trust.

 

After deleting the trust, the snippet will no longer be associated with
 the firewall or folder and becomes a local snippet.








 















 

## Convert Local NGFW Configurations to Reusable Snippets



 
 Maintaining consistent configurations across multiple NGFWs often requires manual
 effort and risks configuration drift. Strata Cloud Manager simplifies the
 migration of locally created NGFW configurations into reusable, shared
 configuration snippets. The conversion process transforms device-level
 configurations into a reusable snippet format that you can import and reuse
 across your NGFW deployment.

 This feature automatically handles complex interface configurations, including
 tunnel, VLANs, loopback, Ethernet, and aggregate Ethernet interfaces, along with
 their associated subinterfaces. For each interface type, Strata Cloud Manager
 creates appropriate object variables that maintain the relationships between
 parent interfaces and subinterfaces.

 By converting local configurations to centrally managed snippets, you gain
 immediate benefits in consistency, scale, and operational efficiency. You can
 review a detailed pre-conversion report showing successfully converted objects
 and those automatically pruned due to incompatibility with centralized
 management. This ensures full transparency before saving the snippet,
 facilitating consistent, synchronized configuration deployment across your
 entire network. This capability accelerates operational efficiency and
 strengthens your overall security posture.

 

1.  Log in to Strata Cloud Manager.
2.  Select ConfigurationNGFW and Prisma AccessOverview and expand the Configuration
 Scope.
 
 
 

 
 

3.  Select the device whose local configuration you want to convert.
 You're redirected to the Overview page.

 

4.  You cannot configure policies and objects in device scope by default. To
 configure them, enable Device Scope
 Configuration.
 
 
 

 
 

 
 
 

 
 

5.  On the Overview page, under Configuration
 Snippets, select Convert local configs to
 snippet.
 
 
 

 
 

6.  Review the detailed report showing the Pruned and
 Converted configuration objects.
7.  Enter a Snippet Name.
8.  Provide and confirm your Master Key.
9.  Save.
10.  Expand the **Configuration Scope** to view the **Snippets**.Newly created snippets appear under **Local **snippets. After
 publishing, they move to **Published **snippets.