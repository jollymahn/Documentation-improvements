<!-- Source: https://docs.paloaltonetworks.com/ngfw/networking/advanced-routing/enable-advanced-routing -->
<!-- Fetched: 2026-04-01T01:59:20.477882+00:00 -->
<!-- Project: scm -->
<!-- Tags: ngfw, routing -->

# Enable Advanced Routing

 

 
 
 
 
 
 

 

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
                            
                                    Advanced Routing](/content/techdocs/en_US/ngfw/networking/advanced-routing.html)
 

 
 

**[Next
                                
                                    Configure a Logical Router](/content/techdocs/en_US/ngfw/networking/advanced-routing/configure-a-logical-router.html)
 

 

---

 
 
 















 

# Enable Advanced Routing



 



 Enable the Advanced Routing Engine.



 
 






















 

- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW (Managed by PAN-OS or Panorama) |  |


Although a supported firewall can have a configuration that
uses the legacy routing engine and a configuration that uses the
Advanced Routing Engine, only one routing engine is in effect at
a time. Each time you change the engine that the firewall will use
(you enable or disable Advanced Routing to access the advanced engine
or legacy engine, respectively), you must commit the configuration
and reboot the firewall for the change to take effect.

 
 Before you switch to the Advanced Routing
Engine, make a backup of your current configuration.

Similarly,
if you configure Panorama with a template that enables or disables Advanced
Routing, after you commit and push the template to devices, you
must reboot the devices in the template for the change to take effect.

 
 When configuring Panorama, create device
groups and Templates for devices that all use the same Advanced
Routing setting (all enabled or all disabled). Panorama won’t push
configurations with Advanced Routing enabled to lower-end firewalls
that don’t support Advanced Routing. For those firewalls, Panorama
will push a legacy configuration if one is present.

The
Advanced Routing Engine supports multiple logical routers (known
as virtual routers on the legacy routing engine). The number of
logical routers supported depends on the firewall model and is the
same as the number of virtual routers supported on the legacy routing
engine. The Advanced Routing Engine has more convenient menu options
and there are many settings that you can easily configure in a profile
(authentication, timers, address family, or redistribution profile)
that you apply to a BGP peer group or peer, for example. There are
also many static route, OSPF, OSPFv3, RIPv2, multicast, and BFD
settings on the Advanced Routing Engine.

The Advanced Routing
Engine supports RIB filtering, which means you can create a route
map to match static routes or routes received from other routing protocols
and thus filter which routes are installed in the RIB for the logical
router. This function is useful on firewalls with a smaller RIB
or FIB capacity; you can still propagate the necessary routing updates
without using memory needed elsewhere.

1.  Make a backup of your current configuration before you enable Advanced
 Routing.
2.  Enable the Advanced Routing Engine.
  1.  Select DeviceSetupManagement and edit the General Settings.
  2.  Enable Advanced Routing.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  3.  Before you click OK, make sure you have made a backup of your
 configuration for the legacy routing engine.
  4.  Click OK.
  5.  A warning appears:
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

 Select Yes to have the migration script
 convert each virtual router to a logical router and migrate your
 configuration to the advanced routing engine. (Select
 Skip to restart the system with an empty
 configuration. Select Cancel to cancel the
 process to enable Advanced Routing.)

 

  6.  Click OK to approve the migration.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  7.  The virtual routers, links to the logical routers, and their
 color-coded status are listed. Resolve any issues that require user
 intervention. Select Continue
 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  8.  Click Yes to accept the migrated
 configuration.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  9.  (PAN-OS 11.0.2 and later 11.1 releases) Click
 OK.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  10.  Commit and then select DeviceSetupOperations and Reboot Device. Then log back
 into the firewall.If the migration is not successful, generate the technical support
 file, log in to [Palo Alto Networks Customer Support
                                Portal](https://support.paloaltonetworks.com/Support/Index), and report your issues to get help with your
 product.

  11.  (Optional) After successful migration, you can delete all
 virtual routers using the configuration mode CLI command:
 
    1. [Access the CLI](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli).
    2. Execute the following command to remove all configurations
 from the legacy routing engine:

```
username@hostname# delete network virtual-router <vr-name>
```

 
 
 You can delete
 virtual routers if you are going to make changes in the
 logical router configuration, which makes the virtual router
 configuration obsolete, causing commit failures. Although
 deleting virtual routers will avoid commit failures, be
 aware that deleting virtual routers will also permanently
 remove all configuration from the legacy routing engine and
 you won't be able to get the configuration back.

    3. Commit the changes to the
 firewall.
```
username@hostname# commit
```

 

 
 
 When configuring in Panorama, you can select
 **Network > Virtual Routers** to delete all virtual routers.
 Commit the changes and push them to the relevant firewalls before
 continuing.

 

3.  Log back into the firewall.
4.  Select Network.
 Notice the menu items, which are more industry-standard and more detailed
 than the single item (Virtual Routers) on the legacy menu.
 Routing includes Logical
 Routers and Routing Profiles, which
 include BGP, BFD,
 OSPF, OSPFv3,
 RIPv2, Filters, and
 Multicast.

 

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

5.  Select Interfaces and configure one or more [Layer 3 interfaces](/content/techdocs/en_US/ngfw/networking/configure-interfaces/layer-3-interfaces/configure-layer-3-interfaces.html#tabs-iddc65fa08-60b8-47b2-a695-2e546b4615e9_iddc65fa08-60b8-47b2-a695-2e546b4615e9) with a
 static IP address or [as a DHCPv4 client](/content/techdocs/en_US/ngfw/networking/dhcp/configure-an-interface-as-a-dhcpv4-client.html#tabs-id5f4bdc6f-780a-441f-a786-04e1c7852d1d_id5f4bdc6f-780a-441f-a786-04e1c7852d1d) to
 received a dynamically assigned address.
6.  (Optional) Create an Admin Role Profile to control granular access to
 logical routers and routing profiles for an Advanced Routing Engine.
  1.  Select DeviceAdmin Roles and Add an Admin Role Profile by
 Name.
  2.  Select Web UI. 
  3.  Enable, Disable, or
 select Read Only the following options:
 Network, Routing,
 Logical Routers, Routing
 Profiles, BGP,
 BFD, OSPF,
 OSPFv3, RIPv2,
 Filters, and Multicast
 (default is Enable).
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  4.  Click OK.
  5.  Assign the role to an administrator. [Configure a Firewall Administrator
                                Account](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/firewall-administration/manage-firewall-administrators/configure-administrative-accounts-and-authentication/configure-a-firewall-administrator-account.html).

7.  Commit the changes.
8.  Continue by [configuring a logical
                    router](/content/techdocs/en_US/ngfw/networking/advanced-routing/configure-a-logical-router.html#tabs-id83b76f3d-1148-43e8-b784-502628a974ab_id83b76f3d-1148-43e8-b784-502628a974ab).