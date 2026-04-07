<!-- Source: https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/manage-the-cloud-identity-engine/cloud-identity-engine-user-context -->
<!-- Fetched: 2026-04-01T01:59:08.406318+00:00 -->
<!-- Project: scm -->
<!-- Tags: cloud-identity, user-context -->

# Cloud Identity Engine User Context

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Identity Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Activation & Onboarding
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Cloud Identity Engine
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Help
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Release Notes
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 

 

 

 

 

 
 
 
---

 
 
 **

[Previous
                            
                                    Configure the Cloud Identity Engine as a Mapping Source (SCM)](/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/configure-the-cloud-identity-engine-as-a-mapping-source/configure-the-cloud-identity-engine-as-a-mapping-source-scm.html)
 

 
 

**[Next
                                
                                    Cloud Identity User Context (PAN-OS)](/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/cloud-identity-engine-user-context/cloud-identity-user-cointext-pan-os.html)
 

 

---

 
 
 















 

# Cloud Identity Engine User Context



 
 






















 

- 
- 
[here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFWPrisma Access | The Cloud Identity Engine service is free; however, the
                                enforcement points utilizing directory data may require specific
                                licenses. Click  for more
                                information. |



 As large enterprise networks continue to become increasingly distributed across
 cities, regions, and countries, enforcing least-privilege user access becomes
 increasingly challenging, especially as scale increases. User Context for the Cloud
 Identity Engine provides simplified granular control over the data that is shared
 across your security devices. It provides administrators with the flexibility to
 specify the data types (such as mappings and quarantine lists) each device sends and
 receives. 

 The simplified deployment of User Context for information such as user mappings and
 tags minimizes time to enforcement. Centralizing visibility for users, tags, and
 mappings makes it easier to segment the data types based on user access needs. This
 method also increases scalability for Virtual Desktop users (VDI) using the Terminal
 Server agent. 

 To enforce policy, User Context provides IP address-to-username[mappings](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/user-id/user-id-concepts/user-mapping), IP port to username mappings,
 user [tags](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/use-tags-to-group-and-visually-distinguish-objects) IP address tags, Host IDs, and
 quarantine list information to other NGFWs and devices in your network through
 segments, which consist of firewalls that you specify. A segment can
 collect information as well as share information. A publishing segment
 sends the data from the firewalls and devices in that segment to the firewalls in
 the subscribed segment, which contains the firewalls that receive the
 data from the publishing segments. 

 NGFWs and Panorama can share multiple data types to one segment. On a firewall or
 Panorama, each data type can only be shared in one segment. Each Firewall or
 Panorama can receive data from up to 100 segments.

  By selecting the data that is collected by a segment and where that data is shared,
 you have full control in ensuring that the information required to enforce
 least-privilege access is available on each enforcement device.

 
 
 If you associate a firewall that you [configure as a User-ID hub](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/user-id/deploy-user-id-in-a-large-scale-network/share-user-id-mappings-across-vsys) with a segment,
 the Cloud Identity Engine provides the data types based on the firewall that is
 subscribed or publishing the segment, not based on the virtual system. To ensure
 that both locally learned data and data that the User Context Cloud Service provides
 are available to all virtual systems, configure the User-ID hub firewall as a
 subscriber in the segment. 

 
 
- [PAN-OS & Panorama](/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/cloud-identity-engine-user-context/cloud-identity-user-cointext-pan-os.html#cloud-identity-user-cointext-pan-os)
- [Strata Cloud Manager](/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/redistribute-identification-information-from-ngfws-to-the-cloud/cloud-identity-engine-user-context/cloud-identity-user-context-scm.html#cloud-identity-user-context-scm)

 
















 

# Cloud Identity User Context (PAN-OS)



 Learn about user context for PAN-OS & Panorama with CIE.



 
 To control data shared over your network with User Context:

 

1.  Onboard your Cloud Identity Engine instance.
  1.  Obtain the serial number for the firewall you want to onboard, and
 [Register the firewall](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/getting-started/register-the-firewall) with the
 Palo Alto Networks Customer Support Portal (CSP).
  2.  Click the magic link provided by Palo Alto Networks to begin onboarding
 your Cloud Identity Engine tenant. 
 The magic link is provided by Palo Alto Networks by email.

 

  3.  Click MSP Cloud Management.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  4.  Continue the onboarding process.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  5.  Claim the license for the tenant you want to
 onboard. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  6.  Select the Customer Support Account you want to
 use.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  7.  Select the Parent Tenant you want to use or
 click Create New to create a new tenant.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  8.  Click Claim and continue to continue the
 onboarding process.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  9.  Click Add Licensed Product to continue the
 onboarding process.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  10.  Select the contract you want to use.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  11.  Select the Region for your Cloud Identity Engine
 instance.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  12.  Click Activate Now to complete the onboarding
 process.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  13.  Confirm that the Status for the Cloud
 Identity Engine is
 Complete.
 You can access your Cloud Identity Engine instance by selecting
 Cloud Identity Engine.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  14.  In the bottom left of the window, select the icon for your tenant and
 select Device Associations.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  15.  Select Add Device.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  16.  Select your Customer Support Account and enter your firewall serial
 number.
  17.  Select the firewall Save your changes.
  18.  Select Associate Apps.
  19.  Select the firewall, select the Cloud Identity
 Engine, and Save your
 selections.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

2.  In the Cloud Identity Engine, activate sharing for mappings. 
  1.  Log in to the Cloud Identity Engine app and select User ContextSegments
 
  2.  Activate sharing for mappings.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

3.  Configure the default segment as a publishing segment.
  1.  Select the Firewalls tab and select one or more
 firewalls.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  2.  After selecting the firewalls that you want to include in this segment,
 Assign Segments to the selected firewalls. 
 Assigning a segment to a firewall allows you to define which data the
 Cloud Identity Engine receives from or provides to that firewall.
 You can only assign segments to a firewall that uses PAN-OS 11.0;
 User Context does not support other source types. 

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  3.  (Optional) If you want to include additional firewalls in the segment,
 Add Firewalls to the segment to specify the
 firewalls you want to include. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  4.  For each Data Type that you want to share,
 select the Segment where you want to publish the
 data type.
 
 
 Firewalls publish each data type to one
 segment. To share data between firewalls, you will need to configure
 a segment for each data type you want share.

 You can select the following data types:

 
    - IP User Mappings—(GlobalProtect,
 Authentication Portal, XFF Headers, Username Header
 Insertion, XML APIs, Syslog, Server Monitoring, Panorama
 TrustSec plugin) Maps the IP address to a username.

    - IP Tag Mappings—([Dynamic Address Group](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/register-ip-addresses-and-tags-dynamically)
 only) Maps the IP address to a tag. 
    - User Tag Mappings—([Dynamic User Group](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/use-dynamic-user-groups-in-policy)
 only) Maps the tag to a user.
    - Quarantine List—(GlobalProtect only)
 Lists the firewalls that GlobalProtect has in quarantine.
    - IP Port Mappings—(Terminal Server agent
 only) Maps the IP address to the port range allocated to a
 Windows-based terminal server user.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  5.  Click Review Changes to review your
 configuration before submitting the changes.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  6.  Save the changes to confirm the
 configuration.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

4.  Create a segment to subscribe to the publishing segment you created in the
 previous step.
 Publishing segments provide the specified data type that the Cloud Identity
 Engine collects from other firewalls to the segment containing the firewalls
 that you select. 

 
 
 You can subscribe up to 100 segments per
 firewall.

 

  1.  Select User ContextSegments and click Add New Segment.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  2.  Enter a unique Segment Name and optionally a
 Description for the segment.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  3.  Click Add New Segment to save the changes.
  4.  Click Segments to add the segments you want to
 receive data.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  5.  Select the segments that you want to include and
 Add the segments.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

5.  (Optional) Edit segments as needed to customize how the Cloud Identity Engine
 provides mappings to the firewalls. 
  1.  If sharing for data type is Enabled and you do
 not want to share this data type in this segment, select it to change
 the setting to Disabled.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  2.  If you no longer need a segment, delete it from the configuration. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

6.  When your configuration is complete, Review Changes and
 Save the configuration.
7.  On your firewall, enable the service that the Cloud Identity Engine uses to
 communicate with your firewall. 
  1.  Ensure that you have configured a device certificate.
  2.  Log in to the firewall and Edit the
 PAN-OS Edge Service Settings (DeviceManagementSetupPAN-OS Edge Service Settings).
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  3.  Enable User Context Cloud Service and click
 OK to confirm the changes.
 
 
 If the firewall traffic uses a management interface, create
 security policy rules to allow connectivity between the firewall
 and the User Context Cloud Service.

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  4.  Commit your changes on the firewall.
 
 

8.  Verify the User Context configuration is successful and view the mappings and
 tags that the Cloud Identity Engine collects from the firewall.
  1.  On the firewall, verify the User Context Cloud Service
 Connection Status is active.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  2.  In the Cloud Identity Engine app, select User ContextMappings & Tags to review the information for the data types. 
 You can review the following data types:

 
    - User-ID—Search User-ID mappings by
 Username or IP
 address.
    - User Tags—Search [Dynamic User Group](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/use-dynamic-user-groups-in-policy)
 tags by Username or by
 Tag.
    - IP Tags—Search [Dynamic Address Group](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/register-ip-addresses-and-tags-dynamically)
 tags by IP address or by
 Tag.
    - IP-Port User—(Terminal Server agent only)
 Search Terminal Server agent mappings by
 IP address. 
    - Host IDs—(GlobalProtect only) Search
 devices (both quarantined and not quarantined) by
 Host ID. 

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 Now that you’ve configured segments, you can use them to [enable user- and group-based
                                    policy](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/user-id/enable-user-and-group-based-policy), [authentication](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/authentication/configure-an-authentication-profile-and-sequence) profiles
 and sequences, and other firewall-based tasks. 

 






















 

# Cloud Identity User Context (SCM)



 Learn about User Context with Strata Cloud Manager and CIE.



 
 Details coming soon.