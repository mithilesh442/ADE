#dictionary

#printing a required value using key = city
my_dict = {"name" : "Teja", "age" : 25, "city" : "Nellore"}
print(my_dict["city"])

#printing a required value using key = name
print(my_dict.get("name"))

#adding a key = country into the dict
my_dict["country"] = "India"
print(my_dict)

#changing the key value = tirupati
my_dict["city"] = "Tirupati"
print(my_dict)