# openapi_client.OrganizationLegalInformationsApi

All URIs are relative to *https://api.helloasso.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_legal_informations_organization_slug_configuration_put**](OrganizationLegalInformationsApi.md#organizations_legal_informations_organization_slug_configuration_put) | **PUT** /organizations/legal-informations/{organizationSlug}/configuration | 


# **organizations_legal_informations_organization_slug_configuration_put**
> organizations_legal_informations_organization_slug_configuration_put(organization_slug, hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body=hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body)



<br/><br/><b>Your token must have one of these roles : </b><br/>OrganizationAdmin<br/><br/>If you are an <b>association</b>, you can obtain these roles with your client.<br/>If you are a <b>partner</b>, you can obtain these roles by the authorize flow.<br/><br/><b>Your clientId must be allowed all of those privileges : </b> <br/> OrganizationAdministration<br/><br/>

### Example


```python
import openapi_client
from openapi_client.models.hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body import HelloAssoApiV5ModelsOrganizationLegalInformationsUpdateOrganizationLegalInformationConfigurationBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.helloasso.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.helloasso.com/v5"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OrganizationLegalInformationsApi(api_client)
    organization_slug = 'organization_slug_example' # str | 
    hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body = openapi_client.HelloAssoApiV5ModelsOrganizationLegalInformationsUpdateOrganizationLegalInformationConfigurationBody() # HelloAssoApiV5ModelsOrganizationLegalInformationsUpdateOrganizationLegalInformationConfigurationBody |  (optional)

    try:
        api_instance.organizations_legal_informations_organization_slug_configuration_put(organization_slug, hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body=hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body)
    except Exception as e:
        print("Exception when calling OrganizationLegalInformationsApi->organizations_legal_informations_organization_slug_configuration_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**|  | 
 **hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body** | [**HelloAssoApiV5ModelsOrganizationLegalInformationsUpdateOrganizationLegalInformationConfigurationBody**](HelloAssoApiV5ModelsOrganizationLegalInformationsUpdateOrganizationLegalInformationConfigurationBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized, you must add a valid JWT into Authorization Header with the format : &#x60;Bearer TOKEN&#x60; |  -  |
**403** | The JWT token hasn&#39;t the privileges or Roles for this action |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

