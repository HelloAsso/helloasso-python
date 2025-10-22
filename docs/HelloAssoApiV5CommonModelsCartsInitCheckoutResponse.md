# HelloAssoApiV5CommonModelsCartsInitCheckoutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the checkout intent | [optional] 
**redirect_url** | **str** | Url where the contributor must be redirected to | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_carts_init_checkout_response import HelloAssoApiV5CommonModelsCartsInitCheckoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsCartsInitCheckoutResponse from a JSON string
hello_asso_api_v5_common_models_carts_init_checkout_response_instance = HelloAssoApiV5CommonModelsCartsInitCheckoutResponse.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsCartsInitCheckoutResponse.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_carts_init_checkout_response_dict = hello_asso_api_v5_common_models_carts_init_checkout_response_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsCartsInitCheckoutResponse from a dict
hello_asso_api_v5_common_models_carts_init_checkout_response_from_dict = HelloAssoApiV5CommonModelsCartsInitCheckoutResponse.from_dict(hello_asso_api_v5_common_models_carts_init_checkout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


