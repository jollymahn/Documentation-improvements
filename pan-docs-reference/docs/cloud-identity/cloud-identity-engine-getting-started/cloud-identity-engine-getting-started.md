<!-- Source: https://docs.paloaltonetworks.com/cloud-identity/cloud-identity-engine-getting-started -->
<!-- Fetched: 2026-03-31T18:05:31.139560+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: identity, cie -->

# Get Started with Cloud Identity Engine

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Identity Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Activation & Onboarding
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Cloud Identity Engine
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Help
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Release Notes
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 

 

 

 

 

 
 
 
---

 
 

 
 

**[Next
                                
                                    Cloud Identity Engine Licensing](/content/techdocs/en_US/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing.html)
 

 

---

 
 
 















 

# Get Started with Cloud Identity Engine



 How to get started with the Cloud Identity Engine.



 






















 

- 
- 
[here](https://docs.paloaltonetworks.com/identity/activation-and-onboarding/get-started-with-the-cloud-identity-engine/cloud-identity-engine-licensing)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFWPrisma Access | The Cloud Identity Engine service is free; however, the enforcement
                            points utilizing directory data may require specific licenses. Click
                                 for more
                            information. |


Welcome to the Cloud Identity Engine! The Cloud Identity Engine provides a centralized,
 cloud-native source of truth for user identity and authentication, enabling your
 organization to move toward a Zero Trust security posture. By aggregating and
 normalizing identity data from on-premises, cloud-based, and hybrid infrastructures, the
 service allows you to enforce consistent security policies based on users and groups
 rather than IP addresses,. This ensures that security decisions remain accurate and
 effective across data centers, campuses, public clouds, and remote user
 environments.

Deployment begins with planning your architecture, specifically selecting the appropriate
 region to ensure compliance with data residency regulations and defining the visibility
 scope to control firewall access to your tenants. Next, you activate the service within
 the Palo Alto Networks Hub to provision your tenant and prepare for synchronization. You
 then set up your identity sources by installing the Cloud Identity Agent for on-premises
 directories or establishing secure API connections for cloud-based providers like
 Microsoft Entra ID and Okta. Finally, you associate the Cloud Identity Engine with your
 Palo Alto Networks applications, such as Prisma Access or Next-Generation Firewalls, to
 enable them to consume identity data for policy enforcement.