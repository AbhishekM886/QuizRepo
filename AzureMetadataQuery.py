from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import json

# Create a Compute Management Client
credential = DefaultAzureCredential()
subscription_id = 'YOUR_SUBSCRIPTION_ID'
compute_client = ComputeManagementClient(credential, subscription_id)

# Get the current VM's resource group and name
resource_group = 'YOUR_RESOURCE_GROUP'
vm_name = 'YOUR_VM_NAME'

# Retrieve instance metadata
vm = compute_client.virtual_machines.get(resource_group, vm_name, expand='instanceView')

# Define the key you want to retrieve
data_key = 'location'

# Check if the key exists in the metadata
if hasattr(vm, data_key):
    data_value = getattr(vm, data_key)
    metadata = {data_key: data_value}
    json_output = json.dumps(metadata, indent=4)
    print(json_output)
else:
    print(f"Key '{data_key}' not found in the metadata.")
