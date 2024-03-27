def km_to_miles(km):
    miles = km * 0.621371
    return miles

def miles_to_km(miles):
    km = miles / 0.621371
    return km

# Kilometre cinsinden bir mesafe verelim
km_distance = 100

# Kilometreyi mil'e çevirelim
miles_distance = km_to_miles(km_distance)
print(f"{km_distance} kilometre, {miles_distance:.2f} mil eder.")

# Mil cinsinden bir mesafe verelim
miles_distance = 62.1371

# Mili kilometreye çevirelim
km_distance = miles_to_km(miles_distance)
print(f"{miles_distance} mil, {km_distance:.2f} kilometre eder.")
