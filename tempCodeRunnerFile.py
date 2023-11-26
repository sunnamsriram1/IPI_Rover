
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