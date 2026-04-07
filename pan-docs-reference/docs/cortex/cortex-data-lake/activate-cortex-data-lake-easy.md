<!-- Source: https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/activate-cortex-data-lake-toc/activate-cortex-data-lake-easy -->
<!-- Fetched: 2026-04-01T01:59:23.974888+00:00 -->
<!-- Project: scm -->
<!-- Tags: cortex, data-lake, activation -->

# Activate Strata Logging Service

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Strata Logging Service Docs

 
---

 

 
 

 
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
 

 

 
 
- 
 
 
 
 
 

 Release Notes
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Log Reference
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 

 

 

 

 

 
 
 
---

 
 
 **

[Previous
                            
                                    TCP Ports and FQDNs Required for Strata Logging Service](/content/techdocs/en_US/strata-logging-service/activation-and-onboarding/planning/ports-and-fqdns.html)
 

 
 

**[Next
                                
                                    Onboard Firewalls to Strata Logging Service](/content/techdocs/en_US/strata-logging-service/activation-and-onboarding/onboard-overview.html)
 

 

---

 
 
 















 

# Activate Strata Logging Service



 This is how you activate Strata Logging Service.



 
 






















 

- [Software NGFW
                                            Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- 

- [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)
- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW, including those funded by Prisma Access | One of these:Strata Logging Service |


After purchasing Strata Logging Service, you should have received an email with a
 link to activate Strata Logging Service. Click on the link and follow
 the steps below to complete activation.

You do not need to follow this procedure if you have already activated Strata Logging Service as part of another product purchase (for example, Prisma Access).

 
 If you are using PAN-OS 10.0 or later firewalls, and if you were sharing telemetry data with Palo
 Alto Networks prior to purchasing a Strata Logging Service license, then
 you already have a small, unlicensed Strata Logging Service instance.
 This instance exists solely for the purpose of processing your PAN-OS telemetry
 data. 

When you activate your license, Palo Alto Networks will upgrade this tenant to a full Strata Logging Service instance, so long as the region you use to send
 telemetry data to Palo Alto Networks is the same region that you use when you
 activate your Strata Logging Service license. If you use different
 regions for this purpose, then the small telemetry-specific tenant will not
 upgrade to your new, licensed Strata Logging Service instance. 

1.  Click on the link in your purchase confirmation
email.
2.  Select your Strata Logging Service subscription and click
 Activate Subscription.
3.  Log in to the [hub](https://apps.paloaltonetworks.com/) with your Palo Alto Networks Customer Support
 credentials.
4.  Select the customer support account that you want to associate with your
 subscription.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

5.  If you are activating the Strata Logging Service instance in a new
 [tenant service group](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/manage-multitenants/what-is-a-tenant) (TSG), select
 **Create New** from the Tenant drop-down list and then enter a tenant
 name. 
 
 

 Or

If you want to add the Strata Logging Service instance to an
 existing TSG, select the TSG from the drop-down list. A tenant can have only one
 Strata Logging Service instance running on it.

6.  Select the geographical Region for your Strata Logging Service instance.
7.  Learn about how to onboard devices to Strata Logging Servicebefore you
 complete activation.
8.  Review your selections, Agree to the Terms and Conditions, and click
 Activate Now.
9.  Verify the Strata Logging Service status.
 
  1. **Sign In** to the hub at [https://apps.paloaltonetworks.com/](https://apps.paloaltonetworks.com/).
  2. Select the Strata Logging Service instance for which you want to
 view status. If you have multiple Strata Logging Service
 instances, hover over the Strata Logging Service tile and then
 select from the list of available instances associated with your
 account.
  3. Confirm the following Status details:
    - Service status and the amount of storage used as a ratio of
 total storage you have purchased.
    - The geographic [region](https://docs.paloaltonetworks.com/content/techdocs/en_US/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/overview/supported-regions.html#id3e742928-a709-42be-aaf2-5481b781ecb9) where your logs
 are stored.
    - Verify your configuration on the different log types (sources)
 from which the Strata Logging Service is receiving logs,
 and the [log retention days](/content/techdocs/en_US/strata-logging-service/activation-and-onboarding/set-retention-days.html)
 allocated for each [log subtype](https://docs.paloaltonetworks.com/strata-logging-service/administration/monitoring/log-types).

 

10.  [Onboard devices](/content/techdocs/en_US/strata-logging-service/activation-and-onboarding/onboard-overview.html) to Strata Logging Service, then configure
 your devices to [send logs to Strata Logging Service](/content/techdocs/en_US/strata-logging-service/activation-and-onboarding/start-sending-logs.html), and
 [configure your log storage settings](/content/techdocs/en_US/strata-logging-service/activation-and-onboarding/set-retention-days.html).
11.  [Allow traffic](/content/techdocs/en_US/strata-logging-service/activation-and-onboarding/planning/ports-and-fqdns.html) from your source to connect to Strata Logging Service.