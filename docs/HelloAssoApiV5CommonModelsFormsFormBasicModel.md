# HelloAssoApiV5CommonModelsFormsFormBasicModel

A basic form model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_slug** | **str** | The form slug | [optional] 
**form_type** | [**HelloAssoApiV5CommonModelsEnumsFormType**](HelloAssoApiV5CommonModelsEnumsFormType.md) |  | [optional] 
**url** | **str** | The form url | [optional] 
**organization_slug** | **str** | The organization slug | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_forms_form_basic_model import HelloAssoApiV5CommonModelsFormsFormBasicModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsFormsFormBasicModel from a JSON string
hello_asso_api_v5_common_models_forms_form_basic_model_instance = HelloAssoApiV5CommonModelsFormsFormBasicModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsFormsFormBasicModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_forms_form_basic_model_dict = hello_asso_api_v5_common_models_forms_form_basic_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsFormsFormBasicModel from a dict
hello_asso_api_v5_common_models_forms_form_basic_model_from_dict = HelloAssoApiV5CommonModelsFormsFormBasicModel.from_dict(hello_asso_api_v5_common_models_forms_form_basic_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


