<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/verify-bootstrap-completion -->
<!-- Fetched: 2026-03-31T18:05:02.359791+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Verify Bootstrap Completion



 



 You can see basic status logs on the console
during the bootstrap and you can verify that the process is complete.

1.  If you included panorama-server, tplname,
and dgname in your init-cfg.txt file, check
Panorama managed devices, the device group, and the template name.
2.  Verify the general system settings and configuration.
Access the web interface and select DashboardWidgetsSystem or
use the CLI operational commands show system info and showconfig running.
3.  Verify the license installation. Select DeviceLicenses or
use the CLI operational command request license info.
4.  If you have Panorama configured, manage the content versions
and software versions from Panorama. If you do not have Panorama
configured, use the web interface to manage content versions and
software versions.