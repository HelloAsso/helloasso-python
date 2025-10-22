# HelloAssoApiV5CommonModelsFormsTierPublicModel

TierPublicModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | [**List[HelloAssoApiV5CommonModelsFormsCustomFieldPublicModel]**](HelloAssoApiV5CommonModelsFormsCustomFieldPublicModel.md) | List of custom fields to be filled by the user | [optional] 
**extra_options** | [**List[HelloAssoApiV5CommonModelsFormsExtraOptionPublicModel]**](HelloAssoApiV5CommonModelsFormsExtraOptionPublicModel.md) | List of available extra options to buy along the tier | [optional] 
**id** | **int** | id | [optional] 
**label** | **str** | label | [optional] 
**description** | **str** | description | [optional] 
**tier_type** | [**HelloAssoApiV5CommonModelsEnumsTierType**](HelloAssoApiV5CommonModelsEnumsTierType.md) |  | [optional] 
**price** | **int** | the Price in cents  if price equals 0 then it is free or there is a MinAmount | [optional] 
**vat_rate** | **float** | Vat rate if applicable  Amount have to be 0.10 for 10% | [optional] 
**min_amount** | **int** | If set, it means the payment is free to choose, according to the specified minAmount in cents | [optional] 
**payment_frequency** | [**HelloAssoApiV5CommonModelsEnumsPaymentFrequencyType**](HelloAssoApiV5CommonModelsEnumsPaymentFrequencyType.md) |  | [optional] 
**max_per_user** | **int** | Max quantity buyable in this cart | [optional] 
**meta** | [**HelloAssoApiV5CommonModelsCommonMetaModel**](HelloAssoApiV5CommonModelsCommonMetaModel.md) |  | [optional] 
**sale_start_date** | **datetime** | The datetime (Inclusive) at which the users can start buying this tier.  If null the tier will be available at the start of the event. | [optional] 
**sale_end_date** | **datetime** | The datetime (Inclusive) at which the tier is no longer available.  If null the tier will be available until the end of the event. | [optional] 
**is_eligible_tax_receipt** | **bool** | Whether this is eligible to a deduction | [optional] 
**terms** | [**List[HelloAssoApiV5CommonModelsFormsTermModel]**](HelloAssoApiV5CommonModelsFormsTermModel.md) | Terms of tier | [optional] 
**picture** | [**HelloAssoApiV5CommonModelsCommonDocumentModel**](HelloAssoApiV5CommonModelsCommonDocumentModel.md) |  | [optional] 
**is_excluded_from_form_payment_terms** | **bool** | True means this tier must be paid in the initial payment, false means it can be paid in payment with installments  Null when the form payment terms are disabled or not compatible with the related form | [optional] 
**is_favorite** | **bool** | Indicates whether this tier is marked as a favorite.  Used only in Donation form type. | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_forms_tier_public_model import HelloAssoApiV5CommonModelsFormsTierPublicModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsFormsTierPublicModel from a JSON string
hello_asso_api_v5_common_models_forms_tier_public_model_instance = HelloAssoApiV5CommonModelsFormsTierPublicModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsFormsTierPublicModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_forms_tier_public_model_dict = hello_asso_api_v5_common_models_forms_tier_public_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsFormsTierPublicModel from a dict
hello_asso_api_v5_common_models_forms_tier_public_model_from_dict = HelloAssoApiV5CommonModelsFormsTierPublicModel.from_dict(hello_asso_api_v5_common_models_forms_tier_public_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


