<!-- Source: https://docs.paloaltonetworks.com/vm-series/10-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/manage-a-deployment-profile -->
<!-- Fetched: 2026-03-31T18:04:43.788590+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Manage a Deployment Profile



 



 Manage your deployment profiles.



 After you create your deployment profile
you can edit, copy, or delete it. Additionally, you can transfer
a deployment profile from one credit pool to another.

Before modifying your deployment profile, ensure that you understand
the following terms—**consumption** and **allocation** in
the context of Software NGFW credits.

- Consumption—the number for Software NGFW credits used
by a deployment profile to license deployed firewalls and subscriptions.

- Allocation—the total number of Software NGFW credits assigned
to a particular deployment profile.

Additionally, consider the following limitations before modifying
your deployment profile.

- You can remove or add subscriptions. However, when adding
or removing subscriptions, the net consumption must be less than
or equal to the total allocation of the deployment profile. 

- You can increase the vCPU and/or number of firewalls. This
increases the allocation by pulling credits from you Software NGFW
credit pool. This cannot be done if your credit pool has sufficient
available credits.

- You can change the number of vCPUs and number of firewalls.
However, the net consumption must be less than or equal to the total
allocation of the deployment profile. 

  - You cannot
decrease **only** vCPU because this decreases the allocation
to an amount past than what has already been consumed.

  - You cannot decrease **only** the number of firewalls because
this decreases the allocation to an amount past than what has already
been consumed. 

  - You can decrease vCPU and increase the number of firewalls
(or vice-versa) as long as the net consumption is less than or equal
to the total allocation of the deployment profile.

  - Optionally, you can deregister firewalls to free Software
NGFW credits to make changes to the deployment profile. 

See the following procedures for more information about managing
a deployment profile. 

- Edit a Deployment Profile
- Clone a Deployment Profile
- Transfer a Deployment Profile
- Delete a Deployment Profile



 















 

## Edit a Deployment Profile



 Use the CSP to edit a Software NGFW credits profile.



 
1. Select AssetsSoftware NGFW Credits and click
the Details button on the credit pool you
used to create your profile. 
2. Select the Current Deployment Profiles tab. 
3. On the far right, select the vertical ellipsis (More
Options) and select Edit Profile.
4. Make your changes and select Update Deployment
Profile.
5. Select the Audit Trail tab and
use search to locate your profile. Use search to locate your profile, and expand the row to
view the configuration you specified when you created the profile.








 















 

## Clone a Deployment Profile



 Use the CSP to clone a Software NGFW credits profile.



 
1. Select AssetsSoftware NGFW Credits and click
the Details button on the credit pool you
used to create your profile. 
2. On the far right, select the vertical ellipsis (More
Options) and select Clone Profile.
3. Change the profile name, make any other changes, and
select Create Deployment Profile.
4. Select the Audit Trail tab and
use search to locate your profile. Expand the row to view the configuration you cloned. It
is a new configuration with a different Profile Name and auth code.








 















 

## Transfer a Deployment Profile



 Use the following procedure to transfer a
deployment profile from one credit pool to another.

1. Select AssetsSoftware NGFW Credits and click
the Details button on the credit pool you
used to create your profile. 
2. On the far right, select the vertical ellipsis (More
Options) and select Transfer Profile.
3. Select the target credit pool and click Transfer.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 








 















 

## Delete a Deployment Profile



 Delete a Software NGFW credits deployment profile.



 Before deleting a deployment profile, you
must [Deactivate License (Software NGFW Credits)](/content/techdocs/en_US/vm-series/10-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/deactivate-a-firewall.html#id4b6af333-477c-4318-aa26-0709f5505fde) on any firewall
using the deployment profile and then [deactivate the VM](/content/techdocs/en_US/vm-series/10-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/deactivate-the-licenses/deactivate-vm.html#id73484ab8-62a9-4329-9f0e-edb143a2a974).

 
 
 If your deployment profile was used to enable Panorama,
 you must deprovision that Panorama instance before deleting the deployment
 profile.

1. Select AssetsSoftware NGFW Credits and click
the Details button on the credit pool you
used to create your profile. 
2. On the far right, select the vertical ellipsis (More
Options) and select Delete.