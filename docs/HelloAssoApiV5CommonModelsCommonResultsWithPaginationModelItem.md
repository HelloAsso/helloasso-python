# HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelItem

ResultsWithPaginationModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HelloAssoApiV5CommonModelsStatisticsItem]**](HelloAssoApiV5CommonModelsStatisticsItem.md) | Data property | [optional] 
**pagination** | [**HelloAssoApiV5CommonModelsCommonPaginationModel**](HelloAssoApiV5CommonModelsCommonPaginationModel.md) |  | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_common_results_with_pagination_model_item import HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelItem

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelItem from a JSON string
hello_asso_api_v5_common_models_common_results_with_pagination_model_item_instance = HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelItem.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelItem.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_common_results_with_pagination_model_item_dict = hello_asso_api_v5_common_models_common_results_with_pagination_model_item_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelItem from a dict
hello_asso_api_v5_common_models_common_results_with_pagination_model_item_from_dict = HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelItem.from_dict(hello_asso_api_v5_common_models_common_results_with_pagination_model_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


