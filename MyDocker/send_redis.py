import redis
import psutil
from rq import Queue
import json

# Get memory information
mem = psutil.virtual_memory()
mem_total = round(mem.total / (1024 * 1024))
mem_used = round(mem.used / (1024 * 1024))

# Get disk usage information
disk = psutil.disk_usage('/')
disk_total = round(disk.total / (1024 * 1024 * 1024))
disk_used = round(disk.used / (1024 * 1024 * 1024))

space = {"Total_Disk_Space":disk_total,
	"Disk_Used":disk_used,
	"Total_Memory":mem_total,
	"Used_Memory":mem_used}
	
	
# Connect to Redis
r = redis.Redis(host='192.168.142.128', port=6379, password='d9f9ef5f2fef8da852b43c58c7f1c6c1')

space_dict_str = json.dumps(space)
            
r.rpush('server_resource', space_dict_str)

# Pass information to the Redis queue
#r.set("Total_Disk_Space",str(disk_total))
#r.set("Disk_Used",str(disk_used))
#r.set("Total_Memory",str(mem_total))
#r.set("Used_Memory",str(mem_used))
#print(r.get("Used_Memory"))
