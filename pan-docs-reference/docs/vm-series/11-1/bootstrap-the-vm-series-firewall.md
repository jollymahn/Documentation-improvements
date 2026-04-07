<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall -->
<!-- Fetched: 2026-03-31T18:04:45.966317+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Bootstrap the VM-Series Firewall



 



 Bootstrapping allows you to create a repeatable and
streamlined process of deploying new VM-Series firewalls on your
network because it allows you to create a package with the model
configuration for your network and then use that package to deploy
VM-Series firewalls anywhere. 

You can either bootstrap the firewall with **complete** configuration
so that the firewall is fully configured at startup, or you can
begin with a **basic** configuration—a minimal initial configuration
that enables you to boot the firewall and then register with Panorama
to complete the configuration. 

If you choose the **basic** configuration and you are deploying
on AWS, Azure or GCP, you can use the bootstrap package and an init-cfg.txt file.
Alternatively, you can bootstrap with **user data**. Instead
of providing bootstrap configuration parameters in files, you enter
them as key-value pairs directly into the AWS or GCP user interface
when you launch a VM-Series firewall. Azure has a similar process
with which you provide the bootstrap parameters in a template or
other text file accessed from the Azure CLI. 

If you create the bootstrap package, you deliver it from an external device (such as a virtual
 disk, a virtual CD-ROM, or a cloud storage device (such as a bucket). 

- [Choose a Bootstrap Method](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/choose-a-bootstrap-method.html#idf6412176-e973-488e-9d7a-c568fe1e33a9)
- [VM-Series
Firewall Bootstrap Workflow](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/vm-series-firewall-bootstrap-workflow.html#id59fe5979-c29d-42aa-8e72-14a2c12855f6)
- [Bootstrap
Package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-package.html#id88dce8d3-3665-4794-b7ed-0fd47581ebd2)
- [Bootstrap Configuration Files](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-configuration-files.html#id37d59976-16c6-4c75-af8a-61f46e690d65)
- [Generate the VM Auth Key on Panorama](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/generate-the-vm-auth-key-on-panorama.html#id6507055f-4230-47ac-adc9-cd947bfd83c4)
- [Create the init-cfg.txt File](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file.html#id8770fd72-81ea-48b6-b747-d0274f37860b)
- [Create the bootstrap.xml File](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-bootstrapxml-file.html#id61aa8472-5aba-41c5-ac4f-4a409e3dedb6)
- [Prepare
the Licenses for Bootstrapping](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-licenses-for-bootstrapping.html#idb9fa0ce2-b855-435b-a9b4-5ab7b61a8353)
- [Prepare
the Bootstrap Package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package.html#id5575318c-1de8-497a-960a-1d7417feefa6)
- [Bootstrap
the VM-Series Firewall on AWS](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-in-aws.html#idaaf52d9b-e0bc-4277-834a-23b9a720f448)
- [Bootstrap
the VM-Series Firewall on Azure](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-in-azure.html#idd51f75b8-e579-44d6-a809-2fafcfe4b3b6)
- [Bootstrap the VM-Series Firewall on Azure Stack HCI](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-on-azure-stack-hci.html)
- [Bootstrap
the VM-Series Firewall on ESXi](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-on-esxi.html#id90a58042-2a56-4f23-9efd-3fc6d317c768)
- [Bootstrap
the VM-Series Firewall on Google Cloud Platform](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-on-google.html#id17CRC0V0TR0)
- [Bootstrap
the VM-Series Firewall on Hyper-V](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-on-hyper-v.html#id8daf3d1b-4da7-4dd4-a7c1-3d6c08044986)
- [Bootstrap
the VM-Series Firewall on KVM](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-on-kvm.html#idf5df16ed-a196-47e9-942c-f9b073aee944)
- [Verify
Bootstrap Completion](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/verify-bootstrap-completion.html#id08da20f6-d19b-4a28-9d2d-f4945ebeb230)
- [Bootstrap
Errors](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-errors.html#id3807f302-3037-4816-ac66-7f7ba9073a7d)