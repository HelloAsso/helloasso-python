# HelloAssoApiV5CommonModelsStatisticsPaymentDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_expiration_date** | **datetime** | Card expiration date (only for card payments) | [optional] 
**order** | [**HelloAssoApiV5CommonModelsStatisticsOrderLight**](HelloAssoApiV5CommonModelsStatisticsOrderLight.md) |  | [optional] 
**payer** | [**HelloAssoApiV5CommonModelsStatisticsPayer**](HelloAssoApiV5CommonModelsStatisticsPayer.md) |  | [optional] 
**items** | [**List[HelloAssoApiV5CommonModelsStatisticsPaymentItem]**](HelloAssoApiV5CommonModelsStatisticsPaymentItem.md) | Items linked to this payment | [optional] 
**cash_out_date** | **datetime** | The date of the cash out | [optional] 
**id_cash_out** | **int** | The id of the cash out | [optional] 
**cash_out_state** | [**HelloAssoApiV5CommonModelsEnumsPaymentCashOutState**](HelloAssoApiV5CommonModelsEnumsPaymentCashOutState.md) |  | [optional] 
**payment_receipt_url** | **str** | The Payment Receipt Url | [optional] 
**fiscal_receipt_url** | **str** | The Fiscal Receipt Url | [optional] 
**id** | **int** | The ID of the payment | [optional] 
**amount** | **int** | Total Amount of the payment (in cents) | [optional] 
**amount_tip** | **int** | Tip Amount of the payment (in cents) | [optional] 
**var_date** | **datetime** | Date of the payment | [optional] 
**payment_means** | [**HelloAssoApiV5CommonModelsEnumsPaymentMeans**](HelloAssoApiV5CommonModelsEnumsPaymentMeans.md) |  | [optional] 
**installment_number** | **int** | Indicates the payment number (useful in the case of an order comprising payments with installments) | [optional] 
**state** | [**HelloAssoApiV5CommonModelsEnumsPaymentState**](HelloAssoApiV5CommonModelsEnumsPaymentState.md) |  | [optional] 
**type** | [**HelloAssoApiV5CommonModelsEnumsPaymentType**](HelloAssoApiV5CommonModelsEnumsPaymentType.md) |  | [optional] 
**meta** | [**HelloAssoApiV5CommonModelsCommonMetaModel**](HelloAssoApiV5CommonModelsCommonMetaModel.md) |  | [optional] 
**payment_off_line_mean** | [**HelloAssoApiV5CommonModelsEnumsPaymentMeans**](HelloAssoApiV5CommonModelsEnumsPaymentMeans.md) |  | [optional] 
**refund_operations** | [**List[HelloAssoApiV5CommonModelsStatisticsRefundOperationLightModel]**](HelloAssoApiV5CommonModelsStatisticsRefundOperationLightModel.md) | The refund operations information for the specific payment. | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_statistics_payment_detail import HelloAssoApiV5CommonModelsStatisticsPaymentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsStatisticsPaymentDetail from a JSON string
hello_asso_api_v5_common_models_statistics_payment_detail_instance = HelloAssoApiV5CommonModelsStatisticsPaymentDetail.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsStatisticsPaymentDetail.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_statistics_payment_detail_dict = hello_asso_api_v5_common_models_statistics_payment_detail_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsStatisticsPaymentDetail from a dict
hello_asso_api_v5_common_models_statistics_payment_detail_from_dict = HelloAssoApiV5CommonModelsStatisticsPaymentDetail.from_dict(hello_asso_api_v5_common_models_statistics_payment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


