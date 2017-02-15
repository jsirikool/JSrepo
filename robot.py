from sys import argv

script, robot = argv

repair = raw_input("What major repair do you need? ")

battery = raw_input("What percentage is your battery at? ")

print """
Hi, I'm script %s.
Robot %s, you need the following repair: \n%s.
Your battery life is at %s percent.
""" % (script, robot, repair, battery)
