# Global Freight Calculator

sender_name = input("Enter Sender Name: ")
item_type = input("Enter Type of Item: ")
isFragile = bool("Is it fragile? (True/False): ") == "True"
weight = float(input("Enter Weight (kg): "))
distance = float(input("Enter Distance (km): "))
is_express = input("Is it express? (True/False): ") == "True"
is_international = input("Is it international? (True/False): ") == "True"

# Base Cost
base_cost = (weight * 2.50) + (distance * 0.15)

# Shipping Rates 
if weight <= 2 and distance <= 100 and not is_express and not is_international: 
 shipping_rate = "Free Shipping" 
 total = 0


elif is_express and is_international:
   shipping_rate = "International Shipping"
   total = (base_cost * 1.40) + 50


elif is_express or (is_international and weight > 20):
   shipping_rate = "Heavy Shipping" 
   total =(base_cost * 1.20) + 25


elif weight > 30 or distance > 1000:
   shipping_rate = "Oversized Shipping"
   total = base_cost + 30

else:
   shipping_rate = "Standard Shipping"
   total = base_cost 

print("\n---- Summary of the Item ----")
print("Sender Name:", sender_name)
print("Type of Item:", item_type)
print("Fragile:", isFragile)
print("Express:", is_express)
print("International:", is_international)
print("Total Shipping Cost: $", format(total, ".2f"))