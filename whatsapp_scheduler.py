import pywhatkit
import datetime
import time

# Enter your phone number with country code, e.g., +91 for India
phone_number = "<your_country_code> <your_phone_number>"  # e.g., "+1 1234567890"

# This is the birthday message you want to send
birthday_message = "Happy Birthday 🎉🎂! Wishing you lots of success and happiness!"

# Time to send the message — in 24hr format
scheduled_hour = 12      # 12 AM (early wisher 😉)
scheduled_minute = 0    # on the dot

try:
    print("Scheduling your birthday wish...")  # Just a friendly heads-up
    # Send the message with a 20-second wait (to load WhatsApp Web)
    pywhatkit.sendwhatmsg(phone_number, birthday_message, scheduled_hour, scheduled_minute+1, wait_time=20)
    print("Message scheduled successfully ✅")
except Exception as e:
    print(f"An error occurred: {e}")  # Catch and show any errors during automation
