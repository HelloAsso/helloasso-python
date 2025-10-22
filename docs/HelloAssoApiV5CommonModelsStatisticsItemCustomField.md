# HelloAssoApiV5CommonModelsStatisticsItemCustomField

Custom field associated with the item or option

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**HelloAssoApiV5CommonModelsEnumsFieldType**](HelloAssoApiV5CommonModelsEnumsFieldType.md) |  | [optional] 
**answer** | **str** | Participant or user answer | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_statistics_item_custom_field import HelloAssoApiV5CommonModelsStatisticsItemCustomField

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsStatisticsItemCustomField from a JSON string
hello_asso_api_v5_common_models_statistics_item_custom_field_instance = HelloAssoApiV5CommonModelsStatisticsItemCustomField.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsStatisticsItemCustomField.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_statistics_item_custom_field_dict = hello_asso_api_v5_common_models_statistics_item_custom_field_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsStatisticsItemCustomField from a dict
hello_asso_api_v5_common_models_statistics_item_custom_field_from_dict = HelloAssoApiV5CommonModelsStatisticsItemCustomField.from_dict(hello_asso_api_v5_common_models_statistics_item_custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


