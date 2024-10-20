#Transportation Model Selection
# Choose a mode of transportation based on the distance (e.g <3 km:walk,3-15km: Bike, >15km:Car).

distance =  5
 
if distance <3:
    tranport = "walk"

elif distance <= 15:
    transport = "Bike"
else:
    transport = "car"

print("AI recommends you the transport of:", transport )


 
 

