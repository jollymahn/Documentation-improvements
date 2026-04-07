<!-- Source: https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/panorama-plugins -->
<!-- Fetched: 2026-03-31T18:05:00.274151+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Panorama Plugins



 



 Panorama supports an extensible plugin architecture. 



 The Panorama extensible plugin architecture enables
support for third-party integration plugins, such as VMware NSX,
and other Palo Alto Networks products, such as the GlobalProtect
cloud service. With this modular architecture, you can take advantage
of new capabilities without waiting for a new PAN-OS version.

You can also configure the VM-Series plugin from Panorama. The
VM-Series plugin is a single plugin that enables integration with
public cloud environments such as Google Cloud Platform (GCP), Azure,
AWS and private cloud hypervisors such as KVM, ESXi and others.
The VM-Series plugin enables you to publish metrics from VM-Series
firewalls deployed in public clouds. You can use Panorama to configure the
VM-Series plugin settings for public clouds and push your configuration
to your managed firewalls.

(PAN-OS 12.1.2 and later releases)
 Panorama Plugin Bundling simplifies the upgrade process by automatically handling the
 complex task of managing version compatibility between your PAN-OS software and plugins.
 Previously, you had to manually compare PAN-OS and plugin versions, which often led to
 version mismatches. These conflicts lead to network outages and critical configurations,
 such as VPN pre-shared keys and routing commands, being overwritten. 

By bundling the plugins with the base image,
 this feature automatically ensures version compatibility and eliminates the risk of
 version mismatches, ensuring your configurations are preserved. When you upgrade, the
 system automatically downloads compatible plugins with the base image. This ensures that
 you no longer have to manually download compatible plugin versions, and you can directly
 install the plugins you need. For more information about compatible plugins, see the
 [Compatibility Matrix](https://docs.paloaltonetworks.com/compatibility-matrix/reference/panorama/plugins).

The Plugins interface offers a single,
 easy-to-use location to manage all the bundled plugins. The interface intelligently
 displays and sorts plugins, allowing you to simply install plugins as required. If you
 have the appropriate license, you can manage Cloud Services in a separate, dedicated
 section. For more information about the Plugins interface, see [Panorama>Plugins](https://docs.paloaltonetworks.com/pan-os/11-2/pan-os-web-interface-help/panorama-web-interface/panorama-plugins).

- [About
Panorama Plugins](/content/techdocs/en_US/panorama/11-1/panorama-admin/panorama-plugins/about-panorama-plugins.html#id181P8K0F0LT)
- [VM-Series Plugin and Panorama Plugins](/content/techdocs/en_US/panorama/11-1/panorama-admin/panorama-plugins/plugins-types.html#id7f814955-5e00-4c52-a9b4-4e77a140b2d1)
- [Endpoint Monitoring for Cisco TrustSec](/content/techdocs/en_US/panorama/11-1/panorama-admin/panorama-plugins/endpoint-monitoring-for-cisco-trustsec.html)