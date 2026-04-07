<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models -->
<!-- Fetched: 2026-04-01T01:56:24.313335+00:00 -->
<!-- Project: scm -->
<!-- Tags: vm-series, models, licensing -->

# VM-Series Models



 



 The VM-Series firewall is available in the following
fixed vCPU models—VM-50, VM-100, VM-200, VM-300, VM-500, VM-700,
and VM-1000-HV. These models are available for all supported PAN-OS
versions, unless otherwise noted below. The software package ( .xva, .ova,
or .vhdx file) that is used to deploy the VM-Series
firewall is common across all models. 

 
 You can migrate your fixed model ELA or perpetual license
to a 

[flexible license](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/software-ngfw/migrate-to-a-flexible-vm-series-license.html#id2a17226f-4d81-4b2c-98be-436db72fcff5) and
retain the fixed model, or you can replace the license with a flexible
vCPU license. See [VM-Series Firewall Licensing](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-firewall-licensing.html#id8fea514c-0d85-457f-b53c-d6d6193df07c) to compare
the licensing methods. 

- All models can be deployed as guest virtual machines
on VMware ESXi and vCloud Air, KVM, Microsoft Hyper-V, Cisco ACI,
Cisco ENCS, and Cisco CSP. 

- In public cloud environments—Amazon Web Services, Azure, Google
Cloud Platform, Oracle Cloud Infrastructure, Alibaba Cloud—all models
except the VM-50 are supported.
- For VMware NSX, only the VM-100, VM-300, VM-500, and VM-700 firewalls are supported.
When you apply the capacity [license](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/license-typesvm-series-firewalls.html#idee8aaedc-0452-4b4c-a5fb-b5626ca4297c) on
the VM-Series firewall, the model number and the associated capacities
are implemented on the firewall. Capacity is defined in terms of
the number of sessions, rules, security zones, address objects,
IPSec VPN tunnels, and SSL VPN tunnels that the VM-Series firewall
is optimized to handle. To make sure that you purchase the correct
model for your network requirements, use the following table to
understand the maximum capacity for each model and the capacity
differences by model: 
























 

- 

- 

- 

- 

- 

- 

- 

- 

| Model | Sessions | Security Rules | Dynamic IP Addresses | Security Zones | IPSec VPN Tunnels | SSL VPN Tunnels |
| --- | --- | --- | --- | --- | --- | --- |
| VM-50 | 20,000 (Lite Mode)50,000 | 250200 in Lite mode | 1,000 | 15 | 25025 in Lite mode | 25025 in Lite mode |
| VM-100
                            VM-200 | 200,000 | 1,500 | 2,500 | 40 | 1,000 | 500 |
| VM-300
                            VM-1000-HV | 400,000 | 10,000 | 100,000 | 40 | 2,000 | 2,000 |
| VM-500 | 1,100,000 | 10,000 | 100,000 | 200 | 4,000 | 6,000 |
| VM-700 | 8,500,000 | 20,000 | 100,000 | 200 | 8,000 | 12,000 |


For information on the platforms on which you can deploy the VM-Series firewall, see [VM-Series
                Deployments](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/about-the-vm-series-firewall/vm-series-deployments.html#idbc049c9e-8fdf-40c3-b70a-00176813948e). For more information about the VM-Series firewall models, see
 the Palo Alto Networks Firewall [comparison tool](https://www.paloaltonetworks.com/products/product-selection). You can also review general information
 [About the VM-Series
                Firewall](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/about-the-vm-series-firewall.html#id0341335a-51ec-4856-a85b-3aead63d6a1a). 

- [VM-Series
System Requirements](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/vm-series-system-requirements.html#idb04eb16a-3824-4d10-ae65-2f440608f87b)
- [CPU
Oversubscription](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/cpu-oversubscription.html#idab0db8fe-f5d1-4d15-bc1c-816885aedeaa)
- [VM-50 Lite Mode](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/vm-50-lite-mode.html#id1829E03J04N)
- [VM-Series Model License Types](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/license-typesvm-series-firewalls.html#idee8aaedc-0452-4b4c-a5fb-b5626ca4297c)
- [Activate VM-Series Model Licenses](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/activate-the-license.html#iddae4310c-d316-47d9-ab71-b74e430b31a4)
- [Register the VM-Series Firewall](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/register-the-vm-series-firewall.html#id1c0525c0-f2b8-44b4-9d11-271d53003b20)
- [Install a Device Certificate on the VM-Series Firewall](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/install-a-device-certificate-on-the-vm-series-firewall.html#id63b6c128-5973-469e-bd4a-bdc6da5cb3df)
- [Switch Between the BYOL and the PAYG Licenses](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/switch-between-the-byol-and-the-payg-licenses.html#id20f38f8d-aac6-4347-805c-344f9d8d7d5b)
- [Switch Between VM-Series Model Licenses](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/switch-between-vm-series-ela-and-subscription-bundles-licenses.html#idc2ec10be-2e45-4b95-87f3-0e9836ee2539)
- [Deactivate License(s)](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/deactivate-the-licenses.html#id8562cc5a-ee6b-4e1e-acdc-73736e82f44d)
- [Renew VM-Series Firewall License Bundles](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/renew-vm-series-license-bundles.html#id189HM0910P2)
- [Model-Based Licensing API](/content/techdocs/en_US/vm-series/11-0/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/licensing-api.html#id0873c753-02bd-4371-9e6a-2b35cfc0a44b)