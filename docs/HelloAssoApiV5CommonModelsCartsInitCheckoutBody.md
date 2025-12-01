# HelloAssoApiV5CommonModelsCartsInitCheckoutBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount** | **int** | Total amount, all taxes included, in cents (required)  Must be equal to the sum of the initial amount and subsequent terms | 
**initial_amount** | **int** | The amount for the first term, all taxes included, in cents (required) | 
**item_name** | **str** | Item name (required)  A text describing what the user paid for (&#39;Renew license&#39;, &#39;3 tickets&#39;, donation, etc).  Will be displayed in the near future in the user space and in the organization back office | 
**back_url** | **str** | Url followed by the contributor if he wants to return to its previous site | 
**error_url** | **str** | Url called in case of an error during the checkout process | 
**return_url** | **str** | Url called after the payment | 
**contains_donation** | **bool** | The sale (or a part of) is a donation | 
**terms** | [**List[HelloAssoApiV5CommonModelsCartsCheckoutTerm]**](HelloAssoApiV5CommonModelsCartsCheckoutTerm.md) | The list of future terms (if applicable) | [optional] 
**payer** | [**HelloAssoApiV5CommonModelsCartsCheckoutPayer**](HelloAssoApiV5CommonModelsCartsCheckoutPayer.md) |  | [optional] 
**metadata** | **object** | Metadata (optional)  Json object (max length : 20000) | [optional] 
**payment_options** | [**HelloAssoApiV5CommonModelsCartsCheckoutPaymentOptions**](HelloAssoApiV5CommonModelsCartsCheckoutPaymentOptions.md) |  | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_carts_init_checkout_body import HelloAssoApiV5CommonModelsCartsInitCheckoutBody

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsCartsInitCheckoutBody from a JSON string
hello_asso_api_v5_common_models_carts_init_checkout_body_instance = HelloAssoApiV5CommonModelsCartsInitCheckoutBody.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsCartsInitCheckoutBody.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_carts_init_checkout_body_dict = hello_asso_api_v5_common_models_carts_init_checkout_body_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsCartsInitCheckoutBody from a dict
hello_asso_api_v5_common_models_carts_init_checkout_body_from_dict = HelloAssoApiV5CommonModelsCartsInitCheckoutBody.from_dict(hello_asso_api_v5_common_models_carts_init_checkout_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


