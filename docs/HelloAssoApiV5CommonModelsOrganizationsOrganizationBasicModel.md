# HelloAssoApiV5CommonModelsOrganizationsOrganizationBasicModel

A basic organization model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The organization url | [optional] 
**organization_slug** | **str** | The organization slug | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_organizations_organization_basic_model import HelloAssoApiV5CommonModelsOrganizationsOrganizationBasicModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsOrganizationsOrganizationBasicModel from a JSON string
hello_asso_api_v5_common_models_organizations_organization_basic_model_instance = HelloAssoApiV5CommonModelsOrganizationsOrganizationBasicModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsOrganizationsOrganizationBasicModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_organizations_organization_basic_model_dict = hello_asso_api_v5_common_models_organizations_organization_basic_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsOrganizationsOrganizationBasicModel from a dict
hello_asso_api_v5_common_models_organizations_organization_basic_model_from_dict = HelloAssoApiV5CommonModelsOrganizationsOrganizationBasicModel.from_dict(hello_asso_api_v5_common_models_organizations_organization_basic_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


