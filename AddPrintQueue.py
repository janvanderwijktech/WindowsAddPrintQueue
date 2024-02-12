import os
import sys
import argparse
import configparser
import win32print

def add_printer(printer_name, set_default=True):
    # Path to the server.ini file
    ini_file_path = 'server.ini'

    # Check if the file exists
    if not os.path.exists(ini_file_path):
        print("The server.ini file does not exist.")
        return

    # Parse the server.ini file
    config = configparser.ConfigParser()
    config.read(ini_file_path)

    # Get the server name from server.ini
    server_name = config['ServerName']['Server']

    # Format the printer name to the correct format
    printer_name_with_server = r'\\{}\{}'.format(server_name, printer_name)

    # Add the printer
    try:
        win32print.AddPrinterConnection(printer_name_with_server)
        print("Printer {} successfully added.".format(printer_name_with_server))
    except Exception as e:
        print("An error occurred while adding the printer: ", e)
        return

    # Set the added printer as the default printer
    if set_default:
        try:
            win32print.SetDefaultPrinter(printer_name_with_server)
            print("The printer {} has been set as the default printer.".format(printer_name_with_server))
        except Exception as e:
            print("An error occurred while setting the default printer: ", e)
            return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add a print queue and optionally set it as the default printer.')
    parser.add_argument('printer_name', type=str, help='The name of the print queue')
    parser.add_argument('-n', '--not-default', action='store_false', help='Use this option to add the print queue without setting it as the default printer.')
    args = parser.parse_args()

    add_printer(args.printer_name, set_default=args.not_default)
