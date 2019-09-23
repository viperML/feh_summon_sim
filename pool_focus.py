import csv

print("Please insert nº of Focus Heroes")
red = input("[Red]: ")
blue = input("[Blue]: ")
green = input("[Green]: ")
colorless = input("[Colorless]: ")

with open('pool_focus.csv', 'wt', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['#Red', 'Blue', 'Green', 'Colorless'])
    csv_writer.writerow( [red, blue, green, colorless] )

print("pool_focus.csv generated succesfully")
