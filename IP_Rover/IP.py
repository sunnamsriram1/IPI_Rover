
# IPicker

# Author - D3adpool2K

# github - https://github.com/Deadpool2000



# import json
# import urllib.request
# import webbrowser
# import os
# try:
#     R='\033[91m'
#     Y='\033[93m'
#     G='\033[92m'
#     CY='\033[96m'
#     W='\033[97m'
#     path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
#     def start():
#         os.system('clear')
#         print (CY+"""
#  _ ______ _       _                 
# | (_____ (_)     | |                
# | |_____) )  ____| |  _ _____  ____ 
# | |  ____/ |/ ___) |_/ ) ___ |/ ___)
# | | |    | ( (___|  _ (| ____| |    
# |_|_|    |_|\____)_| \_)_____)_|   """+Y+"""v1.1"""+G+"""

             
#      Simple IP Address locator

# """+R+""">>"""+Y+"""----"""+CY+""" Author - Deadpool2000 """+Y+"""----"""+R+"""<<""")
        
#     def m3():
#         try:
#             print(R+"""\n
# #"""+Y+""" Select option"""+G+""" >>"""+Y+"""

# 1)"""+G+""" Check your IP info"""+Y+"""
# 2)"""+G+""" Check other IP info"""+Y+"""
# 3)"""+G+""" Exit
# """)
#             ch=int(input(CY+"Enter Your choice: "+W))
#             if ch==1:
#                 main2()
#                 m3()
#             elif ch==2:
#                 main()
#                 m3()
#             elif ch==3:
#                 print(Y+"Exit................"+W)
#             else:
#                 print(R+"\nInvalid choice! Please try again\n")
#                 m3()
#         except ValueError:
#             print(R+"\nInvalid choice! Please try again\n")
#             m3()

    
#     def finder(u):
#         try:
#             try:
#                 response = urllib.request.urlopen(u)
#                 data = json.load(response)
   

#                 print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#                 print(Y+'\n>>>'+CY+' IP address details\n ')
#                 print(G+"1) IP Address : "+Y,data['query'],'\n')
#                 print(G+"2) Org : "+Y,data['org'],'\n')
#                 print(G+"3) City : "+Y,data['city'],'\n')
#                 print(G+"4) Region : "+Y,data['regionName'],'\n')
#                 print(G+"5) Country : "+Y,data['country'],'\n')
#                 print(G+"6) Location\n")
#                 print(G+"\tLattitude : "+Y,data['lat'],'\n')
#                 print(G+"\tLongitude : "+Y,data['lon'],'\n')
#                 l='https://www.google.com/maps/place/'+str(data['lat'])+'+'+str(data['lon'])
#                 print(R+"\n#"+Y+" Google Map link : "+CY,l)
#                 path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
#                 if path:
#                     link='am start -a android.intent.action.VIEW -d '+str(l)
#                     pr=input(R+"\n>>"+Y+" Open link in browser?"+G+" (y|n): "+W)
#                     if pr=="y":
#                         lnk=str(link)+" > /dev/null"
#                         os.system(str(lnk))
#                         start()
#                         m3()
#                     elif pr=="n":
#                         print("\nCheck another IP or exit using Ctrl + C\n\n")
#                         start()
#                         m3()
#                     else:
#                         print("\nInvalid choice! Please try again\n")
#                         m3()
#                 else:
#                     pr=input(R+"\n>>"+Y+" Open link in browser?"+G+" (y|n): "+W)
#                     if pr=="y":
#                         webbrowser.open(l,new=0)
#                         start()
#                         m3()
#                     elif pr=="n":
#                         print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#                         print(Y+"\nCheck another IP or exit using "+R+"Ctrl + C\n\n")
#                         start()
#                         m3()
#                     else:
#                         print(R+"\nInvalid choice! Please try again\n")
#                         m3()
#                 return
#             except KeyError:
#                 print(R+"\nError! Invalid IP/Website Address!\n"+W)
#                 m3()
#         except urllib.error.URLError:
#             print(R+"\nError!"+Y+" Please check your internet connection!\n"+W)
#             exit()

        
#     def main():
#         u=input(G+"\n>>> "+Y+"Enter IP Address/website address:"+W+" ")
#         if u=="":
#             print(R+"\nEnter valid IP Address/website address!")
#             main()
#         else:
#             url ='http://ip-api.com/json/'+u
#             finder(url)
#     def main2():
#         url ='http://ip-api.com/json/'
#         finder(url)
        
#     start()
#     m3()
# except KeyboardInterrupt:
#     print(Y+"\nInterrupted ! Have a nice day :)"+W)





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

# def main():
#     ip_address = input("Enter an IP address: ")
#     ip_details = get_ip_details(ip_address)

#     if ip_details:
#         print("\nIP Details:")
#         print(f"IP Address: {ip_details['ip']}")
#         print(f"Location: {ip_details['city']}, {ip_details['region']}, {ip_details['country_name']}")
#         print(f"Latitude/Longitude: {ip_details['latitude']}, {ip_details['longitude']}")
#     else:
#         print("Failed to retrieve IP details.")

# if __name__ == "__main__":
#     main()








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

# def main():
#     ip_address = input("Enter an IP address: ")
#     ip_details = get_ip_details(ip_address)

#     if ip_details:
#         print("\nIP Details:")
#         print(f"1) IP Address: {ip_details['ip']}")
#         print(f"2) Org: {ip_details['org']}")
#         print(f"3) City: {ip_details['city']}")
#         print(f"4) Region: {ip_details['regionName']}")
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

# def main():
#     ip_address = input("Enter an IP address: ")
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

# if __name__ == "__main__":
#     main()



