# HelloAssoApiV5CommonModelsFormsFormActivityModel

Form activity model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Gets the activity identifier | [optional] 
**label** | **str** | Gets the activity label | [optional] 
**short_label** | **str** | Gets the activity short label | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_forms_form_activity_model import HelloAssoApiV5CommonModelsFormsFormActivityModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsFormsFormActivityModel from a JSON string
hello_asso_api_v5_common_models_forms_form_activity_model_instance = HelloAssoApiV5CommonModelsFormsFormActivityModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsFormsFormActivityModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_forms_form_activity_model_dict = hello_asso_api_v5_common_models_forms_form_activity_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsFormsFormActivityModel from a dict
hello_asso_api_v5_common_models_forms_form_activity_model_from_dict = HelloAssoApiV5CommonModelsFormsFormActivityModel.from_dict(hello_asso_api_v5_common_models_forms_form_activity_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


