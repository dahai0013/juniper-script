from junos import Junos
from junos import Junos_Context
from jnpr.junos import Device
import jcs


jdev = Device().open()

inv = jdev.rpc.get_chassis_inventory()

#print "model: %s" % inv.find('chassis/description').text
print "serial-number: %s" % inv.find('chassis/serial-number').text

jdev.close()