# warmup2
# Write two functions:

#celsius_to_fahrenheit(c) — converts Celsius to Fahrenheit using (c * 9/5) + 32
#fahrenheit_to_celsius(f) — converts Fahrenheit to Celsius using (f - 32) * 5/9
#Call each with a few test values and print the results. Use f-strings and round to one decimal place.

#Example output — your test values and wording might differ:
print("test")

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print (f"0° C = {celsius_to_fahrenheit(0):.1f}° F")
print (f"100° C = {celsius_to_fahrenheit(100):.1f}° F")
print (f"35° C = {celsius_to_fahrenheit(35):.1f}° F")

print (f"0° F = {fahrenheit_to_celsius(0):.1f}° C")
print (f"100° F = {fahrenheit_to_celsius(100):.1f}° C")
print (f"250° F = {fahrenheit_to_celsius(250):.1f}° C")