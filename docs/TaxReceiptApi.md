# helloasso_python.TaxReceiptApi

All URIs are relative to *https://api.helloasso.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_organization_slug_tax_receipt_configuration_get**](TaxReceiptApi.md#organizations_organization_slug_tax_receipt_configuration_get) | **GET** /organizations/{organizationSlug}/tax-receipt/configuration | 
[**organizations_organization_slug_tax_receipt_configuration_put**](TaxReceiptApi.md#organizations_organization_slug_tax_receipt_configuration_put) | **PUT** /organizations/{organizationSlug}/tax-receipt/configuration | 
[**organizations_organization_slug_tax_receipt_preview_post**](TaxReceiptApi.md#organizations_organization_slug_tax_receipt_preview_post) | **POST** /organizations/{organizationSlug}/tax-receipt/preview | 


# **organizations_organization_slug_tax_receipt_configuration_get**
> HelloAssoModelsAccountsOrganizationLegalInformationsOrganizationFiscalReceiptOptionsConfiguration organizations_organization_slug_tax_receipt_configuration_get(organization_slug)



<br/><br/><b>Your token must have one of these roles : </b><br/>OrganizationAdmin<br/><br/>If you are an <b>association</b>, you can obtain these roles with your client.<br/>If you are a <b>partner</b>, you can obtain these roles by the authorize flow.<br/><br/><b>Your clientId must be allowed all of those privileges : </b> <br/> OrganizationAdministration<br/><br/>

### Example


```python
import helloasso_python
from helloasso_python.models.hello_asso_models_accounts_organization_legal_informations_organization_fiscal_receipt_options_configuration import HelloAssoModelsAccountsOrganizationLegalInformationsOrganizationFiscalReceiptOptionsConfiguration
from helloasso_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.helloasso.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = helloasso_python.Configuration(
    host = "https://api.helloasso.com/v5"
)


# Enter a context with an instance of the API client
with helloasso_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = helloasso_python.TaxReceiptApi(api_client)
    organization_slug = 'organization_slug_example' # str | 

    try:
        api_response = api_instance.organizations_organization_slug_tax_receipt_configuration_get(organization_slug)
        print("The response of TaxReceiptApi->organizations_organization_slug_tax_receipt_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxReceiptApi->organizations_organization_slug_tax_receipt_configuration_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**|  | 

### Return type

[**HelloAssoModelsAccountsOrganizationLegalInformationsOrganizationFiscalReceiptOptionsConfiguration**](HelloAssoModelsAccountsOrganizationLegalInformationsOrganizationFiscalReceiptOptionsConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized, you must add a valid JWT into Authorization Header with the format : &#x60;Bearer TOKEN&#x60; |  -  |
**403** | The JWT token hasn&#39;t the privileges or Roles for this action |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_slug_tax_receipt_configuration_put**
> organizations_organization_slug_tax_receipt_configuration_put(organization_slug, file, config=config)



<br/><br/><b>Your token must have one of these roles : </b><br/>OrganizationAdmin<br/><br/>If you are an <b>association</b>, you can obtain these roles with your client.<br/>If you are a <b>partner</b>, you can obtain these roles by the authorize flow.<br/><br/><b>Your clientId must be allowed all of those privileges : </b> <br/> OrganizationAdministration<br/><br/>

### Example


```python
import helloasso_python
from helloasso_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.helloasso.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = helloasso_python.Configuration(
    host = "https://api.helloasso.com/v5"
)


# Enter a context with an instance of the API client
with helloasso_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = helloasso_python.TaxReceiptApi(api_client)
    organization_slug = 'organization_slug_example' # str | 
    file = None # bytearray | Upload File
    config = 'config_example' # str | config (optional)

    try:
        api_instance.organizations_organization_slug_tax_receipt_configuration_put(organization_slug, file, config=config)
    except Exception as e:
        print("Exception when calling TaxReceiptApi->organizations_organization_slug_tax_receipt_configuration_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**|  | 
 **file** | **bytearray**| Upload File | 
 **config** | **str**| config | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized, you must add a valid JWT into Authorization Header with the format : &#x60;Bearer TOKEN&#x60; |  -  |
**403** | The JWT token hasn&#39;t the privileges or Roles for this action |  -  |
**404** | Not Found |  -  |
**415** | Client Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_slug_tax_receipt_preview_post**
> organizations_organization_slug_tax_receipt_preview_post(organization_slug, file, config=config)



<br/><br/><b>Your token must have one of these roles : </b><br/>OrganizationAdmin<br/><br/>If you are an <b>association</b>, you can obtain these roles with your client.<br/>If you are a <b>partner</b>, you can obtain these roles by the authorize flow.<br/><br/><b>Your clientId must be allowed all of those privileges : </b> <br/> OrganizationAdministration<br/><br/>

### Example


```python
import helloasso_python
from helloasso_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.helloasso.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = helloasso_python.Configuration(
    host = "https://api.helloasso.com/v5"
)


# Enter a context with an instance of the API client
with helloasso_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = helloasso_python.TaxReceiptApi(api_client)
    organization_slug = 'organization_slug_example' # str | 
    file = None # bytearray | Upload File
    config = 'config_example' # str | config (optional)

    try:
        api_instance.organizations_organization_slug_tax_receipt_preview_post(organization_slug, file, config=config)
    except Exception as e:
        print("Exception when calling TaxReceiptApi->organizations_organization_slug_tax_receipt_preview_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**|  | 
 **file** | **bytearray**| Upload File | 
 **config** | **str**| config | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized, you must add a valid JWT into Authorization Header with the format : &#x60;Bearer TOKEN&#x60; |  -  |
**403** | The JWT token hasn&#39;t the privileges or Roles for this action |  -  |
**415** | Client Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

