# first run start_web_server_add_proxy.py !

import requests
import pprint
import random


def generate_input_variable_values_randomly():
    cache_choice = random.choice([True, False])
    compression_choice = random.choice([True, False])
    print("generated: ")
    print("cache: " + str(cache_choice))
    print("compression: " + str(compression_choice))
    return cache_choice, compression_choice


def find_necessary_component(use_cache, use_compression):
    if use_cache and use_compression:
        return '../repository/http/handler/GET/HTTPGETCHCMP.o'
    if use_cache:
        return '../repository/http/handler/GET/HTTPGETCH.o'
    if use_compression:
        return '../repository/http/handler/GET/HTTPGETCMP.o'
    return '../repository/http/handler/GET/HTTPGET.o'


def get_all_configs(use_cache, use_compression):
    response = requests.get("http://localhost:2011/meta/get_all_configs")
    configs = eval(response.text)["configs"]
    print("There are altogether " + str(len(configs)) + " configurations!")
    return configs


pp = pprint.PrettyPrinter(indent=4)

cache, compression = generate_input_variable_values_randomly()
configs = get_all_configs(cache, compression)

filtered_configs = [c for c in configs if find_necessary_component(cache, compression) in c]
if len(filtered_configs) is not 1:
    print("More than one configurations found for this combination of input parameters. Aborting.")
    exit(0)

selected_config = filtered_configs[0]
print("selected configuration:")
pp.pprint(selected_config)

requests.post("http://localhost:2011/meta/set_config", json={"config":selected_config})
print("New configuration applied successfully!")
