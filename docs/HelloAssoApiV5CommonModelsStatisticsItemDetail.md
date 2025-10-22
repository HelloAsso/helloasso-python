# HelloAssoApiV5CommonModelsStatisticsItemDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**HelloAssoApiV5CommonModelsStatisticsOrderLight**](HelloAssoApiV5CommonModelsStatisticsOrderLight.md) |  | [optional] 
**payer** | [**HelloAssoApiV5CommonModelsStatisticsPayer**](HelloAssoApiV5CommonModelsStatisticsPayer.md) |  | [optional] 
**payments** | [**List[HelloAssoApiV5CommonModelsStatisticsItemPayment]**](HelloAssoApiV5CommonModelsStatisticsItemPayment.md) | Payments linked to this item | [optional] 
**name** | **str** |  | [optional] 
**user** | [**HelloAssoApiV5CommonModelsStatisticsUser**](HelloAssoApiV5CommonModelsStatisticsUser.md) |  | [optional] 
**price_category** | [**HelloAssoApiV5CommonModelsEnumsPriceCategory**](HelloAssoApiV5CommonModelsEnumsPriceCategory.md) |  | [optional] 
**min_amount** | **int** | Minimum amount that was specified on the tier (in cents) | [optional] 
**discount** | [**HelloAssoApiV5CommonModelsStatisticsItemDiscount**](HelloAssoApiV5CommonModelsStatisticsItemDiscount.md) |  | [optional] 
**custom_fields** | [**List[HelloAssoApiV5CommonModelsStatisticsItemCustomField]**](HelloAssoApiV5CommonModelsStatisticsItemCustomField.md) | Custom fields related to this item | [optional] 
**options** | [**List[HelloAssoApiV5CommonModelsStatisticsItemOption]**](HelloAssoApiV5CommonModelsStatisticsItemOption.md) | Extra options taken with this item | [optional] 
**ticket_url** | **str** | The Ticket Url | [optional] 
**qr_code** | **str** | The item QrCode (for ticket scanning only) | [optional] 
**membership_card_url** | **str** | The Membership Card Url | [optional] 
**day_of_levy** | **int** | The day of levy for monthly donation only | [optional] 
**tier_description** | **str** | Tier description | [optional] 
**tier_id** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**id** | **int** | ID of the Item | [optional] 
**amount** | **int** | Total item Price in cents (after discount without extra options) | [optional] 
**type** | [**HelloAssoApiV5CommonModelsEnumsTierType**](HelloAssoApiV5CommonModelsEnumsTierType.md) |  | [optional] 
**initial_amount** | **int** | The raw amount (without reduction) | [optional] 
**state** | [**HelloAssoApiV5CommonModelsEnumsItemState**](HelloAssoApiV5CommonModelsEnumsItemState.md) |  | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_statistics_item_detail import HelloAssoApiV5CommonModelsStatisticsItemDetail

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsStatisticsItemDetail from a JSON string
hello_asso_api_v5_common_models_statistics_item_detail_instance = HelloAssoApiV5CommonModelsStatisticsItemDetail.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsStatisticsItemDetail.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_statistics_item_detail_dict = hello_asso_api_v5_common_models_statistics_item_detail_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsStatisticsItemDetail from a dict
hello_asso_api_v5_common_models_statistics_item_detail_from_dict = HelloAssoApiV5CommonModelsStatisticsItemDetail.from_dict(hello_asso_api_v5_common_models_statistics_item_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


