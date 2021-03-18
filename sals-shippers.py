#this is a program to help optimize shipping for Sal's Shippers
weight = 1.5
#Ground Shipping
if weight <= 2:
  cost_ground_shipping = (weight * 1.50) + 20.00
elif weight > 2 and weight <= 6:
  cost_ground_shipping = (weight * 3.00) + 20.00
elif weight > 6 and weight <= 10:
  cost_ground_shipping = (weight * 4.00) + 20.00
else:
  cost_ground_shipping = (weight * 4.75) + 20.00
#print cost of using ground shipping
print(cost_ground_shipping)

#Premium Ground Shipping
cost_premium_ground_shipping = 125.00
#print cost of premium ground shipping
print(cost_premium_ground_shipping)

#Drone Shipping
if weight <= 2:
  cost_drone_shipping = (weight * 4.50)
elif weight > 2 and weight <= 6:
  cost_drone_shipping = (weight * 9.00)
elif weight > 6 and weight <= 10:
  cost_drone_shipping = (weight * 12.00)
else:
  cost_drone_shipping = (weight * 14.25)
#print the cost of drone shipping
print(cost_drone_shipping)

#if mailing a 8.4 lb package, use ground shipping
#if mailing a 1.5 lb package, use drone shipping
#if mailing a 4.8 lb package, use ground shipping
#if mailing a 41.5 lb package, use flat rate for SURE
