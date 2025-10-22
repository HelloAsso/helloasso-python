# HelloAssoApiV5CommonModelsFormsCustomFieldPublicModel

A custom field can be assigned to a Tier or an ExtraOption  It is used to give extra information during the reservation of a tier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the customField | [optional] [readonly] 
**values** | **List[str]** | The list of possible values if type is a CHOICE_LIST | [optional] [readonly] 
**is_required** | **bool** | True if the custom field must be filled by the user before validating a cart | [optional] [readonly] 
**type** | [**HelloAssoApiV5CommonModelsEnumsFieldType**](HelloAssoApiV5CommonModelsEnumsFieldType.md) |  | [optional] 
**label** | **str** | The label to be displayed to the user | [optional] [readonly] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_forms_custom_field_public_model import HelloAssoApiV5CommonModelsFormsCustomFieldPublicModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsFormsCustomFieldPublicModel from a JSON string
hello_asso_api_v5_common_models_forms_custom_field_public_model_instance = HelloAssoApiV5CommonModelsFormsCustomFieldPublicModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsFormsCustomFieldPublicModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_forms_custom_field_public_model_dict = hello_asso_api_v5_common_models_forms_custom_field_public_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsFormsCustomFieldPublicModel from a dict
hello_asso_api_v5_common_models_forms_custom_field_public_model_from_dict = HelloAssoApiV5CommonModelsFormsCustomFieldPublicModel.from_dict(hello_asso_api_v5_common_models_forms_custom_field_public_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


