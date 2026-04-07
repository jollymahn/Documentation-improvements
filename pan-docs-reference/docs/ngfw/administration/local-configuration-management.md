<!-- Source: https://docs.paloaltonetworks.com/ngfw/administration/onboard-devices-and-deployments/local-configuration-management -->
<!-- Fetched: 2026-04-01T01:59:19.578027+00:00 -->
<!-- Project: scm -->
<!-- Tags: ngfw, onboarding, local-config -->

# Manage a Local Firewall Configuration

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Next-Generation Firewall Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Getting Started
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Administration
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Networking
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Quick Start
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Reference
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Incidents & Alerts
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Release Notes
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 
 Select a Document
 
 **
 
 
 
  - PAN-OS 12.1
 
  - PAN-OS 11.2
 
  - PAN-OS 11.1
 
  - PAN-OS 11.0 (EoL)
 
  - PAN-OS 10.2
 
  - PAN-OS 10.1
 
  - PAN-OS 10.0 (EoL)
 
  - PAN-OS 9.1 (EoL)
 
  - PAN-OS 9.0 (EoL)
 
  - PAN-OS 8.1 (EoL)
 

 

 

 

 
 

 
 
- 
 
 
 
 
 

 Help
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 
 Select a Document
 
 **
 
 
 
  - PAN-OS 12.1
 
  - PAN-OS 11.2
 
  - PAN-OS 11.1
 
  - PAN-OS 10.2
 
  - PAN-OS 10.1
 

 

 

 

 
 

 
 

 

 

 

 

 
 
 
---

 
 
 **

[Previous
                            
                                    Configure the Auxiliary Interface Settings](/content/techdocs/en_US/ngfw/getting-started/device-setup-for-cloud-managed-devices/configure-the-auxiliary-interface-settings.html)
 

 
 

**[Next
                                
                                    Manage Your NGFWs](/content/techdocs/en_US/ngfw/getting-started/manage-your-ngfws.html)
 

 

---

 
 
 















 

# Manage a Local Firewall Configuration



 Enhances readability, simplifies troubleshooting, and reduces manual effort by
 providing visibility and control over local firewall configurations through Strata Cloud Manager.



 
 






















 

- 

- 
- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW (Managed by Strata Cloud Manager) | One of these licenses:Strata Cloud Manager EssentialsStrata Cloud Manager Pro |



 The local configuration management feature eliminates the need for context switching
 from central management to individual firewalls for managing local configurations.
 This feature enhances readability, simplifies troubleshooting, and reduces manual
 effort by providing visibility and control over local firewall configurations
 through Strata Cloud Manager. Additionally, it identifies any conflicting or
 overridden objects between local and pushed configurations, making it easier to
 troubleshoot.

 

1.  Log in to Strata Cloud Manager.
2.  Select ConfigurationNGFW and Prisma AccessOverview and select the configuration Scope.
3.  Select a folder or specific firewall from your Folders
 to view any conflicting configurations.
 
  - Firewalls with config conflicts shows the number
 of firewalls with conflicts. View Conflicts to
 see conflicts for all firewalls and their respective locations. Click
 the individual firewall to further investigate device-level conflicts.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

  - Objects with config conflicts shows the number of
 conflicts per firewall. Click the number to view the conflicted objects
 and their corresponding types specific to that firewall. Click the
 object to get the granular details on the conflict. 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

  - Select objects such as zones and interfaces to view any conflicts with
 the local device configuration.
  - Use the Show Config Diff option to compare
 configurations between the Strata Cloud Manager and the firewall.