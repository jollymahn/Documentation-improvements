<!-- Source: https://docs.paloaltonetworks.com/strata-logging-service/administration/overview -->
<!-- Fetched: 2026-03-31T18:05:28.875388+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: sls, logging -->

# Introduction to  Strata Logging Service

 

 
 
 
 
 
 

 

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
                            
                                    Start Sending Logs to Strata Logging Service](/content/techdocs/en_US/strata-logging-service/activation-and-onboarding/start-sending-logs.html)
 

 
 

**[Next
                                
                                    Strata Logging Service Regions](/content/techdocs/en_US/strata-logging-service/administration/overview/supported-regions.html)
 

 

---

 
 
 















 

# Introduction to  Strata Logging Service



 Learn about the cloud-based logging infrastructure provided
by Palo Alto Networks.



 






















 

- [Software NGFW
                                    Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)
- 
- 
- 
- 

- [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support.html)
- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW, including those funded by Prisma AccessCortex Xpanse™Cortex XSOARCortex
                                    XDR | One of these:Strata Logging Service |


Palo Alto Networks® Strata Logging Service provides cloud-based, centralized log
 storage and aggregation for your on premise, virtual (private cloud and public cloud)
 firewalls, for Prisma Access, and for cloud-delivered services such as Cortex
 XDR.

Strata Logging Service is secure, resilient, and fault-tolerant, and it ensures your
 logging data is up-to-date and available when you need it. It provides a scalable
 logging infrastructure that alleviates the need for you to plan and deploy Log
 Collectors to meet your log retention needs. If you already have on premise Log
 Collectors, the new Strata Logging Service can easily complement your
 existing setup. You can augment your existing log collection infrastructure with the
 cloud-based Strata Logging Service to expand operational capacity as your
 business grows, or to meet the capacity needs for new locations.

With this service, Palo Alto Networks takes care of the ongoing maintenance and monitoring of the
 logging infrastructure so that you can focus on your business. 

 
 

 

Strata Logging Service interacts with several different products.
 Some products send logs to Strata Logging Service, while others use it to view
 and analyze the log data. 

## Features of Strata Logging Service

 Use the Strata Logging Service to-
- [Check the status](/content/techdocs/en_US/strata-logging-service/administration/monitoring/view-status.html) of a Strata Logging Service
 instance
- [View](https://docs.paloaltonetworks.com/strata-logging-service/administration/monitoring/view-associated-devices) the devices and tenants
 onboarded to Strata Logging Service instance.
- [Configure log storage quota](https://docs.paloaltonetworks.com/content/techdocs/en_US/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/set-log-storage-quota.html#id183GG0WA0IW)
- [Search, filter, and export log data](/content/techdocs/en_US/strata-logging-service/administration/view-logs/retrieve-logs.html)
- [Forward log data](https://docs.paloaltonetworks.com/content/techdocs/en_US/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-log-forwarding-app.html#id186EE0A0HTP) to a Syslog
 server, https server, or an email server for long-term storage, SOC, or
 internal audit.

## Products that send logs to Strata Logging Service

 






















 [Palo Alto Networks
                                        Firewalls](https://docs.paloaltonetworks.com/content/techdocs/en_US/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/start-sending-logs-to-cortex-data-lake/start-sending-logs-to-cortex-data-lake-individually-managed.html#id9c9e0713-d2b3-4f95-a507-31cf81434a00)

[view all log records](https://docs.paloaltonetworks.com/cortex/explore)

[Panorama-Managed
                                        Firewalls](https://docs.paloaltonetworks.com/content/techdocs/en_US/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/start-sending-logs-to-cortex-data-lake/start-sending-logs-to-cortex-data-lake-panorama-managed.html#idde1f1db5-8116-4806-982f-41e90570db45)

[Prisma Access](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-admin/prisma-access-overview/prisma-access-product-overview)

|  | You can onboard individual firewalls directly to Strata Logging Service. Use the Strata Logging Service app to 
                                    that the firewalls forward to Strata Logging Service. |
| --- | --- |
|  | If you’re using Panorama, you can onboard firewalls to Strata Logging Service at scale, instead of onboarding
                                    each individual firewall. All Strata Logging Service logs
                                    are visible directly in Panorama. |
|  | With Prisma Access, Palo Alto Networks deploys and manages the
                                    security infrastructure globally to secure your remote networks
                                    and mobile users. Prisma Access logs directly to Strata Logging Service. You can view the logs, ACC, and
                                    reports from Panorama for an aggregated view into your remote
                                    network and mobile user traffic. To enable logging for Prisma
                                    Access, you must purchase a Strata Logging Service
                                    license. Log traffic does not use the licensed bandwidth you
                                    purchased for Prisma Access. |



## Products that use logs stored in Strata Logging Service

 






















 [AIOps for NGFW](https://docs.paloaltonetworks.com/aiops/aiops-for-ngfw)

[Prisma Access](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-admin/prisma-access-overview/prisma-access-product-overview)

[view and filter your log
                                        data](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/monitor.html)[generate reports](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/reports.html)

[IoT Security](https://docs.paloaltonetworks.com/iot.html)

[ACC](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/monitor-network-activity/use-panorama-for-visibility/monitor-the-network-with-the-acc-and-appscope.html)[reports](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/monitor-network-activity/use-panorama-for-visibility/generate-schedule-and-email-reports.html)

[SaaS Security
                                    Inline](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/get-started-with-saas-security-inline/whats-saas-security-inline.html)

[SaaS application usage
                                        data](https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-inline/assess-risks/view-data.html)

[Strata Logging Service
                                        Content Pack](https://cortex.marketplace.pan.dev/marketplace/details/CortexDataLake/)[PAN-OS to Strata Logging Service Monitoring content
                                    pack](https://cortex.marketplace.pan.dev/marketplace/details/PANOStoCDLMonitoring/)

|  | AIOps for NGFW uses Strata Logging Service log
                                    data to assess the health of your firewalls and generate alerts.
                                    You can also view Strata Logging Service log data from
                                    within AIOps for NGFW. |
| --- | --- |
| (Cloud-Managed) | Cloud-managed Prisma Access enables you to , and it can  on
                                    your log data. |
|  | IoT Security is a cloud-based app that ingests the device data
                                    that next-generation firewalls collect from network traffic and
                                    send to Strata Logging Service. IoT Security then uses
                                    this data to discover the “things” on your network and identify
                                    normal device behavior and detect suspicious activity. |
| Panorama | Panorama displays logs stored in Strata Logging Service.
                                    The Panorama  and  give you an
                                    aggregated view into your remote network traffic. |
|  | SaaS Security Inline uses Strata Logging Service logs to
                                    discover users and provide  about those users. |
| Cortex XDR | If you extend your firewall security policy to mobile
                                    users and remote networks using Prisma Access or GlobalProtect,
                                    you can also forward related traffic logs to Strata Logging Service. The analytics engine can then
                                    analyze those logs and raise alerts on anomalous behavior. |
| Cortex XSOAR | In Cortex XSOAR Marketplace, install the
                                    to run queries for critical threat
                                logs, social applications, threat logs, etc. You can also Install
                                the  to monitor the PAN-OS FW log in a recurring
                                job. |
| Cortex
                                Xpanse™ | Cortex
                                    Xpanse™ consumes GlobalProtect login
                                    events on a daily basis to surface external exposures on
                                    employee networks. |