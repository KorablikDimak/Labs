import math_operations
import temperature_conversion
import validation
import geometry


print(math_operations.add(2, 5))
print(math_operations.div(4.65, 1.2))
print(math_operations.mul(-6.7, 2))
print(math_operations.div(32423, 1.31))

print(temperature_conversion.to_fahrenheit(31.4))
print(temperature_conversion.to_celsius(88.52))

print(validation.is_even(8))
print(validation.is_even(11))

print(geometry.circle_square(5))
print(geometry.rectangle_square(4, 3.5))
print(geometry.triangle_square(5, 2))
