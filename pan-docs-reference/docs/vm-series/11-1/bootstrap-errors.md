<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-errors -->
<!-- Fetched: 2026-03-31T18:05:03.453806+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Bootstrap
Errors



 



 If you receive an error message during the bootstrapping
process, refer to the following table for details.
























 

- 

- 

| Error message (Severity) | Reasons |
| --- | --- |
| Boot image error (high) | No external device was detected
with the bootstrap package.OrA critical
error happened while booting from the image on the external device.
The bootstrap process was aborted. |
| No bootstrap config file on external device
(high) | The external device did not have the bootstrap
configuration file. |
| Bad or no parameters for mandatory networking information
in the bootstrap config file (high) | The networking parameters required for bootstrapping
were either incorrect or missing. The error message lists the value—IP
address, netmask, default gateway—that caused the bootstrap failure. |
| Failed to install license key for file <license-key-filename> (high) | The license key could not be applied. This
error indicates that the license key used was invalid. The output
includes the name of the license key that could not be applied. |
| Failed to install license key using authcode <authcode>
(high) | The license auth code could not be applied.
This error indicates that the license auth code used was invalid.
The output includes the name of the authcode that could not be applied. |
| Failed content update commits (high) | The content updates were not successfully
applied. |
| USB media prepared successfully using given bundle
(informational) | The bootstrap image has been successfully
complied on the USB flash device. <username>: Successfully prepared
the USB using bundle <bundlename> |
| Successful bootstrap (informational) | The firewall was successfully provisioned
with the bootstrap configuration file. The output includes the license
keys installed and the filename of the bootstrap configuration.
On the VM-Series firewalls only, the PAN-OS version and content update
version are also displayed. |


Read about the [Bootstrap Package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-package.html#id88dce8d3-3665-4794-b7ed-0fd47581ebd2) and
how to [Prepare the Bootstrap Package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package.html#id5575318c-1de8-497a-960a-1d7417feefa6).