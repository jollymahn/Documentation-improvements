<!-- Source: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-cli-quick-start/get-started-with-the-cli/access-the-cli -->
<!-- Fetched: 2026-04-01T01:59:30.441538+00:00 -->
<!-- Project: scm -->
<!-- Tags: ngfw, cli -->

# Get Started with the CLI

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 
 
 Expand All
 |
 Collapse All
 

 
 

### Next-Generation Firewall Docs

 
---

 

 
 

 
- 
 
 
 
 
 

 Getting Started
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Administration
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Networking
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Quick Start
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Reference
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Incidents & Alerts
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 

 
 
- 
 
 
 
 
 

 Release Notes
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 
 Select a Document
 
 **
 
 
 
  - PAN-OS 12.1
 
  - PAN-OS 11.2
 
  - PAN-OS 11.1
 
  - PAN-OS 11.0 (EoL)
 
  - PAN-OS 10.2
 
  - PAN-OS 10.1
 
  - PAN-OS 10.0 (EoL)
 
  - PAN-OS 9.1 (EoL)
 
  - PAN-OS 9.0 (EoL)
 
  - PAN-OS 8.1 (EoL)
 

 

 

 

 
 

 
 
- 
 
 
 
 
 

 Help
 

 *
 ![directional arrow](/content/dam/techdocs/en_US/images/icons/css/thick-greater-than-icon.svg)
 *
 

 
 Select a Document
 
 **
 
 
 
  - PAN-OS 12.1
 
  - PAN-OS 11.2
 
  - PAN-OS 11.1
 
  - PAN-OS 10.2
 
  - PAN-OS 10.1
 

 

 

 

 
 

 
 

 

 

 

 

 
 
 
---

 
 
 **

[Previous
                            
                                    Configure Fail Open](/content/techdocs/en_US/ngfw/networking/fail-open/configure-fail-open.html)
 

 
 

**[Next
                                
                                    Verify SSH Connection to Firewall](/content/techdocs/en_US/ngfw/pan-os-cli-quick-start/get-started-with-the-cli/verify-ssh-connection-to-firewall.html)
 

 

---

 
 
 















 

# Get Started with the CLI



 Learn how to use the PAN command-line interface (CLI) to monitor and configure your
 firewall or Panorama device, including access methods, SSH connections, and basic
 navigation.



 
 






















 

- 

| Where Can I Use This? | What Do I Need? |
| --- | --- |
| NGFW (Managed by PAN-OS or Panorama) | No prerequisites needed |



 Every Palo Alto Networks device includes a command-line interface (CLI) that allows
 you to monitor and configure the device. Although this guide does not provide
 detailed command reference information, it does provide the information you need to
 learn how to use the CLI. It includes information to help you find the command you
 need and how to get syntactical help after you find it. It also explains how to
 verify the SSH connection to the firewall when you access the CLI remotely, and how
 to refresh the SSH keys and configure key options when connecting to the management
 interface.

 Use a terminal emulator, such as PuTTY, to connect to the CLI of a Palo Alto Networks
 device in one of the following ways:

 
- **SSH Connection**—To ensure you are logging in to your firewall and not a
 malicious device, you can [verify the SSH connection to the
                            firewall](/content/techdocs/en_US/ngfw/pan-os-cli-quick-start/get-started-with-the-cli/verify-ssh-connection-to-firewall.html#iddbcafb19-5afe-425d-9090-07e9a04ef470) when you perform [initial configuration](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/getting-started/integrate-the-firewall-into-your-management-network/perform-initial-configuration.html). After you
 have completed [initial configuration](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/getting-started/integrate-the-firewall-into-your-management-network/perform-initial-configuration.html), you can
 establish a CLI connection over the network using a secure shell (SSH)
 connection.

- **Serial Connection**—If you have not yet completed initial configuration
 or if you chose not to enable SSH on the Palo Alto Networks device, you can
 establish a direct serial connection from a serial interface on your
 management computer to the Console port on the device.

 

1.  Launch the terminal emulation software and select the type of connection
 (Serial or SSH).
 
  - To establish an SSH connection, enter the hostname or IP address of
 the device you want to connect to and set the port to
 22.

  - To establish a Serial connection, connect a serial interface on
 management computer to the Console port on the device. Configure the
 Serial connection settings in the terminal emulation software as
 follows:

    - Data rate: 9600

    - Data bits: 8

    - Parity: none

    - Stop bits: 1

    - Flow control: none

 

2.  When prompted to log in, enter your administrative username.
 The default superuser username is admin. To set up CLI
 access for other administrative users, see [Give
                            Administrators Access to the CLI](/content/techdocs/en_US/ngfw/pan-os-cli-quick-start/get-started-with-the-cli/give-administrators-access-to-the-cli.html#id5477c742-2ebd-4662-83d3-0fa364d8e73d).

 If prompted to acknowledge the login banner, enter
 Yes.

 

3.  Enter the administrative password.
 The default superuser password is admin. However, for
 security reasons you should immediately change the [admin
                            password](/content/techdocs/en_US/ngfw/pan-os-cli-quick-start/use-the-cli/cli-jump-start.html#ida3c274d7-4c4e-4a4c-b96e-ee43bd6441bc_id9e343aca-b0e6-4dda-a4ec-4c3dba1ab502).

 After you log in, the [message of the day](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/firewall-administration/use-the-web-interface.html) displays,
 followed by the CLI prompt in Operational mode:

 
```
username@hostname>
```

 You can tell you are in operational mode because the command prompt ends with
 a >.