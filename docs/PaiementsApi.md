# helloasso_python.PaiementsApi

All URIs are relative to *https://api.helloasso.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_organization_slug_forms_form_type_form_slug_payments_get**](PaiementsApi.md#organizations_organization_slug_forms_form_type_form_slug_payments_get) | **GET** /organizations/{organizationSlug}/forms/{formType}/{formSlug}/payments | Obtenir les informations des paiements effectués sur un formulaire
[**organizations_organization_slug_payments_get**](PaiementsApi.md#organizations_organization_slug_payments_get) | **GET** /organizations/{organizationSlug}/payments | Obtenir les informations des paiements effectués sur une organisation
[**payments_payment_id_get**](PaiementsApi.md#payments_payment_id_get) | **GET** /payments/{paymentId} | Obtenir les informations détaillées d&#39;un paiement.
[**payments_payment_id_refund_post**](PaiementsApi.md#payments_payment_id_refund_post) | **POST** /payments/{paymentId}/refund | Rembourser un paiement.


# **organizations_organization_slug_forms_form_type_form_slug_payments_get**
> HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment organizations_organization_slug_forms_form_type_form_slug_payments_get(organization_slug, form_slug, form_type, var_from=var_from, to=to, user_search_key=user_search_key, page_index=page_index, page_size=page_size, continuation_token=continuation_token, states=states, sort_order=sort_order, sort_field=sort_field)

Obtenir les informations des paiements effectués sur un formulaire

<br/><br/><b>Votre token doit avoir l'un de ces rôles : </b><br/>FormAdmin<br/>OrganizationAdmin<br/><br/>Si vous êtes une <b>association</b>, vous pouvez obtenir ces rôles avec votre client.<br/>Si vous êtes un <b>partenaire</b>, vous pouvez obtenir ces rôles par le flux d'autorisation.<br/><br/><b>Votre clientId doit être autorisé à tous ces privilèges : </b> <br/> AccessTransactions<br/><br/>

### Example

* OAuth Authentication (OAuth2):

```python
import helloasso_python
from helloasso_python.models.hello_asso_api_v5_common_models_common_results_with_pagination_model_payment import HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment
from helloasso_python.models.hello_asso_api_v5_common_models_enums_form_type import HelloAssoApiV5CommonModelsEnumsFormType
from helloasso_python.models.hello_asso_api_v5_common_models_enums_payment_state import HelloAssoApiV5CommonModelsEnumsPaymentState
from helloasso_python.models.hello_asso_api_v5_common_models_enums_sort_field import HelloAssoApiV5CommonModelsEnumsSortField
from helloasso_python.models.hello_asso_api_v5_common_models_enums_sort_order import HelloAssoApiV5CommonModelsEnumsSortOrder
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
    api_instance = helloasso_python.PaiementsApi(api_client)
    organization_slug = 'organization_slug_example' # str | The organization slug
    form_slug = 'form_slug_example' # str | The form slug
    form_type = helloasso_python.HelloAssoApiV5CommonModelsEnumsFormType() # HelloAssoApiV5CommonModelsEnumsFormType | The form type CrowdFunding, Membership, Event, Donation, PaymentForm, Checkout, Shop
    var_from = '2013-10-20T19:20:30+01:00' # datetime | First Date Filter (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | End Date Filter (exclusive) (optional)
    user_search_key = 'user_search_key_example' # str | Filter results on user or payer first name, last name or email (optional)
    page_index = 1 # int | The page of results to retrieve (optional) (default to 1)
    page_size = 20 # int | The number of items per page (optional) (default to 20)
    continuation_token = 'continuation_token_example' # str | Continuation Token from which we wish to retrieve results (optional)
    states = [helloasso_python.HelloAssoApiV5CommonModelsEnumsPaymentState()] # List[HelloAssoApiV5CommonModelsEnumsPaymentState] | Filter results by states of payments  Available values: * `Pending` - A payment scheduled at a later date, not yet processed. * `Authorized` - The payment has been authorized, validated, processed. * `Refused` - The payment has been refused by the bank. * `Unknown` * `Registered` - Represents a payment made offline.             Probably for an item of type * `Refunded` - The payment has been refunded. * `Refunding` - The payment is being refunded. * `Contested` - Payment has been contested by the contributor * `WaitingBankValidation` - The payment is pending validation from the bank (used by SEPA direct debit). (optional)
    sort_order = helloasso_python.HelloAssoApiV5CommonModelsEnumsSortOrder() # HelloAssoApiV5CommonModelsEnumsSortOrder | Sort payments by ascending or descending order. Default is descending (optional)
    sort_field = helloasso_python.HelloAssoApiV5CommonModelsEnumsSortField() # HelloAssoApiV5CommonModelsEnumsSortField | Sort payments by a specific field (Date or UpdateDate). Default is date (optional)

    try:
        # Obtenir les informations des paiements effectués sur un formulaire
        api_response = api_instance.organizations_organization_slug_forms_form_type_form_slug_payments_get(organization_slug, form_slug, form_type, var_from=var_from, to=to, user_search_key=user_search_key, page_index=page_index, page_size=page_size, continuation_token=continuation_token, states=states, sort_order=sort_order, sort_field=sort_field)
        print("The response of PaiementsApi->organizations_organization_slug_forms_form_type_form_slug_payments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaiementsApi->organizations_organization_slug_forms_form_type_form_slug_payments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**| The organization slug | 
 **form_slug** | **str**| The form slug | 
 **form_type** | [**HelloAssoApiV5CommonModelsEnumsFormType**](.md)| The form type CrowdFunding, Membership, Event, Donation, PaymentForm, Checkout, Shop | 
 **var_from** | **datetime**| First Date Filter | [optional] 
 **to** | **datetime**| End Date Filter (exclusive) | [optional] 
 **user_search_key** | **str**| Filter results on user or payer first name, last name or email | [optional] 
 **page_index** | **int**| The page of results to retrieve | [optional] [default to 1]
 **page_size** | **int**| The number of items per page | [optional] [default to 20]
 **continuation_token** | **str**| Continuation Token from which we wish to retrieve results | [optional] 
 **states** | [**List[HelloAssoApiV5CommonModelsEnumsPaymentState]**](HelloAssoApiV5CommonModelsEnumsPaymentState.md)| Filter results by states of payments  Available values: * &#x60;Pending&#x60; - A payment scheduled at a later date, not yet processed. * &#x60;Authorized&#x60; - The payment has been authorized, validated, processed. * &#x60;Refused&#x60; - The payment has been refused by the bank. * &#x60;Unknown&#x60; * &#x60;Registered&#x60; - Represents a payment made offline.             Probably for an item of type * &#x60;Refunded&#x60; - The payment has been refunded. * &#x60;Refunding&#x60; - The payment is being refunded. * &#x60;Contested&#x60; - Payment has been contested by the contributor * &#x60;WaitingBankValidation&#x60; - The payment is pending validation from the bank (used by SEPA direct debit). | [optional] 
 **sort_order** | [**HelloAssoApiV5CommonModelsEnumsSortOrder**](.md)| Sort payments by ascending or descending order. Default is descending | [optional] 
 **sort_field** | [**HelloAssoApiV5CommonModelsEnumsSortField**](.md)| Sort payments by a specific field (Date or UpdateDate). Default is date | [optional] 

### Return type

[**HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment**](HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **organizations_organization_slug_payments_get**
> HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment organizations_organization_slug_payments_get(organization_slug, var_from=var_from, to=to, user_search_key=user_search_key, page_index=page_index, page_size=page_size, continuation_token=continuation_token, states=states, sort_order=sort_order, sort_field=sort_field)

Obtenir les informations des paiements effectués sur une organisation

Retourne la liste des paiements selon les paramètres<br/><br/><b>Votre token doit avoir l'un de ces rôles : </b><br/>OrganizationAdmin<br/><br/>Si vous êtes une <b>association</b>, vous pouvez obtenir ces rôles avec votre client.<br/>Si vous êtes un <b>partenaire</b>, vous pouvez obtenir ces rôles par le flux d'autorisation.<br/><br/><b>Votre clientId doit être autorisé à tous ces privilèges : </b> <br/> AccessTransactions<br/><br/>

### Example

* OAuth Authentication (OAuth2):

```python
import helloasso_python
from helloasso_python.models.hello_asso_api_v5_common_models_common_results_with_pagination_model_payment import HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment
from helloasso_python.models.hello_asso_api_v5_common_models_enums_payment_state import HelloAssoApiV5CommonModelsEnumsPaymentState
from helloasso_python.models.hello_asso_api_v5_common_models_enums_sort_field import HelloAssoApiV5CommonModelsEnumsSortField
from helloasso_python.models.hello_asso_api_v5_common_models_enums_sort_order import HelloAssoApiV5CommonModelsEnumsSortOrder
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
    api_instance = helloasso_python.PaiementsApi(api_client)
    organization_slug = 'organization_slug_example' # str | The organization Slug
    var_from = '2013-10-20T19:20:30+01:00' # datetime | First Date Filter (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | End Date Filter (exclusive) (optional)
    user_search_key = 'user_search_key_example' # str | Filter results on user or payer first name, last name or email (optional)
    page_index = 1 # int | The page of results to retrieve (optional) (default to 1)
    page_size = 20 # int | The number of items per page (optional) (default to 20)
    continuation_token = 'continuation_token_example' # str | Continuation Token from which we wish to retrieve results (optional)
    states = [helloasso_python.HelloAssoApiV5CommonModelsEnumsPaymentState()] # List[HelloAssoApiV5CommonModelsEnumsPaymentState] | The payment states  Available values: * `Pending` - A payment scheduled at a later date, not yet processed. * `Authorized` - The payment has been authorized, validated, processed. * `Refused` - The payment has been refused by the bank. * `Unknown` * `Registered` - Represents a payment made offline.             Probably for an item of type * `Refunded` - The payment has been refunded. * `Refunding` - The payment is being refunded. * `Contested` - Payment has been contested by the contributor * `WaitingBankValidation` - The payment is pending validation from the bank (used by SEPA direct debit). (optional)
    sort_order = helloasso_python.HelloAssoApiV5CommonModelsEnumsSortOrder() # HelloAssoApiV5CommonModelsEnumsSortOrder | Sort payments by ascending or descending order. Default is descending (optional)
    sort_field = helloasso_python.HelloAssoApiV5CommonModelsEnumsSortField() # HelloAssoApiV5CommonModelsEnumsSortField | Sort payments by a specific field (Date or UpdateDate). Default is date (optional)

    try:
        # Obtenir les informations des paiements effectués sur une organisation
        api_response = api_instance.organizations_organization_slug_payments_get(organization_slug, var_from=var_from, to=to, user_search_key=user_search_key, page_index=page_index, page_size=page_size, continuation_token=continuation_token, states=states, sort_order=sort_order, sort_field=sort_field)
        print("The response of PaiementsApi->organizations_organization_slug_payments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaiementsApi->organizations_organization_slug_payments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**| The organization Slug | 
 **var_from** | **datetime**| First Date Filter | [optional] 
 **to** | **datetime**| End Date Filter (exclusive) | [optional] 
 **user_search_key** | **str**| Filter results on user or payer first name, last name or email | [optional] 
 **page_index** | **int**| The page of results to retrieve | [optional] [default to 1]
 **page_size** | **int**| The number of items per page | [optional] [default to 20]
 **continuation_token** | **str**| Continuation Token from which we wish to retrieve results | [optional] 
 **states** | [**List[HelloAssoApiV5CommonModelsEnumsPaymentState]**](HelloAssoApiV5CommonModelsEnumsPaymentState.md)| The payment states  Available values: * &#x60;Pending&#x60; - A payment scheduled at a later date, not yet processed. * &#x60;Authorized&#x60; - The payment has been authorized, validated, processed. * &#x60;Refused&#x60; - The payment has been refused by the bank. * &#x60;Unknown&#x60; * &#x60;Registered&#x60; - Represents a payment made offline.             Probably for an item of type * &#x60;Refunded&#x60; - The payment has been refunded. * &#x60;Refunding&#x60; - The payment is being refunded. * &#x60;Contested&#x60; - Payment has been contested by the contributor * &#x60;WaitingBankValidation&#x60; - The payment is pending validation from the bank (used by SEPA direct debit). | [optional] 
 **sort_order** | [**HelloAssoApiV5CommonModelsEnumsSortOrder**](.md)| Sort payments by ascending or descending order. Default is descending | [optional] 
 **sort_field** | [**HelloAssoApiV5CommonModelsEnumsSortField**](.md)| Sort payments by a specific field (Date or UpdateDate). Default is date | [optional] 

### Return type

[**HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment**](HelloAssoApiV5CommonModelsCommonResultsWithPaginationModelPayment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized, you must add a valid JWT into Authorization Header with the format : &#x60;Bearer TOKEN&#x60; |  -  |
**403** | The JWT token hasn&#39;t the privileges or Roles for this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_payment_id_get**
> HelloAssoApiV5CommonModelsStatisticsPaymentDetail payments_payment_id_get(payment_id, with_failed_refund_operation=with_failed_refund_operation)

Obtenir les informations détaillées d'un paiement.

<br/><br/><b>Votre token doit avoir l'un de ces rôles : </b><br/>FormAdmin<br/>OrganizationAdmin<br/><br/>Si vous êtes une <b>association</b>, vous pouvez obtenir ces rôles avec votre client.<br/>Si vous êtes un <b>partenaire</b>, vous pouvez obtenir ces rôles par le flux d'autorisation.<br/><br/><b>Votre clientId doit être autorisé à tous ces privilèges : </b> <br/> AccessTransactions<br/><br/>

### Example

* OAuth Authentication (OAuth2):

```python
import helloasso_python
from helloasso_python.models.hello_asso_api_v5_common_models_statistics_payment_detail import HelloAssoApiV5CommonModelsStatisticsPaymentDetail
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
    api_instance = helloasso_python.PaiementsApi(api_client)
    payment_id = 56 # int | The payment identifier.
    with_failed_refund_operation = False # bool | True to retrieve the refund operation in the states 'ABORTED', 'CANCELED', 'ERROR', 'REFUSED'. (optional) (default to False)

    try:
        # Obtenir les informations détaillées d'un paiement.
        api_response = api_instance.payments_payment_id_get(payment_id, with_failed_refund_operation=with_failed_refund_operation)
        print("The response of PaiementsApi->payments_payment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaiementsApi->payments_payment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **int**| The payment identifier. | 
 **with_failed_refund_operation** | **bool**| True to retrieve the refund operation in the states &#39;ABORTED&#39;, &#39;CANCELED&#39;, &#39;ERROR&#39;, &#39;REFUSED&#39;. | [optional] [default to False]

### Return type

[**HelloAssoApiV5CommonModelsStatisticsPaymentDetail**](HelloAssoApiV5CommonModelsStatisticsPaymentDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **payments_payment_id_refund_post**
> HelloAssoApiV5CommonModelsPaymentRefundOperationModel payments_payment_id_refund_post(payment_id, comment=comment, cancel_order=cancel_order, send_refund_mail=send_refund_mail, amount=amount, x_mfa_access_authorization=x_mfa_access_authorization, x_mfa_sms_access_authorization=x_mfa_sms_access_authorization, x_mfa_password_authorization=x_mfa_password_authorization)

Rembourser un paiement.

<br/><br/><b>Votre token doit avoir l'un de ces rôles : </b><br/>OrganizationAdmin<br/>FormAdmin<br/><br/>Si vous êtes une <b>association</b>, vous pouvez obtenir ces rôles avec votre client.<br/>Si vous êtes un <b>partenaire</b>, vous pouvez obtenir ces rôles par le flux d'autorisation.<br/><br/><b>Votre clientId doit être autorisé à tous ces privilèges : </b> <br/> RefundManagement<br/><br/>

### Example

* OAuth Authentication (OAuth2):

```python
import helloasso_python
from helloasso_python.models.hello_asso_api_v5_common_models_payment_refund_operation_model import HelloAssoApiV5CommonModelsPaymentRefundOperationModel
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
    api_instance = helloasso_python.PaiementsApi(api_client)
    payment_id = 56 # int | The payment identifier.
    comment = 'comment_example' # str | The comment about this refund. (optional)
    cancel_order = False # bool | Whether the future payments and linked items of this order must be canceled (possible only if the payment is fully refunded) (optional) (default to False)
    send_refund_mail = True # bool | Whether a refund mail must be sent or not. (optional) (default to True)
    amount = 0 # int | The amount in cents to refund. Enter this amount only for a partial refund for stripe. If not filled in then the entire payment is refunded (optional) (default to 0)
    x_mfa_access_authorization = 'x_mfa_access_authorization_example' # str | Must be filled only if AuthorizationErrors.MFA.AccessTokenRequired error code was returned previously. (optional)
    x_mfa_sms_access_authorization = 'x_mfa_sms_access_authorization_example' # str | Must be filled only if AuthorizationErrors.MFA.AccessOtpSmsRequired error code was returned previously. (optional)
    x_mfa_password_authorization = 'x_mfa_password_authorization_example' # str | Must be filled only if AuthorizationErrors.MFA.AccessPasswordTokenRequired error code was returned previously. (optional)

    try:
        # Rembourser un paiement.
        api_response = api_instance.payments_payment_id_refund_post(payment_id, comment=comment, cancel_order=cancel_order, send_refund_mail=send_refund_mail, amount=amount, x_mfa_access_authorization=x_mfa_access_authorization, x_mfa_sms_access_authorization=x_mfa_sms_access_authorization, x_mfa_password_authorization=x_mfa_password_authorization)
        print("The response of PaiementsApi->payments_payment_id_refund_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaiementsApi->payments_payment_id_refund_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **int**| The payment identifier. | 
 **comment** | **str**| The comment about this refund. | [optional] 
 **cancel_order** | **bool**| Whether the future payments and linked items of this order must be canceled (possible only if the payment is fully refunded) | [optional] [default to False]
 **send_refund_mail** | **bool**| Whether a refund mail must be sent or not. | [optional] [default to True]
 **amount** | **int**| The amount in cents to refund. Enter this amount only for a partial refund for stripe. If not filled in then the entire payment is refunded | [optional] [default to 0]
 **x_mfa_access_authorization** | **str**| Must be filled only if AuthorizationErrors.MFA.AccessTokenRequired error code was returned previously. | [optional] 
 **x_mfa_sms_access_authorization** | **str**| Must be filled only if AuthorizationErrors.MFA.AccessOtpSmsRequired error code was returned previously. | [optional] 
 **x_mfa_password_authorization** | **str**| Must be filled only if AuthorizationErrors.MFA.AccessPasswordTokenRequired error code was returned previously. | [optional] 

### Return type

[**HelloAssoApiV5CommonModelsPaymentRefundOperationModel**](HelloAssoApiV5CommonModelsPaymentRefundOperationModel.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized, you must add a valid JWT into Authorization Header with the format : &#x60;Bearer TOKEN&#x60; |  -  |
**403** | The JWT token hasn&#39;t the privileges or Roles for this action |  -  |
**409** | ### Multi-Factor Authentication Required This endpoint requires MFA. Below are the possible error codes and required headers:  --- **Code: &#x60;AuthorizationErrors.MFA.AccessTokenRequired&#x60;**   MFA token not found &lt;br/&gt;&lt;br/&gt; A MFA token is expected in x-mfa-access-authorization header or in cookie mfa-{protectedOperation}-{organizationId}.  --- **Code: &#x60;AuthorizationErrors.MFA.AccessOtpSmsRequired&#x60;**   MFA access otp sms not found &lt;br/&gt;&lt;br/&gt; A MFA token is expected in x-mfa-sms-access-authorization header or in cookie mfa-{protectedOperation}-{organizationId}-otp-sms.  --- **Code: &#x60;AuthorizationErrors.MFA.AccessPasswordTokenRequired&#x60;**   MFA access password token not found &lt;br/&gt;&lt;br/&gt; A MFA token is expected in x-mfa-password-authorization header or in cookie mfa-{protectedOperation}-{organizationId}-pwd.  --- **Code: &#x60;AuthorizationErrors.UserNotEnrolled&#x60;**   User 123 not enrolled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

