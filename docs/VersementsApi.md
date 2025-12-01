# helloasso_python.VersementsApi

All URIs are relative to *https://api.helloasso.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_organization_slug_cash_out_cash_out_id_export_get**](VersementsApi.md#organizations_organization_slug_cash_out_cash_out_id_export_get) | **GET** /organizations/{organizationSlug}/cash-out/{cashOutId}/export | Détails d&#39;un versement


# **organizations_organization_slug_cash_out_cash_out_id_export_get**
> organizations_organization_slug_cash_out_cash_out_id_export_get(organization_slug, cash_out_id)

Détails d'un versement

<br/><br/><b>Votre token doit avoir l''un de ces rôles : </b><br/>OrganizationAdmin<br/><br/>Si vous êtes une <b>association</b>, vous pouvez obtenir ces rôles avec votre client.<br/>Si vous êtes un <b>partenaire</b>, vous pouvez obtenir ces rôles par le flux d''autorisation.<br/><br/><b>Votre clientId doit être autorisé à tous ces privilèges : </b> <br/> AccessTransactions<br/><br/>

### Example

* OAuth Authentication (OAuth2):

```python
import helloasso_python
from helloasso_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.helloasso.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = helloasso_python.Configuration(
    host = "https://api.helloasso.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with helloasso_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = helloasso_python.VersementsApi(api_client)
    organization_slug = 'organization_slug_example' # str | The organization slug
    cash_out_id = 56 # int | The cash-out id to details

    try:
        # Détails d'un versement
        api_instance.organizations_organization_slug_cash_out_cash_out_id_export_get(organization_slug, cash_out_id)
    except Exception as e:
        print("Exception when calling VersementsApi->organizations_organization_slug_cash_out_cash_out_id_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**| The organization slug | 
 **cash_out_id** | **int**| The cash-out id to details | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get cash-out details |  -  |
**401** | Unauthorized, you must add a valid JWT into Authorization Header with the format : &#x60;Bearer TOKEN&#x60; |  -  |
**403** | The JWT token hasn&#39;t the privileges or Roles for this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

