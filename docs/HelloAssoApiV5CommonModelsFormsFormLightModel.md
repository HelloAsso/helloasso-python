# HelloAssoApiV5CommonModelsFormsFormLightModel

FormLightModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner** | [**HelloAssoApiV5CommonModelsCommonDocumentModel**](HelloAssoApiV5CommonModelsCommonDocumentModel.md) |  | [optional] 
**currency** | **str** | Currency | [optional] 
**description** | **str** | Short description (one line) | [optional] 
**start_date** | **datetime** | The datetime of the activity start | [optional] 
**end_date** | **datetime** | The datetime of the activity end | [optional] 
**logo** | [**HelloAssoApiV5CommonModelsCommonDocumentModel**](HelloAssoApiV5CommonModelsCommonDocumentModel.md) |  | [optional] 
**meta** | [**HelloAssoApiV5CommonModelsCommonMetaModel**](HelloAssoApiV5CommonModelsCommonMetaModel.md) |  | [optional] 
**state** | [**HelloAssoApiV5CommonModelsEnumsFormState**](HelloAssoApiV5CommonModelsEnumsFormState.md) |  | [optional] 
**title** | **str** | Title | [optional] 
**private_title** | **str** | Private Title | [optional] 
**widget_button_url** | **str** | Url of the widget button | [optional] 
**widget_full_url** | **str** | Url of the form widget | [optional] 
**widget_vignette_horizontal_url** | **str** | Url of the horizontal vignette widget | [optional] 
**widget_vignette_vertical_url** | **str** | Url of the vertical vignette widget | [optional] 
**widget_counter_url** | **str** | Url of the counter widget | [optional] 
**form_slug** | **str** | The form slug | [optional] 
**form_type** | [**HelloAssoApiV5CommonModelsEnumsFormType**](HelloAssoApiV5CommonModelsEnumsFormType.md) |  | [optional] 
**url** | **str** | The form url | [optional] 
**organization_slug** | **str** | The organization slug | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_forms_form_light_model import HelloAssoApiV5CommonModelsFormsFormLightModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsFormsFormLightModel from a JSON string
hello_asso_api_v5_common_models_forms_form_light_model_instance = HelloAssoApiV5CommonModelsFormsFormLightModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsFormsFormLightModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_forms_form_light_model_dict = hello_asso_api_v5_common_models_forms_form_light_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsFormsFormLightModel from a dict
hello_asso_api_v5_common_models_forms_form_light_model_from_dict = HelloAssoApiV5CommonModelsFormsFormLightModel.from_dict(hello_asso_api_v5_common_models_forms_form_light_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


