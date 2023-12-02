"""
Work as a team to write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the following 

12 steel can sizes. Then visually examine the output and answer this question, “Which can size has the highest storage efficiency?”

Your program must compute the volume of all 12 can sizes.
Your program must compute the surface area of all 12 can sizes.
Your program must compute and print the storage efficiency of all 12 can sizes.

"""
import math

def main():
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
    storage_efficiency_greatest = 0

    for item in items:
        radius = item["radius"]
        height = item["height"]

        volume = compute_volume(radius, height)

        surface_area = compute_surface_area(radius, height)

        storage_efficiency = compute_storage_efficieny(volume, surface_area)

        if storage_efficiency < 100:
            storage_efficiency_greatest = storage_efficiency
            name = item["name"]
        
        print(f'{name} {storage_efficiency_greatest:.2f}')
    pass

# def main():
#     file_path = "week04\can_production_info.txt"
#     can_information = []
#     with open(file_path, "r") as file:
#         lines = file.readlines()

#         for line in lines:
#             components = line.split(", ")
        
#             name = components[0].split(": ")[1]
#             radius = float(components[1].split(": ")[1])
#             height = float(components[2].split(": ")[1])
#             cost_per_can = float(components[3].split(": ")[1])

#             item = {"name": name, "radius": radius, "height": height, "cost_per_can": cost_per_can}
#             can_information.append(item)
#     volumes = []
#     for item in can_information:
#         volume = compute_volume(radius, height)
#         name = name
#         volumes.append((name, volume))
#     surface_areas = []
#     for item in can_information:
#         surface_area = compute_surface_area(radius, height)
#         name = name
#         surface_areas.append((name, surface_area))
#     storage_efficiencies = []
#     for volume_item, surface_area_item in zip(volumes, surface_areas):
#         name = volume_item[0]
#         volume = volume_item[1]
#         surface_area = surface_area_item[1]

#         storage_efficiency = compute_storage_efficieny(volume, surface_area)
#         storage_efficiencies.append({"name": name, "storage_efficiency": storage_efficiency})        
#         file_path = "storage_efficiencies.txt"
#     with open(file_path, "w") as file:
#         for item in storage_efficiencies:
#             file.write(f"Name: {item['name']}, Storage_efficiency: {item['storage_efficiency']}")
#     cost_efficiences = []
#     for item in can_information:
#         volume = compute_volume(radius, height)
#         cost_efficiency = compute_cost_efficieny(volume, cost_per_can)

#         cost_efficiences.append(cost_efficiency)
#     file_path = "cost_efficiencies.txt"
#     with open(file_path, "w") as file:
#         for item in cost_efficiences:
#             file.write(f"Name: {item['name']}, Cost_efficiency: {item['cost_efficiency']}")
#     pass

def compute_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficieny(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficieny(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()

""" Stretch Challenges """

"""

Add another function named compute_storage_efficiency to your program. 
This function should call the compute_volume and compute_surface_area 
functions and then compute and return the storage efficiency of a steel 
can size. Replace code in the main function with a call to the 
compute_storage_efficiency function as appropriate. Did adding and 
calling the compute_storage_efficiency function reduce the number of lines of code in your program?

The table of can sizes that appears in the Assignment section above 
includes a column that contains the cost per can of each steel can size. 
Add another function to your program named compute_cost_efficiency 
that computes and returns the volume of a steel can divided by its cost. 
Write code to call the compute_cost_efficiency function and print the 
cost efficiency for each can size. Then visually examine the output 
and answer this question, “Which can size has the highest cost efficiency?”

If you remember how to use lists and a for loop from CSE 110, 
rewrite your main function so that it uses a list or lists that 
contain the can size names and dimensions. Then write a loop that processes the values in the list.
Add if statements inside the loop to automatically determine 
which can size has the best storage efficiency and which can size has the best cost efficiency.

"""