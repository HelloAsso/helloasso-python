# HelloAssoApiV5CommonModelsPaymentCashoutExportCashoutExportRowModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_type** | [**HelloAssoApiV5CommonModelsEnumsFormType**](HelloAssoApiV5CommonModelsEnumsFormType.md) |  | [optional] 
**campaign_name** | **str** |  | [optional] 
**operation_type** | [**HelloAssoApiV5CommonModelsPaymentCashoutExportCashoutExportPaymentOperation**](HelloAssoApiV5CommonModelsPaymentCashoutExportCashoutExportPaymentOperation.md) |  | [optional] 
**credit** | **float** |  | [optional] 
**debit** | **float** |  | [optional] 
**order_id** | **int** |  | [optional] 
**payment_id** | **int** |  | [optional] 
**payment_date** | **datetime** |  | [optional] 
**payment_method** | [**HelloAssoApiV5CommonModelsEnumsPaymentMeans**](HelloAssoApiV5CommonModelsEnumsPaymentMeans.md) |  | [optional] 
**payment_status** | [**HelloAssoApiV5CommonModelsPaymentCashoutExportCashoutExportPaymentStatus**](HelloAssoApiV5CommonModelsPaymentCashoutExportCashoutExportPaymentStatus.md) |  | [optional] 
**cash_out_date** | **datetime** |  | [optional] 
**cash_out_id** | **int** |  | [optional] 
**designation** | **str** |  | [optional] 
**payer_company** | **str** |  | [optional] 
**payer_last_name** | **str** |  | [optional] 
**payer_first_name** | **str** |  | [optional] 
**payer_email** | **str** |  | [optional] 
**payer_siren** | **str** |  | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_payment_cashout_export_cashout_export_row_model import HelloAssoApiV5CommonModelsPaymentCashoutExportCashoutExportRowModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsPaymentCashoutExportCashoutExportRowModel from a JSON string
hello_asso_api_v5_common_models_payment_cashout_export_cashout_export_row_model_instance = HelloAssoApiV5CommonModelsPaymentCashoutExportCashoutExportRowModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsPaymentCashoutExportCashoutExportRowModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_payment_cashout_export_cashout_export_row_model_dict = hello_asso_api_v5_common_models_payment_cashout_export_cashout_export_row_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsPaymentCashoutExportCashoutExportRowModel from a dict
hello_asso_api_v5_common_models_payment_cashout_export_cashout_export_row_model_from_dict = HelloAssoApiV5CommonModelsPaymentCashoutExportCashoutExportRowModel.from_dict(hello_asso_api_v5_common_models_payment_cashout_export_cashout_export_row_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


