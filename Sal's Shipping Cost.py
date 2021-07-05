# This is a project I did while taking the "Learn Python 3" course in Codecademy

# Weight of Package in lbs
weight = 12

# Cost of Ground Shipping
if weight <= 2:
    cost_ground = weight * 1.50 + 20.00
elif weight <= 6:
    cost_ground = weight * 3.00 + 20.00
elif weight <= 10:
    cost_ground = weight * 4.00 + 20.00
else:
    cost_ground = weight * 4.75 + 20.00
print("Cost of Ground Shipping: $", cost_ground)

# Cost of Premium Ground Shipping
cost_ground_premium = 125.00
print("Premium Ground Shipping: $", cost_ground_premium)

# Cost of Drone Shipping
if weight <=2:
    cost_drone = weight * 4.50
elif weight <= 6:
    cost_drone = weight * 9.00
elif weight <= 10:
    cost_drone = weight * 12.00
else:
    cost_drone = weight * 14.25
print("Cost of Drone Shipping: $", cost_drone)