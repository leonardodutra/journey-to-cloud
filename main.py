import yaml
import sys
from yaml.loader import SafeLoader
service = sys.argv[1]
yaml_file = service + '-hom.yaml'
env_file = 'C:/Users/leona/PycharmProjects/pythonProject/' + service + '.env'
env_vars = [] # or dict {}
total_number_vars_dot_env = 0
total_number_vars_configmap_yaml = 0
with open(env_file) as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue

        key, value = line.strip().split('=', 1)


        with open(yaml_file, 'r') as yml:
            data = yaml.load(yml, Loader=SafeLoader)

            if value == data['data'][key]:
#                print(key)
 #               print(sys.argv[1])
                total_number_vars_configmap_yaml += 1
                total_number_vars_dot_env += 1
print("Total total_number_vars_dot_env: ")
print(total_number_vars_dot_env)
print("Total total_number_vars_configmap_yaml: ")
print(total_number_vars_configmap_yaml)
