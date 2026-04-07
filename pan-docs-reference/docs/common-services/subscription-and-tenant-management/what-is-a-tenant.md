<!-- Source: https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant -->
<!-- Fetched: 2026-03-31T18:05:34.416607+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: common-services, tenants -->

# What is a Tenant?



 



 Learn about tenants, Tenant Service Groups, and TSGs. A tenant is a logical container for
 managing and monitoring licensed products. Tenant Service Groups enable the management of
 multiple customers or business units in a tenant hierarchy that reflects your existing
 organizational structure. Each tenant is isolated and can have its own set of policies and
 resources, while still being managed from a single location.



 Common Services enables you to manage a hierarchy of business units and organizations that
 is referred to as a tenant service group. A tenant service group (TSG) is
 used to provide a logical container that contains tenants and other TSGs.
 It is the building block for a multitenant hierarchy. Generally, this multitenant
 hierarchy is described as a series of nested tenants, where a tenant is used to manage,
 monitor, and license products. But mechanically, a tenant is just a TSG. The terms are
 often used interchangeably.

After you have received information about the transition of your app instance to a tenant, your
 instance is now a single tenant. You have access to Common Services for
 subscription management, tenant management, and identity and access management. You do
 not have access to the multitenant summary dashboards, as those are not applicable and
 not available for single tenants. See the [FAQ](https://docs.paloaltonetworks.com/common-services/faq/faq) if you have more questions about the migration.

Each tenant is automatically assigned a TSG ID, which is primarily for use with [service accounts](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/add-service-accounts). However, the TSG ID is also
 used for default login purposes. If you clear your cache, or if you log out of the
 Strata Multitenant Cloud Manager and log back in, you are logged into the top-level parent
 tenant with the lowest TSG ID by default. The top-level parent tenant with the lowest
 TSG ID is likely the first one you created. 

The [tenant hierarchy limits](/content/techdocs/en_US/common-services/subscription-and-tenant-management/manage-multitenants/limits-tenants.html#limits-tenants) explain the number of
 used and unused tenants you can create.