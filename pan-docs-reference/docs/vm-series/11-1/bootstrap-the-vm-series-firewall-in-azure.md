<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-the-vm-series-firewall-in-azure -->
<!-- Fetched: 2026-03-31T18:05:01.314695+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Bootstrap the VM-Series Firewall on Azure



 



 Use the Azure Files service to bootstrap the VM-Series
Firewall on Azure.



 The VM-Series firewall on Azure supports Azure
Files service for bootstrapping. 

1.  [Choose a bootstrap
method](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/choose-a-bootstrap-method.html#idf6412176-e973-488e-9d7a-c568fe1e33a9).
  - To [add a basic configuration
to the bootstrap package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/choose-a-bootstrap-method.html#idf6412176-e973-488e-9d7a-c568fe1e33a9_idf453f878-b5e1-4793-bbf7-a047ec994d07), continue to Step 2. 

To
manage the bootstrap package for the VM-Series firewall on Azure,
you must be familiar with storage accounts on Azure and know how
to create a file share and directory objects that contain the folder
structure required for the bootstrap package. You can share an Azure
file share across many virtual machines so that all firewalls deployed
in the same region as the storage account that hosts the file share
can access the files concurrently.

The management interface
of the VM-Series firewall must be able to access the file share
that holds the bootstrap package so that it can complete bootstrapping.

  - To [Enter a Basic Configuration as User Data (AWS, Azure, or GCP)](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/choose-a-bootstrap-method.html#idf6412176-e973-488e-9d7a-c568fe1e33a9_id3433e9c0-a589-40d5-b0bd-4bc42234aa0f), continue
to Step 3.2.

2.  Set up
the bootstrap package within an Azure Files service.
  1.  On the Azure portal, select or create a
storage account.
  2.  Create a file share within the Azure Files service.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

  3.  Create the folders within the storage account.
    - [Create the top-level
directory structure for the bootstrap package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package.html#id5575318c-1de8-497a-960a-1d7417feefa6_id18a5a1de-0b4c-46f2-ae9a-bd49af0678aa) directly in the
root folder and create a subfolder for each bootstrap configuration.
    - [Add
content folders within each folder.](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package.html#id5575318c-1de8-497a-960a-1d7417feefa6_id899d49ac-2baf-4b68-9117-a86afcc5b5ba) You can leave a folder
empty but you must have all four folders (config, license, software
and content) in the parent folder. In the following screenshot,
you can see that the config folder
has the init-cfg.txt file uploaded
to it.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

3.  [Deploy
the VM-Series Firewall from the Azure Marketplace (Solution Template)](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-azure/deploy-the-vm-series-firewall-on-azure-solution-template.html#ide37bac08-683a-4245-a412-2f74a56855fa). 
  - If you are using a file to configure the firewall,
continue to Step 3.1

  - If you are using custom data to configure the firewall, continue
to Step 3.2.

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

  1.  If
you choose to use the bootstrap package, select Enable
Bootstrap: Yes and provide the information required
to access the file share that holds the bootstrap files.
    1. **Storage Account Name**— This is the Azure
storage account in which you created the file share for the bootstrap
folders.

    2. **Storage Account Access Key**—The firewall needs this
access key to authenticate to the storage account and access the
files stored within. To copy this access key, select the storage
account name, and then select SettingsAccess Keys.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

    3. **File-share**—The file-share name that contains the bootstrap
package.

    4. (Optional) Share-directory—The
path to a subfolder within the file-share. If you have a common
file share that serves as a repository for bootstrap configurations
for different set ups, you can use a share-directory to create a folder
hierarchy and access a specific set of subfolders within the common file-share.

  2.  Enter
the configuration parameters as custom data. For the key-value pairs,
see [Enter a Basic Configuration as User Data (AWS, Azure, or GCP)](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/choose-a-bootstrap-method.html#idf6412176-e973-488e-9d7a-c568fe1e33a9_id3433e9c0-a589-40d5-b0bd-4bc42234aa0f). Separate
each key-value pair with a semicolon. For example:
```
type=dhcp-client; op-command-modes=jumbo-frame;
vm-series-auto-registration-pin-id=abcdefgh1234****;
vm-series-auto-registration-pin-value=zyxwvut-0987****
```
Provide
custom data using one of the methods in [Custom data and Cloud-Init on
Azure Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/custom-data).

4.  [Verify
Bootstrap Completion](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/verify-bootstrap-completion.html#id08da20f6-d19b-4a28-9d2d-f4945ebeb230).