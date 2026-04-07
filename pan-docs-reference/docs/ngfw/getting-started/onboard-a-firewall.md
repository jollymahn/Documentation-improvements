<!-- Source: https://docs.paloaltonetworks.com/ngfw/getting-started/onboard-your-ngfws/onboard-a-firewall -->
<!-- Fetched: 2026-03-31T18:59:40.397183+00:00 -->
<!-- Project: scm -->
<!-- Tags: ngfw, onboarding, firewall -->

# Onboard a Firewall

 

 
 
 
 
 
 

 

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

 
 

 

 

---

 
 
 















 

# Onboard a Firewall



 Learn how to onbaord your Next-Generation Firewalls to Strata Cloud Manager and Panorama.



 
 






















 

- 

- 
- 

- 

- 

| Where Can I Use
                                This? | What Do I Need? |
| --- | --- |
| NGFW (Cloud Managed)
                                    NGFW (PAN-OS or Panorama Managed)
                                        VM-Series, funded with Software NGFW Credits | AIOps for NGFW Premium license (use the Strata Cloud Manager app)
                                    
                                        Cortex
Data Lake license |



 
 
 
 Contact your account team to enable Cloud Management for NGFWs using Strata Cloud
 Manager.

 

 To use Strata Cloud Manager or the Panorama™ management server for managing
 Next-Generation Firewalls, you must first add the firewalls as a managed device.

 
 
