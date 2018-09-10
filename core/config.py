import yaml

def load(env):
    config = None
    try:
        config = yaml.safe_load(open("config/" + env  + ".yaml", "r")) 
    except yaml.YAMLError as e:
        print("Error loading YAML", e)

    return config
