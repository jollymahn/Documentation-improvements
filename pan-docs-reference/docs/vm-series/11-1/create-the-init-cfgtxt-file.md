<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file -->
<!-- Fetched: 2026-03-31T18:04:52.777350+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Create the init-cfg.txt File



 



 Learn how create the init-cfg.txt file.



 The init-cfg.txt file
is required to bootstrap the VM-Series firewall. It provides the basic
information the firewall needs to connect to your network.

- [init-cfg.txt
File Components](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file/init-cfgtxt-file-components.html#id07933d91-15be-414d-bc8d-f2a5f3d8df6b)
- [Sample
init-cfg.txt File](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file/sample-init-cfgtxt-file.html#id114bde92-3176-4c7c-a68a-eadfff80cb29)
Complete the following procedure
to create the init-cfg.txt file.

1.  Create a new text file.Use a text editor such as Notepad, EditPad, or other plain-text
editors to create a text file.

2.  Add the basic network configuration for the management
interface on the firewall.
 
 If any of the required parameters are missing in
the file, the firewall exits the bootstrap process and boots up
using the default IP address, 192.168.1.1. You can view the system
log on the firewall to detect the reason for the bootstrap failure.
For errors, see [Licensing
API](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/licensing-api.html#id0873c753-02bd-4371-9e6a-2b35cfc0a44b).

 
 There are no spaces between the key
and value in each field. Do not add spaces as they could cause failures
during parsing on the mgmtsrvr side.

  - To configure
the management interface with a static IP address, you must specify the
IP address, type of address, default gateway, and netmask. An IPv4
address is required, IPv6 address is optional. For syntax, see [Sample
init-cfg.txt File](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file/sample-init-cfgtxt-file.html#id114bde92-3176-4c7c-a68a-eadfff80cb29).
  - To configure the management interface as a DHCP client, you
must specify only the type of address. If you enable the DHCP client
on the management interface, the firewall ignores the IP address,
default gateway, netmask, IPv6 address, and IPv6 default gateway
values defined in the file. For syntax, see [Sample
init-cfg.txt File](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file/sample-init-cfgtxt-file.html#id114bde92-3176-4c7c-a68a-eadfff80cb29).
When you enable DHCP on the
management interface, the firewall takes the DHCP assigned IP address
and is accessible over the network. You can view the DHCP assigned
IP address on the General Information widget on the Dashboard or
with the CLI command show system info. However,
the default static management IP address 192.168.1.1 is retained
in the running configuration (show config running)
on the firewall. This static IP address ensures that you can always
restore connectivity to your firewall, in the event you lose DHCP
access to the firewall.

3.  Add the VM auth key to register a VM-Series firewall
with Panorama.To add a VM-Series firewall on Panorama, you must add the
VM auth key that you generated on Panorama to the basic configuration
(init-cfg.txt) file. For details on generating
a key, see [Generate
the VM Auth Key on Panorama](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/generate-the-vm-auth-key-on-panorama.html#id6507055f-4230-47ac-adc9-cd947bfd83c4).

4.  Add details for accessing Panorama.
  - Add IP addresses for the primary and secondary Panorama
servers.
  - A firewall hostname.
  - Specify the template and the device group to which you want
to assign the firewall.
  - To specify Strata Cloud Manager for your Panorama host, use set
 panorama-server=cloud to initiate a TLS connection with the
 cloud management service edge.

 
 
 When you include Panorama connectivity parameters in
 your init-cfg.txt, Panorama attempts to push configuration to the VM-Series
 firewall upon first connection. The connection to Panorama fails if
 hostname, template stack, or device group values are missing from the
 init-cfg.txt file.

5.  (Recommended) Add the VM-Series registration pin and
value for installing the device certificate.If you want to install the device certificate on the VM-Series
firewall at launch, you must generate the VM-Series registration
pin ID and value on the [CSP](https://www.paloaltonetworks.com/company/contact-support) and include it in
the init-cfg.txt file. This pin and value also
applies any site licenses that use the PAYG license.

6.  Optional Include additional parameters for the firewall.
 
  - Add IP address for the primary and secondary DNS servers.
  - Add the hostname for the firewall.
  - Enable either jumbo frames or multiple-virtual systems (or both)
  - Enable management interface swap (mgmt) and the dataplane interface
 (ethernet 1/1) for the VM-Series firewall on AWS or GCP. For more
 information on changing the management interface, see [Management Interface Mapping for Use with Amazon ELB](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-aws/about-the-vm-series-firewall-on-aws/management-interface-mapping-for-use-with-amazon-elb.html#id7e1c2653-88af-4a85-8bb8-aae1847c0d9f) or
 [Management Interface Swap for Google Cloud Platform Load Balancing](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform/deploy-vm-series-on-gcp/management-interface-mapping-for-google-internal-load-balancing.html#id17CQ1G00Z4K).
  - Enable or disable DPDK.