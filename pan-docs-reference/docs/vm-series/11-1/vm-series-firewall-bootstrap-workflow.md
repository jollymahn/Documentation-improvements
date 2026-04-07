<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/vm-series-firewall-bootstrap-workflow -->
<!-- Fetched: 2026-03-31T18:04:48.098037+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# VM-Series Firewall Bootstrap Workflow



 



 Use the following workflow to bootstrap your
VM-Series firewall. Refer to the following figure for an overview
of both complete and basic bootstrapping procedures.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

1.  (Optional) For security reasons, you
can only bootstrap a firewall when it is in factory default state.
If you want to use the bootstrap package to bootstrap a VM-Series
firewall that has been previously configured, [reset the firewall to factory
default settings](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/firewall-administration/reset-the-firewall-to-factory-default-settings.html). 
2.  [Choose a bootstrap
method](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/choose-a-bootstrap-method.html#idf6412176-e973-488e-9d7a-c568fe1e33a9). After you familiarize yourself with the [bootstrap
package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-package.html#id88dce8d3-3665-4794-b7ed-0fd47581ebd2), assess whether you want to use a [complete](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/choose-a-bootstrap-method.html#idf6412176-e973-488e-9d7a-c568fe1e33a9_id0af596a6-630b-422c-b122-da59ea9f82d0) configuration,
or use a [basic](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/choose-a-bootstrap-method.html#idf6412176-e973-488e-9d7a-c568fe1e33a9_id5226b617-6454-4aef-844a-e1227f7ce27f) configuration
and optionally use Panorama to manage the bootstrapped firewall. 

If
you choose a basic configuration, decide whether to use the [bootstrap package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/choose-a-bootstrap-method.html#idf6412176-e973-488e-9d7a-c568fe1e33a9_idf453f878-b5e1-4793-bbf7-a047ec994d07),
or enter the configuration parameters as key-value pairs in [user data](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/choose-a-bootstrap-method.html#idf6412176-e973-488e-9d7a-c568fe1e33a9_id3433e9c0-a589-40d5-b0bd-4bc42234aa0f). 

3.  (Optional) If you want to use Panorama to manage
the VM-Series firewalls being bootstrapped, [generate
the VM auth key on Panorama](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/generate-the-vm-auth-key-on-panorama.html#id6507055f-4230-47ac-adc9-cd947bfd83c4). You must include this key in
the init-cfg.txt file (vm-auth-key)
or enter the key-value pair as user data. 
4.  [Prepare
the licenses for bootstrapping](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-licenses-for-bootstrapping.html#idb9fa0ce2-b855-435b-a9b4-5ab7b61a8353). The license retrieval mechanism only works using the VM-Series
management interface. Service routes are not supported because they
occur after the license is retrieved.

5.  If you choose the basic configuration and you plan to
bootstrap with user data, skip to Step 7. If you plan to use the basic configuration and the bootstrap
package, [create
the init-cfg.txt file](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file.html#id8770fd72-81ea-48b6-b747-d0274f37860b) and [prepare
the bootstrap package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package.html#id5575318c-1de8-497a-960a-1d7417feefa6). 

If you choose the complete
configuration, [create
the bootstrap.xml file](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-bootstrapxml-file.html#id61aa8472-5aba-41c5-ac4f-4a409e3dedb6) and prepare the full [bootstrap
package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package.html#id5575318c-1de8-497a-960a-1d7417feefa6). 

6.  [Prepare
the bootstrap package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package.html#id5575318c-1de8-497a-960a-1d7417feefa6) and save the bootstrap package in the
appropriate [delivery format](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-package.html#id88dce8d3-3665-4794-b7ed-0fd47581ebd2_id6465dc83-5fde-4e8e-92e1-38c067ea5e8a) for
your hypervisor. 
7.  Bootstrap
the VM-Series firewall.
  - [Bootstrap
the VM-Series Firewall on AWS](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-in-aws.html#idaaf52d9b-e0bc-4277-834a-23b9a720f448)

  - [Bootstrap
the VM-Series Firewall on Azure](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-in-azure.html#idd51f75b8-e579-44d6-a809-2fafcfe4b3b6)

  - [Bootstrap
the VM-Series Firewall on ESXi](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-on-esxi.html#id90a58042-2a56-4f23-9efd-3fc6d317c768)

  - [Bootstrap
the VM-Series Firewall on Google Cloud Platform](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-on-google.html#id17CRC0V0TR0)

  - [Bootstrap
the VM-Series Firewall on Hyper-V](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-on-hyper-v.html#id8daf3d1b-4da7-4dd4-a7c1-3d6c08044986)

  - [Bootstrap
the VM-Series Firewall on KVM](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-on-kvm.html#idf5df16ed-a196-47e9-942c-f9b073aee944)

8.  [Verify
bootstrap completion](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/verify-bootstrap-completion.html#id08da20f6-d19b-4a28-9d2d-f4945ebeb230).