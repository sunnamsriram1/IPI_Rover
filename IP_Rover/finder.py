



# import ipapi
# from setup.banner import banner, banner2, clear
# from files import colors

# c = colors

# clear()
# banner()


# def program():
#     ip = input(c.ran + "Enter target ip: " + c.ran)
#     location = ipapi.location(ip)

#     for k, v in location.items():
#         print(c.c + k + " : " + c.lr + str(v))


#     location = ipapi.location(ip)

#     if location:
#         google_maps_link = f'https://www.google.com/maps/place/{location["latitude"]},{location["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#     else:
#         print("Failed to retrieve IP details.")


# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()








# import ipapi
# import csv
# from setup.banner import banner, banner2, clear
# from files import colors

# c = colors

# clear()
# banner()

# def program():
#     ip = input(c.ran + "Enter target ip: " + c.ran)
#     location = ipapi.location(ip)

#     print("\nIP Details:")
#     for k, v in location.items():
#         print(f"{c.c}{k} : {c.lr}{v}")

#     save_to_csv(location)

#     if location:
#         google_maps_link = f'https://www.google.com/maps/place/{location["latitude"]},{location["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#     else:
#         print("Failed to retrieve IP details.")

# def save_to_csv(location):
#     csv_file = 'ip_details.csv'

#     with open(csv_file, mode='a', newline='') as file:
#         writer = csv.writer(file)

#         # Check if the file is empty, if yes, write the header
#         if file.tell() == 0:
#             header = ['IP Address', 'Org', 'City', 'Region', 'Country', 'Latitude', 'Longitude']
#             writer.writerow(header)

#         # Write the IP details to the CSV file
#         writer.writerow([location.get('ip', ''),
#                          location.get('network', ''),
#                          location.get('version', ''),
#                          location.get('region', ''),
#                          location.get('region_code', ''),
#                          location.get('country', ''),
#                          location.get('country_name', ''),
#                          location.get('country_code', ''),
#                          location.get('country_code_iso3', ''),
#                          location.get('country_capital', ''),
#                          location.get('country_tld', ''),
#                          location.get('continent_code', ''),
#                          location.get('in_en', ''),
#                          location.get('postal', ''),
#                          location.get('latitude', ''),
#                          location.get('longitude', ''),
#                          location.get('timezone', ''),
#                          location.get('utc_offset', ''),
#                          location.get('country_calling_code', ''),
#                          location.get('currency', ''),
#                          location.get('currency_name', ''),
#                          location.get('languages', ''),
#                          location.get('country_area', '')
#                          location.get('country_population', ''),
#                          location.get('asn', ''),
#                          location.get('org', ''),
#                          location.get('link', '')])

# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()

















########################################################################################


# import ipapi
# import csv
# from setup.banner import banner, banner2, clear
# from files import colors

# c = colors

# clear()
# banner()

# def program():
#     ip = input(c.ran + "Enter target ip: " + c.ran)
#     location = ipapi.location(ip)

#     print("\nIP Details:")
#     for k, v in location.items():
#         print(f"{c.c}{k} : {c.lr}{v}")

#     save_to_csv(location)

#     if location:
#         google_maps_link = f'https://www.google.com/maps/place/{location["latitude"]},{location["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#     else:
#         print("Failed to retrieve IP details.")

# def save_to_csv(location):
#     csv_file = 'ip_details.csv'

#     with open(csv_file, mode='a', newline='') as file:
#         writer = csv.writer(file)

#         # Check if the file is empty, if yes, write the header
#         if file.tell() == 0:
#             header = ['IP Address', 'Org', 'City', 'Region', 'Country', 'Latitude', 'Longitude',
#                       'Network', 'Version', 'Region Code', 'Country Name', 'Country Code',
#                       'Country Code ISO3', 'Country Capital', 'Country TLD', 'Continent Code',
#                       'In English', 'Postal Code', 'Timezone', 'UTC Offset', 'Calling Code',
#                       'Currency', 'Currency Name', 'Languages', 'Area', 'Population', 'ASN',
#                       'Organization', 'Link']

