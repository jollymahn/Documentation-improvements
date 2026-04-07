<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/about-the-vm-series-firewall/vm-series-plugin -->
<!-- Fetched: 2026-03-31T18:04:57.121445+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# VM-Series Plugin



 



 The VM-Series plugin enables Palo Alto Networks to release
cloud provider integrations or hypervisor integrations without upgrading
PAN-OS.



 The VM-Series firewalls include the VM-Series plugin,
a built-in plugin architecture for integration with public cloud
providers or private cloud hypervisors. The VM-Series plugin can
be manually upgraded independent of PAN-OS, enabling Palo Alto Networks®
to accelerate the release of new features, fixes, or integrations
with new cloud providers or hypervisors. 

The VM-Series plugin enables you to manage cloud-specific interactions
between the VM-Series firewalls and the supported public cloud platforms—AWS,
GCP, and Azure. The plugin enables publishing custom metrics to
cloud monitoring services (such as AWS CloudWatch), bootstrapping,
configuring user credential provisioning information from public
cloud environments, and seamless updates for cloud libraries or agents
on PAN-OS.

 
 The VM-Series plugin does not manage capabilities that are
common to both VM-Series firewalls and hardware-based firewalls.
For example, VM Monitoring is not part of the VM-Series plugin because
it is a core PAN-OS feature that helps you enforce policy consistently
on your virtual machine workloads from both VM-Series firewalls
and hardware-based firewalls.

 
 The VM-Series plugin does not manage [Panorama plugins](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-plugins.html).
For the difference between the VM-Series plugin and Panorama plugins,
see [VM-Series Plugin and Panorama
Plugins](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-plugins/plugins-types.html).

The VM-Series plugin is a built-in component that can be upgraded
or downgraded, but not removed. Each PAN-OS release includes a specific
VM-Series plugin version that corresponds to the PAN-OS software
version. When you downgrade to an earlier PAN-OS software version,
the plugin version is downgraded to the version compatible with
the PAN-OS version. You can upgrade or downgrade the VM-Series plugin locally
on the virtual firewall, or manage the plugin version centrally
from Panorama. 

To enable Panorama to manage the VM-Series plugin version itself,
or cloud-specific metrics publishing your managed firewalls, you
must manually install the VM-Series plugin on Panorama as described
in [Panorama Plugins](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-plugins.html).

- [Configure the VM-Series Plugin on the Firewall](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/about-the-vm-series-firewall/vm-series-plugin/configure-the-vm-series-plugin-on-the-firewall.html#id4a8e9155-ddef-4bd3-a786-c42839a5530b)

- [Upgrade the VM-Series Plugin](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/about-the-vm-series-firewall/vm-series-plugin/upgrade-the-vm-series-plugin.html#idb1ae3965-dc57-4444-aae1-2a798d5a455a)