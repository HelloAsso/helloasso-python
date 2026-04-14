# HelloAssoApiV5CommonModelsFormsFormStatsModel

FormStatsModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_participant** | **int** | The number of participant for this event | [optional] 
**un_grouped_tiers** | [**List[HelloAssoApiV5CommonModelsFormsTierStatsModel]**](HelloAssoApiV5CommonModelsFormsTierStatsModel.md) | The list of ungrouped tiers, sorted as they must be displayed | [optional] 
**additional_options** | [**List[HelloAssoApiV5CommonModelsFormsTierStatsModel]**](HelloAssoApiV5CommonModelsFormsTierStatsModel.md) | The list of additional options, sorted as they must be displayed | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_forms_form_stats_model import HelloAssoApiV5CommonModelsFormsFormStatsModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsFormsFormStatsModel from a JSON string
hello_asso_api_v5_common_models_forms_form_stats_model_instance = HelloAssoApiV5CommonModelsFormsFormStatsModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsFormsFormStatsModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_forms_form_stats_model_dict = hello_asso_api_v5_common_models_forms_form_stats_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsFormsFormStatsModel from a dict
hello_asso_api_v5_common_models_forms_form_stats_model_from_dict = HelloAssoApiV5CommonModelsFormsFormStatsModel.from_dict(hello_asso_api_v5_common_models_forms_form_stats_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


