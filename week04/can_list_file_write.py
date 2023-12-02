items = [
{"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost_per_can": 0.28},
{"name": "#1 Tall", "radius": 7.78, "height": 11.91, "cost_per_can": 0.43},
{"name": "#2", "radius": 8.73, "height": 11.59, "cost_per_can": 0.45},
{"name": "#2.5", "radius": 10.32, "height": 11.91, "cost_per_can": 0.61},
{"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost_per_can": 0.86},
{"name": "#5", "radius": 13.02, "height": 14.29, "cost_per_can": 0.83},
{"name": "#6Z", "radius": 5.40, "height": 8.89, "cost_per_can": 0.22},
{"name": "#8Z short", "radius": 6.83, "height": 7.62, "cost_per_can": 0.26},
{"name": "#10", "radius": 15.72, "height": 17.78, "cost_per_can": 1.53},
{"name": "#211", "radius": 6.83, "height": 12.38, "cost_per_can": 0.34},
{"name": "#300", "radius": 7.62, "height": 11.27, "cost_per_can": 0.38},
{"name": "#303", "radius": 8.10, "height": 11.11, "cost_per_can": 0.42}
]

# Specify the file path
file_path = "can_production_info.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write each item's information to the file
    for item in items:
        file.write(f"Name: {item['name']}, Radius: {item['radius']}, Height: {item['height']}, Cost per can: {item['cost_per_can']}\n")

print(f"Data has been written to {file_path}")