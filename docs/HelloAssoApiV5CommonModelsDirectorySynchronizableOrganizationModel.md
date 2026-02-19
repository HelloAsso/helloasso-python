# HelloAssoApiV5CommonModelsDirectorySynchronizableOrganizationModel

SynchronizableOrganizationModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**HelloAssoApiV5CommonModelsEnumsRecordActionType**](HelloAssoApiV5CommonModelsEnumsRecordActionType.md) |  | [optional] 
**record** | [**HelloAssoApiV5CommonModelsOrganizationsOrganizationBasicModel**](HelloAssoApiV5CommonModelsOrganizationsOrganizationBasicModel.md) |  | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_directory_synchronizable_organization_model import HelloAssoApiV5CommonModelsDirectorySynchronizableOrganizationModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsDirectorySynchronizableOrganizationModel from a JSON string
hello_asso_api_v5_common_models_directory_synchronizable_organization_model_instance = HelloAssoApiV5CommonModelsDirectorySynchronizableOrganizationModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsDirectorySynchronizableOrganizationModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_directory_synchronizable_organization_model_dict = hello_asso_api_v5_common_models_directory_synchronizable_organization_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsDirectorySynchronizableOrganizationModel from a dict
hello_asso_api_v5_common_models_directory_synchronizable_organization_model_from_dict = HelloAssoApiV5CommonModelsDirectorySynchronizableOrganizationModel.from_dict(hello_asso_api_v5_common_models_directory_synchronizable_organization_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


