# helloasso_python.FormsApi

All URIs are relative to *https://api.helloasso.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_organization_slug_forms_form_type_form_slug_state_put**](FormsApi.md#organizations_organization_slug_forms_form_type_form_slug_state_put) | **PUT** /organizations/{organizationSlug}/forms/{formType}/{formSlug}/state | Update a form state
[**organizations_organization_slug_forms_form_type_form_slug_stats_get**](FormsApi.md#organizations_organization_slug_forms_form_type_form_slug_stats_get) | **GET** /organizations/{organizationSlug}/forms/{formType}/{formSlug}/stats | Get Stats for the form


# **organizations_organization_slug_forms_form_type_form_slug_state_put**
> organizations_organization_slug_forms_form_type_form_slug_state_put(organization_slug, form_slug, form_type, hello_asso_api_v5_common_models_forms_form_state_request=hello_asso_api_v5_common_models_forms_form_state_request)

Update a form state

Update form state.<br/><br/><b>Your token must have one of these roles : </b><br/>FormAdmin<br/>OrganizationAdmin<br/><br/>If you are an <b>association</b>, you can obtain these roles with your client.<br/>If you are a <b>partner</b>, you can obtain these roles by the authorize flow.<br/><br/><b>Your clientId must be allowed all of those privileges : </b> <br/> FormAdministration<br/><br/>

### Example


```python
import helloasso_python
from helloasso_python.models.hello_asso_api_v5_common_models_enums_form_type import HelloAssoApiV5CommonModelsEnumsFormType
from helloasso_python.models.hello_asso_api_v5_common_models_forms_form_state_request import HelloAssoApiV5CommonModelsFormsFormStateRequest
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
    api_instance = helloasso_python.FormsApi(api_client)
    organization_slug = 'organization_slug_example' # str | 
    form_slug = 'form_slug_example' # str | 
    form_type = helloasso_python.HelloAssoApiV5CommonModelsEnumsFormType() # HelloAssoApiV5CommonModelsEnumsFormType | 
    hello_asso_api_v5_common_models_forms_form_state_request = helloasso_python.HelloAssoApiV5CommonModelsFormsFormStateRequest() # HelloAssoApiV5CommonModelsFormsFormStateRequest |  (optional)

    try:
        # Update a form state
        api_instance.organizations_organization_slug_forms_form_type_form_slug_state_put(organization_slug, form_slug, form_type, hello_asso_api_v5_common_models_forms_form_state_request=hello_asso_api_v5_common_models_forms_form_state_request)
    except Exception as e:
        print("Exception when calling FormsApi->organizations_organization_slug_forms_form_type_form_slug_state_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**|  | 
 **form_slug** | **str**|  | 
 **form_type** | [**HelloAssoApiV5CommonModelsEnumsFormType**](.md)|  | 
 **hello_asso_api_v5_common_models_forms_form_state_request** | [**HelloAssoApiV5CommonModelsFormsFormStateRequest**](HelloAssoApiV5CommonModelsFormsFormStateRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_organization_slug_forms_form_type_form_slug_stats_get**
> HelloAssoApiV5CommonModelsFormsFormStatsModel organizations_organization_slug_forms_form_type_form_slug_stats_get(organization_slug, form_slug, form_type)

Get Stats for the form

<br/><br/><b>Your token must have one of these roles : </b><br/>FormAdmin<br/>OrganizationAdmin<br/><br/>If you are an <b>association</b>, you can obtain these roles with your client.<br/>If you are a <b>partner</b>, you can obtain these roles by the authorize flow.<br/><br/><b>Your clientId must be allowed all of those privileges : </b> <br/> AccessPublicData<br/><br/>

### Example


```python
import helloasso_python
from helloasso_python.models.hello_asso_api_v5_common_models_enums_form_type import HelloAssoApiV5CommonModelsEnumsFormType
from helloasso_python.models.hello_asso_api_v5_common_models_forms_form_stats_model import HelloAssoApiV5CommonModelsFormsFormStatsModel
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
    api_instance = helloasso_python.FormsApi(api_client)
    organization_slug = 'organization_slug_example' # str | 
    form_slug = 'form_slug_example' # str | 
    form_type = helloasso_python.HelloAssoApiV5CommonModelsEnumsFormType() # HelloAssoApiV5CommonModelsEnumsFormType | 

    try:
        # Get Stats for the form
        api_response = api_instance.organizations_organization_slug_forms_form_type_form_slug_stats_get(organization_slug, form_slug, form_type)
        print("The response of FormsApi->organizations_organization_slug_forms_form_type_form_slug_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormsApi->organizations_organization_slug_forms_form_type_form_slug_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**|  | 
 **form_slug** | **str**|  | 
 **form_type** | [**HelloAssoApiV5CommonModelsEnumsFormType**](.md)|  | 

### Return type

[**HelloAssoApiV5CommonModelsFormsFormStatsModel**](HelloAssoApiV5CommonModelsFormsFormStatsModel.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

