# helloasso_python.ValuesDefinitionsApi

All URIs are relative to *https://api.helloasso.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**values_form_form_type_types_get**](ValuesDefinitionsApi.md#values_form_form_type_types_get) | **GET** /values/form/{formType}/types | Get all activity types for a form type


# **values_form_form_type_types_get**
> List[HelloAssoApiV5CommonModelsFormsFormActivityModel] values_form_form_type_types_get(form_type)

Get all activity types for a form type

Use this in order to build your dropdown of form subtypes<br/><br/><b>Your clientId must be allowed all of those privileges : </b> <br/> FormAdministration<br/><br/>

### Example


```python
import helloasso_python
from helloasso_python.models.hello_asso_api_v5_common_models_enums_form_type import HelloAssoApiV5CommonModelsEnumsFormType
from helloasso_python.models.hello_asso_api_v5_common_models_forms_form_activity_model import HelloAssoApiV5CommonModelsFormsFormActivityModel
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
    api_instance = helloasso_python.ValuesDefinitionsApi(api_client)
    form_type = helloasso_python.HelloAssoApiV5CommonModelsEnumsFormType() # HelloAssoApiV5CommonModelsEnumsFormType | 

    try:
        # Get all activity types for a form type
        api_response = api_instance.values_form_form_type_types_get(form_type)
        print("The response of ValuesDefinitionsApi->values_form_form_type_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValuesDefinitionsApi->values_form_form_type_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_type** | [**HelloAssoApiV5CommonModelsEnumsFormType**](.md)|  | 

### Return type

[**List[HelloAssoApiV5CommonModelsFormsFormActivityModel]**](HelloAssoApiV5CommonModelsFormsFormActivityModel.md)

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

