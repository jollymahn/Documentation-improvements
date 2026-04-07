<!-- Source: https://docs.paloaltonetworks.com/plugins/vm-series-and-panorama-plugins-release-notes/panorama-plugin-for-aiops/panorama-cloudconnector-plugin-3-0-0 -->
<!-- Fetched: 2026-03-31T18:05:36.352748+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: panorama, cloudconnector -->

# Panorama CloudConnector Plugin 3.0.0



 What's new for Panorama CloudConnector Plugin 3.0.0 (For AIOps and Cloud NGFW for
 AWS)



 Panorama CloudConnector plugin 3.0.0 supports the following enhancements:

- **Support for Panorama configuration operations**: You can
 synchronize configuration changes between Strata Cloud Manager and on-premises
 Panorama devices using an asynchronous communication framework. When you enable
 this plugin, you gain the ability to seamlessly propagate configuration changes
 from Strata Cloud Manager to your Panorama management platform without requiring
 direct cloud-to-on-premises network connectivity. This synchronization is
 supported for [Policy Optimizer](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/security-posture/policy-optimizer) and [Config Cleanup](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/security-posture/config-cleanup) features in Strata
 Cloud Manager.

Strata Cloud Manager provides you with comprehensive audit trails and
 status tracking for every configuration operation, ensuring you maintain full
 visibility into what changes were requested, when they were applied, and whether
 they succeeded or failed. This plugin supports multiple operation types
 including create, update, delete, and multi-configure operations, giving you
 flexibility in how you structure and deploy your configuration changes while
 maintaining the compliance of your Panorama configuration management workflows.
 All commit changes pushed to your Panorama are managed under the administrator
 name **__cloudconnector**.

Use the below command to enable or disable the synchronization after
 you enable the CloudConnector plugin:

```
> request plugins cloudconnector sync
  disable   Disable cloud connector sync functionality
  enable    Enable cloud connector sync functionality
 
> request plugins cloudconnector sync enable

```

- **Support for High Availability (HA) configurations**: When you
 deploy firewalls or Panoramas in HA configurations, Strata Cloud Manager
 simplifies management by treating paired firewalls or Panoramas as a single
 logical unit. This unification streamlines operations like policy analysis and
 configuration cleanup by preventing duplicate results and allowing you to manage
 the HA pair through one consolidated entity instead of separate device
 entries.

This feature ensures consistency during failover scenarios regardless
 of which device is currently active, policy analysis results and configuration
 cleanup operations remain accessible. Strata Cloud Manager processes each HA
 pair once, avoiding duplicated efforts across both members for policy
 optimization, configuration cleanup, or analysis operations, while still
 providing complete visibility into the health and status of both devices.

After installing the CloudConnector Plugin, you need to enable this plugin using the
 command:

> request plugins cloudconnector enable basic

 
 If you have already installed both the AIOps plugin and the CloudConnector plugin,
 uninstall the AIOps plugin, as they are identical and only the name has changed.
 Ensure that you have only one plugin installed, which should be the latest version
 of the CloudConnector plugin. 

If you installed the AIOps plugin on PAN-OS 10.2.3 and then upgraded to PAN-OS 11.0.1 or
 later, a default version of a plugin will be installed with the new PAN-OS version. This
 results in both plugins being present on Panorama. In this case, follow these steps:

1. In the Panorama web interface, select Panorama >
 Plugins and Uninstall the AIOps
 plugin.

2. Enable the CloudConnector plugin:

> request
 plugins cloudconnector enable basic

 
 If you upgrade to PAN-OS 11.0.* or 11.1.* without the
 CloudConnector plugin installed, you may receive an incorrect plugin version by default.
 To resolve this, you must uninstall the incorrect version and install the latest
 CloudConnector plugin.

Here is the support for CloudConnector Plugin 3.0.0.
























 ************

| Panorama | Version Range | Installation Method |
| --- | --- | --- |
| 10.2.x | 10.2.3 and later | Manual Download
                            Download via Customer Support Portal or Panorama >
                                Plugins. |
| 11.x | All Versions | Manual Download
                            Download via Customer Support Portal or Panorama >
                                Plugins. |
| 12.1.x | 12.1.2 | CloudConnector Plugin 2.1.0 is preinstalled.
                            Upgrade to PAN-OS 12.1.4 or later to use the CloudConnector
                                Plugin 3.0.0. |
| 12.1.4 and later | Preinstalled (Bundled) |  |