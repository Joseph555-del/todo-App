from bonus.converters14 import convert
import parsers14

feet_inches = input("Enter feet and inches: ")

parsed = parsers14.(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kis can use the slide.")