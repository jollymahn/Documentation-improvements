<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-nsx/set-up-the-vm-series-firewall-on-nsx-t-east-west/deploy-the-vm-series-using-the-security-centric-workflow/create-templates-and-device-groups-nsx-t-ew-security-centric -->
<!-- Fetched: 2026-03-31T18:04:44.900025+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Create Template Stacks and Device Groups on Panorama



 



 



 To manage the VM-Series firewalls for NSX-T
using Panorama, the firewalls must belong to a device group and
a template that is a member of a template stack. Device groups allow
you to assemble firewalls that need similar policies and objects
as a logical unit; the configuration is defined using the Objects and Policies tabs
on Panorama. Use template stacks to configure the settings that
are required for the VM-Series firewalls to operate on the network
and associate; the configuration is defined using the Device and Network tabs
on Panorama. And each template stack with zones used in your NSX-T
configuration on Panorama must be associated with a service definition
that you will create later; at a minimum, you must create a zone
within the template stack so that the NSX-T Manager can redirect
traffic to the VM-Series firewall. Later, you will associate a device
group and template to your NSX-T deployment create a [service definition](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-nsx/set-up-the-vm-series-firewall-on-nsx-t-east-west/deploy-the-vm-series-using-the-security-centric-workflow/configure-the-service-definition-on-panorama-nsx-t-ew-security-centric.html#id94ddc10d-8ed8-45f2-8d68-4780432e136d).

Panorama
can support deployments of both NSX-T North-South and NSX-T East-West
at the same time. You must configure separate device groups, template
stacks, and service definitions for NSX-T North-South and NSX-T
East-West. 

1.  Add a device group or a device group hierarchy.
  1.  Select PanoramaDevice Groups, and click Add.
You can also create a [device group hierarchy](https://docs.paloaltonetworks.com/panorama/11-1/panorama-admin/manage-firewalls/manage-device-groups/create-a-device-group-hierarchy).
  2.  Enter a unique Name and a Description to
identify the device group.
  3.  Click OK.
  4.  Click Commit and select Panorama as
the Commit Type to save the changes to the
running configuration on Panorama.

2.  Add a template.
  1.  Select PanoramaTemplates, and click Add. 
  2.  Enter a unique Name and a Description to
identify the template.
  3.  Click OK.
  4.  Click Commit, and select Panorama as
the Commit Type to save the changes to the
running configuration on Panorama.

3.  Create a template stack and add your newly created template.
  1.  Select PanoramaTemplates, and click Add
Stack. 
  2.  Enter a unique Name and a Description to
identify the template stack.
  3.  Under Templates, click Add and
select the template you created in step 2 from the drop-down.
  4.  Click OK.
  5.  Click Commit, and select Commit
to Panorama to save the changes to the running configuration
on Panorama.

4.  Create
the zone(s) for each template.The Panorama plugin for VMware NSX maps each zone to a
service profile on NSX-T Manager. To qualify, a zone must be of
the virtual wire type and be part of a template you will associate
with a service definition; see [Configure the Service Definition on Panorama](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/set-up-the-vm-series-firewall-on-nsx/set-up-the-vm-series-firewall-on-nsx-t-east-west/deploy-the-vm-series-using-the-security-centric-workflow/configure-the-service-definition-on-panorama-nsx-t-ew-security-centric.html#id94ddc10d-8ed8-45f2-8d68-4780432e136d) for more information.
In most uses cases, a single zone is sufficient. However, you must
create multiple zones for multi-tenancy

You can add up to
32 zones in each template.

  1.  Select NetworkZones.
  2.  Select the correct template in the Template drop-down.
  3.  Select Add and enter a zone Name.
  4.  Set the interface Type to Virtual
Wire.
  5.  Click OK.
  6.  Verify that the zones are attached to the correct
template.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

  7.  Click Commit, and select Panorama as
the Commit Type to save the changes to the
running configuration on Panorama.

5.  Update the DNS and NTP server information of your template
stack. You must complete this step if you are [using device certificates](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/install-a-device-certificate-on-the-vm-series-firewall.html#id63b6c128-5973-469e-bd4a-bdc6da5cb3df) in your
deployment. This is required to ensure the firewalls deployed in
your NSX-T environment have the correct DNS information needed to
reach the device certificate server.
  1.  Verify that you specified the correct template
stack from the Template drop-down.
  2.  Select DeviceSetupServices and
click the Edit icon.
  3.  On the Services tab, enter the IP address of the Primary
DNS Server and Secondary DNS Server.
  4.  On the NTP tab, enter the IP address of the NTP
Server.
  5.  Click OK.
  6.  Commit your changes to Panorama.