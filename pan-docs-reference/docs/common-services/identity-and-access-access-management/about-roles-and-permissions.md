<!-- Source: https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions -->
<!-- Fetched: 2026-03-31T18:05:35.202289+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: common-services, iam -->

# About Roles and Permissions Through Common Services



 



 Learn about Common Services roles and permissions for role-based access control
 (RBAC).



 






















 

- 
- 
- 

- [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| Strata Cloud ManagerStrata Multitenant Cloud ManagerThe hub | Superuser or Multitenant Superuser |


Common Services: Identity and Access supports role-based access control
 (RBAC). Using Identity and Access, you can manage tenant users, service accounts, and
 access to various resources within Common Services, Strata Multitenant Cloud Manager,
 and enterprise apps. You're required to assign roles for users but roles are optional
 for service accounts.

Roles work as a union. If you assign a role to a user for a specific app and another role
 for All Apps & Services, the user will get the union of both
 permissions. For example, consider a scenario where a user is assigned a role for the
 Strata Logging Service app with a role that does not allow download or
 share permissions. If that same user is also assigned the Superuser role for All Apps
 & Services, the user is able to download and share. The behavior is to check the
 specific app first and if the permission isn't available, then check All Apps &
 Services. For more information about what each role can do, you can view the
 permissions in the platform for each role. 

 
 If you have [received information](https://live.paloaltonetworks.com/t5/customer-resources/prisma-access-changes-coming-in-activation-and-identity-access/ta-p/511357) about the transition
 of your app instance to a [tenant or tenant service group](https://docs.paloaltonetworks.com/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant.html) (TSG), see
 [where are my roles?](https://docs.paloaltonetworks.com/common-services/faq/faq) for a mapping of
 previous roles to IAM roles.

## Permissions

Permissions are actions that are allowed in the system. Permissions represent a specific set of
 application programming interface (API) calls that you use to read, write, and
 delete objects within the system. You can view the permissions in the
 platform grouped into roles. 

## Multitenant Platform Roles

Multitenant platform roles are a predefined set of permissions for managing tenants
 in a multitenant hierarchy. These roles include a collection of one or more system
 permissions that are specific to the platform. 

By default, every user automatically gets a
 role that provides access to only the essential features required by Palo Alto
 Networks web interface applications. This isn't the same as a “view only” role, as
 it's necessary for the web interface. You can't assign or unassign this role.

The following table describes general roles and responsibilities. For more
 information about what each role can do, you can view the permissions in the
 platform for each role. 
























 

- 
- 
- 
- 
- 
- 
- 
- 

- 
- 

- 

- 

- 
- 

| Multitenant Platform Roles | Permissions | Supported
                                    Applications |
| --- | --- | --- |
| Multitenant Superuser | Read and write access to manage all apps, Strata Logging Service logs, and services within the
                                    assigned level of the nested hierarchy. Includes all permissions
                                    assigned to all roles, including Superuser. Includes access to
                                    dashboards, create custom dashboards, and download, share, and
                                    schedule reports. Includes the ability to activate product
                                    licenses through an email activation link. Assign this role only
                                    to users or service accounts that require unrestricted
                                    access. | Enterprise DLPCloud Identity EngineStrata Logging ServiceIoT SecurityNext-Generation CASBPrisma AccessPrisma SD-WANSaaS Security Posture Management |
| Multitenant IAM Administrator | Read and write access to identity and authentication functions
                                    for all tenants in a multitenant hierarchy. Restricted to
                                    read-only access for logs. No access to dashboards and Strata Logging Service logs. | Prisma AccessPrisma SD-WAN |
| Multitenant Manage User | This role provides access to functions related to
                                multitenant management and other common resources. | All Apps & Services |
| Multitenant Monitor User | This role provides access to functions related to
                                multitenant monitoring and other common resources. | All Apps & Services |
| Business Administrator | Read and write access to all subscription and license management
                                    for the selected app. Includes read-only access to other
                                    functions, such as access policies, service accounts, and tenant
                                    Service Group operations. No access to dashboards and Strata Logging Service logs. Includes the ability to
                                    activate product licenses through an email activation link.
                                    Assign this role to administrators who manage devices, licenses,
                                    and subscriptions. | All Apps & ServicesOnly available at the tenant or tenant service group (TSG)
                                        level. Can't be assigned to a specific app. |


When you [add user access](/content/techdocs/en_US/common-services/identity-and-access-access-management/manage-identity-and-access/add-users.html#add-users-2) or [add a service account](/content/techdocs/en_US/common-services/identity-and-access-access-management/manage-identity-and-access/add-service-accounts.html#idb687396b-71de-47d4-a9b9-7cc28df71420),
you can [assign a predefined
role](/content/techdocs/en_US/common-services/identity-and-access-access-management/manage-identity-and-access/assign-predefined-roles.html#id9a032461-859e-4598-8645-3c28030bad75) to execute specific functions within the platform. You
can also [assign a batch of
predefined roles](/content/techdocs/en_US/common-services/identity-and-access-access-management/manage-identity-and-access/assign-predefined-bulk-roles.html#id521e4d2c-ff06-41d5-9931-1d35b15624e5) to assign a role in bulk to multiple users
or service accounts at the same time.

## Enterprise
Roles

Enterprise roles are a predefined set of permissions for managing enterprise applications and
 services. These roles include a collection of one or more system permissions for any
 app to use. The following table describes general enterprise roles and
 responsibilities. For more information about what each role can do, you can view the
 permissions in the platform for each role. 
























 

- 

- 

- 
- 

- 

- 

- 

- 
- 

- 
- 

- 

- 
- 
- 

- 
- 

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

- 

- 

- 
- 
- 
- 
- 
- 
- 
- 
- 

- 

| Enterprise Roles | Permissions | Supported
                                    Applications |
| --- | --- | --- |
| ADEM Tier 1 Support | For use with the Prisma Access app. Read-only access to
                                    specific incident remediation workflows for only Prisma Access Autonomous Digital Experience Management
                                    (ADEM). No access to other Prisma Access services. No
                                    access to dashboards and Strata Logging Service
                                    logs. Assign this role to third-party helpdesk employees, tier 2
                                    and 3 support, or administrators who only need ADEM access. | Prisma Access |
| Auditor | Read-only access to functions related to all configurations,
                                    including subscriptions and licenses for the selected app.
                                    Includes access to view dashboards but can't download, share,
                                    and schedule reports. Includes access to Strata Logging Service logs. Assign this role to
                                    administrators who are tasked with examining the system for
                                    accuracy. | Prisma Access |
| Data Security Administrator | Read and write access to all data security functions for the
                                    selected app. Includes access to Strata Logging Service logs, dashboards, create custom
                                    dashboards, and download, share, and schedule reports. Includes
                                    read-only access to logs. This role includes a small subset of
                                    privileges included in the Security Admin role. Assign this role
                                    to administrators who manage only decryption rule
                                    configurations. | Next-Generation CASBPrisma Access |
| Deployment Administrator | Access to functions related to deployments. In addition, this
                                    role provides read-only access to other functions. | Cloud Identity Engine |
| DLP Incident Administrator | This role provides access to functions related to DLP
                                incidents and reports. This role also provides read-only access to
                                other functions, including but not limited to: data profile, data
                                filtering profile, data pattern, EDM, and OCR settings. | Enterprise DLP |
| DLP Policy Administrator | This role provides access to functions related to DLP
                                policy, including but not limited to: data profile, data filtering
                                profile, data pattern, EDM, and OCR settings. | Enterprise DLP |
| IAM Administrator | Read and write access to identity and authentication functions
                                    for the selected app. Includes read-only access to logs. No
                                    access to dashboards and Strata Logging Service
                                    logs. Assign this role to administrators who manage users. | Prisma AccessPrisma SD-WAN |
| Network Administrator | Read and write access to logs and network policy configurations
                                    for the selected app. Includes read-only access to other
                                    functions: alerts, license quotas, devices, and tenant Service
                                    Group  operations. Includes access to dashboards, create custom
                                    dashboards, and download, share, and schedule reports. Assign
                                    this role to administrators who need to maintain authentication,
                                    certificates, and decryption rules. | Prisma AccessPrisma SD-WAN |
| Posture Security Administrator | This role provides full SSPM functionality, but only for the SaaS
                                    applications that the administrators onboard themselves. It is
                                    intended to give IT/SaaS administrators visibility and full SSPM
                                    read and write access to the SaaS apps they are responsible
                                    for. | Next-Generation CASB |
| Security Administrator | Read and write access to logs and security policy configurations
                                    for the selected app. This includes read-only access to other
                                    functions, such as alerts, license quotas, devices, and tenant
                                    Service Group operations. Includes access to dashboards, create
                                    custom dashboards, and download, share, and schedule reports.
                                    Assign this role to administrators who need to maintain
                                    authentication, certificates, and decryption rules. | Next-Generation CASBPrisma AccessPrisma SD-WAN |
| SOC Analyst | Access to functions related to logs, reports, events, alerts, and
                                    all configurations for the selected app. Assign this role to
                                    administrators who need to view and investigate threats and
                                    trends. | Strata Logging ServicePrisma Access |
| Superuser | Read and write access to all available system-wide functions for
                                    the selected app. This includes all permissions assigned to all
                                    other roles, including MSP Superuser. This includes the ability
                                    to activate product licenses through an email activation link.
                                    Assign this role only to users or service accounts that require
                                    unrestricted access. | AIOps for NGFWAIOps for NGFW FreeCloud Identity EngineStrata Logging ServiceEnterprise DLPIoT SecurityNext-Generation CASBPrisma AccessPrisma SD-WANSaaS Security Posture Management |
| Tier 1 Support | Read and write access to remediation workflows that update
                                    network, security, and device configurations for the selected
                                    app. This includes read-only access for alerts, access policies,
                                    configurations, license quotas, devices, and tenant Service
                                    Group  operations. Full access to view dashboards, create custom
                                    dashboards, download, share, and schedule reports, and Strata Logging Service logs. | Prisma Access |
| Tier 2 Support | Read and write access to remediation workflows that update
                                    network, security, and device configurations for the selected
                                    app. This includes read-only access for alerts, access policies,
                                    configurations, license quotas, devices, and tenant Service
                                    Group  operations. Full access to view dashboards, create custom
                                    dashboards, download, share, and schedule reports, andStrata Logging Service logs. | Prisma Access |
| View Only Administrator | Read-only access to all available system-wide functions for the
                                    selected app and logs (except DNS logs). Includes access to view
                                    dashboards except DNS dashboard. No access to download, share,
                                    and schedule dashboards. | Cloud Identity EngineAIOps for NGFWStrata Logging ServiceEnterprise DLPIoT SecurityNext-Generation CASBPrisma AccessPrisma SD-WANSaaS Security Posture Management |
| Web Security Admin | This role provides access to functions related to web
                                security for Prisma Access. | Prisma Access |


When you [add user access](/content/techdocs/en_US/common-services/identity-and-access-access-management/manage-identity-and-access/add-users.html#add-users-2) or [add a service account](/content/techdocs/en_US/common-services/identity-and-access-access-management/manage-identity-and-access/add-service-accounts.html#idb687396b-71de-47d4-a9b9-7cc28df71420),
you can [assign a predefined
role](/content/techdocs/en_US/common-services/identity-and-access-access-management/manage-identity-and-access/assign-predefined-roles.html#id9a032461-859e-4598-8645-3c28030bad75) to execute specific functions within a network. You
can also [assign a batch of
predefined roles](/content/techdocs/en_US/common-services/identity-and-access-access-management/manage-identity-and-access/assign-predefined-bulk-roles.html#id521e4d2c-ff06-41d5-9931-1d35b15624e5) to assign a role in bulk to multiple users
or service accounts at the same time.



 















 

## View Role Permissions



 For more granular information about what each role can do, you can view the
 permissions. 

1. Use one of the [various ways to access](/content/techdocs/en_US/common-services/identity-and-access-access-management/get-started.html)
 Common ServicesIdentity & Access.
2. Select Common ServicesIdentity & Access/Access ManagementRoles to view role permissions.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
3. Select a role, such as Auditor to view the
 permissions.