# helloasso-python.OrganizationApi

All URIs are relative to *https://api.helloasso.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_legal_informations_organization_slug_configuration_put**](OrganizationApi.md#organizations_legal_informations_organization_slug_configuration_put) | **PUT** /organizations/legal-informations/{organizationSlug}/configuration | Mettre à jour la configuration des informations juridiques de l&#39;organisation.


# **organizations_legal_informations_organization_slug_configuration_put**
> organizations_legal_informations_organization_slug_configuration_put(organization_slug, hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body=hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body)

Mettre à jour la configuration des informations juridiques de l'organisation.

<br/><br/><b>Votre token doit avoir l'un de ces rôles : </b><br/>OrganizationAdmin<br/><br/>Si vous êtes une <b>association</b>, vous pouvez obtenir ces rôles avec votre client.<br/>Si vous êtes un <b>partenaire</b>, vous pouvez obtenir ces rôles par le flux d'autorisation.<br/><br/><b>Votre clientId doit être autorisé à tous ces privilèges : </b> <br/> OrganizationAdministration<br/><br/>

### Example

* OAuth Authentication (OAuth2):

```python
import helloasso-python
from helloasso-python.models.hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body import HelloAssoApiV5ModelsOrganizationLegalInformationsUpdateOrganizationLegalInformationConfigurationBody
from helloasso-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.helloasso.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = helloasso-python.Configuration(
    host = "https://api.helloasso.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with helloasso-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = helloasso-python.OrganizationApi(api_client)
    organization_slug = 'organization_slug_example' # str | 
    hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body = helloasso-python.HelloAssoApiV5ModelsOrganizationLegalInformationsUpdateOrganizationLegalInformationConfigurationBody() # HelloAssoApiV5ModelsOrganizationLegalInformationsUpdateOrganizationLegalInformationConfigurationBody |  (optional)

    try:
        # Mettre à jour la configuration des informations juridiques de l'organisation.
        api_instance.organizations_legal_informations_organization_slug_configuration_put(organization_slug, hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body=hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body)
    except Exception as e:
        print("Exception when calling OrganizationApi->organizations_legal_informations_organization_slug_configuration_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**|  | 
 **hello_asso_api_v5_models_organization_legal_informations_update_organization_legal_information_configuration_body** | [**HelloAssoApiV5ModelsOrganizationLegalInformationsUpdateOrganizationLegalInformationConfigurationBody**](HelloAssoApiV5ModelsOrganizationLegalInformationsUpdateOrganizationLegalInformationConfigurationBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

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

