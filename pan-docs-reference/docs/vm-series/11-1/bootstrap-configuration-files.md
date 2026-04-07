<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-configuration-files -->
<!-- Fetched: 2026-03-31T18:04:50.583426+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Bootstrap Configuration Files



 



 The bootstrap package must include the basic configuration
in config/init-cfg.txt. The complete configuration
(in /config/bootstrap.xml file) is optional. 

When you include init-cfg.txt file and the bootstrap.xml file
in the bootstrap package, the firewall merges the configurations
of those files, and if any settings overlap, the firewall uses the
values defined in the init-cfg.txt file.

- init-cfg.txt
- bootstrap.xml


 















 

## init-cfg.txt



 Contains basic information for configuring the management
interface on the firewall, such as the IP address type (static or
DHCP), IP address (IPv4 only or both IPv4 and IPv6), netmask, and
default gateway. The DNS server IP address, Panorama IP address
and device group and template stack parameters are optional. 

You can use the generic name init-cfg.txt,
or to be more specific, you can prepend the UUID or Serial number
of each firewall to the filename (for example: 0008C100105-init-cfg.txt).

When the firewall boots, it searches for a text file that matches
its UUID or serial number and, if none is found, it searches using
the generic filename init-cfg.txt. For a sample
file, see [Create
the init-cfg.txt File](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file.html#id8770fd72-81ea-48b6-b747-d0274f37860b). 

 
 If you are using Panorama to manage your bootstrapped VM-Series
firewalls:

- You must generate a VM auth key on Panorama
and include the key in the init-cfg.txt file.
For more information, see [Generate
the VM Auth Key on Panorama](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/generate-the-vm-auth-key-on-panorama.html#id6507055f-4230-47ac-adc9-cd947bfd83c4).

- The Panorama appliance that manages the firewalls must be
in Panorama mode. If you use a Panorama appliance in Management-Only
mode, firewall logs are dropped because Panorama in Management-Only
mode does not have a Log Collector Group that can store firewall
logs.

- When you include Panorama connectivity parameters in your init-cfg.txt,
 Panorama attempts to push configuration to the VM-Series firewall upon first
 connection. The connection to Panorama fails if hostname, template stack, or
 device group values are missing from the init-cfg.txt file.








 















 

## bootstrap.xml



 The optional bootstrap.xml file
contains a complete configuration for the firewall. If you are not
using Panorama to centrally manage your firewalls, the bootstrap.xml file
provides a way to automate the process of deploying firewalls that
are configured at launch. 

You can define the configuration manually or export the running
configuration (running-config.xml) from an
existing firewall and save the file as bootstrap.xml.
If you export bootstrap.xml file, make sure
to export the XML file from a firewall deployed on the same platform
or hypervisor as your deployment. See [Create
the bootstrap.xml File](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-bootstrapxml-file.html#id61aa8472-5aba-41c5-ac4f-4a409e3dedb6).

 
 To ensure successful bootstrapping for Advanced Routing
using both init-cfg.txt* and bootstrap.xml files, enable Advanced
Routing in both* init-cfg.txt* and bootstrap.xml. Failing to enable
Advanced Routing in both files could result in an unstable environment;
for example, if you use **show advanced routing route** the output
indicates that Advanced Routing is enabled, however, the command **show
deviceconfig setting** indicates that Advanced Routing is not
enabled. Further, Advanced Routing will not be completely working,
and may end up in commit failure. If the setup is in the above state,
to enable Advanced Routing, reboot VM-Series firewall after configuring **set
deviceconfig setting advanced-routing yes**

.