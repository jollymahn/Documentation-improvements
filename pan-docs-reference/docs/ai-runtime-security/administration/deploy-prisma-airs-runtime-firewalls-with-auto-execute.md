<!-- Source: https://docs.paloaltonetworks.com/ai-runtime-security/administration/deploy-prisma-airs-runtime-firewalls-with-auto-execute -->
<!-- Fetched: 2026-03-31T18:59:37.717926+00:00 -->
<!-- Project: c-docs-scm -->
<!-- Tags: scm, prisma-airs, deploy -->

# Deploy Prisma AIRS Runtime and VM-Series Firewalls with Auto-Execute

 

 
 
 
 
 
 

 

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
                            
                                    Harvest IP-Tags from Kubernetes Clusters Secured by Panorama Managed Prisma AIRS AI Runtime Firewall](/content/techdocs/en_US/ai-runtime-security/administration/deploy-panorama-managed-airs-firewall/harvest-ip-tags-for-panorama-managed-firewalls.html)
 

 
 

**[Next
                                
                                    Manage Auto-Execute Deployed Firewalls](/content/techdocs/en_US/ai-runtime-security/administration/manage-auto-execute-deployed-firewalls.html)
 

 

---

 
 
 















 

# Deploy Prisma AIRS Runtime and VM-Series Firewalls with Auto-Execute



 Learn about the Auto-Execute workflow and Cloud Mesh.



 






















 

- 

- [Onboard Cloud Account in
                                        AWS](https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/onboard-and-activate-cloud-account-in-scm/aws-onboarding-prereqs-and-steps)
- [Onboard Cloud Account in
                                        Azure](https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/onboard-and-activate-cloud-account-in-scm/azure-onboarding-prereqs-and-steps/onboard-azure-cloud-account-in-scm)

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| Prisma AIRS AI Runtime Firewall |  |


Multi-Cloud Security Fabric (MSF) Auto-Execute orchestrates the complete lifecycle of AI
 Runtime firewall and VM-Series firewall infrastructure provisioning and traffic
 redirection across cloud environments. The deployment process transforms complex manual
 tasks into an intelligent, automated workflow that minimizes configuration errors and
 reduces deployment time from hours to minutes.

After completing network discovery using the [Prisma AIRS Cloud Asset Map](/content/techdocs/en_US/ai-runtime-security/administration/discover-your-cloud-resources/cloud-asset-map.html),
 administrators can select specific applications and traffic flows directly from the
 topology view. This approach pre-populates deployment parameters based on discovered
 network relationships and traffic patterns. The Auto-Execute workflow deploys and
 configures:

- **Security VPCs in AWS and VNets in Azure**—Appropriately sized subnets for
 management, dataplane, and high availability requirements. Additionally, Prisma AIRS
 deploys internet gateways for firewall management and internet egress traffic.
- **AI Runtime and VM-Series firewall instances**—Firewall instances sized based on
 expected traffic volume,automatic licensing and activation, and bootstrapping
 configuration for zero-touch provisioning. 
- **Load balancer configuration**—Load balancers automatically configured to
 distribute traffic across multiple firewall insatnces, maintain session persistence,
 and scale firewall capacity based on traffic demands. 
- **Route table configuration**—Prisma AIRS automatically modifies existing route
 tables and creates new routes to redirect traffic to firewall instances.
This automated approach transforms traditional firewall deployment from a complex,
 multi-day project into a streamlined process that can be completed in minutes while
 ensuring optimal security coverage and minimal operational disruption.

Multi-cloud environments present unique challenges for secure traffic routing,
 particularly when applications need to communicate across different cloud providers or
 regions. Cloud Mesh addresses this challenge by establishing secure tunnels between Palo
 Alto Networks firewalls deployed in different cloud environments, creating a cohesive
 security fabric that spans your entire multi-cloud infrastructure.

 At its core, Cloud Mesh works by creating an Auto VPN cluster between
 firewalls, enabling secure communication paths between applications regardless of their
 location. When you enable mesh during deployment, the service configures VPN tunnels
 between designated firewalls and handles the advertisement of selected routes to ensure
 traffic flows securely through these tunnels while being inspected by the appropriate
 security controls.

 Cloud Mesh operates as a day-zero configuration option during deployment,
 meaning it must be enabled when you first deploy your cloud infrastructure. Once
 configured, it establishes a single mesh cluster for your MSF and adds firewalls to this
 cluster as part of the deployment process.

