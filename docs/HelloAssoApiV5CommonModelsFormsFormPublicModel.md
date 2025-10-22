# HelloAssoApiV5CommonModelsFormsFormPublicModel

FormPublicModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_logo** | **str** | Organization Logo | [optional] 
**organization_name** | **str** | Organization Name | [optional] 
**tiers** | [**List[HelloAssoApiV5CommonModelsFormsTierPublicModel]**](HelloAssoApiV5CommonModelsFormsTierPublicModel.md) | Tiers | [optional] 
**activity_type** | **str** | Activity type of the event eg. \&quot;Atelier(s) / Stage(s)\&quot; matching one of the provided type values &lt;a href&#x3D;\&quot;index#!/Values/Values_Get\&quot;&gt; provided here&lt;/a&gt; or a custom value is allowed. | [optional] 
**activity_type_id** | **int** | Activity type identifier | [optional] 
**place** | [**HelloAssoApiV5CommonModelsCommonPlaceModel**](HelloAssoApiV5CommonModelsCommonPlaceModel.md) |  | [optional] 
**sale_end_date** | **datetime** | The datetime (Inclusive) at which the sales end.  If null the orders will be available until the end of the campaign. | [optional] 
**sale_start_date** | **datetime** | The datetime (Inclusive) at which the users can start placing orders.  If null the orders will be available as soon as the campaign is published. | [optional] 
**validity_type** | [**HelloAssoApiV5CommonModelsEnumsMembershipValidityType**](HelloAssoApiV5CommonModelsEnumsMembershipValidityType.md) |  | [optional] 
**personalized_message** | **str** | A message customized by the organization administrator. | [optional] 
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
from helloasso_python.models.hello_asso_api_v5_common_models_forms_form_public_model import HelloAssoApiV5CommonModelsFormsFormPublicModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsFormsFormPublicModel from a JSON string
hello_asso_api_v5_common_models_forms_form_public_model_instance = HelloAssoApiV5CommonModelsFormsFormPublicModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsFormsFormPublicModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_forms_form_public_model_dict = hello_asso_api_v5_common_models_forms_form_public_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsFormsFormPublicModel from a dict
hello_asso_api_v5_common_models_forms_form_public_model_from_dict = HelloAssoApiV5CommonModelsFormsFormPublicModel.from_dict(hello_asso_api_v5_common_models_forms_form_public_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