#             writer.writerow(header)
#             writer.writerow(['Attribute', 'Value'])
#         # ... (writing profile data to CSV)
#             # writer.writerow(['IP =',  ip])
#             # writer.writerow(['Network =',  network])

#         # Write the IP details to the CSV file
#             writer.writerow([location.get('ip', ''),
#                          location.get('org', ''),
#                          location.get('city', ''),
#                          location.get('region', ''),
#                          location.get('country', ''),
#                          location.get('latitude', ''),
#                          location.get('longitude', ''),
#                          location.get('network', ''),
#                          location.get('version', ''),
#                          location.get('region_code', ''),
#                          location.get('country_name', ''),
#                          location.get('country_code', ''),
#                          location.get('country_code_iso3', ''),
#                          location.get('country_capital', ''),
#                          location.get('country_tld', ''),
#                          location.get('continent_code', ''),
#                          location.get('in_en', ''),
#                          location.get('postal', ''),
#                          location.get('timezone', ''),
#                          location.get('utc_offset', ''),
#                          location.get('country_calling_code', ''),
#                          location.get('currency', ''),
#                          location.get('currency_name', ''),
#                          location.get('languages', ''),
#                          location.get('country_area', ''),
#                          location.get('country_population', ''),
#                          location.get('asn', ''),
#                          location.get('org', ''),
#                          location.get('link', '')])

# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()

#########################################################################################





























# import ipapi
# import csv
# from setup.banner import banner, banner2, clear
# from files import colors

# c = colors

# clear()
# banner()

# def program():
#     ip = input(c.ran + "Enter target ip: " + c.ran)
#     location = ipapi.location(ip)

#     print("\nIP Details:")
#     for k, v in location.items():
#         print(f"{c.c}{k} : {c.lr}{v}")

#     save_to_csv(location)

#     if location:
#         google_maps_link = f'https://www.google.com/maps/place/{location["latitude"]},{location["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#     else:
#         print("Failed to retrieve IP details.")

# def save_to_csv(location):
#     csv_file = 'ip_details.csv'

#     with open(csv_file, mode='a', newline='') as file:
#         writer = csv.writer(file)

#         # Check if the file is empty, if yes, write the header
#         if file.tell() == 0:
#             header = ['IP Address', 'Org', 'City', 'Region', 'Country', 'Latitude', 'Longitude',
#                       'Network', 'Version', 'Region Code', 'Country Name', 'Country Code',
#                       'Country Code ISO3', 'Country Capital', 'Country TLD', 'Continent Code',
#                       'In English', 'Postal Code', 'Timezone', 'UTC Offset', 'Calling Code',
#                       'Currency', 'Currency Name', 'Languages', 'Area', 'Population', 'ASN',
#                       'Organization', 'Link']

#             writer.writerow(header)
#             writer.writerow(['Attribute', 'Value'])
#         # ... (writing profile data to CSV)
#             writer.writerow(['IP =',  ip])
#             writer.writerow(['Network =',  network])


# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()











# import ipapi
# import csv
# from setup.banner import banner, banner2, clear
# from files import colors

# c = colors

# clear()
# banner()

# def program():
#     ip = input(c.ran + "Enter target ip: " + c.ran)
#     location = ipapi.location(ip)

#     print("\nIP Details:")
#     for k, v in location.items():
#         print(f"{c.c}{k} : {c.lr}{v}")

#     save_to_csv(ip, location)

#     if location:
#         google_maps_link = f'https://www.google.com/maps/place/{location["latitude"]},{location["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#     else:
#         print("Failed to retrieve IP details.")

# def save_to_csv(ip, location):
#     csv_file = 'ip_details.csv'

#     with open(csv_file, mode='a', newline='') as file:
#         writer = csv.writer(file)

