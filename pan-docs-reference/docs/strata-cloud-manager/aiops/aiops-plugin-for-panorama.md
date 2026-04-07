<!-- Source: https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/about/aiops-plugin-for-panorama -->
<!-- Fetched: 2026-04-01T01:59:36.573472+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags:  -->

# Panorama CloudConnector Plugin

 

 
 
 
 
 
 

 

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

 
 
 **

[Previous
                            
                                    How to Activate Strata Cloud Manager](/content/techdocs/en_US/strata-cloud-manager/aiops/about/activate-aiops-for-ngfw.html)
 

 
 

**[Next
                                
                                    Troubleshoot NGFW Connectivity and Policy Enforcement Anomalies](/content/techdocs/en_US/strata-cloud-manager/aiops/about/troubleshooting.html)
 

 

---

 
 
 















 

# Panorama CloudConnector Plugin



 Learn about the Panorama CloudConnector Plugin and what you need to get
 started.



 
 






















 

- [Software NGFW
                                            Credits](https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/software-ngfw)

- [Strata Cloud Manager Pro](https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/strata-cloud-manager-licenses-and-support)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW, including those funded by | AIOps for NGFW Premium or |



 Want to proactively check your policy rules for adherence to best practices? You
 should not have to wait to get an alert and then fix a problem after you’ve pushed
 your policy rules. Connect AIOps for NGFW or Strata Cloud Manager to your Panorama
 to evaluate your configuration against certain best practice checks before pushing
 it to your managed firewalls. See [Proactively Enforcing Security Checks](https://docs.paloaltonetworks.com/strata-cloud-manager/aiops/security-posture/proactively-enforce-security-checks).

 Updates to your Security policy rules are often time-sensitive and require
 you to act quickly. However, you want to ensure that any update you make to your
 security policy rulebase meets your requirements and does not introduce errors or
 misconfigurations (such as changes that result in duplicate or conflicting
 rules).

 To achieve this, the Policy Analyzer in Strata Cloud Manager enables you to
 optimize time and resources when implementing a change request. Policy Analyzer not
 only analyzes and provides suggestions for possible consolidation or removal of
 specific rules to meet your intent but also checks for anomalies, such as Shadows,
 Redundancies, Generalizations, Correlations and Consolidations in your rulebase.

 Connect AIOps for NGFW or Strata Cloud Manager to your Panorama and use
 Policy Analyzer to add or optimize your Security policy rulebase. See [Policy Analyzer](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/security-posture/policy-analyzer).

 You’ll need these things to connect AIOps for NGFW to your Panorama: 

 

-  AIOps for NGFW or Strata Cloud Manager instance: You don't need an AIOps for
 NGFW Premium license to install the Panorama CloudConnector plugin. However, the
 Premium license is required to use premium features like the Policy Analyzer and
 Proactive Best Practice Assessment (BPA). 
-  A Panorama with a [device certificate installed](https://docs.paloaltonetworks.com/panorama/10-2/panorama-admin/set-up-panorama/install-the-panorama-device-certificate). 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

-  The Panorama CloudConnector Plugin
 [installed](https://docs.paloaltonetworks.com/panorama/10-1/panorama-admin/panorama-plugins/about-panorama-plugins/install-panorama-plugins) on your Panorama running PAN
 OS 10.2.3 and above. You need to enable this plugin using the command:

>
 request plugins cloudconnector enable basic
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 
 
  - To help customers, we have preinstalled this plugin with newer
 Panorama versions (11.0.1 and above).
  - If you have already installed both the AIOps plugin and the
 CloudConnector plugin, uninstall the AIOps plugin, as they are
 identical and only the name has changed. Ensure that you have only
 one plugin installed, which should be the latest version of the
 CloudConnector plugin. 

If you installed the AIOps plugin on PAN-OS 10.2.3 and then upgraded
 to PAN-OS 11.0.1 or later, a default version of the plugin will be installed
 with the new PAN-OS version. This results in both plugins being present on
 Panorama. In this case, follow these steps:

  1. In the Panorama web interface, select Panorama >
 Plugins and Uninstall the
 AIOps plugin.

  2. Enable the CloudConnector plugin:

>
 request plugins cloudconnector enable basic
CloudConnector plugin 2.2.0 supports proxy configuration
 settings from Panorama. These settings only take effect after a commit. Here
 are the scenarios:

  - Configuring Proxy Settings: When you configure proxy settings and
 perform a commit, the CloudConnector plugin won't recognize the new
 proxy settings during this commit. After the commit, the plugin will
 use the proxy configuration for future interactions with the cloud.
 

  - Removing Proxy Settings: When you remove proxy settings and perform a
 commit, the CloudConnector plugin won't recognize the removed proxy
 settings during the commit. After the commit, the plugin will no
 longer use the proxy configuration for future interactions with the
 cloud.

-  [Device telemetry](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/device-telemetry) enabled
on your Panorama. 
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

-  A [security policy rule](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/policy/security-policy/create-a-security-policy-rule) that
allows communication between Panorama and the FQDN that corresponds
to your Strata Logging Service host region: 






















 

| Americas (americas) | https://prod.us.secure-policy.cloudmgmt.paloaltonetworks.com/ |
| --- | --- |
| Australia (au) | https://prod.au.secure-policy.cloudmgmt.paloaltonetworks.com/ |
| Canada (ca) | https://prod.ca.secure-policy.cloudmgmt.paloaltonetworks.com/ |
| Europe (europe) | https://prod.eu.secure-policy.cloudmgmt.paloaltonetworks.com/ |
| FedRAMP (gov) | https://prod.gov.secure-policy.cloudmgmt.paloaltonetworks.com/ |
| Germany (de) | https://prod.de.secure-policy.cloudmgmt.paloaltonetworks.com/ |
| India (in) | https://prod.in.secure-policy.cloudmgmt.paloaltonetworks.com/ |
| Japan (jp) | https://prod.jp.secure-policy.cloudmgmt.paloaltonetworks.com/ |
| Singapore (sg) | https://prod.sg.secure-policy.cloudmgmt.paloaltonetworks.com/ |
| United Kingdom (uk) | https://prod.uk.secure-policy.cloudmgmt.paloaltonetworks.com/ |