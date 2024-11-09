#!/usr/bin/env python
# coding: utf-8

# In[9]:


import nmap


# In[ ]:





# In[16]:


nm = nmap.PortScanner()


# In[ ]:





# In[17]:


target = "64.13.134.52"


# In[18]:


options = "-sV -sC scan_results"


# In[ ]:





# In[ ]:


nm.scan(target, arguments=options)


# In[ ]:





# In[20]:


for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))


# In[ ]:





# In[ ]:




