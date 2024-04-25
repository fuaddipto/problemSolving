import time

# Retrieve current timestamp
timestamp = int(time.strftime('%H'))

# Print current time
print("Current time:", time.strftime('%H:%M:%S'))

# Extract hour, minute, and second components
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

# Check the time of the day
if hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
elif hour <23.59:
    print("Good Evening")
else: 
    print("good night")