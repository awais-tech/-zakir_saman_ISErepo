 def find_season(country_name, month_name):
     seasons = {
         'Australia': {
             'Meteorological Seasons': {
                 'December': 'Summer',
                 'January': 'Summer',
                 'February': 'Summer',
                 'March': 'Autumn',
                 'April': 'Autumn',
                 'May': 'Autumn',
                 'June': 'Winter',
                 'July': 'Winter',
                 'August': 'Winter',
                 'September': 'Spring',
                 'October': 'Spring',
                 'November': 'Spring'
             },
             'Noongar Seasons': {
                 'December': 'Birak',
                 'January': 'Birak',
                 'February': 'Bunuru',
                 'March': 'Bunuru',
                 'April': 'Djeran',
                 'May': 'Djeran',
                 'June': 'Makuru',
                 'July': 'Makuru',
                 'August': 'Djilba',
                 'September': 'Djilba',
                 'October': 'Kambarang',
                 'November': 'Kambarang'
             }
         },
         'Spain': {
             'Meteorological Seasons': {
                 'December': 'Winter',
                 'January': 'Winter',
                 'February': 'Winter',
                 'March': 'Spring',
                 'April': 'Spring',
                 'May': 'Spring',
                 'June': 'Summer',
                 'July': 'Summer',
                 'August': 'Summer',
                 'September': 'Autumn',
                 'October': 'Autumn',
                 'November': 'Autumn'
             }
         },
         'Japan': {
             'Meteorological Seasons': {
                 'December': 'Winter',
                 'January': 'Winter',
                 'February': 'Winter',
                 'March': 'Spring',
                 'April': 'Spring',
                 'May': 'Spring',
                 'June': 'Summer',
                 'July': 'Summer',
                 'August': 'Summer',
                 'September': 'Autumn',
                 'October': 'Autumn',
                 'November': 'Autumn'
             }
         },
         'Mauritius': {
             'Meteorological Seasons': {
                 'December': 'Summer',
                 'January': 'Summer',
                 'February': 'Summer',
                 'March': 'Summer',
                 'April': 'Summer',
                 'May': 'Autumn',
                 'June': 'Winter',
                 'July': 'Winter',
                 'August': 'Winter',
                 'September': 'Winter',
                 'October': 'Spring',
                 'November': 'Summer'
             }
         },
         'Malaysia': {
             'Meteorological Seasons': {
                 'December': 'Northeast Monsoon',
                 'January': 'Northeast Monsoon',
                 'February': 'Northeast Monsoon',
                 'March': 'Inter-monsoon',
                 'April': 'Inter-monsoon',
                 'May': 'Southeast Monsoon',
                 'June': 'Southeast Monsoon',
                 'July': 'Southeast Monsoon',
                 'August': 'Southeast Monsoon',
                 'September': 'Southeast Monsoon',
                 'October': 'Inter-monsoon',
                 'November': 'Inter-monsoon'
             }
         },
         'Sri Lanka': {
             'Meteorological Seasons': {
                 'December': 'Northeast Monsoon',
                 'January': 'Northeast Monsoon',
                 'February': 'Northeast Monsoon',
                 'March': 'Inter-monsoon',
                 'April': 'Inter-monsoon',
                 'May': 'Southeast Monsoon',
                 'June': 'Southeast Monsoon',
                 'July': 'Southeast Monsoon',
                 'August': 'Southeast Monsoon',
                 'September': 'Southeast Monsoon',
                 'October': 'Inter-monsoon',
                 'November': 'Inter-monsoon'
             }
         }
     }
 
     if country_name in seasons:
         country_seasons = seasons[country_name]
         season_type = input("Choose the type of season (1: Meteorological Seasons, 2: Noongar Seasons): ")
         
         if country_name == 'Australia' and season_type == '2':
             season_dict = country_seasons['Noongar Seasons']
         else:
             season_dict = country_seasons['Meteorological Seasons']
         
         if month_name in season_dict:
             return season_dict[month_name]
         else:
             return 'Unknown'
     else:
         return 'Unknown'
 
 
 def main():
     country_name = input("Enter the country: ")
     month_name = input("Enter the month: ")
     
     season = find_season(country_name, month_name)
     
     print(f"The season in {country_name} during {month_name} is {season}")
     
     if season == 'Summer':
         print("Insert summer image here")
     elif season == 'Autumn':
         print("Insert autumn image here")
     elif season == 'Winter':
         print("Insert winter image here")
     elif season == 'Spring':
         print("Insert spring image here")
     else:
         print("Unknown season")
 
 
 if __name__ == '__main__':
     main()

