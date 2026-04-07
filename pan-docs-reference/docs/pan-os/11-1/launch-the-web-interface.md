<!-- Source: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/firewall-administration/use-the-web-interface/launch-the-web-interface -->
<!-- Fetched: 2026-03-31T20:05:43.659967+00:00 -->
<!-- Project: ngfw -->
<!-- Tags: web-ui, management -->

# Launch the Web Interface

 

 
 
 
 
 
 

 

 Table of Contents

 

 
 

 *
 
 *

 
 
 ![Filter icon](/content/dam/techdocs/en_US/images/icons/css/filter.svg)
 

 Filter
 

 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

 

 

 

 

 

 
 
 
---

 
 
 **

[Previous
                            
                                    Use the Web Interface](/content/techdocs/en_US/pan-os/11-1/pan-os-admin/firewall-administration/use-the-web-interface.html)
 

 
 

**[Next
                                
                                    Configure Banners, Message of the Day, and Logos](/content/techdocs/en_US/pan-os/11-1/pan-os-admin/firewall-administration/use-the-web-interface/configure-banners-message-of-the-day-and-logos.html)
 

 

---

 
 
 















 

# Launch the Web Interface



 



 The following web browsers are supported for
access to the web interface:

- Google Chrome 104+

- Microsoft Edge 104+

- Mozilla Firefox 103+

- Safari 15+

Perform the following tasks to
launch the web interface.

1.  Launch an Internet browser and enter the IP address
of the firewall in the URL field (https://<IP address>).
 
 By default, the management (MGT) interface
allows only HTTPS access to the web interface. To enable other protocols,
select DeviceSetupInterfaces and edit the Management interface.

2.  Log in to the firewall according to the type of authentication
used for your account. If logging in to the firewall for the first
time, use the default value **admin** for your username and password.
  - **SAML**—Click Use Single Sign-On (SSO).
If the firewall performs authorization (role assignment) for administrators,
enter your Username and Continue.
If the SAML identity provider (IdP) performs authorization, Continue without
entering a Username. In both cases, the firewall
redirects you to the IdP, which prompts you to enter a username
and password. After you authenticate to the IdP, the firewall web
interface displays.

  - **Any other type of authentication**—Enter your user Name and Password.
Read the login banner and select I Accept and Acknowledge
the Statement Below if the login page has the banner
and check box. Then click Login.

3.  Read and Close the messages of
the day.