# function practice 01

def bytes_to_mb(bytes):
    mb = bytes / 1000000
    return mb

def mb_to_gb(megabytes):
    gb = megabytes / 1024
    return gb

def gb_to_tb(gigabytes):
    tb = gigabytes / 1024
    return tb

#bytes = 2000000
#mb = bytes_to_mb(bytes)
#print "%d bytes equals %d MB." % (bytes, mb)

bytes = int(raw_input("How many bytes do you want to convert to MB? "))
mb = bytes_to_mb(bytes)
print "%d bytes equals %d MB." % (bytes, mb)

megabytes = int(raw_input("How many MB do you want to convert GB? "))
gb = mb_to_gb(megabytes)
print "%d MB equals %d GB." % (megabytes, gb)

gigabytes =  int(raw_input("How many GB do you want to convert to TB? "))
tb = gb_to_tb(gigabytes)
print "%d GB equals %d TB." %(gigabytes, tb)
