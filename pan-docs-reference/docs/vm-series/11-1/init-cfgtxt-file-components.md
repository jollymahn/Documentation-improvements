<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file/init-cfgtxt-file-components -->
<!-- Fetched: 2026-03-31T18:37:09.929174+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags: vm-series, bootstrap, init-cfg -->

# init-cfg.txt File Components



 



 The following table describes the bootstrap parameters
in the init-cfg.txt file.
























 

[template stack](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-overview/centralized-firewall-configuration-and-update-management/templates-and-template-stacks)

[device group](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-overview/centralized-firewall-configuration-and-update-management/device-groups)

[collector group](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-log-collection/manage-collector-groups/configure-a-collector-group.html)

[Generate the VM Auth Key on Panorama](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/generate-the-vm-auth-key-on-panorama.html#id6507055f-4230-47ac-adc9-cd947bfd83c4)

- 

- 

- 

  - [Management
Interface Mapping for Use with Amazon ELB](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-aws/about-the-vm-series-firewall-on-aws/management-interface-mapping-for-use-with-amazon-elb.html#id7e1c2653-88af-4a85-8bb8-aae1847c0d9f)
  - [Management Interface Swap for Google Cloud Platform Load Balancing](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform/deploy-vm-series-on-gcp/management-interface-mapping-for-google-internal-load-balancing.html#id17CQ1G00Z4K)
  - [Use the VM-Series CLI to Swap the Management Interface on ESXi](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-a-vm-series-firewall-on-an-esxi-server/install-a-vm-series-firewall-on-vmware-vsphere-hypervisor-esxi/use-the-vm-series-firewall-cli-to-swap-the-management-interface-on-esxi.html#id1f6b1306-0489-49e2-8e6b-457cc57c9b1e)
  - [Use the VM-Series CLI to Swap the Management Interface on KVM](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-kvm/install-the-vm-series-firewall-on-kvm/use-the-vm-series-firewall-cli-to-swap-the-management-interface-on-kvm.html#id1f6b1306-0489-49e2-8e6b-457cc57c9b1e)

[firewall supports DPDK](https://docs.paloaltonetworks.com/compatibility-matrix/vm-series-firewalls/vms-series-hypervisor-support.html)

- [ESXi](https://docs.paloaltonetworks.com/compatibility-matrix/vm-series-firewalls/vms-series-hypervisor-support.html#ida171dac5-7ebf-40a0-a6d6-4e2c35329211_idbd366b11-f7f4-4f52-bab9-58e5b152bc6c)[KVM](https://docs.paloaltonetworks.com/compatibility-matrix/vm-series-firewalls/vms-series-hypervisor-support.html#ida171dac5-7ebf-40a0-a6d6-4e2c35329211_id81807d03-803f-4c2c-927f-90b620d8989e)

- [VM-Series Integration with an AWS Gateway Load Balancer](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-aws/vm-series-integration-with-gateway-load-balancer.html#idbe4a3f98-f81f-4cd4-82b9-76f67e22b737)

- [Associate a VPC Endpoint with a VM-Series Interface](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-aws/vm-series-integration-with-gateway-load-balancer/integrate-the-vm-series-with-an-aws-gateway-load-balancer/associate-a-vpc-endpoint-with-a-vm-series-interface.html#idfa08d566-ce68-4733-a17f-b67ae9110aa9)

- [Enable Overlay Routing for the VM-Series on AWS](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-aws/vm-series-integration-with-gateway-load-balancer/integrate-the-vm-series-with-an-aws-gateway-load-balancer/enable-overlay-routing-for-the-vm-series-on-aws.html#id32ad6f23-75d9-4b7b-bb03-e774322205d3)

- [Customize Dataplane Cores](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/customize-data-plane-cores.html#id4e6cde84-2453-4173-b55c-f4e02c7f0e46)

- [Enable NUMA Performance Optimization on the VM-Series](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/about-the-vm-series-firewall/enable-numa-performance-optimization-on-the-vm-series.html#idc775ff5f-070a-44b1-8d2a-70bd1f6d05d7)

- ************

- [AWS](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-aws/vm-series-integration-with-gateway-load-balancer/enable-session-resiliency-on-vm-series-for-aws.html)[GCP](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform/deploy-vm-series-on-gcp/enable-session-resiliency-on-vm-series-for-gcp.html)

[Palo Alto Networks CSP](https://support.paloaltonetworks.com/support)[Install a Device Certificate on the VM-Series Firewall](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/install-a-device-certificate-on-the-vm-series-firewall.html#id63b6c128-5973-469e-bd4a-bdc6da5cb3df)

| Field | Description |
| --- | --- |
| type= | Type of management IP address: static or
dhcp-client. This field is required. |
| ip-address= | IPv4 address. This field is ignored if the
type is dhcp-client. If the type is static, an IPv4 address is required;
the ipv6-address field is optional and can be included.You
cannot specify the management IP address and netmask configuration
for the VM-Series firewall in AWS and Azure. If defined, the firewall
ignores the values you specify. |
| default-gateway= | IPv4 default gateway for the management
interface. This field is ignored if the type is dhcp-client. If
the type is static, and ip-address is used, this field is required. |
| netmask= | IPv4 netmask. This field is ignored if the
type is dhcp-client. If the type is static, and ip-address is used,
this field is required. |
| ipv6-address= | IPv6 address and /prefix length of the management interface. This field is ignored if the type is
                                dhcp-client. If the type is static, this field can be specified
                                along with the ip-address field, which is required. |
| ipv6-default-gateway= | IPv6 default gateway for the management
interface. This field is ignored if the type is dhcp-client. If
the type is static and ipv6-address is used, this field is required. |
| hostname= | Hostname for the firewall. This field is required when adding Panorama configuration
                                parameters. |
| panorama-server= | IPv4 or IPv6 address of the primary Panorama
server. This field is not required but recommended for centrally
managing your firewalls.
                            When creating a bootstrap package, set
                                    panorama-server=cloud. The cloud
                                parameter should be used when connecting the firewall to Strata
                                Cloud Manager.
                            
    
    When you provide a Panorama IP address in
                                your init-cfg.txt file, Panorama pushes configuration to firewall
                                automatically upon first connection. |
| panorama-server-2= | IPv4 or IPv6 address of the secondary Panorama
server. This field is not required but recommended.
                            A value defined for panorama-server-2 is
                                ignored when panorama-server=cloud is used. |
| tplname= | Panorama  name. If
                                you add a Panorama server IP address, you must include a template
                                stack name in this field so that you can centrally manage and push
                                configuration settings to the firewall. If you do not include a
                                template stack name, the firewalls connection to Panorama fails. |
| dgname= | Panorama name. If you
                                add a Panorama server IP address, you must include a device group
                                name in this field so that you can group the firewalls logically and
                                push policy rules to the firewall.  If you do not include a device
                                group name, the firewalls connection to Panorama fails. |
| cgname= | Panorama  name.
If you want to bootstrap the firewall to send logs to a Panorama
collector group, you must first configure a collector group on Panorama
and then configure the firewall to forward logs to Panorama. On
the M-Series appliances, a default Collector Group is predefined
and already contains the local Log Collector as a member. On the
Panorama virtual appliance, you must add the Collector Group and
add the local Log Collector as a member. |
| dns-primary= | IPv4 or IPv6 address of the primary DNS
server. |
| dns-secondary= | IPv4 or IPv6 address of the secondary DNS
server. |
| vm-auth-key= | Virtual machine authentication key for Panorama
(see ). This field
is ignored when bootstrapping hardware firewalls. |
| op-command-modes= | The following values are allowed: multi-vsys,
jumbo-frame, mgmt-interface-swap. If you enter multiple values,
use a space or a comma to separate the entries.multi-vsys—Hardware-based firewalls only Enables multiple virtual
                                        systems.jumbo-frame—Enables the default MTU
size for all Layer 3 interfaces to be set at 9192 bytes.mgmt-interface-swap—VM-Series firewall on AWS, Google, ESXi, and KVM
                                            only Allows you to swap the management interface
                                        (MGT) with the dataplane interface (ethernet 1/1) when
                                        deploying the firewall. For details, see |
| op-cmd-dpdk-pkt-io= | The value on or off allows
you to enable or disable Data Plane Development Kit (DPDK) in environments
where the . DPDK allows the
host to process packets faster by bypassing the Linux kernel; interactions
with the NIC are performed using drivers and the DPDK libraries. |
| plugin-op-commands= | Specify VM-Series plugin operation commands. 
    
    Multiple
commands must be entered on a single, comma separated list with
no spaces.
sriov-access-mode-on—This
command is only valid for VM-Series firewall on  and  hypervisors. For
KVM only, if you enable sriov-access-mode-on,
do not enable op-command-modes=jumbo-frame.aws-gwlb-inspect:enable—Enables .aws-gwlb-associate-vpce:<vpce-id>@ethernet<subinterface> —Allows
you to  or subinterface
on the firewall. The specified interface is assigned to a security
zone.aws-gwlb-overlay-routing:enable—Use
this command to  when integrated
with a AWS GWLB.set-dp-cores:<#-cores>—Customize
the number of dataplane vCPUs for a VM-Series firewall running PAN-OS
11.0 or later deployed with a Software NGFW license. This option
is not supported on NSX-T. For more information, see .numa-perf-optimize:enable—enables
NUMA performance optimization on the VM-Series firewall with VM-Series
plugin 2.1.2 or later installed. For more information, see .advance-routing:enable—enables advanced routing. To ensure successful
                                        bootstrapping for Advanced Routing using both init-cfg.txt*
                                        and bootstrap.xml files, enable Advanced Routing in both*
                                        init-cfg.txt* and bootstrap.xml. Failing to enable Advanced
                                        Routing in both files could result in an unstable
                                        environment; for example, if you use show advanced
                                            routing route the output indicates that Advanced
                                        Routing is enabled, however, the command show
                                            deviceconfig setting indicates that Advanced Routing
                                        is not enabled. Further, Advanced Routing will not be
                                        completely working, and may end up in commit failure. If the
                                        setup is in the above state, to enable Advanced Routing,
                                        reboot VM-Series firewall after configuring set
                                            deviceconfig setting advanced-routing yes.setsess-ress:True—enables session
                                    resiliency on the VM-Series firewall for  and . |
| dhcp-send-hostname= | The value of yes or no comes from the DHCP
server. If yes, the firewall will send its hostname to the DHCP
server. This field is relevant only if type is dhcp-client. |
| dhcp-send-client-id= | The value of yes or no comes from the DHCP
server. If yes, the firewall will send its client ID to the DHCP
server. This field is relevant only if type is dhcp-client. |
| dhcp-accept-server-hostname= | The value of yes or no comes from the DHCP
server. If yes, the firewall will accept its hostname from the DHCP
server. This field is relevant only if type is dhcp-client. |
| dhcp-accept-server-domain= | The value of yes or no comes from the DHCP
server. If yes, the firewall will accept its DNS server from the
DHCP server. This field is relevant only if type is dhcp-client. |
| vm-series-auto-registration-pin-idandvm-series-auto-registration-pin-value | The VM-Series registration PIN ID and value for installing the device certificate on the
                                VM-Series firewall. The PIN ID and value also enable you to
                                automatically activate the site licenses for AutoFocus and Strata
                                Logging Service on PAYG instances of the firewall.You must generate this in registration PIN
ID and value on the .
See  for information
on generating PIN ID and value. |
| redis-endpoint= | Provide the IP address or FQDN and port of your Redis endpoint. For
                                use with session resiliency in the VM-Series for AWS and GCP. |
| redis-auth= | Optional The auth code your VM-Series firewall
                            uses to connect with the Redis endpoint. For use with session resiliency
                            in the VM-Series for AWS and GCP. |
| redis-certificate= | Optional The root CA certificate string used to
                            connect to the Redis endpoint. The certificate must be a base64-encoded
                            string using utf-8 encoding. For use with session resiliency in the
                            VM-Series for GCP; not required for session resiliency on AWS. |