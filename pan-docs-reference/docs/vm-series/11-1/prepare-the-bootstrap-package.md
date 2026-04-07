<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package -->
<!-- Fetched: 2026-03-31T18:04:56.064510+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Prepare the Bootstrap Package



 



 On AWS, Azure, or GCP, you can create the
bootstrap package in your public cloud storage. 

- VM-Series
plugin version 1.0.13 and earlier, and versions 2.0.0 and 2.0.1 support
one bootstrap package per storage bucket.

- VM-Series plugin versions 2.0.2 and later also support subfolders
within your public cloud storage bucket. Within a bucket you can
create multiple folders and subfolders, each containing a bootstrap
package. Typically a folder represents configuration for a group
of VMs, such as a Panorama device group.

To access the bootstrap
package, specify the full path to the bootstrap folder. For example: my-storage/my-firewalls/bootstrap-2020-10-15

Use
the following procedure to prepare the bootstrap package. 

1.  Create
the top-level directory structure for the bootstrap package.On your local client or laptop, or in a public cloud storage
bucket, create the following folders:

```
/config 
/content 
/software 
/license
/plugins
```
You can leave a folder empty, but
you must have /config, /license, /software,
and /content folders. The /plugins folder
is optional, and only required if you are upgrading the [VM-Series plugin](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/about-the-vm-series-firewall/vm-series-plugin.html#id729e85bb-240c-42d5-af95-852a95b62c2a) independent
of a PAN-OS release.

Do not place any other files or folders
in the bootstrap structure. Adding other files or folders will result
in a bootstrapping failure. 

```
/my-storage                     
   /my-firewalls                
      /internal     /external   
        /config        /config  
        /content       /content 
        /license       /license 
        /plugins       /plugins 
        /software      /software
```

2.  Add content
within each folder.For an overview of the process, see [Bootstrap
Package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-package.html#id88dce8d3-3665-4794-b7ed-0fd47581ebd2). For details on the files in the /config folder,
see [Bootstrap
Configuration Files](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-configuration-files.html#id37d59976-16c6-4c75-af8a-61f46e690d65).

```
/config 
  0008C100105-init-cfg.txt 
  0008C100107-init-cfg.txt 
  bootstrap.xml
/content 
  panupv2-all-contents-488-2590 
  panup-all-antivirus-1494-1969 
  panup-all-wildfire-54746-61460 
/software 
  PanOS_vm-10.0.0 
/license
  authcodes 
  0001A100110-url3.key
  0001A100110-threats.key 
  0001A100110-url3-wildfire.key
/plugins
  vm_series-2.0.2
```

 
 
  - If you save the keys to the license folder,
you can use a file naming convention that works for you, but keep
the .key extension in the filename. For auth
codes, create a text file named authcodes (without
a file extension), add your auth codes to that file, and save it
to the license folder.

  - Use an auth code bundle instead of individual auth codes
so that the firewall or orchestration service can simultaneously
fetch all license keys associated with a firewall. If you use individual
auth codes instead of a bundle, the firewall will retrieve only
the license key for the first auth code included in the file.

  - In the /plugins folder, supply only
one VM-Series plugin binary. Do not supply multiple plugin versions.

3.  Create the bootstrap package.For VM-Series firewalls, create the image in the appropriate
format for your hypervisor. See [Bootstrap Package Delivery](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-package.html#id88dce8d3-3665-4794-b7ed-0fd47581ebd2_id6465dc83-5fde-4e8e-92e1-38c067ea5e8a).