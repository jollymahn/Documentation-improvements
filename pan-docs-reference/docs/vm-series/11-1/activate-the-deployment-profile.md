<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-the-deployment-profile -->
<!-- Fetched: 2026-04-01T01:52:23.067506+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags: vm-series, deployment-profile -->

# Activate the Deployment Profile



 



 Ensure to activate additional licenses on your tenants if you have enrolled to a
 cloud service subscription (consisting of IoT, SaaS Inline, SCM Pro, and SLS).



 
 If you have enrolled to a cloud service subscription (consisting of IoT, SaaS Inline,
 Strata Cloud Manager Pro, and Strata Logging Service), you will need to activate
 additional licenses on your tenants after you [create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series) on the
 Customer Support Portal. You will find the deployment profile that you need to
 activate, listed under Current Deployment Profiles.

 

1.  After you [create a deployment profile](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series), click
 **Finish SetUp** against the deployment profile you created.
 
 
 In case of Deployment profiles with no cloud based subscription, you will
 not view the **Finish SetUp** link.

 

 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 You will be prompted with authentication to SSO after which you will view the
 Activate Subscriptions based on the deployment profiles page.

 

2.  Login to the HUB with your SSO.
3.  Click **Subscriptions and Add-ons** and click the tenant in which your
 deployment profile is created. You will view the **Activate Subscriptions based
 on Deployment Profiles** page.
4.  Select the Customer Support Portal account that you are subscribed to.
5.  Select or Create the required tenant and the region it belongs to.
6.  Select the deployment profile that you wish to associate with the selected
 tenant. You can also search for the deployment profile using its name or auth
 code.
 
 
  If you have not subscribed to any of the cloud services, you will still
 be able to view the deployment profile in this section.

The status of the deployment profiles is listed as **Available** or
 **Not available** and the required dependency to make the
 deployment profile available is also listed. The Deployment Profiles
 listed as available can be associated with the tenant.

The deployment profiles listed as **Not available** might have a
 missing or a conflicting service under the selected tenant. For example,
 if you have a deployment profile with Strata Cloud Manager Pro
 subscription that is associated with a TSG, and another deployment
 profile with AIOps subscription, the deployment profiles will be listed
 as available. However, you won't be able to activate the deployment
 profile with AIOps under the same TSG, and this will result in an error
 due to conflicting services. If you have a deployment profile with
 Strata Cloud Manager Pro, then you must not associate some profiles with
 Strata Cloud Manager Pro, some with Strata Logging Service and some with
 no subscription. Ensure that you associate all the profiles with Strata
 Cloud Manager Pro.

 

7.  (optional) Select the **Additional Services** that you would like
 all your flex firewall devices to be associated with. You can either select the
 required Cloud Identity Engine service or create a new one.
 
 
 

 
 

 
 

 
 
 Selecting an additional service onboards all Flex firewalls associated
 with the tenant to the Cloud Identity Engine. If you unselect any of the
 additional services, the system dissociates all Flex firewalls
 associated with the tenant from that service.

.

 

8.  Agree to the terms and conditions and click **Activate**.
 
 
 Tenant provisioning takes approximately 15–50 minutes. During this
 process, the Profile Association Status on the hub displays
 **Associating**. Once provisioning is complete, the Finish Setup
 link disappears automatically.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

9.  The registered devices are viewed at **Common Services** > **Device
 Associations** on the hub.
 
 
 

 
 

 Alternatively, if you don't wish to activate the deployment profile through
 Finish SetUp, you can navigate to **Common Services** > **Subscriptions
 & Add-ons**. You will find the deployment profile under the Ready
 for Activation section. Click **Activate Now** to activate the deployment
 profile.

 



 















 

## Remove Deployment Profile Association From a TSG



 To remove a deployment profile from a TSG:

1.  On the hub, go to **Common Services** > **Tenant Management** >
 **Deployment Profiles**.
2.  Click the **ellipses** (⋮) next to the deployment profile you want to
 remove the association and click **Remove Association**.
 
 
 

 
 

3.  Click **Delete** on the confirmation dialog.
 
 
 The system notifies the Customer Support Portal
 Customer Support Portal super user whenever a deployment profile is
 added or removed from a TSG.

 








 















 

## Scenarios during Deployment Profile Activation



 The following are some of the use case scenarios you
 might face while activating a deployment profile.
1. A deployment profile can be associated with only one Tenant Service Group
 (TSG) at a time. If you need to use it with another TSG:
  1. Remove the required deployment profile from the tenant. This
 action removes all VM-Series devices from the tenant and all
 associated data will be lost.

  2. Navigate to the required TSG and associate the deployment profile
 with it.

2. You cannot associate a TSG with two deployment profiles with one of them
 using Strata Cloud Manager Pro and the other using Strata Logging Service.
 All the deployment profiles linked to a TSG must use either Strata Cloud
 Manager Pro or Strata Logging Service.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
3. In case of an upgrade scenario, where you have a subscription to Strata
 Logging Service and need Cloud Management and ADEM:
  1. You will need to upgrade to only Strata Cloud Manager Pro. The new
 prices will be calculated as per the new subscription and the
 **Finish SetUp** link appears again.The Profile
 Association Status for the SLS deployment profile on the hub
 will now change from Complete to **Pending**.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
  2. Agree to the Terms and Conditions on the Activate
 Subscriptions based on the Deployment Profile window and click
 **Activate Now**.

The SCM deployment profile will now spin up and after the Profile
 Association Status turns to complete, the Finish SetUp link
 disappears.

4. If you wish to remove all the VMFlex devices from the association of Cloud
 Identity Engine on a TSG, then,
  1. Select the required TSG from the **Activate Subscriptions based on
 Deployment Profile(s)** page
  2. Uncheck the **Associate Cloud Identity Engine on this tenant**
 checkbox. This will dissociate all the VMFlex devices that are
 associated with the TSG and not one device. Click
 **Activate**.
  3. Check the **Agree to the Terms and Conditions**.
  4. Click **Activate**.