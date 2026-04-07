<!-- Source: https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/add-tenants -->
<!-- Fetched: 2026-03-31T18:05:33.438863+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: common-services, tenants -->

# Add a Tenant Through Common Services



 



 Learn about adding a tenant through Common Services.



 
 






















 

- 
- 
- 
- 
- 

- [role](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-roles-and-permissions)

| Where Can I Use
                                This? | What Do I Need? |
| --- | --- |
| Strata Cloud ManagerThe Activation ConsoleStrata Multitenant Cloud ManagerPrisma SASE Multitenant PortalCommercial or FedRAMP deployments | IAM  of
                                            Superuser, Multitenant Superuser, Multitenant IAM
                                            Admin |


After you create a tenant, you can allocate a supported product license to it or you can create a
 child tenant and allocate the license to it. Licenses are allocated per each child
 tenant that you need to manage.

If you are adding a tenant for the first time, you are automatically directed to
 Tenants when you follow the [license activation flow](/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started.html) flow, in which case
 you can skip to the select a tenant step. 

If you are not adding a tenant for the first time or you are otherwise not following the general
 flow, you can add a tenant from Tenants. 

You can create your tenant
hierarchy to reflect your existing organizational structure. You
can also consider [identity and access inheritance](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/about-identity-and-access) when
creating the hierarchy, in addition to [tenant hierarchy
limits](/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants).

1.  Use one of the [various ways to access](/content/techdocs/en_US/common-services/subscription-and-tenant-management/get-started.html)
 Tenants.
 If you have a single tenant environment, you will see [Products](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/settings/products)
 instead. The steps are basically the same. 

 

2.  Select a tenant to be the
parent of the child tenant you want to add.
3.  Select New Tenant. 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

4.  Specify a Name for the child that
is representative of its function and select a Business Vertical. 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 
 The
Business Vertical is used for summarizing tenant network traffic
information. 

5.  Select the **Telemetry Tier**, which defines the type of telemetry data
 transferred to the **Data Region** for monitoring and analysis. 
 
  - Full (Recommended)- collects comprehensive data
 to support in-depth monitoring and analysis. This is the default
 setting.
  - Diagnostic- collects only essential data required
 for diagnostics and troubleshooting.

 To learn more about the data collected in each tier, see [Device Telemetry Metrics
                        Reference](https://docs.paloaltonetworks.com/pan-os/u-v/pan-os-device-telemetry-metrics-reference/pan-os-device-telemetry-overview/telemetry-tiers).

 
 
 Telemetry Tier must be set to Full if the tenant
 includes Strata Cloud Manager.

 

6.  Select the Data Region  where the telemetry data will be
 stored.
 
  - You cannot edit the region if Strata Logging Service, Strata Cloud
 Manager, or IOT Security is already enabled in the tenant.

  - If you add Strata Logging Service, Strata Cloud Manager, or IOT
 Security to the tenant later, the data region automatically switches
 to the region used by that product.

 

7.  Specify a Support
Contact, such as an email address or a phone number
of a person to contact for support purposes. The maximum character
limit for the contact is 255. 
  - Select Inherit from parent if
the contact person is the same as the parent.
  - Select Use custom if the contact person
is different from the parent.

8.  Set the User Inactivity Timeout to automatically log out
 idle users after a specific period. The default timeout is 30 minutes, but you
 can customize this value between 10 and 60 minutes. Choose a shorter or longer
 duration based on your organization's security policy and operational needs.
 This flexibility allows you to balance security requirements with user
 convenience. 
 
 
 When no timeout value is set, new tenants automatically adopt the default
 timeout value from their parent tenant. Once you customize the timeout
 value, it becomes independent and is maintained separately for that
 tenant.

 

9.  Add Tenant as a child of the current
parent tenant in the tenant hierarchy. 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

10.  (Optional) Specify license and activation details
for your product.