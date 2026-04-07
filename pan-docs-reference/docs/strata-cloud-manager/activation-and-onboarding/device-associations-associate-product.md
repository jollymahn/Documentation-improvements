<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/device-associations-associate-product -->
<!-- Fetched: 2026-03-31T18:30:09.823178+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: scm, device-associations -->

# Device Associations (Associate Devices with a Product)

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Strata Cloud Manager Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Activation & Onboarding
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Subscription & Tenant Management
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Getting Started
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 AIOps
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Release Notes
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 

 

 

 

 

 
 
 
---

 
 

 

 

---

 
 
 















 

# Device Associations (Associate Devices with a Product)



 Learn about associating your devices with a product.



 After activating the license for a [supported product](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager.html), you
 use Device Associations to
 specify the firewalls or Panorama appliances that you want to use with the
 product.

1.  Activate your product license.How you do this depends on the license you are activating. Please see the
 specific product documentation for more details. You can also see the license
 compatibility with Strata Cloud Manager here.

2.  Navigate to Device Associations using the 
 Activation Console or Strata Cloud Manager.
  1.  (Optional) Log in to the 
 [Activation Console](https://apps.paloaltonetworks.com/hub) using your Palo Alto Networks CSP credentials and select Common ServicesDevice Associations.
 
 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 

  2.  (Optional) Log into Strata Cloud Manager and select SettingsDevice Associations.
 

3.  Associate products with firewalls or Panorama appliances.
 
 

 

  1.  Select Associate Products.
 
  2.  In the Products selection column, select the product you want to
 associate.
  3.  If applicable, select the type of license.Some products have licenses for specific validity terms and device
 models. Only the devices [compatible with the license type](/content/techdocs/en_US/strata-cloud-manager/activation-and-onboarding/device-associations-in-stata-cloud-manager/firewall-and-license-type-compatibility.html)
 you selected will appear for association.

  4.  Select
 devices.
  5.  Save or Apply Licenses.
 

4.  Verify that the association was successful.If the association failed, copy the error ID and follow [the steps to open a support case](https://docs.paloaltonetworks.com/sase/prisma-sase-multitenant-platform/related-documentation/open-support-case). When
 opening the support case, be sure to include the error ID, device serial number,
 TSG ID, and the name of the product that failed association.

5.  Return to the documentation for the product you are associating for further
 onboarding steps.