import csv
import gpxpy
import gpxpy.gpx
import streamlit as st

def csv_to_gpx(csv_content, gpx_file):
    # Create a new GPX object
    gpx = gpxpy.gpx.GPX()

    # Read the CSV data
    reader = csv.reader(csv_content)
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
            st.warning(f"Skipped invalid row: {row}")

    # Write GPX data to file
    with open(gpx_file, 'w') as gpxfile:
        gpxfile.write(gpx.to_xml())

    st.success("GPX file created successfully.")

# Streamlit app
st.title("CSV to GPX Converter")

uploaded_csv = st.file_uploader("Choose a CSV file", type="csv")
output_filename = st.text_input("Enter output GPX filename", "output.gpx")

if st.button("Convert"):
    if uploaded_csv and output_filename:
        csv_file_content = uploaded_csv.getvalue().decode("utf-8").splitlines()
        csv_reader = csv.reader(csv_file_content)
        output_path = output_filename
        csv_to_gpx(csv_reader, output_path)
        with open(output_path, 'rb') as f:
            st.download_button(
                label="Download GPX file",
                data=f,
                file_name=output_filename,
                mime='application/gpx+xml'
            )
    else:
        st.error("Please upload a CSV file and enter a GPX filename.")
