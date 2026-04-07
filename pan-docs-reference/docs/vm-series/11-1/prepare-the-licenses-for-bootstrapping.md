<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-licenses-for-bootstrapping -->
<!-- Fetched: 2026-03-31T18:04:54.887551+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Prepare the Licenses for Bootstrapping



 



 To license the firewall during the bootstrapping
process, you must purchase the auth codes and register the licenses
and subscriptions on the Palo Alto Networks Support portal before
you begin bootstrapping. 

For the VM-Series firewalls running
BYOL (not applicable for usage-based licensing—PAYG), you must have
an auth code bundle that includes the capacity auth code, support
subscription, and any other subscriptions you require. The process
of preparing the licenses for bootstrapping depends on whether the
firewall has Internet access when bootstrapping:

- Direct
Internet access—The firewall is connected directly to the Internet.

- Indirect Internet access—The firewall is managed by Panorama,
which has direct Internet access and the ability to fetch the license
keys on behalf of the firewall.

- No Internet access—The firewall uses an orchestration service
or a custom script to fetch the license keys on behalf of the firewall. 

-  For VM-Series firewalls with Internet
access.Enter the auth code in the /license folder
when you [Prepare the Bootstrap Package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package.html#id5575318c-1de8-497a-960a-1d7417feefa6).

-  For VM-Series firewalls with indirect Internet access.
  1.  Register the auth code on the Palo Alto
Networks Support portal.
    1. Go to the [Support portal](https://support.paloaltonetworks.com/support), log in, and
 select ProductsVM-Series Auth-CodesAdd VM-Series Auth-Code. 

    2. Follow the steps to [Register the VM-Series Firewall](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/register-the-vm-series-firewall.html#id1c0525c0-f2b8-44b4-9d11-271d53003b20).

    3. Click Submit.

  2.  Activate the auth codes on the Palo Alto Networks
Support portal to generate license keys.
    1. Go to the [Support portal](https://support.paloaltonetworks.com/support), log in,
and select the Assets tab.

    2. For each serial number, click the Action link.

    3. Select the Activate Auth-Code button.

    4. Enter the Authorization code, click Agree,
and Submit.

    5. Download the license keys and save it to a local folder.

    6. Continue to [Prepare the Bootstrap Package](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/prepare-the-bootstrap-package.html#id5575318c-1de8-497a-960a-1d7417feefa6); you must
add the license keys that you downloaded to the \license folder
in the bootstrap package.

-  For a custom script or an orchestration service that
can access the Internet on behalf of firewalls.The script or service must fetch the CPU ID and the UUID
from the hypervisor on which the firewall is deployed and access
the Palo Alto Networks Support portal with CPU ID, UUID, API key
and the auth code to obtain the required keys. See [Model-Based Licensing API](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/licensing-api.html#id0873c753-02bd-4371-9e6a-2b35cfc0a44b).