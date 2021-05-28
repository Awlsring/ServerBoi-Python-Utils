import json

with open("./serverboi_utils/region_info.json", "r") as region_file:
    sb_regions = json.load(region_file)

service_regions = {}

for sb_region, sb_region_values in sb_regions.items():
    print(sb_region)
    for service, service_values in sb_region_values.items():
        print(service)
        for region in service_values:
            print(region)
            service_regions[region["name"]] = {
                "sb_region": sb_region,
                "location": region["location"],
                "emoji": region["emoji"],
                "service": service,
            }

            # Temporary City until I bother to update everything
            if region.get("city", None):
                service_regions[region["name"]].update({"city": region["city"]})


with open("./serverboi_utils/service_region_info.json", "w") as service_region_file:
    json.dump(service_regions, service_region_file, indent=2)