<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/choose-a-bootstrap-method -->
<!-- Fetched: 2026-03-31T18:04:47.005609+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Choose a Bootstrap Method



 



 Choose a basic configuration or a complete configuration
bootstrap method.



 You can bootstrap the VM-Series firewall with a **basic configuration **or
a **complete configuration**. 

A **complete** configuration uses the bootstrap package and
includes everything you need to fully configure the firewall at
boot up. This includes configuration parameters (in [init-cfg.txt](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file.html#id8770fd72-81ea-48b6-b747-d0274f37860b)),
content updates, and software versions. A complete configuration
can include both [init-cfg.txt](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file.html#id8770fd72-81ea-48b6-b747-d0274f37860b) and [bootstrap.xml](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-configuration-files.html#id37d59976-16c6-4c75-af8a-61f46e690d65_id13ef8ab8-3f18-4222-8938-cbf8d6d3d318) files.
























 

****

- 

- 

| Configuration Method | Configuration Location | Comment |
| --- | --- | --- |
| Specify complete configuration information
in /config/bootstrap.xml in the bootstrap package. | Public cloud storageAWS S3
bucket, Azure storage account, or Google storage bucket. | Full bootstrap package in the storage bucket.Requires cloud storage and an IAM role to access it. |


A **basic** configuration is a minimal configuration that
enables you to launch, license, and register the VM-Series firewall.
The basic configuration does not support plugins, content, software
images, or bootstrap.xml.

After you boot the firewall you can connect with Panorama to
complete the configuration, or log in to the firewall to update
content and software manually. The following table briefly contrasts
three ways you can store and access a basic configuration:
























 

****

****

- 

- 

- 

- 

****

****

- 

- 

- 

- 

- 

****

- 

- 

| Configuration Method | Configuration Location | Comment |
| --- | --- | --- |
| init-cfg.txtStore basic configuration
parameters as key-value pairs in config/init-cfg.txt in the bootstrap
package. | Public cloud storageAWS
S3 bucketAzure storage accountGCP storage bucket | Requires cloud storage and an IAM
role to access it. The Panorama admin must also be granted access
to the bucket. |
| User dataEnter configuration parameters
into the public cloud user interface as key-value pairs. | VM InstanceAWS: User
dataAzure: Custom dataGCP: GCP metadata | The initial configuration parameters
are stored with the VM.No need for separate storage and the associated IAM role. |
| AWS Secret ManagerEnter configuration parameters
into the AWS secret manager as key-value pairs. | Encrypted in AWS Secret Manager. | You need an IAM role to create a
secret. Others can be granted permission to get the secret.To get the secret, pass the secret name using user data. |


See the [VM-Series firewall
bootstrap workflow](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/vm-series-firewall-bootstrap-workflow.html#id59fe5979-c29d-42aa-8e72-14a2c12855f6) to compare the workflow for the basic
and complete configurations. 

- Basic Configuration
- Complete Configuration


 















 

## Basic Configuration



 A basic configuration includes the initial configuration
and licenses. You can use the bootstrap package to
pass the key-value pairs for the initial configuration, or you can
enter the bootstrap parameters key-value pairs as user data.

If you do not use Panorama, you can use the initial configuration
to bootstrap the firewall, then log in and complete the configuration
manually. If you use Panorama, your initial configuration must include
bootstrap parameters for the IP addresses for your Panorama servers
and [the
VM Auth Key](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/generate-the-vm-auth-key-on-panorama.html#id6507055f-4230-47ac-adc9-cd947bfd83c4) so the bootstrapped firewall can register with
Panorama and complete the full configuration. 

- Add a Basic Configuration to the Bootstrap Package
- Enter a Basic Configuration as User Data (AWS, Azure, or GCP)
- Save a Basic Configuration in the AWS Secrets Manager


 















 

### Add a Basic Configuration to the Bootstrap Package



 The initial configuration is a minimal configuration
that enables you to launch, license, and register the VM-Series
firewall, and connect with Panorama, if applicable. You deliver
the configuration ([init-cfg.txt](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file.html#id8770fd72-81ea-48b6-b747-d0274f37860b))
in the [bootstrap package](https://docs.paloaltonetworks.com/vm-series/10-0/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-package.html). 








 















 

### Enter a Basic Configuration as User Data (AWS, Azure, or
GCP)



 
 
 When you include Panorama connectivity parameters in
 your init-cfg.txt, Panorama attempts to push configuration to the VM-Series
 firewall upon first connection. The connection to Panorama fails if hostname,
 template stack, or device group values are missing from the init-cfg.txt
 file.

When you deploy the VM-Series firewall from the AWS,
Azure, or GCP user interface, you can enter the configuration parameters
as user data during the launch/deployment process. If you have sufficient
permissions to deploy a firewall from your cloud account, and access
Panorama (if you are using it), you can skip creating a bootstrap
package, creating configuration files, and other bootstrap tasks
related to cloud storage (a storage bucket, IAM roles, or service
accounts that grant external access to storage).

Configuration parameters include the values in [init-cfg.txt File Components](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file/init-cfgtxt-file-components.html#id07933d91-15be-414d-bc8d-f2a5f3d8df6b), and the
following additional values only available as user data: 

- authcodes—The authcode use to [register the VM-Series
firewall](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/register-the-vm-series-firewall.html#id1c0525c0-f2b8-44b4-9d11-271d53003b20). For example, authcodes=I7115398. 

- mgmt-interface-swap—Used to swap the management
interface when the VM-Series firewall is behind a load balancer
in an AWS or GCP deployment. For example, mgmt-interface-swap=enable. 

You can enter configuration parameters as key-value pairs directly
into the AWS or GCP user interface. You can also define the configuration
from a text file or a cloud-native template, such as an AWS Cloud
Formation template, Azure ARM template, a GCP YAML file, or a Terraform
template.

Each cloud has a different term for user data, and uses different
separators between bootstrap parameters.

- **AWS User Data**—Use a semicolon or newline (\n).
If a parameter has more than one option, separate options with a
comma. For example:

If you choose to save your basic configuration
in the AWS Secrets Manager, enter the secret name as a key-value
pair in the user data field. For example:

```

  type=dhcp-client
  hostname=palo1
  panorama-server=<PANORAMA-1 IP>
  panorama-server-2=<PANORAMA-2 IP>
  tplname=STK-NGFW-01
  dgname=DG-NGFW-01
  dns-primary=169.254.169.253
  dns-secondary=8.8.8.8
  op-command-modes=mgmt-interface-swap
  dhcp-send-hostname=yes
  dhcp-send-client-id=yes
  dhcp-accept-server-hostname=yes
  dhcp-accept-server-domain=yes
  vm-auth-key= <YOUR AUTH KEY HERE>
  authcodes= <<YOUR AUTH CODE HERE>
                                                                                         
```

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
- **Azure Custom Data**—Use a semicolon. If a parameter
has more than one option, separate options with a comma. For example:

```
type=dhcp-client; op-command-modes=jumbo-frame;
vm-series-auto-registration-pin-id=abcdefgh1234****;
vm-series-auto-registration-pin-value=zyxwvut-0987****
```

- **GCP Custom Metadata**—In a file, such as a YAML file
or Terraform template, use a newline (\n) for each parameter, and
if a parameter has multiple options, use commas to separate them.
For example:

```
type=dhcp-client
op-command-modes=mgmt-interface-swap,jumbo-frame
vm-series-auto-registration-pin-id=abcdefgh1234****
vm-series-auto-registration-pin-value=zyxwvut-0987****
```








 















 

### Save a Basic Configuration in the AWS Secrets Manager



 You can use the [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/index.html) to store
the basic configuration as
a secret, and then use User Data to bootstrap a VM with the parameters
stored in the secret. To perform this task you need permission to
use the Secrets Manager.

- The secret creator must have [full Secrets Manager administrator
permissions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_identity-based-policies.html#permissions_grant-admin-actions). A Secrets Manager administrator can permit others
to use the secret, as described in [Authentication and access control
for AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_identity-based-policies.html).

For example, the following
policy statement allows you to get the secret value:

```
{
  "Version": "2012-10-17",
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": 
      "arn:aws:secretsmanager:us-east-1:688382******:secret:My_bts-******"
    }
}
```
Refer to [Actions, Resources, and Context
Keys You Can Use in an IAM Policy or Secret Policy for AWS Secrets
Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html) to see actions that require permission, such as list,
get, and rotate secret.

- (Optional) To encrypt the secret you can use the
DefaultEncryptionKey from AWS Secrets Manager. 

1.  Log in to the AWS console and under Security,
Identity and Compliance, select Secrets Manager and
select Store a new secret.
2.  Select other type of secrets.
  1.  Enter the key-value pairs to define the
basic configuration.
 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 
 
 mgmt-interface-swap does
not work as a key-value pair in an AWS secret. It must be entered
as: op-command-modes=mgmt-interface-swap

  2.  Select the DefaultEncryptionKey, and click Next.

3.  Supply the secret name and description.
  1.  Edit the resource permissions to securely
access secrets across AWS accounts. For example:
```
{
    "Version": "2012-10-17",
    "Statement": [
    {
        "Sid": "VisualEditor0",
        "Effect": "Allow",
        "Action": "s3:ListBucket",
        "Resource": "arn:aws:s3:::sn-bootstrap"
    },
    {
        "Sid": "VisualEditor1",
        "Effect": "Allow",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::sn-bootstrap/*"
    },
    {
        "Effect": "Allow",
        "Action": "secretsmanager:GetSecretValue",
        "Resource": "arn:aws:secretsmanager:us-east-1:688382******:
                           secret:My_bootstrap"
    }
  ]
}
```

  2.  (Optional) You can examine the secret from
the command line (if you have permission). For example:
```
# aws secretsmanager get-secret-value --secret-id My_bootstrap
{
    "ARN": "arn:aws:secretsmanager:us-east-1:688382******:
                secret:My_bootstrap",
    "Name": "My_bootstrap",
    "VersionId": "01b6853d-e187-479f-***********",
    "SecretString": "{\"mgmt-interface-swap\":\"enable\",
        \"vm-auth-key\":\"AAA\",\"panorama-server\":\"10.*.*.1\",
        \"panorama-server-2\":\"10.*.*.2\",\"dgname\":\"dg-s0000h\",
        \"tplname\":\"tpl-santosh\",\"license-authcode\":\"AAAA\"}",
    "VersionStages": [ "AWSCURRENT" ],
    "CreatedDate": 1581018411.847
}
```













 















 

## Complete Configuration



 A complete configuration ensures the firewall is fully
configured on boot up. The [bootstrap.xml](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-configuration-files.html#id37d59976-16c6-4c75-af8a-61f46e690d65_id13ef8ab8-3f18-4222-8938-cbf8d6d3d318) file includes
the initial configuration, licenses, software, content, and a version
of the VM-Series plugin. You can create bootstrap.xml manually
or you can export an existing configuration, as described in [Create
the bootstrap.xml File](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-bootstrapxml-file.html#id61aa8472-5aba-41c5-ac4f-4a409e3dedb6).