#         # Check if the file is empty, if yes, write the header
#         if file.tell() == 0:
#             header = ['Attribute', 'Value']
#             writer.writerow(header)

#         # Write IP and network information to the CSV file
#         writer.writerow(['IP Address', ip])
#         writer.writerow(['Network', location.get('network', '')])
#         writer.writerow(['Version', version.get('network', '')])
#         writer.writerow(['City', city.get('city', '')])
#         writer.writerow(['Region', region.get('region', '')])
        
        
        
# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()







# import ipapi
# import csv
# from setup.banner import banner, banner2, clear
# from files import colors

# c = colors

# clear()
# banner()

# def program():
#     ip = input(c.ran + "Enter target ip: " + c.ran)
#     location = ipapi.location(ip)

#     print("\nIP Details:")
#     for k, v in location.items():
#         print(f"{c.c}{k} : {c.lr}{v}")

#     save_to_csv(ip, location)
    
# # def locat():
    
#     if location:
#         google_maps_link = f'https://www.google.com/maps/place/{location["latitude"]},{location["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#     else:
#         print("Failed to retrieve IP details.")

# def save_to_csv(ip, location):
#     csv_file = 'ip_details.csv'

#     with open(csv_file, mode='a', newline='') as file:
#         writer = csv.writer(file)

#         # Check if the file is empty, if yes, write the header
#         if file.tell() == 0:
#             header = ['Attribute', 'Value']
#             writer.writerow(header)
#         writer.writerow(['\n\n'])
#         # Write IP and network information to the CSV file
#         writer.writerow(['IP Address', ip])
#         writer.writerow(['Network', location.get('network', '')])
#         writer.writerow(['Version', location.get('version', '')])
#         writer.writerow(['City', location.get('city', '')])
#         writer.writerow(['Region', location.get('region', '')])        #writer.writerow(['IP Address', ip])
#         writer.writerow(['Region_Code', location.get('region_code', '')])
#         writer.writerow(['Country', location.get('country', '')])
#         writer.writerow(['Country_Name', location.get('country_name', '')])
#         writer.writerow(['Country_Code', location.get('country_code', '')])        #writer.writerow(['IP Address', ip])
#         writer.writerow(['Country_Code_Iso3', location.get('country_code_iso3', '')])
#         writer.writerow(['Country_Capital', location.get('country_capital', '')])
#         writer.writerow(['Country_Tld', location.get('country_tld', '')])
#         writer.writerow(['Continent_Code', location.get('continent_code', '')])       # writer.writerow(['IP Address', ip])
#         writer.writerow(['In_Eu', location.get('in_eu', '')])
#         writer.writerow(['Postal_Code', location.get('postal', '')])
#         writer.writerow(['Latitude', location.get('latitude', '')])
#         writer.writerow(['Longitude', location.get('longitude', '')])
#         writer.writerow(['TimeZone', location.get('timezone', '')])
#         writer.writerow(['Utc_Offset', location.get('utc_offset')])
#         writer.writerow(['Country_Calling_Code', location.get('country_calling_code', '')])
#         writer.writerow(['Currency', location.get('currency', '')])
#         writer.writerow(['Currency_Name', location.get('currency_name', '')])
#         writer.writerow(['Languages', location.get('languages', '')])
#         writer.writerow(['Country_Area', location.get('country_area')])
#         writer.writerow(['Country_Population', location.get('country_population', '')])
#         writer.writerow(['Asn', location.get('asn', '')])
#         writer.writerow(['Org', location.get('org', '')])
#         writer.writerow(['Google Maps Link:', google_maps_link('location', '')])
        
# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()





















# import ipapi
# import csv
# from setup.banner import banner, banner2, clear
# from files import colors

# c = colors

# clear()
# banner()

# def program():
#     ip = input(c.ran + "Enter target ip: " + c.ran)
#     location = ipapi.location(ip)

