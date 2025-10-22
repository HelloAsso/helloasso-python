# HelloAssoApiV5CommonModelsPaymentRefundOperationModel

RefundOperationModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The refund operation id | [optional] 
**amount** | **int** | The amount to refund | [optional] 
**cancel_order** | **bool** | Whether the future payments and linked items of this order must be canceled (possible only if the payment is fully refunded) | [optional] 
**creation_date** | **datetime** | The refund operation creation date | [optional] 
**state** | [**HelloAssoApiV5CommonModelsEnumsOperationState**](HelloAssoApiV5CommonModelsEnumsOperationState.md) |  | [optional] 
**send_refund_mail** | **bool** | Whether a refund mail must be send or not. | [optional] 
**payment_id** | **int** | The payment id | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_payment_refund_operation_model import HelloAssoApiV5CommonModelsPaymentRefundOperationModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsPaymentRefundOperationModel from a JSON string
hello_asso_api_v5_common_models_payment_refund_operation_model_instance = HelloAssoApiV5CommonModelsPaymentRefundOperationModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsPaymentRefundOperationModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_payment_refund_operation_model_dict = hello_asso_api_v5_common_models_payment_refund_operation_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsPaymentRefundOperationModel from a dict
hello_asso_api_v5_common_models_payment_refund_operation_model_from_dict = HelloAssoApiV5CommonModelsPaymentRefundOperationModel.from_dict(hello_asso_api_v5_common_models_payment_refund_operation_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


