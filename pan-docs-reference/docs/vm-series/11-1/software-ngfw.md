<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw -->
<!-- Fetched: 2026-04-01T01:59:42.023768+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags: vm-series, licensing, software-ngfw -->

# Software NGFW Credits



 



 Learn about Software NGFW credits, and the licenses they
fund.



 Software NGFW credits can be used to fund Software NGFWs
(VM-Series and CN-Series), Cloud-Delivered Security Services (CDSS),
or virtual Panorama appliances in networks with or without internet
access (air-gapped networks, for example).

You create a deployment profile to configure one or more firewalls based on the PAN-OS version,
 the number of vCPUs per firewall, the total number of firewalls supported by the
 deployment profile, Panorama management or log collection, and security services. All
 the VMs created with a deployment profile share the same authcode.

- Fixed vCPUs—Compatible with all PAN-OS versions. Based
on [VM-Series Models](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models.html#idf50b94d2-e1ec-4205-8a42-8c409f3629d1) and security
service bundles. Changing the model or service options requires
a new license.

- Flexible vCPUs—Select a flexible number of vCPUs, and a flexible selection of security services.
 You can modify the deployment profile to add or decrease the number of vCPUs,
 add new services as they become available, or remove services. The maximum
 number of vCPUs for a deployment profile is 64.

Software NGFW credits are term-based. Terms can be defined for
any amount of time between 1 and 5 years. Both allocated and unallocated
credits expire at the end of the agreed upon term. You can purchase
additional credits for a credit pool but the expiration date must
be the same as the target pool. Use [Software NGFW Credit Estimator](https://www.paloaltonetworks.com/resources/tools/ngfw-credits-estimator) to
calculate and get credits for your deployment profile.

If you have an internet connection to the license server and
you stop using a firewall, a security service, or Panorama deployment,
the credits allocated to that resource are refunded to the credit
pool and can be reallocated to a new resource. 

If you do not have an internet connection and cannot connect
to the Palo Alto Networks update server (for example, you are in
an air-gapped network) you can manage the VM-Series firewall locally
from its user interface, or from Panorama. Your administrator must
then log in to the Customer Support Portal to return the license
token so the funds can be reused.

Use the **Supported Hypervisor** table below and the **Total
vCPUs on Dataplane** tables that follow to ensure that you allocate
the necessary hardware resources for your chosen number of vCPUs.
























 

| Tier | Memory |
| --- | --- |
| Tier 1 | 4.5 GB, 5 GB, 5 GB, 5.5 GB, 6 GB, 6.5 GB,
7 GB, 8 GB |
| Tier 2 | 9 GB, 10 GB, 12 GB, 14 GB, 16 GB, 18 GB |
| Tier 3 | 20 GB, 24, GB, 28 GB, 32 GB, 36 GB, 40 GB,
44 GB, 48 GB, 52 GB, 56 GB, 60 GB, 64 GB |
| Tier 4 | 128 GB |

























 

- 

- 

| Memory Profile | Supported Hypervisors | Minimum Hard Drive |
| --- | --- | --- |
| Tier 1(4.5GB, 5 GB, 5.5GB, 6GB memory) | ESXi, Hyper-V, KVM | With 4.5 GB Mem: 32GB (60GB
at boot)60GB |
| Tier 1 | AWS, Azure, ESXi, Google Cloud Platform,
Hyper-V, KVM, OCI, Alibaba Cloud, Cisco ACI, Cisco CSP, Cisco ENCS,
NSX-T | 60GB |
| Tier 2 | AWS, Azure, ESXi, Google Cloud Platform,
Hyper-V, KVM, OCI, Alibaba Cloud, Cisco ACI, Cisco CSP, Cisco ENCS,
NSX-T | 60GB |
| Tier 3 | AWS, Azure, ESXi, Google Cloud Platform,
Hyper-V, KVM, OCI, Alibaba Cloud, Cisco ACI, Cisco CSP, NSX-T | 60GB |
| Tier 4 | AWS, Azure, ESXi, Google Cloud Platform,
Hyper-V, KVM, OCI, Alibaba Cloud, Cisco ACI, Cisco CSP, NSX-T | 60GB |


For all memory profiles listed above, the minimum vCPUs is 2. 

 
 Tier 1 withrequires minimum 32GB of hard drive space. However,
because the VM-Series base image is common for all vCPU combinations,
you must allocate 60GB of hard drive space until you license a VM-Series firewall
with 4.5GB memory.

 
 To achieve the best performance, all of the required cores
should be available on a single CPU socket.

By default, management plane and dataplane vCPUs are assigned
on one to three ratio, unless you assign four or fewer vCPUs. Additionally,
the maximum dataplane vCPUs is tied to the allocated memory, as
described in the tables below. For example, if you assign 16 vCPUs
to a VM-Series firewall, four vCPUs are allocated to the management
plane and 12 are allocated to the dataplane. If you 20 vCPUs and
20GB of memory to a VM-Series firewall, 12 vCPUs are allocated to
the dataplane and the remaining are assigned to the management plane. 

Alternatively, you can use the VM-Series firewall CLI to [Customize Dataplane Cores](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/customize-data-plane-cores.html#id4e6cde84-2453-4173-b55c-f4e02c7f0e46). This allows
you to specify the number of vCPUs are assigned to the dataplane
on your VM-Series firewall. 

 
 The maximum number of total cores (management plane and
dataplane) is 64, regardless of memory profile.
























 

| Tier 1 | 4.5 GB | 5 GB | 5.5 GB | 6 GB | 6.5 GB | 7 GB | 8 GB |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Default Dataplane vCPUs | 1 | 1 | 1 | 1 | 2 | 2 | 2 |
| Default Management Plane vCPUs | 1 | 1 | 1 | 1 | 2 | 2 | 2 |

























 

| Tier 2 | 9 GB | 10 GB | 12 GB | 14 GB | 16 GB | 18 GB | 20 GB |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Default Dataplane vCPUs | 4 | 4 | 4 | 4 | 12 | 12 | 12 |
| Default Management Plane vCPUs | 2 | 2 | 2 | 2 | 4 | 4 | 4 |

























 

| Tier 3 | 20 GB | 24 GB | 28 GB | 32 GB | 36 GB | 40 GB | 44 GB | 48 GB | 52 GB | 56 GB | 64 GB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default Dataplane vCPUs | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 24 | 47 |
| Default Management Plane vCPUs | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 8 | 17 |

























 

| Tier 4 | 121 - 128 GB |
| --- | --- |
| Default Dataplane vCPUs | 47 |
| Default Management Plane vCPUs | 17 |


Continue to Software NGFW tasks:

- 

- [Activate Credits](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/activate-credits.html#id62dd9448-83a1-4622-8b60-71a99b2e5f1e)
- [Create a Deployment Profile](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/create-a-deployment-profile-vm-series.html#id761611f1-47db-4cef-81ef-f16294cdbf62)
- [Manage a Deployment Profile](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/manage-a-deployment-profile.html#idd82ff145-26f6-44dd-848e-13dcec6ba8a3)
- [Register the VM-Series Firewall (Software NGFW Credits)](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/register-the-vm-series-firewall-software-ngfw-credits.html#idc4362038-243c-45ad-9a14-d88eac6582a6)
- [Provision Panorama](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/provision-panorama.html#id9ef04c10-9ae0-4a60-a366-c3ad3adf8949)
- [Migrate Panorama to a Software NGFW License](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/migrate-panorama-to-a-flexible-license.html#idb979078e-8b2d-4afc-9fb5-aa6c940d463c)
- [Transfer Credits](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/transfer-credits.html#id28dcccbe-75e9-44f9-a35b-f9e491157559)
- [Renew Your Software NGFW Credits](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/renew-your-software-ngfw-credit-license.html#id0b854ffe-7b56-444f-b221-230808db2db8)
- [Deactivate License (Software NGFW Credits)](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/deactivate-a-firewall.html#id4b6af333-477c-4318-aa26-0709f5505fde)
- [Delicense Ungracefully Terminated Firewalls](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/delicense-ungracefully-terminated-firewalls.html)
- [Set the Number of Licensed vCPUs](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/set-the-number-of-licensed-vcpus.html#id7cefad42-95dd-4b51-9fee-2deae471fe25)
- [Customize Dataplane Cores](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/customize-data-plane-cores.html#id4e6cde84-2453-4173-b55c-f4e02c7f0e46)
- [Migrate a Firewall to a Flexible VM-Series License](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/migrate-to-a-flexible-vm-series-license.html#id2a17226f-4d81-4b2c-98be-436db72fcff5)
- [Software NGFW Licensing API](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/software-ngfw-licensing-api.html)