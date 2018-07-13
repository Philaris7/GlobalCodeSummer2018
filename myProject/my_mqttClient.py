import paho.mqtt.client as  mqtt
import monitor as mon
import paho.mqtt.publish as publish
import time


# Disk information
DISK_stats = mon.getDiskSpace()
disk={'name': "Phil", 'Disk_total':DISK_stats[0], 'Disk_free':DISK_stats[1], 'Disk_Percentage ':DISK_stats[3]}
disk = str(disk)
addr = str(mon.myaddress)
#msg = addr.upddate(disk)

mqttc = mqtt.Client(client_id='10.10.3.162')

try:
	mqttc.connect(host ='82.165.16.151')
	print('connected')
except:
	print('not connected')


while True:
	mqttc.publish('UCC/pihealth', disk)
	time.sleep(20)	


#mqttc.publish(topic='UCC/iphealth', payload=addr, hostname ='82.165.16.151')