To effectively implement Cloud Mesh, you'll need to understand several key
 components. First, the Strata Cloud Manager (SCM) serves as the control plane for
 configuring and managing the VPN connections between firewalls. Cloud Mesh interacts
 with SCM's Auto VPN feature to establish these connections. Second, you'll need to
 understand BGP redistribution profiles, which control which routes are advertised into
 the VPN tunnels. Finally, you'll need to be familiar with the orchestration service that
 triggers mesh configuration based on deployment choices.

 Cloud Mesh supports a variety of deployment scenarios, including connections
 within the same cloud across different regions and connections between different cloud
 providers. It enables secure traffic flows between applications and between applications
 and security models. The service requires firewalls to have public IP addresses
 configured on their external interfaces to establish the necessary tunnels.

 By understanding these components and their interactions, you'll be prepared
 to implement Cloud Mesh as part of your multi-cloud security strategy, ensuring that
 traffic between your applications is properly inspected regardless of where those
 applications are hosted.

- [AWS](/content/techdocs/en_US/ai-runtime-security/administration/deploy-prisma-airs-runtime-firewalls-with-auto-execute/add-ai-instance-for-aws-auto.html#add-ai-instance-for-aws)
- [Azure](/content/techdocs/en_US/ai-runtime-security/administration/deploy-prisma-airs-runtime-firewalls-with-auto-execute/add-ai-instance-for-azure-auto.html#add-ai-instance-for-azure)

















 

# AWS



 Complete the deployment workflow in Strata Cloud Manager to generate the Prisma AIRS AI Runtime Firewall Terraform template.



 
 Learn how to automatically deploy the AI Runtime Firewall to protect your AWS cloud
 resources.

 In this page, you will configure Prisma AIRS AI Runtime
 Firewall in Strata Cloud Manager and deploy it in your AWS environment. This
 workflow integrates the AI Runtime Firewall or VM-Series in your cloud network
 architecture, enabling comprehensive monitoring and protection of your assets.

 After onboarding the cloud account, the Prisma AIRS Cloud Asset Map
 displays which regions have unprotected applications and VPCs. Unprotected regions
 and partially protected regions, and the internet are marked in red and orange until
 you add firewall protection. 

 

1.  Log in to [Strata Cloud Manager](http://stratacloudmanager.paloaltonetworks.com/).
2.  Navigate to AI Security AI Runtime Firewall.
3.  Select **Add Protections **("+" icon).
4.  **Select Cloud Service Provider** as AWS and choose **Next. **
 
 If you arrived at the Firewall Deployment wizard
 from the Cloud Asset Map, the cloud service is already
 selected.

 
 

 

5.  In Firewall Placement, select:
  1.  Select the Traffic Streams to Inspect:
 
    - AI queries and responses: traffic between
 your applications and AI models
    - Inbound traffic to cloud applications:
 user to application traffic
    - Outbound traffic from cloud applications:
 application to the internet traffic
    - Inter VPC/VNet communication: application
 to application traffic
    - Select All Traffic: select this option to
 inspect all traffic streams.

 

  2.  Select your AWS Account and the
 Region.
  3.  Select Auto-Execute as your Deploy
 Type.
  4.  Click Next.

 
 

 

6.  Choose Applications to Protect. Specify which discovered
 applications you want to secure with this firewall cluster. 
  1.  On the Applications tab, use the
 Select Application(s) drop-down to specify
 the discovered applications to secure. The selected application appears
 in the Applications list.
 
 
 The available applications are determined by
 the application definition criteria you configured during [cloud account onboarding](https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/onboard-and-activate-cloud-account-in-scm)
 in the “Application Definition” step.

 

  2.  Set the gateway load balancer (GWLB) endpoint CIDR and zone. Click the
 
 
 

 icon to add the second zone and GWLB
 endpoint CIDR. 
  3.  Optional Select discovered VPCs. The VPC list is prepopulated
 with the VPCs associated with any applications you specified in the
 previous step. 
 
    - Select the VPC(s). This action adds the
 selected VPC to the VPC list.
    - Select the first zone from the drop-down under GWLB
 Endpoints CIDR & Zone Pair. Then enter the
 CIDR of each subnet in the specified VPC. Prisma AIRS uses the
 CIDR(s) entered here to create new subnets in the VPC. Do not
 pre-create the subnets as doing so causes an error that prevents
 the configuration from passing the pre-deployment check.
    - Click the 
 
 

 icon to repeat this process for
 additional zones. 
 
 The GWLB endpoints
 will be created in this CIDR IP address. (Go to AWS
 management console, select your application VPC name, and
 record the IPV4 CIDR address range. Ensure to include the
 CIDR for the GWLB endpoint to be created only within this
 IPV4 CIDR range within your subnet.

 

  4.  Click Next.

7.  Configure the Deployment Parameters. The Auto-Execute
 deployment option supports AI Runtime Security; not VM-Series. The Firewall Type
 option is pre-selected based on the traffic types you previously selected on the
 Choose Traffic Flows to Inspect screen. If you select
 AI queries and responses, the Firewall Type is
 pre-selected and cannot be changed.
  1.  Specify the Number of Firewall Instances.
  2.  Specify the Deployment Zones. The selected zones
 should consist of all availability zones of the applications you want to
 protect.
  3.  Select the AWS Instance Type used by the
 deployed firewalls.
  4.  Optional Enable Deploy NAT Gateway
 through security VPC IGW through a NAT gateway (Enable this option to
 create a NAT gateway).
  5.  Optional
 Enable Overlay Routing. Overlay routing, when
 integrated with your Prisma AIRS AI Runtime
 Firewall and the AWS Gateway Load Balancer (GWLB), lets you use a
 two-zone policy to inspect egress traffic from your AWS environment.
 This allows packets to leave the Prisma AIRS
 firewall through a different interface than the one they entered
 through.For a summary of different configurations for handling egress traffic,
 refer to the **Egress Traffic Handling Scenarios on AWS**
 
 This feature is only supported on PAN-OS
 version **11.2.8 or later**. 

  6.  Optional Enable Cloud Mesh.

8.  Configure the IP Addressing Scheme.
  1.  Enter the CIDR IP address of an unused VPC. (Go
 to [AWS Management Console](https://aws.amazon.com/console/) > VPC, select
 your VPC, and get the CIDR for your VPC).
  2.  Enter your TGW information. When using the Auto-Execute deployment
 option, you must select an existing TGW; you cannot create one as part
 of your firewall deployment. 
 
    - From the TGW Cloud Account drop-down,
 select your AWS account.
    - Select the TGW ID from the
 drop-down.

 

  3.  Select a New or Existing
 Resource Access Manager (RAM). If you select Existing, choose a RAM from
 the RAM Name drop-down.
  4.  Enable **Cross-Zone load balancing** to distribute incoming traffic
 evenly across targets in multiple availability zones.

9.  Enter your Licensing information.
 
  - PAN-OS Software Version for your image from the
 available list.
  - **Flex authentication code** (Copy AUTH CODE for the [deployment profile](https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/create-an-ai-instance-deployment-profile-in-csp) you
 created for AI Runtime Security Firewall in Customer Support
 Portal).
  - Enter your [Device Certificate PIN
                                    ID](https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/activate-your-ai-runtime-security-license/generate-a-device-certificate) and Device Certificate PIN
 Value associated with Customer Support Portal
 account**.**

 

10.  Configure your Management Parameters. Firewalls deployed
 using the Auto-Execute workflow must be managed by Strata Cloud Manager;
 Panorama management is not supported.
 
  - Enter the CIDRs that can access the management interface of the firewall
 under Allowed Management Access.
  - The **SSH key to be used for login** (see how to [Create SSH keys](https://cloud.google.com/compute/docs/connect/create-ssh-keys)).
  - **Manage by SCM** and then select the **SCM folder** to group the
 Prisma AIRS AI Runtime Firewall. 
 
 For Multi-Cloud Mesh to be deployed, you must
 select the folder that contains the required Auto-VPN configuration.
 

Refer to [Workflows: Folders - Strata Cloud
                                    Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/workflows/workflows-ngfw-setup/folder-management).

 

11.  Select **Next**.
12.  In **Review architecture:**
 
 

 






















 

# Azure



 Complete the deployment workflow in Strata Cloud Manager to generate the Prisma AIRS AI Runtime Firewall Terraform template.



 
 Learn how to automatically deploy the AI Runtime Firewall to protect your Azure cloud
 resources.

 In this page, you will configure Prisma AIRS AI Runtime
 Firewall in Strata Cloud Manager and deploy it in your AWS environment. This
 workflow integrates the AI Runtime Firewall or VM-Series in your cloud network
 architecture, enabling comprehensive monitoring and protection of your assets.

 

1.  Log in to [Strata Cloud Manager](http://stratacloudmanager.paloaltonetworks.com/).
2.  Navigate to AI Security AI Runtime Firewall.
3.  Select **Add Protections **("+" icon).
4.  **Select Cloud Service Provider** as Azure and choose **Next. **
 
 
 If you arrived at the Firewall Deployment wizard
 from the Cloud Asset Map, the cloud service is already selected.

 

5.  In Firewall Placement, select:
  1.  Select the Traffic Streams to Inspect:
 
    - AI queries and responses: traffic between
 your applications and AI models
    - Inbound traffic to cloud applications:
 user to application traffic
    - Outbound traffic from cloud applications:
 application to the internet traffic
    - Inter VPC/VNet communication: application
 to application traffic
    - Select All Traffic: select this option to
 inspect all traffic streams.

 

  2.  Select your Azure Account and the
 Region.
  3.  Select Auto-Execute as your Deploy
 Type.
  4.  Click Next.

 
 

 

6.  Choose Applications to Protect. Specify which discovered
 applications you want to secure with this firewall cluster. 
 
 

 

  1.  On the Applications tab, use the
 Select Application(s) drop-down to specify
 the discovered applications to secure. The selected application appears
 in the Applications list.
 
 
 The available applications are determined by
 the application definition criteria you configured during [cloud account onboarding](https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/onboard-and-activate-cloud-account-in-scm)
 in the “Application Definition” step.

 

  2.  Click Next.

7.  Configure the Deployment Parameters. The Auto-Execute
 deployment option supports AI Runtime Security; not VM-Series. The Firewall Type
 option is pre-selected based on the traffic types you previously selected on the
 Choose Traffic Flows to Inspect screen. If you select
 AI queries and responses, the Firewall Type is
 pre-selected and cannot be changed.
  1.  Specify the Number of firewall to deploy.
  2.  Select zones to deploy firewalls. The selected
 zones should consist of all availability zones of the applications you
 want to protect.
  3.  Choose the instance type for the security VM
 used by the deployed firewalls.
  4.  Optional Enable Multi-Cloud Mesh.

8.  Configure the IP Addressing Scheme by entering the CIDR
 IP address of an unused VNet.
9.  Enter your Licensing information.
 
  - PAN-OS Software Version for your image from the
 available list.
  - **Flex authentication code** (Copy AUTH CODE for the [deployment profile](https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/create-an-ai-instance-deployment-profile-in-csp) you
 created for AI Runtime Security Firewall in Customer Support
 Portal).
  - Enter your [Device Certificate PIN
                                    ID](https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/activate-your-ai-runtime-security-license/generate-a-device-certificate) and Device Certificate PIN
 Value associated with Customer Support Portal
 account**.**

 

10.  Configure your Management Parameters. Firewalls deployed
 using the Auto-Execute workflow must be managed by Strata Cloud Manager;
 Panorama management is not supported.
 
  - Enter the CIDRs that can access the management interface of the firewall
 under Allowed Management Access.
  - The **SSH key to be used for login** (see how to [Create SSH keys](https://cloud.google.com/compute/docs/connect/create-ssh-keys)).
  - **Manage by SCM** and then select the **SCM folder** to group the
 Prisma AIRS AI Runtime Firewall. 
 
 For Multi-Cloud Mesh to be deployed, you must
 select the folder that contains the required Auto-VPN configuration.
 

Refer to [Workflows: Folders - Strata Cloud
                                    Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/workflows/workflows-ngfw-setup/folder-management).

 

11.  Select **Next**.
12.  In **Review architecture:**