<!-- Source: https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/onboard-and-activate-cloud-account-in-scm -->
<!-- Fetched: 2026-03-31T18:59:39.437580+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: scm, cloud-account, airs -->

# Onboard and Activate a Cloud Account in Strata Cloud Manager

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Prisma AIRS Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Activation & Onboarding
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Administration
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 AI Model Security
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 AI Red Teaming
 

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
                            
                                    Deployment Workflow for VM-Series and Prisma AIRS](/content/techdocs/en_US/ai-runtime-security/activation-and-onboarding/universal-image-for-prisma-airs.html)
 

 
 

**[Next
                                
                                    Onboard Cloud Account in GCP](/content/techdocs/en_US/ai-runtime-security/activation-and-onboarding/onboard-and-activate-cloud-account-in-scm/gcp-onboarding-prereq-and-steps.html)
 

 

---

 
 
 















 

# Onboard and Activate a Cloud Account in Strata Cloud Manager



 



 Onboard and activate your cloud account in Strata Cloud Manager for asset
 discovery.



 
 






















 

- 

- [Prisma AIRS Licenses](/content/techdocs/en_US/ai-runtime-security/activation-and-onboarding/activate-your-ai-runtime-security-license.html)
- [Create and Associate a Deployment Profile for Prisma AIRS AI Runtime Firewall](/content/techdocs/en_US/ai-runtime-security/activation-and-onboarding/create-an-ai-instance-deployment-profile-in-csp.html)
- [Prisma AIRS AI Runtime Firewall Prerequisites and Limitations](/content/techdocs/en_US/ai-runtime-security/activation-and-onboarding/prerequisites.html)
- [Add a template and device
                                            group in Panorama](https://docs.paloaltonetworks.com/ai-runtime-security/administration/deploy-panorama-managed-airs-firewall/panorama-config-protect-vms-k8s-post-deployment)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| Onboarding cloud account in Strata Cloud Manager for assets
                                        discovery |  |



 Onboard your cloud account to enable cloud asset discovery, including AI
 and non-AI applications, models, and data. This workflow also discovers VM
 workloads, clusters, network traffic, and serverless workloads for Azure and
 AWS.

 The discovery process monitors assets protected by:
- Prisma AIRS AI Runtime firewall managed by Strata Cloud Manager or Panorama.
- VM-Series firewall.

 
 Strata Cloud Manager will not detect or manage VM-Series deployed outside of the Prisma AIRS onboarding discovery workflow.

 The discovery includes monitoring network traffic from VM workloads and clusters
 (pods). For more information on viewing your discovered assets, see [Discover Your Cloud Resources](https://docs.paloaltonetworks.com/ai-runtime-security/administration/discover-your-cloud-resources).

 **Figure: Cloud account onboarding workflow overview**

 
 

 
 

1.  Follow the onboarding workflow for your cloud provider:
 
  - [Onboard Cloud Account in GCP](/content/techdocs/en_US/ai-runtime-security/activation-and-onboarding/onboard-and-activate-cloud-account-in-scm/gcp-onboarding-prereq-and-steps.html)
  - [Onboard Cloud Account in AWS](/content/techdocs/en_US/ai-runtime-security/activation-and-onboarding/onboard-and-activate-cloud-account-in-scm/aws-onboarding-prereqs-and-steps.html)
  - [Onboard Cloud Account in Azure](/content/techdocs/en_US/ai-runtime-security/activation-and-onboarding/onboard-and-activate-cloud-account-in-scm/azure-onboarding-prereqs-and-steps.html)