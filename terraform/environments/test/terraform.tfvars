# Azure subscription vars
subscription_id = ""
client_id = ""
client_secret = ""
tenant_id = ""

# Resource Group/Location
location = "centralus"
resource_group = "tfproject"
application_type = "dev"

# Network
virtual_network_name = "tfnet"
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"

# Virtual machine
setup_script = "./setup.sh"
