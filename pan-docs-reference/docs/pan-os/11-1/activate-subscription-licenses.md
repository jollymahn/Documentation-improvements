<!-- Source: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/subscriptions/activate-subscription-licenses -->
<!-- Fetched: 2026-03-31T20:05:45.240058+00:00 -->
<!-- Project: ngfw -->
<!-- Tags: licenses, subscriptions -->

# Activate Subscription Licenses

 

 
 
 
 
 
 

 

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
                            
                                    NGFW Compatible Subscriptions](/content/techdocs/en_US/ngfw/getting-started/ngfw-compatible-subscriptions.html)
 

 
 

**[Next
                                
                                    What Happens When Licenses Expire?](/content/techdocs/en_US/ngfw/getting-started/ngfw-compatible-subscriptions/what-happens-when-licenses-expire.html)
 

 

---

 
 
 















 

# Activate Subscription Licenses



 Learn about how to activate subscriptions and licenses on your NGFW.



 
 






















 

- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW |  |



 Follow these steps to activate a new license on the NGFW. 

 The Decryption Mirroring feature requires you to activate a free license to unlock
 feature functionality. For those features, you should instead follow the steps to
 activate a free license for Decryption features.

 

1.  Install the device certificate on your NGFW.
 
  - [Install the device
                                    certificate](https://docs.paloaltonetworks.com/ngfw/administration/certificate-management/certificate-deployment/install-device-certificate) for standalone NGFW

  - [Install the device
                                    certificate](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/install-the-device-certificate-for-managed-firewalls) for NGFW (Managed by Panorama or Strata Cloud Manager)

 Palo Alto Networks uses the device certificate to authentication the NGFW and allows the NGFW to connect to [cloud services](https://docs.paloaltonetworks.com/compatibility-matrix/reference/panorama/device-certificate-for-a-palo-alto-networks-cloud-service) such as Advanced WildFire, Advanced Threat Prevention, Advanced Advanced DNS Security, Advanced URL Filtering, and more. This is required to
 successfully use any Palo Alto Networks cloud service.

 

2.  Locate the activation codes for the licenses you purchased.
 When you purchased your subscriptions you should have received an email from
 Palo Alto Networks customer service listing the activation code associated
 with each subscription. If you cannot locate this email, contact [Customer Support](https://support.paloaltonetworks.com/Support/Index) to obtain your activation codes
 before you proceed.

 

3.  Activate your Support license.
 You will not be able to update your PAN-OS software if you do not have a
 valid Support license.

 

  1.  Log in to the web interface and then select DeviceSupport.
  2.  Click Activate support using authorization
 code.
  3.  Enter your Authorization Code and then click
 OK.

4.  Activate each license you purchased.
 Select DeviceLicenses and then activate your licenses and subscriptions in one of
 the following ways:

 
  - Retrieve license keys from license server—Use
 this option if you activated your license on the [Customer Support](https://support.paloaltonetworks.com/Support/Index) portal.
  - Activate feature using authorization code—Use
 this option to enable purchased subscriptions using an authorization
 code for licenses that have not been previously activated on the support
 portal. When prompted, enter the Authorization
 Code and then click OK.
  - Manually upload license key—Use this option if
 your NGFW does not have connectivity to the [Palo Alto Networks Customer Support
                                Portal](https://support.paloaltonetworks.com/Support/Index). In this case, you must download a license key file
 from the support site on an internet-connected computer and then upload
 to the NGFW.

 
 
 To automate activation using the Customer Support Portal API, see the
 process to [Activate Licenses](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/licensing-api/use-the-licensing-api/activate-licenses.html). This
 process works for both the hardware and VM-Series NGFWs.

 

5.  Verify that the license is successfully activated
 On the DeviceLicenses page, verify that the license is successfully activated. For
 example, after activating the WildFire license, you should see that the
 license is valid:

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

6.  (WildFire, Advanced URL Filtering, and DNS Security subscriptions
 only) Commit configuration changes to complete
 subscription activation.
 After activating a WildFire, Advanced URL Filtering, or DNS Security
 subscription license, a commit is required for the NGFW to begin processing
 their corresponding traffic and data types based on the security profile
 configurations. You should:

 
  - Commit any pending changes. If you do not have pending changes, which
 prevents you from committing any configuration updates, you can: issue a
 commit force command through the CLI or make an update that writes to
 the candidate configuration, which enables the commit option.Use the
 following CLI configuration mode command to initiate a commit
 force:

```
username@hostname> configure 
Entering configuration mode 
[edit] 
username@hostname# commit force
```

 
 A commit force bypasses some of the validation checks that
 normally occur with a normal commit operation. Make sure your
 configuration is valid and is semantically and syntactically
 correct before issuing a commit force update.

  - WildFire only Check that the [WildFire Analysis profile
                                rules](https://docs.paloaltonetworks.com/advanced-wildfire/administration/configure-advanced-wildfire-analysis/forward-files-for-advanced-wildfire-analysis.html) include the advanced file types that are now supported
 with the WildFire subscription. If no change to any of the rules is
 required, make a minor edit to a rule description and perform a
 commit.