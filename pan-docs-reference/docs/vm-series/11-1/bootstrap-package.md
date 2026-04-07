<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-package -->
<!-- Fetched: 2026-03-31T18:04:49.196882+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Bootstrap Package



 



 The bootstrap process is initiated only on first boot
when the firewall is in a factory default state. 

- Bootstrap Package Structure
- Bootstrap Package Delivery


 















 

## Bootstrap Package Structure



 The bootstrap package must include the /config, /license, /software,
and /content folders, even if they are empty.
The /plugins folder is optional. For an example,
see [Prepare the Bootstrap Package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package.html#id5575318c-1de8-497a-960a-1d7417feefa6).

- **/config folder**—Contains the configuration files.
The folder can hold two files: init-cfg.txt and
the bootstrap.xml. For details, see [Bootstrap
Configuration Files](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-configuration-files.html#id37d59976-16c6-4c75-af8a-61f46e690d65).

 
 If you intend to pre-register
VM-Series firewalls with Panorama with bootstrapping, you must generate
a VM auth key on Panorama and include the generated key in the init-cfg.txt file.
See [Generate
the VM Auth Key on Panorama](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/generate-the-vm-auth-key-on-panorama.html#id6507055f-4230-47ac-adc9-cd947bfd83c4).

- **/license folder**—Contains the license keys or auth
codes for the licenses and subscriptions that you intend to activate
on the firewalls. If the firewall does not have Internet connectivity,
you must either manually obtain the license keys from the [Palo Alto Networks Support](https://support.paloaltonetworks.com/support) portal
or use the [Licensing
API](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/licensing-api.html#id0873c753-02bd-4371-9e6a-2b35cfc0a44b) to obtain the keys and then save each key in this folder.
For details, see [Prepare
the Licenses for Bootstrapping](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-licenses-for-bootstrapping.html#idb9fa0ce2-b855-435b-a9b4-5ab7b61a8353).

 
 You must include
an auth code bundle instead of individual auth codes so that the
firewall or orchestration service can simultaneously fetch all license keys
associated with a firewall. If you use individual auth codes instead
of a bundle, the firewall will retrieve only the license key for
the first auth code included in the file.

- **/software folder**—Contains the software images required
to upgrade a newly provisioned VM-Series firewall to the desired
PAN-OS version for your network. You must include all intermediate
software versions between the current version and the final PAN-OS
software version to which you want to upgrade the VM-Series firewall.
Refer to [VM-Series Firewall Hypervisor
Support](https://docs.paloaltonetworks.com/compatibility-matrix/vm-series-firewalls/vms-series-hypervisor-support.html) in the Compatibility Matrix.

- **/content folder**—Contains the application and threat
updates, WildFire updates, and the BrightCloud URL filtering database
for the valid subscriptions on the VM-Series firewall. You must
include the minimum content versions required for the desired PAN-OS
version. If you do not have the minimum required content version
associated with the PAN-OS version, the VM-Series firewall cannot
complete the software upgrade. 

- **/plugins folder**—Optional folder contains
a single [VM-Series plugin](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/about-the-vm-series-firewall/vm-series-plugin.html#id729e85bb-240c-42d5-af95-852a95b62c2a) image.

- **/ace folder**—Optional folder contains an [App-ID Cloud Engine (ACE)](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/app-id/cloud-based-app-id-service) content
 package. The VM-Series installs the version of the Cloud App-ID Catalog
 included in the content package upon first boot. You must download the
 content package from the [Customer Support
                            Portal](https://support.paloaltonetworks.com/) and add it to the **ace** folder. To download the
 content package, complete the following steps. 
  1. Log in to the [Customer Support
                                Portal](https://support.paloaltonetworks.com/).
  2. Select UpdatesDynamic Updates.
  3. Select Bootstrap files for VM Flex with SaaS
 Subscription from the Content Type drop-down.
  4. Choose a content package and click
 Download.








 















 

## Bootstrap Package Delivery



 The file type used to deliver the bootstrap package
to the VM-Series firewall varies based on your hypervisor. Use the
table below to determine the file type your hypervisor or cloud
vendor supports.
























 

| External Device for
Bootstrapping (Bootstrap Package Format) | AWS | Azure | ESXi | Google | Hyper-V | KVM |
| --- | --- | --- | --- | --- | --- | --- |
| CD-ROM (ISO image) | — | — | Yes | — | Yes | Yes |
| Block Storage Device | — | — | Yes | — | Yes | Yes |
| Storage Account | — | Yes | — | — | — | — |
| Storage Bucket | Yes | — | — | Yes | — | — |


When you attach the storage device to the firewall, the firewall
scans for a bootstrap package and, if one exists, the firewall uses
the settings defined in the bootstrap package. 

If you have included a Panorama server IP address in the file,
the firewall connects with Panorama. If the firewall has Internet
connectivity, it contacts the licensing server to update the UUID
and obtain the license keys and subscriptions. The firewall is then
added as an asset in the [Palo Alto Networks Support](https://support.paloaltonetworks.com/Support/Index) portal.
If the firewall does not have Internet connectivity, it either uses
the license keys you included in the bootstrap package, or it connects
to Panorama to retrieve the appropriate licenses and deploys them
to the managed firewalls.