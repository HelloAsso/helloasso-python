# HelloAssoModelsAccountsOrganizationLegalInformationsOrganizationFiscalReceiptOptionsConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | **str** |  | [optional] 
**cerfa_type_id** | **int** |  | [optional] 
**jo_category_id** | **int** |  | [optional] 
**format_option_model** | [**HelloAssoModelsAccountsOrganizationLegalInformationsFiscalReceiptFormatOptionModel**](HelloAssoModelsAccountsOrganizationLegalInformationsFiscalReceiptFormatOptionModel.md) |  | [optional] 
**signatory_model** | [**HelloAssoModelsAccountsOrganizationLegalInformationsFiscalReceiptSignatoryModel**](HelloAssoModelsAccountsOrganizationLegalInformationsFiscalReceiptSignatoryModel.md) |  | [optional] 
**address_model** | [**HelloAssoModelsComplianceV2CommonAddressAddressModelSnapshot**](HelloAssoModelsComplianceV2CommonAddressAddressModelSnapshot.md) |  | [optional] 

## Example

```python
from openapi_client.models.hello_asso_models_accounts_organization_legal_informations_organization_fiscal_receipt_options_configuration import HelloAssoModelsAccountsOrganizationLegalInformationsOrganizationFiscalReceiptOptionsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoModelsAccountsOrganizationLegalInformationsOrganizationFiscalReceiptOptionsConfiguration from a JSON string
hello_asso_models_accounts_organization_legal_informations_organization_fiscal_receipt_options_configuration_instance = HelloAssoModelsAccountsOrganizationLegalInformationsOrganizationFiscalReceiptOptionsConfiguration.from_json(json)
# print the JSON string representation of the object
print(HelloAssoModelsAccountsOrganizationLegalInformationsOrganizationFiscalReceiptOptionsConfiguration.to_json())

# convert the object into a dict
hello_asso_models_accounts_organization_legal_informations_organization_fiscal_receipt_options_configuration_dict = hello_asso_models_accounts_organization_legal_informations_organization_fiscal_receipt_options_configuration_instance.to_dict()
# create an instance of HelloAssoModelsAccountsOrganizationLegalInformationsOrganizationFiscalReceiptOptionsConfiguration from a dict
hello_asso_models_accounts_organization_legal_informations_organization_fiscal_receipt_options_configuration_from_dict = HelloAssoModelsAccountsOrganizationLegalInformationsOrganizationFiscalReceiptOptionsConfiguration.from_dict(hello_asso_models_accounts_organization_legal_informations_organization_fiscal_receipt_options_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


