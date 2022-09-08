"""
Ref: https://docs.microsoft.com/en-us/azure/developer/python/sdk/examples/azure-sdk-example-resource-group

Prep work:
pip install -r AzReq1.txt
    Which contains:
    azure-mgmt-resource>=18.0.0
    azure-identity>=1.5.0

Observed Terminal output:
Collecting azure-mgmt-resource>=18.0.0
  Downloading azure_mgmt_resource-21.1.0-py3-none-any.whl (1.8 MB)
     |████████████████████████████████| 1.8 MB 939 kB/s
Collecting azure-identity>=1.5.0
  Downloading azure_identity-1.10.0-py3-none-any.whl (134 kB)
     |████████████████████████████████| 134 kB 3.3 MB/s
Collecting azure-mgmt-core<2.0.0,>=1.3.0
  Downloading azure_mgmt_core-1.3.2-py3-none-any.whl (26 kB)
Collecting azure-common~=1.1
  Downloading azure_common-1.1.28-py2.py3-none-any.whl (14 kB)
Collecting msrest>=0.6.21
  Downloading msrest-0.7.1-py3-none-any.whl (85 kB)
     |████████████████████████████████| 85 kB 1.2 MB/s
Collecting cryptography>=2.5
  Downloading cryptography-38.0.1-cp36-abi3-win_amd64.whl (2.4 MB)
     |████████████████████████████████| 2.4 MB 3.3 MB/s
Collecting msal<2.0.0,>=1.12.0
  Downloading msal-1.18.0-py2.py3-none-any.whl (82 kB)
     |████████████████████████████████| 82 kB 6.1 MB/s
Collecting msal-extensions<2.0.0,>=0.3.0
  Downloading msal_extensions-1.0.0-py2.py3-none-any.whl (19 kB)
Collecting six>=1.12.0
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting azure-core<2.0.0,>=1.11.0
  Downloading azure_core-1.25.1-py3-none-any.whl (178 kB)
     |████████████████████████████████| 178 kB 3.2 MB/s
Collecting requests>=2.18.4
  Downloading requests-2.28.1-py3-none-any.whl (62 kB)
     |████████████████████████████████| 62 kB 571 kB/s
Collecting typing-extensions>=4.0.1
  Downloading typing_extensions-4.3.0-py3-none-any.whl (25 kB)
Collecting cffi>=1.12
  Downloading cffi-1.15.1-cp310-cp310-win_amd64.whl (179 kB)
     |████████████████████████████████| 179 kB 3.2 MB/s
Collecting PyJWT[crypto]<3,>=1.0.0
  Downloading PyJWT-2.4.0-py3-none-any.whl (18 kB)
Collecting portalocker<3,>=1.6
  Downloading portalocker-2.5.1-py2.py3-none-any.whl (15 kB)
Collecting requests-oauthlib>=0.5.0
  Downloading requests_oauthlib-1.3.1-py2.py3-none-any.whl (23 kB)
Collecting isodate>=0.6.0
  Downloading isodate-0.6.1-py2.py3-none-any.whl (41 kB)
     |████████████████████████████████| 41 kB 59 kB/s
Collecting certifi>=2017.4.17
  Downloading certifi-2022.6.15-py3-none-any.whl (160 kB)
     |████████████████████████████████| 160 kB ...
Collecting pycparser
  Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
     |████████████████████████████████| 118 kB 6.4 MB/s
Collecting pywin32>=226
  Downloading pywin32-304-cp310-cp310-win_amd64.whl (12.1 MB)
     |████████████████████████████████| 12.1 MB ...
Collecting charset-normalizer<3,>=2
  Downloading charset_normalizer-2.1.1-py3-none-any.whl (39 kB)
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.12-py2.py3-none-any.whl (140 kB)
     |████████████████████████████████| 140 kB ...
Collecting idna<4,>=2.5
  Downloading idna-3.3-py3-none-any.whl (61 kB)
Collecting oauthlib>=3.0.0
     |████████████████████████████████| 151 kB 6.4 MB/s
Installing collected packages: pycparser, cffi, urllib3, PyJWT, idna, cryptography, charset-normalizer, certifi, typing-extensions, six, requests, pywin32, oauthlib,
requests-oauthlib, portalocker, msal, isodate, azure-core, msrest, msal-extensions, azure-mgmt-core, azure-common, azure-mgmt-resource, azure-identity
Successfully installed PyJWT-2.4.0 azure-common-1.1.28 azure-core-1.25.1 azure-identity-1.10.0 azure-mgmt-core-1.3.2 azure-mgmt-resource-21.1.0 certifi-2022.6.15 cffi
-1.15.1 charset-normalizer-2.1.1 cryptography-38.0.1 idna-3.3 isodate-0.6.1 msal-1.18.0 msal-extensions-1.0.0 msrest-0.7.1 oauthlib-3.2.0 portalocker-2.5.1 pycparser-
2.21 pywin32-304 requests-2.28.1 requests-oauthlib-1.3.1 six-1.16.0 typing-extensions-4.3.0 urllib3-1.26.12

"""


# Import the needed credential and management objects from the libraries.
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential

# Input
subscription_id = "91f711e4-1620-4e8b-a64c-92a170101010"
resourcegroup_name = "INF601b"
location = "centralus"
tag_owner = "Sam Boutros"
tag_endoflife = "12/31/2023"

# Acquire a credential object using CLI-based authentication.
"""
We must login to Azure tenant first. In a Terminal window:
    az login
To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code ABCDEFGHI to authenticate.
[
  {
    "cloudName": "AzureCloud",
    "id": "12341234-1234-1234-1234-123412341234",
    "isDefault": true,
    "name": "Sam something",
    "state": "Enabled",
    "tenantId": "12341234-1234-1234-1234-123412341234",
    "user": {
      "name": "sam@something.com",
      "type": "user"
    }
  }
]
"""
credential = AzureCliCredential()

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)

# Provision the resource group.
rg_result = resource_client.resource_groups.create_or_update(
    resourcegroup_name,
    {
        "location": location
    }
)
print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")

# Update RG, adding tags
Rg_result = resource_client.resource_groups.create_or_update(
    resourcegroup_name,
    {
        "location": location,
        "tags": { "owner":tag_owner, "EndOfLife":tag_endoflife }
    }
)
print(f"Updated resource group {rg_result.name} with tags")