#     print("\nIP Details:")
#     for k, v in location.items():
#         print(f"{c.c}{k} : {c.lr}{v}")



#     # google_maps_link = locat(location)
#     # save_to_csv(ip, location, google_maps_link)
    
#     save_to_csv(ip, location)
#     locat(location)

# def locat(location):
#     if location:
#         google_maps_link = f'https://www.google.com/maps/place/{location["latitude"]},{location["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#         #return google_maps_link
#     else:
#         print("Failed to retrieve IP details.")
#         #return None

# def save_to_csv(ip, location):
#     csv_file = 'ip_details.csv'

#     with open(csv_file, mode='a', newline='') as file:
#         writer = csv.writer(file)

#         # Check if the file is empty, if yes, write the header
#         if file.tell() == 0:
#             header = ['Attribute', 'Value']
#             writer.writerow(header)
#             writer.writerow(['\n\n'])

#         # Write IP and network information to the CSV file
#         writer.writerow(['IP Address', ip])
#         writer.writerow(['Network', location.get('network', '')])
#         writer.writerow(['Version', location.get('version', '')])
#         writer.writerow(['City', location.get('city', '')])
#         writer.writerow(['Region', location.get('region', '')])
#         writer.writerow(['Region_Code', location.get('region_code', '')])
#         writer.writerow(['Country', location.get('country', '')])
#         writer.writerow(['Country_Name', location.get('country_name', '')])
#         writer.writerow(['Country_Code', location.get('country_code', '')])
#         writer.writerow(['Country_Code_Iso3', location.get('country_code_iso3', '')])
#         writer.writerow(['Country_Capital', location.get('country_capital', '')])
#         writer.writerow(['Country_Tld', location.get('country_tld', '')])
#         writer.writerow(['Continent_Code', location.get('continent_code', '')])
#         writer.writerow(['In_Eu', location.get('in_eu', '')])
#         writer.writerow(['Postal_Code', location.get('postal', '')])
#         writer.writerow(['Latitude', location.get('latitude', '')])
#         writer.writerow(['Longitude', location.get('longitude', '')])
#         writer.writerow(['TimeZone', location.get('timezone', '')])
#         writer.writerow(['Utc_Offset', location.get('utc_offset', '')])
#         writer.writerow(['Country_Calling_Code', location.get('country_calling_code', '')])
#         writer.writerow(['Currency', location.get('currency', '')])
#         writer.writerow(['Currency_Name', location.get('currency_name', '')])
#         writer.writerow(['Languages', location.get('languages', '')])
#         writer.writerow(['Country_Area', location.get('country_area', '')])
#         writer.writerow(['Country_Population', location.get('country_population', '')])
#         writer.writerow(['Asn', location.get('asn', '')])
#         writer.writerow(['Org', location.get('org', '')])
#         #writer.writerow(['Google Maps Link', {google_maps_link}])
#         writer.writerow(['Google Maps Link', google_maps_link]) 

# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()














# import ipapi
# import csv
# from setup.banner import banner, banner2, clear
# from files import colors

# c = colors

# clear()
# banner()

# def program():
#     try:
#         ip = input(c.ran + "Enter target ip: " + c.ran)
#         location = ipapi.location(ip)
#     except Exception as e:
#         print(e)
        
#         print("\nIP Details:")
#     for k, v in location.items():
#         print(f"{c.c}{k} : {c.lr}{v}")

#     google_maps_link = locat(location)
#     save_to_csv(ip, location, google_maps_link)

# def locat(location):
#     if location:
#         google_maps_link = f'https://www.google.com/maps/place/{location["latitude"]},{location["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#         return google_maps_link
#     else:
#         print("Failed to retrieve IP details.")
#         return None

# def save_to_csv(ip, location, google_maps_link):
#     csv_file = 'ip_details.csv'

#     with open(csv_file, mode='a', newline='') as file:
#         writer = csv.writer(file)

