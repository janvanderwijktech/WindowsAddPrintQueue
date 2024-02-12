# WindowsAddPrintQueue
Add Printer Script
Description:
This Python script allows you to add a printer queue to a Windows server and optionally set it as the default printer. The script reads the server name from a server.ini file and formats the printer name accordingly. It utilizes the win32print module to interact with the Windows printing system.

Requirements
Python 3.x
pypiwin32 module (install via pip install pypiwin32)
Usage
Create a server.ini file in the same directory as the script with the following content:
[ServerName]
Server = <YourServerName>

Replace <YourServerName> with the name of your Windows server.

Run the script using the following command:

python add_printer.py <printer_name> [-n | --not-default]
<printer_name>: The name of the printer queue to be added.
-n, --not-default (optional): Use this flag to add the printer without setting it as the default printer.

Example
To add a printer named HP-WONEN-MAGAZIJN2 and set it as the default printer, run:
python add_printer.py HP-WONEN-MAGAZIJN2

To add a printer without setting it as the default printer, run:
python add_printer.py HP-WONEN-MAGAZIJN2 -n
or
python add_printer.py HP-WONEN-MAGAZIJN2 --not-default

License
This script is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments
This script was created by Jan van der Wijk
