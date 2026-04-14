# HelloAssoApiV5CommonModelsFormsTierStatsModel

TierStatsModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | [optional] 
**label** | **str** | label | [optional] 
**description** | **str** | description | [optional] 
**entries_taken** | **int** | The number of times this tier as been taken | [optional] 
**max_entries** | **int** | The max number of times this tier can be sold | [optional] 
**price** | **int** | the Price in cents  if price equals 0 then it is free or there is a MinAmount | [optional] 
**min_amount** | **int** | If set, it means the payment is free to choose, according to the specified minAmount in cents | [optional] 
**price_category** | [**HelloAssoApiV5CommonModelsEnumsPriceCategory**](HelloAssoApiV5CommonModelsEnumsPriceCategory.md) |  | [optional] 
**tier_type** | [**HelloAssoApiV5CommonModelsEnumsTierType**](HelloAssoApiV5CommonModelsEnumsTierType.md) |  | [optional] 
**is_enabled** | **bool** | is true if tier state is ENABLED  is false if tier state is DISABLED | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_forms_tier_stats_model import HelloAssoApiV5CommonModelsFormsTierStatsModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsFormsTierStatsModel from a JSON string
hello_asso_api_v5_common_models_forms_tier_stats_model_instance = HelloAssoApiV5CommonModelsFormsTierStatsModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsFormsTierStatsModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_forms_tier_stats_model_dict = hello_asso_api_v5_common_models_forms_tier_stats_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsFormsTierStatsModel from a dict
hello_asso_api_v5_common_models_forms_tier_stats_model_from_dict = HelloAssoApiV5CommonModelsFormsTierStatsModel.from_dict(hello_asso_api_v5_common_models_forms_tier_stats_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


