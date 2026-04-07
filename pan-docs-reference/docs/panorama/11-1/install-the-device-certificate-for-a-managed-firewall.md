<!-- Source: https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/install-the-device-certificate-for-managed-firewalls/install-the-device-certificate-for-a-managed-firewall -->
<!-- Fetched: 2026-03-31T18:05:09.052430+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags:  -->

# Install the Device Certificate for a Managed Firewall



 



 Install the device certificate for selected managed firewalls from the Panorama™
 management server. 



 
 






















 

- 

- 
- 
- 
- 

- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW (Managed by Panorama) | Device management licenseSupport licenseOutbound internet accessCustomer Support Portal (CSP) account with one of the
                                            following user roles:Super User, Standard User, Limited User, Threat
                                            Researcher, AutoFocus Trial Role, Group Super User,
                                            Group Standard User, Group Limited User, Group Threat
                                            Researcher, Authorized Support Center (ASC) User, and
                                            ASC Full Service User.Panorama superuser role |



 Select and install the device certificate for managed firewalls from the Panorama
 management server to use one or more [cloud services](https://docs.paloaltonetworks.com/compatibility-matrix/panorama/device-certificate-for-a-palo-alto-networks-cloud-service). You only need to install a
 device certificate once. The device certificate has a 90-day lifetime. The firewall
 reinstalls the device certificate 15 days before the certificate expires. In the
 event the firewall is unable to reinstall the device certificate on its own, you may
 need to manually [restore an expired device certificate](/content/techdocs/en_US/panorama/11-1/panorama-admin/troubleshooting/restore-an-expired-device-certificate.html).

 To successfully install the device certificate on a firewall, the firewall must have
 outbound internet access and the following Fully Qualified Domain Names (FQDN) and
 ports must be allowed on your network in order to reach to the CSP. Additionally,
 the managed firewall must belong to the same CSP account as Panorama in order to
 generate the One Time Password (OTP) used to install the device certificate. 

 






















 

- 

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
| https://api.paloaltonetworks.comhttp://apitrusted.paloaltonetworks.comhttps://certificatetrusted.paloaltonetworks.comhttps://certificate.paloaltonetworks.com | TCP 443 |
| *.gpcloudservice.com | TCP 444 and TCP 443 |



 
 
 The following Palo Alto Networks Next-Generation firewall models install the
 device certificate when they first connect to the Palo Alto Networks CSP during
 the initial registration process. You do not need to manually install the device
 certificate for these firewall models.

- PA-400 Series firewalls

- PA-1400 Series firewalls

- PA-3400 Series firewalls

- PA-5400 Series firewalls

- PA-5450 firewall

1.  [Log in to the Panorama Web Interface](/content/techdocs/en_US/panorama/11-1/panorama-admin/set-up-panorama/access-and-navigate-panorama-management-interfaces/log-in-to-the-panorama-web-interface.html#id60bb9ed6-4859-441a-8c86-f2a81f2cb38e) as a Superuser.
 A Panorama admin with [Superuser access privileges](/content/techdocs/en_US/panorama/11-1/panorama-admin/panorama-overview/role-based-access-control/administrative-roles.html) is
 required to generate OTP Request Token and apply the OTP used to install the
 device certificate on a managed firewall.

 

2.  (Best Practices) Configure the Network Time Protocol (NTP) server for
 Panorama.
 An NTP server is required to validate the device certification expiration
 date, ensure the device certificate does not expire early or become
 invalid.

 

  1.  Select PanoramaSetupServices.
  2.  Select NTP and enter the hostname or IP address
 of the Primary NTP Server.
  3.  (Optional) Enter a the hostname or IP address of the
 Secondary NTP Server.
  4.  (Optional) To authenticate time updates from the NTP
 server(s), for Authentication Type, select one of
 the following for each server.
 
    - **None** (default)—Disables NTP authentication.

    - **Symmetric Key**—Firewall uses symmetric key exchange
 (shared secrets) to authenticate time updates.

      - **Key ID**—Enter the Key ID (1-65534)

      - **Algorithm**—Select the algorithm to use in NTP
 authentication (MDS or
 SHA1) 

 

  5.  Click OK to save your configuration
 changes.
  6.  Select Commit and Commit to
 Panorama.

3.  Configure the Network Time Protocol (NTP) server for your firewalls.
 An NTP server is required to validate the device certification expiration
 date, ensure the device certificate does not expire early or become
 invalid.

 

  1.  Select DeviceSetupServices and select the Template.
  2.  Select one of the following depending on your platform:
 
    - For multi-virtual system platforms, select
 Global and edit the Services
 section.
    - For single virtual system platforms, edit the Services
 section.

 

  3.  Select NTP and enter the hostname or IP address
 of the Primary NTP Server.
  4.  (Optional) Enter a the hostname or IP address of the
 Secondary NTP Server.
  5.  (Optional) To authenticate time updates from the NTP
 server(s), for Authentication Type, select one of
 the following for each server.
 
    - **None** (default)—Disables NTP authentication.

    - **Symmetric Key**—Firewall uses symmetric key exchange
 (shared secrets) to authenticate time updates.

      - **Key ID**—Enter the Key ID (1-65534)

      - **Algorithm**—Select the algorithm to use in NTP
 authentication (MDS or
 SHA1) 

 

  6.  Click OK to save your configuration
 changes.
  7.  Select Commit and Commit and
 Push your configuration changes to your managed
 firewalls.

4.  Generate the OTP Request Token on Panorama.
 The OTP Request Token generated on Panorama is used to generate the OTP
 required to install the device certificate on a managed firewall.

 

  1.  Select PanoramaManaged DevicesSummary.
  2.  Select one or more managed firewalls that do not have a device
 certificate installed.
  3.  Select Request OTP From CSPCustom selected devices.
  4.  Copy the entire output in the OTP Request Token
 field.

5.  Generate the One Time Password (OTP) for managed firewalls. 
 
 
 An OTP lifetime is 60 minutes and expires if not used within the 60
 minute lifetime.

Firewall may only attempt to retrieve the OTP from the CSP one time. If
 the firewall fails for any reason to fetch the OTP, the OTP expires and
 you must generate a new OTP.

 

  1.  Log in to the [Customer Support Portal](https://support.paloaltonetworks.com/) with a
 user role that has permission to generate an OTP.
  2.  Select ProductsDevice Certificates and Generate OTP.
  3.  For the Device Type, select Generate
 OTP for Panorama managed firewalls and click
 Next.
  4.  Paste the OTP request you copied in the previous step
and Generate OTP.
  5.  Click Done and wait a few minutes for the OTP to
 successfully generate.
  6.  View OTP History.
  7.  In the Current One Time Password History, copy
 or download the OTP
  8.  Copy to Clipboard or Download the
OTP.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

6.  Install the device certificate on managed firewalls.
 The managed firewall must have an outbound internet connection to
 successfully install the device certificate. After you upload the OTP from
 Panorama, the managed firewall connects to the Palo Alto Networks CSP to
 install the device certificate.

 

  1.  [Log in to the Panorama web
                                interface](/content/techdocs/en_US/panorama/11-1/panorama-admin/set-up-panorama/access-and-navigate-panorama-management-interfaces/log-in-to-the-panorama-web-interface.html) as a Superuser user.
  2.  Select PanoramaManaged DevicesSummary and Upload OTP.
  3.  Paste the OTP you generated and Upload.
 
 
 You must still copy and paste the OTP generated from the Palo
 Alto Networks CSP even if you downloaded the OTP in the previous
 step. Uploading the file containing the OTP is not
 supported.

 

7.  (WildFire and Advanced WildFire) [Log in to the firewall CLI](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli) and refresh
 the firewall settings to establish a connection to the Advanced WildFire cloud
 with the updated device certificate.
 Repeat this step for each managed firewall with an activate WildFire or
 Advanced WildFire subscription that is actively communicating with the
 Advanced WildFire cloud service.

 
```
admin>request wildfire registration channel public

```

 

8.  Verify that the Device Certificate column displays as
 Valid and that the Device
 Certificate Expiry Date displays an expiration date.