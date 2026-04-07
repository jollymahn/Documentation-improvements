<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-bootstrapxml-file -->
<!-- Fetched: 2026-03-31T18:04:53.836115+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Create the bootstrap.xml File



 



 Use these instructions to export the configuration
from a firewall running on the same platform or hypervisor as your
target deployment.

1.  Export a configuration from a firewall.
  1.  Select DeviceSetupOperations.
  2.  Select the configuration file you want to export.
    - To export the running configuration, in the Configuration
Management section, Export named configuration snapshot and
select running config.xml from the drop-down.

    - To export a previous version of a firewall configuration,
in the Configuration Management section, Export configuration
version and select the appropriate configuration version
in the drop-down.

2.  Rename the configuration file and save.
  1.  Rename the file to bootstrap.xml. For the bootstrap process to be successful, the filename
must be an exact (case-sensitive) match.

  2.  Save the bootstrap.xml file in
the same location as the init-cfg.txt file.