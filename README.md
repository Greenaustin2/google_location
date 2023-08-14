# Google Location History Visualizer

[graphic-balance.com](https://graphic-balance-3bf05d57cb18.herokuapp.com/)

## About


This program creates a line drawing using Google Location History data points. For this to be effective, your Google Location History tracker has ideally been running for some time. The sample image represents two years of data points. Download your location history below via Google Takeout. Be sure to extract only the location history and include no other metrics. You will need the data to be in JSON format.

[Retrieve your Google Location History](https://takeout.google.com/)

![screen shot one](glh.png?raw=true)

## Running Locally

### Clone the directory
```
git clone https://github.com/Greenaustin2/google_location.git
```
### Move into directory
```
cd google_location
```
### create a JSON file and add your location history data
```
touch records.json
```
### in main.py, set the max and min longitudinal and latitudinal points, this will dictate the size of the canvas.
```
llx = -1230000000
lly = 453000000
urx = -1225000000
ury = 458000000
```

## Future Functionality

The program is not at all user-friendly, a web version is currently in the works, and will overlay the inputted data directly onto a map with user-dictated style functionality and options to export. 
