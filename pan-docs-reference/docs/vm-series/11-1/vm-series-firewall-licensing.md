<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-firewall-licensing -->
<!-- Fetched: 2026-03-31T18:04:41.658959+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# VM-Series Firewall Licensing



 



 Learn about licensing for flexible vCPU and fixed model
licenses.



 This chapter compares the following license information:

- License Types: BYOL versus
PayGo

- Flexible vCPUs and Fixed Model Licensing: Flexible vCPUs
versus fixed models)
- Flexible vCPUs and Fixed Model Deployment: Summary of
deployment steps for flexible and fixed models.


 















 

## License Types



 
 
 New capacity licenses (non-Software NGFW Credits)
are no longer available for purchase. However, you one (1) year
renewals for capacity (perpetual and term-based) licenses are available.

Palo Alto Networks currently supports two license types: Bring
Your Own License (BYOL) and PAYG (Pay-As-You-Go, also called PayGo).
























 

[Software NGFW Credits](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw.html#idd1922e2b-be25-4004-abcf-59d48405cdde)

[Software NGFW Credits](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw.html#idd1922e2b-be25-4004-abcf-59d48405cdde)

[VM-Series Model](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models.html#idf50b94d2-e1ec-4205-8a42-8c409f3629d1)

- **[VM-Series Enterprise License Agreement (Multi-Model ELA)](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/license-typesvm-series-firewalls/vm-series-ela.html#id5f6928b6-edf0-4ecb-9565-1e9c00c9b1ca)**

- 

- 

| Type | Description |
| --- | --- |
| BYOL | —Available
on VM-Series firewalls running all PAN-OS releases. VM-Series firewalls
running PAN-OS versions 10.0.4 and later offer advanced features and
more flexibility. The flexible license cost is based on the number
of vCPUs, the security services you have enabled, and whether you
choose to provision Panorama to manage the firewall or act as a
log collector. See  for a detailed
explanation. |
| BYOL | licenses—Available
for use with all PAN-OS releases. The number of vCPUs is fixed according
to your chosen VM-Series model.
    
    Flexible vCPUs, available
with PAN-OS 10.0.4 and later, support advanced features and more
vCPUs. 
The capacity license cost is based on the VM-Series
model, the device memory, storage costs, and the support entitlement.
Security services and a Panorama deployment to manage your firewalls
are additional costs. The capacity license types are:—A comprehensive one-
or three-year licensing agreement for VM-Series firewalls. An individual
license can include a model, security services, a support entitlement,
and an optional device management license for Panorama. Multi-Model
ELA features a token pool from which you allocate tokens to license VM-Series
firewalls. (It is unique to the ELA, and is not the same as the
Software NGFW Credits pool.) Perpetual VM-Series model capacity license with a support
entitlement and/or security services bundle 1 or bundle 2.Term firewall capacity license with a support entitlement
and your choice of security services. |
| PayGo | Purchased from a public cloud marketplace
(such as AWS, Azure, or GCP), or a Cloud Security Service Provider
(CSSP). Available on the PAN-OS version your provider supports. On
PAN-OS versions earlier than 9.1.1, PayGo supported only the VM-Series
VM-300 model. For PAN-OS 9.1.1 and later PayGo can support fixed
Models. The traditional VM models, such as VM-100, VM-300, VM-500,
and VM-700 are supported. |









 















 

## Flexible vCPUs and Fixed Model Licensing



 What is the difference between flexible vCPU Software
NGFW licensing and fixed vCPU VM-Series Model licenses? They charge
for different things, and they fund them differently. The following
tables provide a quick comparison, and links to greater details. 
























 

[activating](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-credits.html#id62dd9448-83a1-4622-8b60-71a99b2e5f1e)

[VM-Series model](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models.html#idf50b94d2-e1ec-4205-8a42-8c409f3629d1)

- [VM-Series Enterprise License Agreement (Multi-Model ELA)](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/license-typesvm-series-firewalls/vm-series-ela.html#id5f6928b6-edf0-4ecb-9565-1e9c00c9b1ca)

- 

- 

****

****

[activate](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-credits.html#id62dd9448-83a1-4622-8b60-71a99b2e5f1e)

- 
- 

- 

|  | Flexible vCPUs | VM-Series Model (Fixed vCPUs) |
| --- | --- | --- |
| Description | Cost is based on the number of vCPUs and
your chosen Security services.There is no cost for Panorama
other than the vCPUs it consumes.You purchase reusable Software
NGFW credits that expire at the end of a predetermined term. After  your
credits you can portion them into credit pools.To use your credits,
choose a credit profile and create one or more deployment profiles.
Choose your own combination of firewall-as-a-platform components:
VM-Series vCPUs, security services, virtual Panorama for Management
or Dedicated Log Collection, and a support entitlement. All firewalls
deployed with a profile are licensed with the same auth code, and you
can manage them from the deployment profile. | Cost is based on the  capacity
license, device memory, and storage. Panorama and Security services
are separate purchases.—A comprehensive
one- or three-year licensing agreement for VM-Series firewalls. Multi-Model
ELA features a token pool from which you allocate tokens to license
VM-Series firewalls. Perpetual VM-Series model capacity license with a support
entitlement and/or security services bundle 1 or bundle 2.Term firewall capacity license with a support entitlement
and your choice of security services. |
| Activation | Requires an activation email. Activation and
registration occur automatically. | Requires an activation email and a separate
registration step after activation. |
| Security services | Threat Prevention, DNS Security, GlobalProtect,
WildFire, URL Filtering, SD-WAN, DLP, and other services as they
become available. When you create your deployment profile
you can choose any combination of security services. You can add
or remove security services from your profile at any time. | Bundle 1: Threat Prevention and premium
support entitlement.Bundle 2: Threat Prevention, DNS Security,
GlobalProtect, WildFire, URL Filtering, SD-WAN, DLP, and premium support
entitlement. |
| PAN-OS version | Up to 64 flexible vCPUs and advanced service
options for firewalls running 10.0.4 and later. | You can deploy a VM-Series model (fixed
vCPUs) on any PAN-OS version. |
| Funding | Reusable credits that allow you to consume
firewall-as-a-platform components.After you purchase credits
you must  them,
associating them to a particular account for your organization.
Activated credits fund a credit pool from which you can create a deployment
profile.When firewalls are deployed, credits are consumed.
When firewalls are deactivated, the credits are released and returned
to your credit pool for further use. | Multi-Model ELA: tokens. Perpetual VM-Series model capacity license with a support
entitlement and/or security services bundle 1 or bundle 2. You determine
the configuration at time of purchase. You cannot change the configuration unless
you purchase a new license.Term firewall capacity license with a support entitlement
and your choice of security services. |
| Deployment Configuration | Flexible. A deployment profile can be changed
at any time. Changes to the profile propagate to all firewalls that share
the deployment profile auth code. | VM-Series model capacity does not change, but
if you have an ELA, you an can add Security services.Perpetual
and Term licenses are configured and paid for in advance and do
not change. |
| Deployment | After credit activation, create a deployment
profile for a specific environment or use case (such as “Protect
my NSX Environment”) and configure firewall vCPUs, security services,
and an optional virtual Panorama. You can create any number of deployment
profiles and customize them at any point in time. You must have
the Customer Support Portal role Credit Administrator (applies to
account management only) to activate and manage Software NGFW credits. | Accept the VM-Series ELA. Deploy and configure
the VM-Series firewall. Activate the model license and register the
firewall. |
| Panorama | When you create a deployment profile you can
choose to add Panorama for management, or as a dedicated log collector
for firewalls that use a deployment profile. This Panorama can manage
firewalls deployed with the deployment profile’s shared auth code. | Panorama is a separate expense. A physical
or virtual Panorama can be used to for firewall management or for log
collection. |
| Upgrade or Downgrade | If the VM-Series firewall or Panorama has
an internet connection, changes to your deployment profile are automatically
applied to the firewall.If the firewall does not have an
internet connection, manually stop the firewall. In Assets > Software
NGFW Credits change the deployment profile, then in the CSP, download
the license keys, and transfer them to the VM, obtain the profile
from the CSP, transfer it to the VM, restart the VM and apply the license.You
do not have to reboot the firewall in either case. | Change to a different model requires a license
change and a reboot. |









 















 

## Flexible vCPUs and Fixed Model Deployment



 The following checklists compare the deployment processes
for Software NGFW credits and the VM-Series Model licensing methods.
























 ****

1. [Create a Support Account](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/create-a-support-account.html#id4032767e-a4a8-4f5a-9df2-48f5d63780ba)

2. [Activate Credits](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-credits.html#id62dd9448-83a1-4622-8b60-71a99b2e5f1e)

3. [Create a Deployment Profile](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series.html#id761611f1-47db-4cef-81ef-f16294cdbf62)

4. [Alibaba](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-alibaba-cloud.html#id23599bde-5e8b-4567-a3c2-63a0cbd44ab2)[AWS](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-aws.html#idaf5034a5-d7f1-4fc8-a3c1-f96c688d3499)[Azure](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-azure.html#id209ca5c7-c122-4fa2-bccd-0fa4b8cc225d)[Cisco ACI](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-a-firewall-in-cisco-aci.html#id17BUA0R0J9Y)[Cisco CSP](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-cisco-csp.html#id021456aa-f21f-472a-9d82-e65691ac2ae2)[Cisco ENCS](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-cisco-encs.html#idf28d2dd3-602f-45ad-bbca-8f9a65691edd)[ESXi](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-a-vm-series-firewall-on-an-esxi-server.html#id57672878-97bb-4df5-8d81-067e4d435313)[Google
Cloud Platform](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform.html#id181JF0Z02CP)[Hyper-V](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-hyper-v.html#ide72127dc-5aeb-46d7-a315-72668bd0f362)[KVM](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-kvm.html#id6615fb1c-44c7-4752-9319-4513c27403cf)[OpenStack](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-openstack.html#idf314f373-8c2f-4291-925f-79157c4527bc)[Oracle Cloud Infrastructure](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-oracle-cloud-infrastructure.html#ida76fdad1-a6cc-4930-84b6-41c3586af258)[vCloud
Air](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-vcloud-air.html#id16b15ca3-b32f-4670-8c3a-7198a3216af6)

5. [Install a Device Certificate on the VM-Series Firewall](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/install-a-device-certificate-on-the-vm-series-firewall.html#id63b6c128-5973-469e-bd4a-bdc6da5cb3df)

1. [Create a Support Account](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/create-a-support-account.html#id4032767e-a4a8-4f5a-9df2-48f5d63780ba)
2. [Activate VM-Series Model Licenses](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/activate-the-license.html#iddae4310c-d316-47d9-ab71-b74e430b31a4)

3. [Register the VM-Series Firewall](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/register-the-vm-series-firewall.html#id1c0525c0-f2b8-44b4-9d11-271d53003b20)

4. [Alibaba](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-alibaba-cloud.html#id23599bde-5e8b-4567-a3c2-63a0cbd44ab2)[AWS](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-aws.html#idaf5034a5-d7f1-4fc8-a3c1-f96c688d3499)[Azure](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-azure.html#id209ca5c7-c122-4fa2-bccd-0fa4b8cc225d)[Cisco ACI](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-a-firewall-in-cisco-aci.html#id17BUA0R0J9Y)[Cisco CSP](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-cisco-csp.html#id021456aa-f21f-472a-9d82-e65691ac2ae2)[Cisco ENCS](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-cisco-encs.html#idf28d2dd3-602f-45ad-bbca-8f9a65691edd)[ESXi](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-a-vm-series-firewall-on-an-esxi-server.html#id57672878-97bb-4df5-8d81-067e4d435313)[Google
Cloud Platform](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform.html#id181JF0Z02CP)[Hyper-V](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-hyper-v.html#ide72127dc-5aeb-46d7-a315-72668bd0f362)[KVM](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-kvm.html#id6615fb1c-44c7-4752-9319-4513c27403cf)[OpenStack](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-openstack.html#idf314f373-8c2f-4291-925f-79157c4527bc)[Oracle Cloud Infrastructure](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-oracle-cloud-infrastructure.html#ida76fdad1-a6cc-4930-84b6-41c3586af258)[vCloud
Air](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-vcloud-air.html#id16b15ca3-b32f-4670-8c3a-7198a3216af6)

5. [Install a Device Certificate on the VM-Series Firewall](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/install-a-device-certificate-on-the-vm-series-firewall.html#id63b6c128-5973-469e-bd4a-bdc6da5cb3df)

| Flexible vCPUs | Fixed vCPUs (VM-Series Model) |
| --- | --- |
| ..Your
organization can have many accounts to represent different cost
centers. During registration you associate your credit purchase
with an account. .Deploy the VM-Series firewall on , , , , , , , , , , . , , NSX-T, or NSX-V (for site licenses such as Strata Logging
           Service and Auto Focus). | ...Deploy the VM-Series firewall on , , , , , , , , , , . , , NSX-T, or NSX-V. (for site licenses such as Strata Logging
           Service and Auto Focus). |