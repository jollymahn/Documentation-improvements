<!-- Source: https://docs.paloaltonetworks.com/ngfw/administration/certificate-management/certificate-deployment/install-device-certificate -->
<!-- Fetched: 2026-03-31T20:05:41.457421+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags:  -->

# Install or Restore a Device Certificate

 

 
 
 
 
 
 

 

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
                            
                                    Import a Certificate and Private Key](/content/techdocs/en_US/ngfw/administration/certificate-management/certificate-deployment/import-certificate-and-private-key.html)
 

 
 

**[Next
                                
                                    Restore an Expired Device Certificate](/content/techdocs/en_US/ngfw/administration/certificate-management/certificate-deployment/restore-expired-device-certificate.html)
 

 

---

 
 
 















 

# Install or Restore a Device Certificate



 



 Learn how to install a device certificate on your NGFW to authenticate and secure
 communication with cloud services.



 
 






















 

- 

- 
- 
- 

- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW (Managed by PAN-OS or Panorama) | Support licenseOutbound internet accessCustomer Support Portal (CSP) account with one of the
                                            following user roles:Super User, Standard User, Limited User, Threat
                                            Researcher, AutoFocus Trial Role, Group Super User,
                                            Group Standard User, Group Limited User, Group Threat
                                            Researcher, Authorized Support Center (ASC) User, and
                                            ASC Full Service User.Superuser privileges to the firewall |



 You must install the device certificate on your Next-Generation Firewall (NGFW) to
 use one or more [cloud services](https://docs.paloaltonetworks.com/compatibility-matrix/panorama/device-certificate-for-a-palo-alto-networks-cloud-service). You only need to install a
 device certificate once. The device certificate has a 90-day lifetime. The firewall
 reinstalls the device certificate 15 days before the certificate expires.

 For successful installation, the firewall must have outbound internet access and the
 following Fully Qualified Domain Names (FQDN) and ports must be allowed on your
 network to reach to the Customer Support Portal.

 For Panorama managed firewalls, you can [install the device certificate for managed
                    firewalls](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/install-the-device-certificate-for-managed-firewalls) from the Panorama management server. This enables you to
 install the device certificate for multiple managed firewalls at once.

 
 






















 

- 

- 

- 

- 

- 

- 

- 

| FQDN | Ports |
| --- | --- |
| http://ocsp.paloaltonetworks.comhttp://crl.paloaltonetworks.comhttp://ocsp.godaddy.com | TCP 80 |
| https://api.paloaltonetworks.comhttps://apitrusted.paloaltonetworks.comhttps://certificatetrusted.paloaltonetworks.comhttps://certificate.paloaltonetworks.com | TCP 443 |



 
 
 The following Palo Alto Networks NGFW models automatically install the device
 certificate when they first connect to the Customer Support Portal during the
 initial registration process. You don’t need to manually install the device
 certificate for these models:

- PA-400 Series firewalls

- PA-500 Series firewalls

- PA-1400 Series firewalls

- PA-3400 Series firewalls

- PA-5400 Series firewalls

- PA-5450 firewall

- PA-5500 Series firewalls

- PA-7500 Series firewalls

1.  Generate a one-time password (OTP).
 
 
 An OTP lifetime is 60 minutes and expires if not used within the
 60-minute lifetime.

The firewall may only attempt to retrieve the OTP from the Customer
 Support Portal one time. If it fails to fetch the OTP for any reason,
 the OTP expires and you must generate a new OTP.

 

  1.  Log in to the [Customer Support Portal](https://support.paloaltonetworks.com/) with a
 user role that has permission to generate an OTP.
  2.  Select ProductsDevice Certificates, and then click Generate
 OTP.
  3.  For the Device Type, select Generate
 OTP for a Next-Gen Firewall (PanOS), and then click
 Next.
  4.  Select your PAN-OS Device serial number, and
 then Generate OTP.
  5.  Download OTP or Copy to
 Clipboard.

 
 
 

 
 

2.  [Log in to the firewall web interface](/content/techdocs/en_US/ngfw/administration/firewall-administration/launch-the-web-interface.html) as a
 Superuser.
 An admin with [Superuser access
                            privileges](/content/techdocs/en_US/ngfw/administration/firewall-administration/manage-firewall-administrators.html#id34cb14e2-7c4e-4b8f-948c-ba42a049b7c5_concept-w12_d5f_fgc) is required to apply the OTP used to install the
 device certificate.

 

3.  Configure the Network Time Protocol (NTP) server.
 An NTP server is required to validate the device certification expiration
 date and ensure the device certificate does not expire early or become
 invalid.

 

  1.  Select DeviceSetupServices and edit the Services section.
  2.  Select NTP and enter the hostname or IP address
 of the Primary NTP Server.
  3.  (Optional) Enter the hostname or IP address of the
 Secondary NTP Server.
  4.  (Optional) To authenticate time updates from the NTP servers,
 for Authentication Type, select one of the
 following for each server:
 
    - **None** (default)—Disables NTP authentication.

    - **Symmetric Key**—Firewall uses symmetric key exchange
 (shared secrets) to authenticate time updates.

      - **Key ID**—Enter the Key ID (1-65534)

      - **Algorithm**—Select an algorithm to use for NTP
 authentication: MD5,
 SHA1, (PAN-OS 12.1.2
 & later) SHA256,
 or SHA512.

    - Autokey—Firewall uses autokey (public
 key cryptography) to authenticate time updates.

 

  5.  Click OK to save your changes.
  6.  Commit your changes.

4.  Select DeviceSetupManagementDevice Certificate and Get certificate.
 
 
 You can also install the device certificate from the [firewall CLI](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli) using the
 command:

admin>request certificate fetch
 otp <otp_value>

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

5.  Paste the One-time Password you generated and click
 OK.
6.  Your next-generation firewall successfully retrieves and installs the
 certificate.
 You may need to refresh the page to verify that device certificate
 installation was successful.

 

7.  (WildFire and Advanced WildFire) [Log in to the firewall CLI](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli) and refresh
 the firewall settings to establish a connection to the Advanced WildFire cloud
 with the updated device certificate.
 
```
admin>request wildfire registration channel public
```

 



 















 

## Restore an Expired Device Certificate



 
 The device certificate installed on your firewall has a 90-day lifetime. A
 firewall with the device certificate installed automatically attempts to
 reinstall the device certificate 15 days before the certificate expires.
 However, reinstallation can fail for multiple reasons, including network
 connectivity issues. When a device certificate expires, the
 Current Device Certificate Status displays
 Expired. If this happens, you can manually
 reinstall the device certificate.

 

1.  [Log in to the firewall web
                            interface](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/firewall-administration/use-the-web-interface/launch-the-web-interface).
2.  Verify that the device certificate has expired.
 Select DeviceSetupManagement, and then check that the Current Device
 Certificate Status is
 Expired.

 
 
 

 
 

3.  [Install a device certificate](/content/techdocs/en_US/ngfw/administration/certificate-management/certificate-deployment/install-device-certificate.html).
 
 
 If the request certificate fetch otp
 <otp_value> command isn’t available, it means the
 firewall is a Trusted Platform Module (TPM) device.

To restore the device certificate for a TPM device, run the following
 command:

request certificate
 fetch