#         # Check if the file is empty, if yes, write the header
#         if file.tell() == 0:
#             header = ['Attribute', 'Value']
#             writer.writerow(header)
            
#         writer.writerow(['\n\n'])

#         # Write IP and network information to the CSV file
#         writer.writerow(['IP Address', ip])
#         writer.writerow(['Network', location.get('network', '')])
#         writer.writerow(['Version', location.get('version', '')])
#         writer.writerow(['City', location.get('city', '')])
#         writer.writerow(['Region', location.get('region', '')])
#         writer.writerow(['Region_Code', location.get('region_code', '')])
#         writer.writerow(['Country', location.get('country', '')])
#         writer.writerow(['Country_Name', location.get('country_name', '')])
#         writer.writerow(['Country_Code', location.get('country_code', '')])
#         writer.writerow(['Country_Code_Iso3', location.get('country_code_iso3', '')])
#         writer.writerow(['Country_Capital', location.get('country_capital', '')])
#         writer.writerow(['Country_Tld', location.get('country_tld', '')])
#         writer.writerow(['Continent_Code', location.get('continent_code', '')])
#         writer.writerow(['IN_EU', location.get('in_eu', '')])
#         writer.writerow(['Postal_Code', location.get('postal', '')])
#         writer.writerow(['Latitude', location.get('latitude', '')])
#         writer.writerow(['Longitude', location.get('longitude', '')])
#         writer.writerow(['TimeZone', location.get('timezone', '')])
#         writer.writerow(['UTC_Offset', location.get('utc_offset', '')])
#         writer.writerow(['Country_Calling_Code', location.get('country_calling_code', '')])
#         writer.writerow(['Currency', location.get('currency', '')])
#         writer.writerow(['Currency_Name', location.get('currency_name', '')])
#         writer.writerow(['Languages', location.get('languages', '')])
#         writer.writerow(['Country_Area', location.get('country_area', '')])
#         writer.writerow(['Country_Population', location.get('country_population', '')])
#         writer.writerow(['ASN', location.get('asn', '')])
#         writer.writerow(['ORG', location.get('org', '')])
#         # ... (other rows)
#         writer.writerow(['Google Maps Link', google_maps_link])

# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()




















import ipapi
import csv
from setup.banner import banner, banner2, clear
from files import colors

c = colors

clear()
banner()

def program():
    try:
        ip = input(c.ran + "Enter target ip: " + c.ran)
        location = ipapi.location(ip)

        print("\nIP Details:")
        for k, v in location.items():
            print(f"{c.c}{k} : {c.lr}{v}")

        google_maps_link = locat(location)
        save_to_csv(ip, location, google_maps_link)
    except Exception as e:
        print(e)

def locat(location):
    if location:
        google_maps_link = f'https://www.google.com/maps/place/{location["latitude"]},{location["longitude"]}'
        print(f"\nGoogle Maps Link: {google_maps_link}")
        return google_maps_link
    else:
        print("Failed to retrieve IP details.")
        return None

