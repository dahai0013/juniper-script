from junos import Junos
from junos import Junos_Context
from lxml import etree
from jnpr.junos import Device
import jcs

jdev = Device(host='localhost')
jdev.open()

#cli: method, for example
result = jdev.cli("show version", format="xml")
print etree.tostring(result)

# CLI rendered format
xml_rsp = jdev.cli("show version")
print xml_rsp

jdev.close()