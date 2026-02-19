# HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment

ResultsWithPaginationModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HelloAssoApiV5CommonModelsStatisticsPayment]**](HelloAssoApiV5CommonModelsStatisticsPayment.md) | Data property | [optional] 
**pagination** | [**HelloAssoApiV5CommonModelsCommonPaginationModel**](HelloAssoApiV5CommonModelsCommonPaginationModel.md) |  | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_common_results_with_pagination_model_payment import HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment from a JSON string
hello_asso_api_v5_common_models_common_results_with_pagination_model_payment_instance = HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_common_results_with_pagination_model_payment_dict = hello_asso_api_v5_common_models_common_results_with_pagination_model_payment_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment from a dict
hello_asso_api_v5_common_models_common_results_with_pagination_model_payment_from_dict = HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment.from_dict(hello_asso_api_v5_common_models_common_results_with_pagination_model_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


