# HelloAssoApiV5CommonModelsStatisticsOrderAmountModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total amount in cents | [optional] 
**vat** | **int** | Vat amount in cents | [optional] 
**discount** | **int** | Discount amount in cents | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_statistics_order_amount_model import HelloAssoApiV5CommonModelsStatisticsOrderAmountModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsStatisticsOrderAmountModel from a JSON string
hello_asso_api_v5_common_models_statistics_order_amount_model_instance = HelloAssoApiV5CommonModelsStatisticsOrderAmountModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsStatisticsOrderAmountModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_statistics_order_amount_model_dict = hello_asso_api_v5_common_models_statistics_order_amount_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsStatisticsOrderAmountModel from a dict
hello_asso_api_v5_common_models_statistics_order_amount_model_from_dict = HelloAssoApiV5CommonModelsStatisticsOrderAmountModel.from_dict(hello_asso_api_v5_common_models_statistics_order_amount_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


