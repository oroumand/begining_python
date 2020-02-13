CONST_STARS_COUNT = 70
message = "Hello world from python"
upper_message = message.upper()
lower_meesage = message.lower()
title_message = message.title()
white_spate_string = "   Python   "

format_upper_message = f"this is result of upper function: {upper_message}"
format_lower_message = f"this is result of lower function: {lower_meesage}"
format_title_message = f"this is result of title function: {title_message}"


print("*" * CONST_STARS_COUNT)
print(format_upper_message)
print("*" * CONST_STARS_COUNT)
print(format_lower_message)
print("*" * CONST_STARS_COUNT)
print(format_title_message)
print("*" * CONST_STARS_COUNT)
print(f"Number of * in line is {CONST_STARS_COUNT}")
print("*" * CONST_STARS_COUNT)
print(f"{white_spate_string.rstrip()}{white_spate_string.strip()}{white_spate_string.lstrip()}")
