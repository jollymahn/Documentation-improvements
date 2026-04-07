<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series -->
<!-- Fetched: 2026-04-01T01:59:40.772410+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags: vm-series, deployment-profile -->

# Create a Deployment Profile



 



 Use the Customer Support Portal to create a Software NGFW deployment profile for PAN-OS
 10.0.3 and earlier, or PAN-OS 10.0.4 or later.



 
 Strata Cloud Manager supports two [licensing tiers](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support#strata-cloud-manager-feature-support)—[Strata Cloud Manager Essentials](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support#strata-cloud-manager-essentials) (included
 with NGFW at no additional cost), and [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support#strata-cloud-manager-pro) (available as an
 upgrade). These licenses unlock a range of network security features and management
 tools to optimize NGFW operations.
 
 Palo Alto Networks has announced May 8,
 2025, as the [End-of-Sale date](https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-sale) for the Strata Cloud
 Manager on VM Flex licenses. Starting in March 2025, Palo Alto Networks will
 automatically migrate customers using these licenses to [alternate licenses at no extra cost](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support/license-migration).
 The updated licenses will retain the same expiration dates and terms as the
 original licenses.

To create a deployment profile, you must have a [Customer Support Portal account](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/create-a-support-account.html#id4032767e-a4a8-4f5a-9df2-48f5d63780ba)
 and access to an [activated credit pool](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-credits.html#id62dd9448-83a1-4622-8b60-71a99b2e5f1e). 

Before you begin, estimate the number of firewalls that will use the configuration in the
 deployment profile. You don't have to deploy all the firewalls at once.

1.  If you already have a credit pool, log into the account, and from the
 dashboard, select ProductsSoftware NGFW CreditsCreate Deployment Profile. 
 If you have activated a credit pool, the Create Deployment
 Profile form appears.

 

  1.  Select the VM-Series firewall type and click
 **Next**.
  2.  Select the PAN-OS version. 
 
 
 Fixed models are legacy models and Palo Alto Networks recommends
 using **Flexible vCPUs**.

 

 
    - Fixed vCPU models ([VM-Series Models](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models.html#idf50b94d2-e1ec-4205-8a42-8c409f3629d1))

    - Flexible vCPUs (PAN-OS 10.0.4 and
 above)

 

  3.  Click Next.

2.  Create the VM-Series profile. 
  1.  Profile Name.
 Name the profile.

 

  2.  Number of Firewalls. 
 Enter the number of firewalls this profile deploys, assuming you have
 sufficient credits. Credits are only deducted when a firewall is
 deployed.

 

  3.  PAN-OS 11.1.3 and later releasesNumber of
 vSYS
 Enter the number of virtual systems support that you require on your
 VM-Series firewall.

 
 
 Use a flexible VM-Series firewall license and Tier 3 or Tier 4
 instances supporting a minimum of 16 vCPUs or more.

    - VM-Series in Tier 3 instance supports a maximum
 of 25 virtual systems. 

    - VM-Series in Tier 4 instance, supports a
 maximum of 100 virtual systems. 

 For information on the maximum number for a particular object or
 resource that a single VM-Series firewall deployment can create,
 store, manage, or interact with based on allocated memory or
 tier, see [Maximum Limits Based on Tier
                                        and Memory](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/maximum-limits-based-on-memory).

 

  4.  Firewall Model: 
 Choose a VM-Series model.

 Planned vCPU/Firewall (PAN-OS 10.0.4 or
 above). 

 Enter the number of vCPUs per firewall.

 Security Use Case:  Choose a use case. 

 

  5.  Customize Subscriptions. 
 After selecting a use case, you can add or remove security
 services.

 

  6.  Select your Strata Cloud Manager subscription—**Strata Cloud Manager
 Pro** or **Strata Logging Service**. If you're using Strata
 Cloud Manager Essentials, do not select these options.
 
 
 

 
 
 
 Strata Cloud Manager offers multiple subscription tiers. Strata
 Cloud Manager Pro includes AIOps, Autonomous Digital Experience
 Management (ADEM), Strata Logging Service (SLS), and Cloud
 Configuration Management. Strata Logging Service (SLS) provides
 logging services only. Select Strata Cloud Manager Pro to access
 both Strata Cloud Manager and SLS, as it comes bundled with
 SLS.

If you don’t select either Strata Cloud Manager Pro, Strata
 Logging Service, IoT, or SaaS Inline, while creating a
 deployment profile, [SCM Essentials](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support#strata-cloud-manager-feature-support)
 activates automatically.

SCM Essentials does not activate if you have choosen either
 Strata Cloud Manager Pro, Strata Logging Service, IoT, or SaaS
 Inline service.

 

  7.  (optional) Hover over the question mark to view subscription
 details:
 
    - Strata Cloud Manager Pro includes AIOps, ADEM, Strata Logging
 Service, and Cloud Configuration Management.
    - Strata Logging Service provides logging services only.

 

3.  (optional) Hover over the question mark following Protect
more, save more to see how your credit allocation affects
savings.
4.  Click Calculate Estimated Cost to
view the credit total, and the number of credits available before
the deployment.(optional) Hover over the question mark following
the estimate to view the credit breakdown for each component. 

5.  Create the Deployment Profile.You might have to wait several seconds for the profile to appear in the Current
 Deployment Profiles tab list. Before the allocation is
 complete, the Credits Consumed or Allocated column
 shows 0 and Update Pending. Scroll to the bottom and
 go to the last page to find your profile.

To view
your deployment profile later on, click the Details button
on the parent credit pool and select Current Deployment
Profiles.

  - Note the auth code for your profile on the far right; Software NGFW credit auth codes start with
 D.

  - The Credits Consumed or Allocated column shows 0 and Update
 Pending before the allocation is complete.

  - The Audit Trail tab shows Credit
Transactions and the Deployment Profiles you
manage. You can also search for a profile by time in this tab.

Use
search to locate your profile, and expand the row to view the configuration you
specified when you created the profile.