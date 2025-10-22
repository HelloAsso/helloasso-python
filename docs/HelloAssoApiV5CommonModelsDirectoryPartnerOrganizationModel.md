# HelloAssoApiV5CommonModelsDirectoryPartnerOrganizationModel

PartnerOrganizationModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**HelloAssoApiV5CommonModelsDirectoryDirectoryOrganizationPublicModel**](HelloAssoApiV5CommonModelsDirectoryDirectoryOrganizationPublicModel.md) |  | [optional] 
**available_access_token** | **bool** | True if exist a valid organization access token obtained by authorize flow | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_directory_partner_organization_model import HelloAssoApiV5CommonModelsDirectoryPartnerOrganizationModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsDirectoryPartnerOrganizationModel from a JSON string
hello_asso_api_v5_common_models_directory_partner_organization_model_instance = HelloAssoApiV5CommonModelsDirectoryPartnerOrganizationModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsDirectoryPartnerOrganizationModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_directory_partner_organization_model_dict = hello_asso_api_v5_common_models_directory_partner_organization_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsDirectoryPartnerOrganizationModel from a dict
hello_asso_api_v5_common_models_directory_partner_organization_model_from_dict = HelloAssoApiV5CommonModelsDirectoryPartnerOrganizationModel.from_dict(hello_asso_api_v5_common_models_directory_partner_organization_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


