#Importa las librerias

import time 
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
#Función para el despegue
def arm_and_takeoff(TargetAltitude):
	print ("Executing Takeoff")

	while not drone.is_armable:
		print ("Vehicle is not armable, waiting....")
		time.sleep(1)

	print("Ready to arm")
	drone.mode = VehicleMode("GUIDED")
	drone.armed = True

	while not drone.armed:
		print("waiting for arming...")
		time.sleep(1)
		
	print ("ready for takeoff, taking off...")
	drone.simple_takeoff(TargetAltitude)

	while True:
		Altitude = drone.location.global_relative_frame.alt
		print("Altitude: ", Altitude)
		time.sleep(1)

		if Altitude >= TargetAltitude * 0.95:
			print("Altitude Reached")
			break


#Vehicle Connection
drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(20)

a_location = LocationGlobal(20.733747,-103.453114, 20)
drone.simple_goto(a_location)

time.sleep(50)

b_location = LocationGlobal(20.733940,-103.454716, 20)
drone.simple_goto(b_location)

time.sleep(50)

c_location = LocationGlobal(20.735665,-103.456460, 20)
drone.simple_goto(c_location)

time.sleep(50)

d_location = LocationGlobal(20.736528,-103.453687, 20)
drone.simple_goto(d_location)

time.sleep(50)

drone.mode = VehicleMode("RTL")
print (drone.battery.level, "v")