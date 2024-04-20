import csv
import gpxpy
import gpxpy.gpx
import tkinter as tk
from tkinter import filedialog

def csv_to_gpx(csv_file, gpx_file):
    # Create a new GPX object
    gpx = gpxpy.gpx.GPX()

    # Open the CSV file and read data
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                # Extract data from CSV
                name = row[0]
                latitude = float(row[1])
                longitude = float(row[2])

                # Create GPX waypoint
                waypoint = gpxpy.gpx.GPXWaypoint(latitude, longitude, name=name)
                gpx.waypoints.append(waypoint)
            except (IndexError, ValueError) as e:
                print(f"Skipped invalid row: {row}")

    # Write GPX data to file
    with open(gpx_file, 'w') as gpxfile:
        gpxfile.write(gpx.to_xml())

    print("GPX file created successfully.")

def select_input_file():
    input_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if input_file_path:
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, input_file_path)

def select_output_file():
    output_file_path = filedialog.asksaveasfilename(defaultextension=".gpx", filetypes=[("GPX files", "*.gpx")])
    if output_file_path:
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, output_file_path)

def convert():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    if input_file and output_file:
        csv_to_gpx(input_file, output_file)
        status_label.config(text="Conversion completed successfully.")
    else:
        status_label.config(text="Please select input and output files.")

# Create the main application window
root = tk.Tk()
root.title("CSV to GPX Converter")

# Create GUI elements
input_file_label = tk.Label(root, text="Input CSV File:")
input_file_label.grid(row=0, column=0, sticky="w")
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=5, pady=5)
input_file_button = tk.Button(root, text="Browse", command=select_input_file)
input_file_button.grid(row=0, column=2)

output_file_label = tk.Label(root, text="Output GPX File:")
output_file_label.grid(row=1, column=0, sticky="w")
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=5, pady=5)
output_file_button = tk.Button(root, text="Browse", command=select_output_file)
output_file_button.grid(row=1, column=2)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=1, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
