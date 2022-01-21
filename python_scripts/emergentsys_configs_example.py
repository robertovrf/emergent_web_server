# first run start_web_server_add_proxy.py !

import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

show_configs = True
show_variable_components = False
get_metric_data = False

# Function get_all_configs -- get a list of all possible configuration
response = requests.get("http://localhost:2011/meta/get_all_configs")
configs = eval(response.text)["configs"]

if show_configs:
    print("There are " + str(len(configs)) + " configurations")

    ind = 0
    for config in configs:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("%%%%%%% config " + str(ind) + " %%%%%%%%")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        ind +=1

        config = config.split("|")
        components = sorted(config[1].split(","))
        print("#############################")
        print("There are " + str(len(components)) + " components:")
        print("#############################")
        index = 0
        for c in components:
            print(str(index) + ": " + c)
            index += 1
        print("#############################")

        connectors = config[2].split(",")
        print("#############################")
        print("There are " + str(len(connectors)) + " interfaces:")
        print("#############################")
        for c in connectors:
            print(c)
        print("#############################")
        print("***********************************************************")

if show_variable_components:
    components_list = []
    for config in configs:
        config = config.split("|")
        components = config[1].split(",")
        components_list.append(components)

    all_variable_components = []
    for config_ind in range(4):
        # print(config_ind)
        # pp.pprint(components_list)
        rest_components_list = components_list[:]
        components = rest_components_list.pop(config_ind)

        variable_components = []
        index = 0
        for component in components:
            not_found = False
            for rest_components in rest_components_list:
                if component not in rest_components:
                    not_found = True
            if not_found:
                variable_components.append(component)
            index += 1
        all_variable_components += variable_components

    print("########################")
    variation_points = set(all_variable_components)
    print(len(variation_points))
    pp.pprint(variation_points)
    print("########################")


if get_metric_data:
    # Function get_perception -- get the data percieved by the system
    response = requests.get("http://localhost:2011/meta/get_perception")
    print("***********************************************************")
    print("*********************** METRIC DATA ***********************")
    print("***********************************************************")
    config = eval(response.text.replace("false", "False"))["metrics"][0]["config"]
    config = config.split("|")

    components = config[1].split(",")
    print("#############################")
    print("There are " + str(len(components)) + " components:")
    print("#############################")
    index = 0
    for c in components:
        print(str(index) + ": " + c)
        index += 1
    print("#############################")

    connectors = config[2].split(",")
    print("#############################")
    print("There are " + str(len(connectors)) + " interfaces:")
    print("#############################")
    for c in connectors:
        print(c)
    print("***********************************************************")