- [Cloud Management](/content/techdocs/en_US/ngfw/getting-started/onboard-your-ngfws/onboard-a-firewall/onboard-a-firewall-cloud-management.html#onboard-a-firewall-cloud-management)
- [Panorama](/content/techdocs/en_US/ngfw/getting-started/onboard-your-ngfws/onboard-a-firewall/onboard-a-firewall-pan-os-and-panorama.html#onboard-a-firewall-pan-os-and-panorama)

 
















 

# Cloud Management



 Learn how to configure and onboard firewalls in Strata Cloud Manager.



 
 After you activate your AIOps for NGFW Premium license, you can begin to
 onboard Palo Alto Networks firewalls to Strata Cloud Manager. Onboarding to Strata Cloud Manager is supported for firewalls running PAN-OS 10.2.3 and later
 releases.

 There are four components involved in firewall onboarding:

 
- 
 The tenant — Created when you activate a product license on your
 Customer Support Portal (CSP) account. You add firewalls to your tenant to
 associate them with Strata Cloud Manager. 

 
- 
 The firewall — The Palo Alto Networks firewall that you intend to use with
 Strata Cloud Manager.

 
 
 
 You can only onboard a firewall not already associated with Cortex Data
 Lake (CDL). If a firewall is already associated with CDL, it’s
 ineligible for Strata Cloud Manager and isn’t displayed. 

 

 
- 
 AIOps for NGFW Premium—License required for cloud management of
 firewalls.

 
- 
 Strata Cloud Manager — The app you will be associating with the firewall to
 manage its configuration from the cloud.

 

 

1. Review the [prerequisites for onboarding your
                        firewall](/content/techdocs/en_US/ngfw/getting-started/integrate-ngfws-into-your-network/prerequisites-for-onboarding-ngfws.html) to Strata Cloud Manager.
2. [Activate](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/activate-cortex-data-lake-toc/activate-cortex-data-lake-easy) the Cortex
Data Lake license.
 Skip this step if you already activated the Prisma Access
(Cloud Management) license on
 the same tenant you are activating AIOps for NGFW Premium license.
 

 

3. [Activate](https://docs.paloaltonetworks.com/common-services/subscription-and-tenant-management/aiops-for-ngfw/activate-aiops-for-ngfw) the AIOps for NGFW Premium license.
 Skip this step if you already activated the AIOps for NGFW Premium
 license.

 

4. (Optional) [Activate](https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started/get-started-with-the-cloud-identity-engine/activate-the-cloud-identity-engine) the Cloud Identity Engine
 license.
 Activate Cloud Identity Engine (CIE) if you plan to use user-based
 authentication policies. CIE activation is not required for initial
 onboarding and can be activated at a later time as needed.

 

5. Register the firewall with the Palo Alto Networks Customer Support Portal (CSP)
 and activate licenses.
  1. [Log in to the firewall web
                                interface](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli) and find the Serial #
 under the General Information widget in the
 Dashboard. 
  2. [Register your Next-Generation
                                Firewall](/content/techdocs/en_US/ngfw/getting-started/set-up-your-ngfws/register-your-next-generation-firewall.html). 
  3. [Activate the Support license](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/subscriptions/activate-subscription-licenses)
 on the firewall.

6. [Install the device certificate](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/certificate-management/obtain-certificates/device-certificate) on the
 firewall.
 This is required to successfully authenticate the firewall with the Palo Alto
 Networks CSP and use Strata Cloud Manager.

 

7. Configure the firewall Panorama Settings required to connect to Strata Cloud Manager. 
  1. [Log in to the firewall web
                                interface](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/firewall-administration/use-the-web-interface/launch-the-web-interface).
  2. Configure the firewall DNS and NTP servers.
 This is required to successfully connect the firewall to Strata Cloud Manager and install software and content updates.

 
    1. 
 Select DeviceSetupServices and edit the Services.

 
    2. 
 Select Servers and configure the
 Primary DNS Server and
 Secondary DNS Server.

 
    3. 
 Select NTP and configure the Primary
 and Secondary NTP Server Address.

 
    4. 
 Click OK.

 

 

  3. Configure the Panorama Settings. 
 
    1. 
 Select DeviceSetupManagement and edit the Panorama Settings.

 
    2. 
 Select Managed By Cloud Service.

 
    3. 
 Click OK.

 

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  4. Commit.

8. [Associate a firewall](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-devices-with-a-tenant) with your Palo
 Alto Networks Customer Support Portal (CSP) account.
  1. Log in to Strata Cloud Manager.
  2. In the bottom-left corner of the window, select the icon for your
 tenant and select SettingsDevice Associations.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  3. Add Devices. 
  4. Select one or more firewalls you want to onboard with your CSP
 account.
 You can use the firewall serial number you gathered in the previous
 step to search for a specific firewall. 

 

  5. Save. 
 
 
 

 
 

9. [Associate the firewall](https://docs.paloaltonetworks.com/common-services/device-associations/get-started/associate-apps-with-devices) with Strata Cloud Manager.
  1. In Device Associations, select the firewall you added and
 Associate Apps.
 
 
 

 
 

  2. For the Licensed Products, select AIOps for
 NGFW.
  3. From the Select Firewall Model, License Type, and
 Term drop-down, select the firewall and support license
 to apply to the firewall.
 The model for the firewall license must match the firewall model you
 are onboarding to Strata Cloud Manager.

 

  4. Apply Licenses.
 
 
 

 
 

  5. In the Device Associations page, verify the Associated Apps for the
 onboarded firewall display AIOps for NGFW
 and Cortex Data Lake.
 
 

10. Add the available device to Strata Cloud Manager.
  1. Select WorkflowsNGFW SetupDevice ManagementAvailable Devices.
  2. In the Available Devices select the
 firewall you just added.
  3. Move to Cloud Management.
 You are prompted to confirm the number of selected firewalls. Click
 Move to Cloud Management to continue.

 
 
 

 
 

  4. Confirm that the selected firewall is now listed in the list of
 Cloud Managed Devices.
 
 
 

 
 

11. Verify that the firewall successfully onboarded to Strata Cloud Manager.
 
 
 
 Two configuration pushes occur by default to the firewall after
 successful onboarding to Strata Cloud Manager. The first push from Strata Cloud Manager enables Advanced Routing and restarts the
 firewall. The second pushes the configuration from Strata Cloud Manager
 to the firewall.

 

 

  1. Select WorkflowsNGFW SetupDevice ManagementCloud Managed Devices.
 You should see the serial number for the firewall that you just
 added, but you won’t see any additional device information for it
 yet.

 

  2. [Log in to the firewall CLI](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli) and
 verify the firewall successfully connected to Strata Cloud Manager.
 After you connect the firewall to Strata Cloud Manager, it’s
 automatically converted to logical router mode, restarted, and Strata Cloud Manager pushes the default configuration to the
 firewall.

 
 
 
 For this to work, make sure:

 
    - 
 You’ve completed the earlier step to install the device
 certificate on the firewall.

 
    - 
 The firewall meets the [prerequisites](/content/techdocs/en_US/ngfw/getting-started/integrate-ngfws-into-your-network/prerequisites-for-onboarding-ngfws.html) for Strata Cloud Manager.

 
    - 
 You’ve resolved variables. If variables aren’t resolved,
 Strata Cloud Manager will fail to push the default
 configuration to the firewall.

 

 

 
```
admin> show cloud-management-status

```

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 Verify the firewall successfully connected to a Strata Cloud Manager
 Endpoint and that the
 Connected status displays
 Yes.

 Once the firewall is Connected, the
 firewall automatically converts to logical router mode and restarts,
 and Strata Cloud Manager pushes the default configuration to the
 firewall.

 

  3. Return to [Strata Cloud Manager](https://sase.paloaltonetworks.com/) and select WorkflowsNGFW SetupDevice Management and verify that the details for the firewall appear, such
 as serial number, model, type, and IP address. 
 By default, newly onboarded firewalls are added to the Firewalls
 folder. 

 

12. Create and associate your firewall with a [folder](https://docs.paloaltonetworks.com/cloud-management/administration/workflows/workflows-ngfw-setup/folder-management).
 Folders are used to logically group your firewalls for simplified
 configuration management. 

 
 
 
 (HA only) Both firewalls must be in the same folder to configure
 HA. If you need to configure your firewalls in a [high availability](https://docs.paloaltonetworks.com/ngfw/administration/high-availability) (HA)
 configuration, be sure to plan your folder structure accordingly and
 move both firewalls to the same folder before you configure HA. 

 Additionally, firewalls in an HA configuration cannot be moved to a new
 folder. To move them, you must first break the HA configuration, move
 both firewalls to the new folder, and then reconfigure HA. 

 

 

  1. Select WorkflowsNGFW SetupFolder Management and Add Folder to create a new
 folder.
  2. Locate the newly added firewall that is associated with the
 All Firewalls by default. 
  3. In the Action column, Move the firewall to the
 folder you created. 

13. (Optional) Modify the displayed firewall name.
 By default, firewalls onboarded to Strata Cloud Manager display the firewall
 serial number as the displayed firewall name throughout Strata Cloud Manager. Rename the displayed firewall from the serial number to a more
 user-friendly name to make it easier to identify.

 

  1. Select WorkflowsNGFW SetupFolder Management and locate the firewall you onboarded.
  2. In the Actions column, expand the Actions menu and
 Edit.
  3. Enter a new Display Name for the firewall.
  4. Save.

14. Review the predefined interface and logical router configurations.
 The predefined interfaces and logical router configuration are required to
 successfully push configuration changes to managed firewalls after they’re
 successfully added to Strata Cloud Manager.

 
  - 
 **$eth-internet (eth1/3)**—Ethernet interface for outbound
 internet connections. Associated with the default logical router
 configuration.

 
  - 
 **$eth-local (eth1/4)**—Ethernet interface for local network
 connections. Associated with the default router configuration.

 

 The predefined interface and logical router configuration are associated with
 the default All Firewalls folder and are
 inherited by all other folders you create. You might reassign the
 $eth-internet and $eth-local
 interfaces for a newly created folder or for the individual
 firewall as needed.

 

  1. Select ManageConfigurationDevice SettingsInterfacesEthernet and verify that
 $eth-internet and
 $eth-local are displayed. 
 
 
 
 To reassign the interface, click the interface name to select a
 new Default Interface Assignment and
 Save.

 

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  2. Select ManageConfigurationDevice SettingsRoutingLogical Routers and verify the default
 logical router is displayed. 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

15. Push Config to push your configuration changes.
16. Select ManageOperationPush Status and to verify that your configuration push was successful. 





 
 
 

















 

# Panorama



 Learn how to onboard firewalls to Panorama.



 
 Next-Generation Firewalls can be centrally managed using Panorama.

 To start onboarding your Next-Generation Firewalls to Panorama, follow the guide
 [here](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/add-a-firewall-as-a-managed-device).