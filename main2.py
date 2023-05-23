 def compare_temperature(city_name, temperature_reading, time_period):
     temperature_data = {
         'Perth': {
             'Morning': 18.2,
             'Evening': 23.0
         },
         'Melbourne': {
             'Morning': 13.5,
             'Evening': 18.9
         },
         'Sydney': {
             'Morning': 18.8,
             'Evening': 23.4
         },
         'Adelaide': {
             'Morning': 16.5,
             'Evening': 21.0
         }
     }
 
     if city_name in temperature_data:
         if time_period in temperature_data[city_name]:
             average_temperature = temperature_data[city_name][time_period]
             temperature_difference = temperature_reading - average_temperature
             
             if temperature_difference > 5:
                 return f"The temperature in {city_name} {time_period} is {temperature_reading}°C, which is {temperature_difference}°C above the average temperature."
             elif temperature_difference < -5:
                 return f"The temperature in {city_name} {time_period} is {temperature_reading}°C, which is {abs(temperature_difference)}°C below the average temperature."
             else:
                 return f"The temperature in {city_name} {time_period} is {temperature_reading}°C, which is close to the average temperature."
         else:
             return 'Unknown Time Period'
     else:
         return 'Unknown City'
 
 
 def main():
     city_name = input("Enter the city: ")
     temperature_reading = float(input("Enter the temperature: "))
     time_period = input("Enter the time period (Morning/Evening): ")
 
     result = compare_temperature(city_name, temperature_reading, time_period)
 
     print(result)
 
 
 if __name__ == '__main__':
     main()