def save_to_csv(ip, location, google_maps_link):
    csv_file = 'ip_details.csv'

    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Check if the file is empty, if yes, write the header
        if file.tell() == 0:
            header = ['Attribute', 'Value']
            writer.writerow(header)

        writer.writerow(['\n\n'])

        # Write IP and network information to the CSV file
        writer.writerow(['IP Address', ip])
        writer.writerow(['Network', location.get('network', '')])
        writer.writerow(['Version', location.get('version', '')])
        writer.writerow(['City', location.get('city', '')])
        writer.writerow(['Region', location.get('region', '')])
        writer.writerow(['Region_Code', location.get('region_code', '')])
        writer.writerow(['Country', location.get('country', '')])
        writer.writerow(['Country_Name', location.get('country_name', '')])
        writer.writerow(['Country_Code', location.get('country_code', '')])
        writer.writerow(['Country_Code_Iso3', location.get('country_code_iso3', '')])
        writer.writerow(['Country_Capital', location.get('country_capital', '')])
        writer.writerow(['Country_Tld', location.get('country_tld', '')])
        writer.writerow(['Continent_Code', location.get('continent_code', '')])
        writer.writerow(['IN_EU', location.get('in_eu', '')])
        writer.writerow(['Postal_Code', location.get('postal', '')])
        writer.writerow(['Latitude', location.get('latitude', '')])
        writer.writerow(['Longitude', location.get('longitude', '')])
        writer.writerow(['TimeZone', location.get('timezone', '')])
        writer.writerow(['UTC_Offset', location.get('utc_offset', '')])
        writer.writerow(['Country_Calling_Code', location.get('country_calling_code', '')])
        writer.writerow(['Currency', location.get('currency', '')])
        writer.writerow(['Currency_Name', location.get('currency_name', '')])
        writer.writerow(['Languages', location.get('languages', '')])
        writer.writerow(['Country_Area', location.get('country_area', '')])
        writer.writerow(['Country_Population', location.get('country_population', '')])
        writer.writerow(['ASN', location.get('asn', '')])
        writer.writerow(['ORG', location.get('org', '')])
        # ... (other rows)
        writer.writerow(['Google Maps Link', google_maps_link])

yes = ['y', 'yes']
no = ['n', 'no']

cont = ""
while cont not in no:
    program()
    cont = input(c.lg + "Do you want to continue? [y/n]")
    if cont in no:
        clear()
        banner2()
    else:
        clear()
        banner2()























# import ipapi
# import csv
# from setup.banner import banner, banner2, clear
# from files import colors

# c = colors

# clear()
# banner()

# def program():
#     ip = input(c.ran + "Enter target ip: " + c.ran)
#     location = ipapi.location(ip)

#     print("\nIP Details:")
#     for k, v in location.items():
#         print(f"{c.c}{k} : {c.lr}{v}")

#     save_to_csv(location)

#     if location:
#         google_maps_link = f'https://www.google.com/maps/place/{location["latitude"]},{location["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#     else:
#         print("Failed to retrieve IP details.")

# def save_to_csv(location):
#     csv_file = 'ip_details.csv'

#     with open(csv_file, mode='a', newline='') as file:
#         writer = csv.writer(file)

#         # Check if the file is empty, if yes, write the header
#         if file.tell() == 0:
#             header = ['IP Address', 'Org', 'City', 'Region', 'Country', 'Latitude', 'Longitude', 'languages']
#             writer.writerow(header)

#         # Write the IP details to the CSV file
#         writer.writerow([location.get('ip', ''),
#                          location.get('org', ''),
#                          location.get('city', ''),
#                          location.get('region', ''),
#                          location.get('country', ''),
#                          location.get('latitude', ''),
#                          location.get('longitude', ''),
#                          location.get('languages',  '')])

# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()















# import ipapi
# import csv
# from setup.banner import banner, banner2, clear
# from files import colors

# c = colors

# clear()
# banner()

# def program():
#     ip = input(c.ran + "Enter target ip: " + c.ran)
#     location = ipapi.location(ip)

#     for k, v in location.items():
#         print(c.c + k + " : " + c.lr + str(v))

#     save_to_csv(location)

#     if location:
#         google_maps_link = f'https://www.google.com/maps/place/{location["latitude"]},{location["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#     else:
#         print("Failed to retrieve IP details.")

# def save_to_csv(location):
#     csv_file = 'ip_details.csv'

#     with open(csv_file, mode='a', newline='') as file:
#         writer = csv.writer(file)

#         # Check if the file is empty, if yes, write the header
#         if file.tell() == 0:
#             header = ['IP Address', 'Org', 'City', 'Region', 'Country', 'Latitude', 'Longitude']
#             writer.writerow(header)

