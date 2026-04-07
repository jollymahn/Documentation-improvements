<!-- Source: https://docs.paloaltonetworks.com/cloud-management/administration/workflows/workflows-ngfw-setup/folder-management -->
<!-- Fetched: 2026-04-01T01:59:11.657597+00:00 -->
<!-- Project: scm -->
<!-- Tags: cloud-management, folders -->

# System Settings: Folder Management

 

 
 
 
 
 
 

 

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
                            
                                    System Settings: Device Management](/content/techdocs/en_US/strata-cloud-manager/getting-started/system-settings/system-settings-device-management.html)
 

 
 

**[Next
                                
                                    System Settings: Scope Management](/content/techdocs/en_US/strata-cloud-manager/getting-started/system-settings/system-settings-scope-management.html)
 

 

---

 
 
 















 

# System Settings: Folder Management



 Create or modify folders for folder management.



 






















 

- 

- 

- 

- 

| Where Can I Use
                                This? | What Do I Need? |
| --- | --- |
| Prisma Access (Managed by Strata Cloud Manager)NGFW (Managed by Strata Cloud Manager) | AIOps for NGFW Premium licensePrisma Access license |


Folders are used to logically group your firewalls or deployment types (Prisma Access mobile users, remote networks, or service connections) for simplified
 configuration management. You can create a folder that contains multiple nested folders
 to group firewalls and deployments that require similar configurations. Folders that are
 already nested can have multiple nested folders as well.

Folders for Prisma Access and your NGFWs are separate; you can't group NGFWs in a
 folder with Prisma Access deployments. However, you can easily apply shared settings
 globally across all folders or use [Configuration: Snippets](/content/techdocs/en_US/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/configuration-overview/snippets.html) to easily apply standard settings and policy
 requirements across multiple folders.

 
 

 
- [NGFW](/content/techdocs/en_US/strata-cloud-manager/getting-started/system-settings/system-settings-folder-management/folder-management-ngfws.html#folder-management-ngfws)
- [Prisma Access](/content/techdocs/en_US/strata-cloud-manager/getting-started/system-settings/system-settings-folder-management/folder-management-prisma-access.html#folder-management-prisma-access)

















 

# Folder Management (NGFWs)



 How to use folders to simplify configuration for NGFWs you are managing with Strata Cloud Manager. 



 
  To help manage folders and firewalls, you can apply labels to filter
 and target specific groups of firewalls for configuration changes. Additionally,
 each folder displays the currently installed software version, dynamic content
 release versions, and GlobalProtect app Version of the firewalls associated with the
 folder.

 For firewall folders, Strata Cloud Manager supports up to four nested folders within
 any given folder hierarchy, with the default All
 Firewalls folder always being the top-most level of any folder
 hierarchy. For example, consider the below when designing your folder hierarchy. In
 the example below Folder1,
 Folder2, Folder3, and
 Folder4 are nested under the All
 Firewalls folder and you can’t best any additional folders to
 this particular folder hierarchy. Additionally,
 Folder2.1 and
 Folder2.2 are nested under
 Folder2 and you can’t add any nest any additional
 folders either.
 
 

 

 



 















 

## Create a Folder



 
 
 Create a folder to logically group your firewalls for simplified configuration
 management. You can create a folder under the default
 Firewalls
 folder
 or under another existing folder. 

 

1.  Log in to Strata Cloud Manager.
2.  Select System SettingsFolder Management and Add
 Folder.
3.  Give the folder a descriptive
 Name.
4.  (Optional)
 Enter a Description for the
 folder.
5.  (Optional)
 Assign one or more Labels.
 You
 can select an existing label or create a new label by typing the label
 you wanted to
 create.

 

6.  Specify where to create the folder In. 
 Select
 All Firewalls or select an existing folder to
 nest the folder under
 it.

 

7.  Create
 the folder.
 
 
 

 
 








 















 

## Modify a Folder



 
 Modify an existing folder to edit the name, description, and to add or change the
 labels. Additionally, you can move or delete the folder as needed.

 

1.  Log in to Strata Cloud Manager.
2.  Select System SettingsFolder Management and expand the Actions menu.
 
 
 

 
 

3.  Modify the folder as needed.
 
  - Edit the folder

 

  1.  Edit the folder Name.
  2.  (Optional) edit the folder
 Description.
  3.  Select or create Labels.
 You can assign entirely different labels to the folder or add
 additional labels.

 

  4.  Save.

 
  - Move the folder and select the
 Destination.

 You can move a folder in the following ways.

 
  - You can move a folder to nest it under a different folder.

  - You can move a nested folder under the
 Firewalls folder.

  - You can move a nested folder from one folder to another.

 Move the folder after you select the folder
 destination.

 
  - Delete Folder and click
 OK to confirm.

 You can only delete a folder that has no firewalls associated with it and
 no folders nested under it.

 



























 

# Folder Management (Prisma Access)



 



 
 Prisma Access folders are predefined; you can use them to specify configuration
 scope and ensure that Prisma Access deployment types – mobile users, remote
 networks, and service connections – receive all global settings and then settings
 that are required or specific for each type.

 The configurations defined under a folder are inherited by all folders nested under
 that folder hierarchy. For example, you can configure settings that are common
 across GlobalProtect, Explicit Proxy, Remote Networks, and Service Connections under
 the **Prisma Access** folder. Similarly, you can configure settings that are
 common across GlobalProtect and Explicit Proxy under the **Mobile Users
 Container** and so on.

 You cannot edit the folder hierarchy for Prisma Access.

 At the folder level, you can also enable [web security](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/web-security) for the Prisma Access
 mobile user, remote network, or service connection deployment.