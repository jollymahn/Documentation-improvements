<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/about-the-vm-series-firewall/vm-series-plugin/upgrade-the-vm-series-plugin -->
<!-- Fetched: 2026-03-31T18:04:59.254999+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Upgrade the VM-Series Plugin



 



 
 When a plugin update is released independent
 of PAN-OS, you can independently upgrade the plugin version from
 your VM-Series firewall (like software or content updates) or from
 a bootstrap file.

 Each plugin version provides PAN-OS compatibility
 information and includes new features or bug fixes for one or more
 cloud environments.

 

1.  Before upgrading, check the latest Release Notes
 for details on whether a new VM-Series plugin affects your environment.
 For example, suppose a new VM-Series plugin version only
 includes AWS features. To take advantage of the new features, you
 must update the plugin on your VM-Series firewall instances on AWS. 

 
 
 Do not install an upgrade that does not
 apply to your environment.

 
 
 VM-Series 3.0.0 Plugin is supported only in PAN-OS 10.2.0.

 

2.  Log in to the VM-Series firewall and check the dashboard
 to view the plugin version.
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

3.  Select
 PanoramaPlugins 
 
 
 

  and type
 vm_series in
 the search field.
 
 Select
 Check Now to view the available
 versions.
 

 

4.  Choose a VM-Series plugin version and click
 Download. 
 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

5.  When the download finishes, click
 Install in
 the
 Actions column. 
 
 The firewall automatically uninstalls the previously installed
 version of the plugin.

 

6.  View the
 Dashboard to verify that
 the plugin upgraded successfully.