#         # Write the IP details to the CSV file
#         writer.writerow([location.get('ip', ''),
#                          location.get('org', ''),
#                          location.get('city', ''),
#                          location.get('region', ''),
#                          location.get('country', ''),
#                          location.get('latitude', ''),
#                          location.get('longitude', '')])

# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()
















# import ipapi
# from setup.banner import banner , banner2 , clear
# from files import colors
# import json
# import urllib.request
# import webbrowser
# import os
# import IP



# c = colors

# clear()

# banner()

# # IP.finder()

# def program():

#     ip = input(c.ran + "Enter target ip: " +c.ran)
#     location = ipapi.location(ip)

#     for k , v in location.items():
#         print(c.c + k + " : " + c.lr + str(v))



# yes = ['y' , 'yes']
# no = ['n' , 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()


# import requests

# def get_ip_details(ip_address):
#     api_url = f'http://ipapi.co/{ip_address}/json/'

#     try:
#         response = requests.get(api_url)
#         data = response.json()
#         return data
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# def main(program):
#     #ip = input("Enter an IP address: ")
#     ip_details = get_ip_details(ip)

#     if ip_details:
#         print("\nIP Details:\n")
#         print(f"1) IP Address: {ip_details['ip']}")
#         print(f"2) Org: {ip_details['org']}")
#         print(f"3) City: {ip_details['city']}")
        
#         # Check if 'region' key exists before attempting to print it
#         if 'region' in ip_details:
#             print(f"4) Region: {ip_details['region']}")
        
#         print(f"5) Country: {ip_details['country']}")
#         print("6) Location:")
#         print(f"   Latitude: {ip_details['latitude']}")
#         print(f"   Longitude: {ip_details['longitude']}")

#         # Constructing the Google Maps link
#         google_maps_link = f'https://www.google.com/maps/place/{ip_details["latitude"]},{ip_details["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#     else:
#         print("Failed to retrieve IP details.")

# if __name__ == "__main__":
#     main()






# import ipapi
# from setup.banner import banner, banner2, clear
# from files import colors

# c = colors

# clear()
# banner()

# def program():
#     ip = input(c.ran + "Enter target ip: " + c.ran)
#     location = ipapi.location(ip)

#     for k, v in location.items():
#         print(c.c + k + " : " + c.lr + str(v))

# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()
#     else:
#         clear()
#         banner2()

# # Updated main function to accept an IP address as a parameter
# def main(ip_address):
#     ip_details = get_ip_details(ip_address)

#     if ip_details:
#         print("\nIP Details:\n")
#         print(f"1) IP Address: {ip_details['ip']}")
#         print(f"2) Org: {ip_details['org']}")
#         print(f"3) City: {ip_details['city']}")
        
#         # Check if 'region' key exists before attempting to print it
#         if 'region' in ip_details:
#             print(f"4) Region: {ip_details['region']}")
        
#         print(f"5) Country: {ip_details['country']}")
#         print("6) Location:")
#         print(f"   Latitude: {ip_details['latitude']}")
#         print(f"   Longitude: {ip_details['longitude']}")

#         # Constructing the Google Maps link
#         google_maps_link = f'https://www.google.com/maps/place/{ip_details["latitude"]},{ip_details["longitude"]}'
#         print(f"\nGoogle Maps Link: {google_maps_link}")
#     else:
#         print("Failed to retrieve IP details.")

# # Example usage
# if __name__ == "__main__":
#     ip_address = input("Enter an IP address: ")
#     main(ip_address)









# Example usage
# if __name__ == "__main__":
#     ip_address = input("Enter an IP address: ")
#     main(ip_address)





# yes = ['y', 'yes']
# no = ['n', 'no']

# cont = ""
# while cont not in no:
#     program()
#     cont = input(c.lg + "Do you want to continue? [y/n]")
#     if cont in no:
#         clear()
#         banner2()

        
    # else:
    #     clear()
    #     banner2()



































