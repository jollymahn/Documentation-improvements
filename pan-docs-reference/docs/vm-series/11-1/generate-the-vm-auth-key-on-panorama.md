<!-- Source: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/generate-the-vm-auth-key-on-panorama -->
<!-- Fetched: 2026-03-31T18:04:51.717835+00:00 -->
<!-- Project: c-bootstrapping -->
<!-- Tags:  -->

# Generate the VM Auth Key on Panorama



 



 To manage VM-Series firewalls using Panorama, generate a VM auth key on Panorama and
 include it in the basic configuration file.



 If you want to use Panorama to manage the
VM-Series firewalls that you are bootstrapping, you must generate
a VM auth key on Panorama and include the key in the basic configuration
(init-cfg.txt) file. The VM auth key allows Panorama to authenticate
the newly bootstrapped VM-Series firewall. So, to manage the firewall
using Panorama, you must include the IP address for Panorama and
the VM auth key in the basic configuration file as well as the license
auth codes in the /license folder of the bootstrap package. The
firewall can then provide the IP address, serial number, and the
VM auth key in its initial connection request to Panorama so that
Panorama can verify the validity of the VM auth key and add the
firewall as a managed device. If you provide a device group and
template in the basic configuration file, Panorama will assign the
firewall to the appropriate device group and template so that you
can centrally configure and administer the firewall using Panorama.

The
lifetime of the key can vary between 1 hour and 8760 hours (1 year).
After the specified time, the key expires and Panorama will not
register VM-Series firewalls without a valid auth-key in this connection
request.

1.  Log in to the Panorama CLI or access the API:
  - In the CLI, use the following operational command:

```
request bootstrap vm-auth-key generate lifetime <1-8760>
```
For
example to generate a key that is valid for 24 hrs, enter the following:

```
request bootstrap vm-auth-key generate lifetime 24 
VM auth key 755036225328715 generated. Expires at: 2015/12/29 12:03:52 
```

  - In the API, use the following URL:

https://<Panorama_IP_address>/api/?type=op&cmd=<request><bootstrap><vm-auth-key><generate><lifetime><number-of-hours></lifetime></generate></vm-auth-key></bootstrap></request>where
the lifetime is the number of hours for which the VM auth key is valid.

2.  Verify the validity term of the VM auth key(s) you generated
on Panorama. Make sure that the validity term allows enough time
for the firewall(s) to register with Panorama.
```
https://<Panorama_IP_address>/api/?type=op&cmd=<request><bootstrap><vm-auth-key><show></show></vm-auth-key></bootstrap></request>
```

 
 
 
 
 
 
 

 

 
 
 
 

 

 

 

 

3.  Add the generated VM auth key to the basic configuration (init-cfg.txt) file.
 See [Create the
                        init-cfg.txt File](/content/techdocs/en_US/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall/create-the-init-cfgtxt-file.html#id8770fd72-81ea-48b6-b747-d0274f37860b).
4.  Verify the device registration authentication key you generated are
 successfully created.request bootstrap vm-auth-key show