<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/use-panorama-based-software-firewall-license-management -->
<!-- Fetched: 2026-03-31T18:04:40.489782+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Use Panorama-Based Software Firewall License Management



 



 Learn about how to use the Panorama Software Firewall
License plugin to license VM-Series firewalls.



 The Panorama Software Firewall License plugin
allows you to automatically license a VM-Series firewall when it
connects to Panorama. If your VM-Series firewalls are located in
the perimeter of your deployment and do not have connectivity to
the Palo Alto Networks licensing server, the Software Firewall License
plugin simplifies the license activation process by using Panorama
to license the VM-Series firewall. 

Additionally, the Software
Firewall License plugin simplifies the license activation and deactivation
of VM-Series firewalls in environments that use auto-scaling and
automation to deploy and delete firewalls to address changes in
the cloud.

 
 Pay-as-you-go (PAYG) licenses are not supported
for use with this plugin.

 
 Do not use the Software
Firewall License plugin to license the VM-Series firewall for VMware
NSX. The Panorama plugin for VMware NSX automatically licenses VM-Series
firewalls deployed in NSX and NSX-T

.Also, do not use this
plugin to license firewalls deployed in device groups that include
instances of the VM-Series firewall deployed in NSX-T.

To
install the Panorama Software Firewall License plugin, you must
be using Panorama 10.0.0 or later and VM-Series plugin 2.0.4 or
later. Your VM-Series firewalls must be running PAN-OS 9.1.0 or
later. 

 
 The VM-Series firewall for Azure requires VM-Series
plugin 2.0.8 or later.

If you have a standalone Panorama
or two Panorama appliances installed in an HA pair with multiple
plugins installed, plugins might not receive updated IP-tag information
if one or more of the plugins is not configured. This occurs because
Panorama will not forward IP-tag information to unconfigured plugins.
Additionally, this issue can occur if one or more of the Panorama
plugins is not in the Registered or Success state (positive state
differs on each plugin). Ensure that your plugins are in the positive
state before continuing or executing the commands described below.

If
you encounter this issue, there are two workarounds:

- Uninstall
the unconfigured plugin or plugins. It is recommended that you do
not install a plugin that you do not plan to configure right away

- You can use the following commands to work around this issue.
Execute the following command for each unconfigured plugin on each Panorama
instance to prevent Panorama from waiting to send updates. If you
do not, your firewalls may lose some IP-tag information. 

request plugins dau plugin-name <plugin-name> unblock-device-push yesYou
can cancel this command by executing:

request plugins dau plugin-name <plugin-name> unblock-device-push no
The
commands described are not persistent across reboots and must be
used again for any subsequent reboots. For Panorama in HA pair, the
commands must be executed on each Panorama.

1.  Install the Software Firewall License Plugin for
Panorama.
  1.  Log in to the Panorama web interface.
  2.  Select PanoramaPlugins.
  3.  Click Check Now to get the
list of available plugins.
  4.  Search for sw_fw_license to locate the plugin.
  5.  Select Download and Install the
Software Licensing plugin.
After you successfully install, Panorama refreshes and
the Software Licensing plugin displays on the Panorama tab. 

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

2.  Configure a Bootstrap Definition.
  1.  Select PanoramaSW Firewall LicenseBootstrap Definitions.
  2.  Click Add.
  3.  Enter a descriptive Name to
identify the Bootstrap Definition.
  4.  (Optional) Enter a Description of
the Bootstrap Definition.
  5.  Enter the Auth Code that Panorama
will use to license the VM-Series firewall when it connects to Panorama.
  6.  Click OK.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

3.  Configure a License Manager.
  1.  Select PanoramaSW Firewall LicenseLicense Managers.
  2.  Click Add.
  3.  Enter a descriptive Name to
identify the License Manager.
  4.  (Optional) Enter a Description of
the License Manager.
  5.  Select a Device Group from
the drop-down. When a VM-Series firewall bootstrapped using the
license manager connects to Panorama, it is placed in the specified
device group.
  6.  Select a Template Stack from
the drop-down. When a VM-Series firewall bootstrapped using the
license manager connects to Panorama, it is placed in the specified
template Stack.
  7.  In the Auto Deactivate field,
specify the amount of time, in hours, that Panorama waits before
deactivating the license of a disconnected VM-Series firewall. When
you select Never, Panorama does not deactivate
a disconnected VM-Series firewall. Auto Deactivate is set to Never by
default. You can set the deactivation time, in hours, from one to
24.Before deactivating, set the API key using: 

request license api-key set key <key>

 
 When
an Auto Deactivate interval is configured, the plugin might also
deactivate the license of stopped VM-Series firewalls in addition
to disconnected firewalls. 

4.  (Optional) Create an init-cfg.txt file
for [bootstrap the VM-Series
firewall](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file.html#id8770fd72-81ea-48b6-b747-d0274f37860b). After configuring a license manager, you can copy
and paste bootstrap parameters generated by Panorama when deploy
your VM-Series firewalls. Depending on your deployment, the parameters displayed
might be a subset of those shown in the image below. For example,
if your Panorama appliance is deployed in a public cloud, the bootstrap
parameters will not include the public IP address for Panorama.
In that case, you must manually enter the public IP address in the init-cfg.txt file.
Panorama will always generate the auth-key and plugin-op-commands=panorama-licensing-mode-on for
use in your init-cfg.txt.The auth key displayed here is generated by Panorama and
used to authenticate the VM-Series firewall connection to Panorama.
Additionally, this auth key is used instead of the VM auth key that
you might [generate on Panorama](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/bootstrap-the-vm-series-firewall/generate-the-vm-auth-key-on-panorama.html) and
add to your init-cfg.txt file.

 
 If you use the auth key
displayed here in your init-cfg.txt file, do not use a manually
generated VM auth key. 

  1.  Select PanoramaSW Firewall LicenseLicense Managers.
  2.  In the Action column of a given license manager, click Show
Bootstrap Parameters.
  3.  Copy the displayed information and paste it into a
text editor to create an init-cfg.txt file
for bootstrapping. 
  4.  Click Close when finished.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

5.  (Optional) View and deactivate a managed VM-Series
firewall. From the Show Devices dialogue,
you can view the devices associated with a given license manager.
You can view the name, serial number, management IP address, connection
status, and amount of time Panorama waits to deactivate a disconnected
firewall. Additionally, you can manually deactivate the license
of managed VM-Series firewall.
  1.  Select PanoramaSW Firewall LicenseLicense Managers.
  2.  In the Action column of a given license manager, click Show
Devices.
  3.  To manually deactivate a connected or disconnected
(but not yet deactivated) managed VM-Series firewall, select a one
or more listed VM-Series firewalls and click Deactivate.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

6.  (Optional) Verify that Panorama has completed
the necessary API calls to license connected firewalls.
  1.  Log in to the Panorama command line interface.
  2.  Execute the following command.show plugins sw_fw_license panorama-api-requests