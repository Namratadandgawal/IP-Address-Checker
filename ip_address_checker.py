"""
=========================================================
                IP ADDRESS CHECKER v1.0
---------------------------------------------------------
Author : Namrata Dandgawal

Description:
A simple networking tool that displays computer
information and performs website/IP lookups.

Features:
✔ View Computer Information
✔ Check Internet Connection
✔ Website DNS Lookup
✔ Reverse DNS Lookup
✔ Detect Private/Public IP
✔ Detect IPv4 / IPv6
✔ Accept Website OR IP Address
=========================================================
"""

# Import required modules
import socket
import ipaddress
from datetime import datetime


# -------------------------------------------------------
# Function: Check Internet Connection
# -------------------------------------------------------
def check_internet():
    """
    Tries to connect to Google's DNS server.
    Returns Connected or Not Connected.
    """
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return "Connected"
    except OSError:
        return "Not Connected"


# -------------------------------------------------------
# Function: Check Private or Public IP
# -------------------------------------------------------
def check_ip_type(ip):
    """
    Returns whether an IP is Private or Public.
    """
    ip_obj = ipaddress.ip_address(ip)

    if ip_obj.is_private:
        return "Private"
    else:
        return "Public"


# -------------------------------------------------------
# Function: Display Computer Information
# -------------------------------------------------------
def computer_information():

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print("\n" + "=" * 50)
    print("COMPUTER INFORMATION")
    print("=" * 50)

    print("Date & Time :", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("Computer    :", hostname)
    print("Local IP    :", local_ip)
    print("IP Type     :", check_ip_type(local_ip))
    print("IP Version  : IPv" + str(ipaddress.ip_address(local_ip).version))
    print("Internet    :", check_internet())


# -------------------------------------------------------
# Function: Website / IP Lookup
# -------------------------------------------------------
def lookup():

    user_input = input("\nEnter Website or IP Address: ").strip()

    if user_input == "":
        print("Input cannot be empty.")
        return

    # ---------------------------------------------------
    # Check whether user entered an IP Address
    # ---------------------------------------------------
    try:

        ipaddress.ip_address(user_input)

        print("\n" + "=" * 50)
        print("IP ADDRESS INFORMATION")
        print("=" * 50)

        print("IP Address  :", user_input)
        print("IP Type     :", check_ip_type(user_input))
        print("IP Version  : IPv" + str(ipaddress.ip_address(user_input).version))

        # Reverse DNS Lookup
        try:
            hostname = socket.gethostbyaddr(user_input)
            print("Host Name   :", hostname[0])

        except socket.herror:
            print("Host Name   : Reverse DNS Not Available")

        return

    except ValueError:
        pass

    # ---------------------------------------------------
    # Treat Input as Website
    # ---------------------------------------------------
    try:

        ip = socket.gethostbyname(user_input)

        print("\n" + "=" * 50)
        print("WEBSITE INFORMATION")
        print("=" * 50)

        print("Website     :", user_input)
        print("IP Address  :", ip)
        print("IP Type     :", check_ip_type(ip))
        print("IP Version  : IPv" + str(ipaddress.ip_address(ip).version))

        try:
            hostname = socket.gethostbyaddr(ip)
            print("Host Name   :", hostname[0])

        except socket.herror:
            print("Host Name   : Reverse DNS Not Available")

    except socket.gaierror:
        print("Invalid Website or IP Address.")


# -------------------------------------------------------
# Main Program
# -------------------------------------------------------
while True:

    print("\n" + "=" * 55)
    print("              IP ADDRESS CHECKER")
    print("=" * 55)

    print("1. View Computer Information")
    print("2. Lookup Website / IP Address")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        computer_information()

    elif choice == "2":
        lookup()

    elif choice == "3":
        print("\nThank you for using IP Address Checker!")
        break

    else:
        print("Invalid choice. Please enter 1, 2 or 3.")