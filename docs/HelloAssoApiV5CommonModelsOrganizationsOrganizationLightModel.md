# HelloAssoApiV5CommonModelsOrganizationsOrganizationLightModel

OrganizationLightModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo** | **str** | Logo of organization | [optional] 
**name** | **str** | Name of organization | [optional] 
**role** | [**HelloAssoModelsEnumsGlobalRole**](HelloAssoModelsEnumsGlobalRole.md) |  | [optional] 
**city** | **str** | Organization city | [optional] 
**zip_code** | **str** | Organization zip code | [optional] 
**description** | **str** | Organization description | [optional] 
**update_date** | **datetime** | Last update date of the organization | [optional] 
**category_jo_id** | **int** |  | [optional] 
**url** | **str** | The organization url | [optional] 
**organization_slug** | **str** | The organization slug | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_organizations_organization_light_model import HelloAssoApiV5CommonModelsOrganizationsOrganizationLightModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsOrganizationsOrganizationLightModel from a JSON string
hello_asso_api_v5_common_models_organizations_organization_light_model_instance = HelloAssoApiV5CommonModelsOrganizationsOrganizationLightModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsOrganizationsOrganizationLightModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_organizations_organization_light_model_dict = hello_asso_api_v5_common_models_organizations_organization_light_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsOrganizationsOrganizationLightModel from a dict
hello_asso_api_v5_common_models_organizations_organization_light_model_from_dict = HelloAssoApiV5CommonModelsOrganizationsOrganizationLightModel.from_dict(hello_asso_api_v5_common_models_organizations_organization_light_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


