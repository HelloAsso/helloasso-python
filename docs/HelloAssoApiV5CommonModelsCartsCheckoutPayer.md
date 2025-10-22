# HelloAssoApiV5CommonModelsCartsCheckoutPayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | FirstName | [optional] 
**last_name** | **str** | LastName | [optional] 
**email** | **str** | Email | [optional] 
**date_of_birth** | **datetime** | Date of birth (Date only, no time part) | [optional] 
**address** | **str** | Address | [optional] 
**city** | **str** | City | [optional] 
**zip_code** | **str** | ZipCode | [optional] 
**country** | **str** | 3 letter country code | [optional] 
**company_name** | **str** | Used if the payer is a company | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_carts_checkout_payer import HelloAssoApiV5CommonModelsCartsCheckoutPayer

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsCartsCheckoutPayer from a JSON string
hello_asso_api_v5_common_models_carts_checkout_payer_instance = HelloAssoApiV5CommonModelsCartsCheckoutPayer.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsCartsCheckoutPayer.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_carts_checkout_payer_dict = hello_asso_api_v5_common_models_carts_checkout_payer_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsCartsCheckoutPayer from a dict
hello_asso_api_v5_common_models_carts_checkout_payer_from_dict = HelloAssoApiV5CommonModelsCartsCheckoutPayer.from_dict(hello_asso_api_v5_common_models_carts_checkout_payer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


