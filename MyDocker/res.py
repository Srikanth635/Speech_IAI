import psutil

# Get CPU information
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq()
print(f"CPU Count: {cpu_count}")
print(f"CPU Frequency: {cpu_freq.current} MHz")

# Get memory information
mem = psutil.virtual_memory()
mem_total = round(mem.total / (1024 * 1024))
mem_used = round(mem.used / (1024 * 1024))
mem_percent = mem.percent
print(f"Total Memory: {mem_total} MB")
print(f"Used Memory: {mem_used} MB")
print(f"Memory Usage: {mem_percent}%")

# Get disk usage information
disk = psutil.disk_usage('/')
disk_total = round(disk.total / (1024 * 1024 * 1024))
disk_used = round(disk.used / (1024 * 1024 * 1024))
disk_percent = disk.percent
print(f"Total Disk Space: {disk_total} GB")
print(f"Used Disk Space: {disk_used} GB")
print(f"Disk Usage: {disk_percent}%")

# Complete system information
disk_info = psutil.disk_partitions(all=True)
space = []
for disk in disk_info:
    #print(f"Device: {disk.device}")
    #print(f"File System Type: {disk.fstype}")
    #print(f"Mount Point: {disk.mountpoint}")
    ds = round(psutil.disk_usage(disk.mountpoint).total / (1024 * 1024 * 1024),2)
    #print(f"Total Size: {ds} GB")
    space.append(ds)

Total_DiskSpace = sum(space)
print(f"Total System Hard disk: ",Total_DiskSpace)

space = {"Total_Disk_Space":Total_DiskSpace,
	"Disk_Used":disk_used,
	"Total_Memory":mem_total,
	"Used_Memory":mem_used}
print(space)
