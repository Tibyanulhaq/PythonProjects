import phonenumbers
from phonenumbers import geocoder,carrier,timezone

number=input("Enter your Number +-- : ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
carr=carrier.name_for_number(phone,"en")
registration=geocoder.description_for_number(phone,"en")

print("Number : ",number)
print(phone)
print("Timezone : ",time)
print("Company : ",carr)
print("Country : ",registration)