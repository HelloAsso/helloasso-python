# HelloAssoApiV5CommonModelsApiNotificationsPostApiUrlNotificationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The Api notification Url | 
**notification_type** | [**HelloAssoApiV5CommonModelsApiNotificationsApiNotificationType**](HelloAssoApiV5CommonModelsApiNotificationsApiNotificationType.md) |  | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_api_notifications_post_api_url_notification_body import HelloAssoApiV5CommonModelsApiNotificationsPostApiUrlNotificationBody

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsApiNotificationsPostApiUrlNotificationBody from a JSON string
hello_asso_api_v5_common_models_api_notifications_post_api_url_notification_body_instance = HelloAssoApiV5CommonModelsApiNotificationsPostApiUrlNotificationBody.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsApiNotificationsPostApiUrlNotificationBody.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_api_notifications_post_api_url_notification_body_dict = hello_asso_api_v5_common_models_api_notifications_post_api_url_notification_body_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsApiNotificationsPostApiUrlNotificationBody from a dict
hello_asso_api_v5_common_models_api_notifications_post_api_url_notification_body_from_dict = HelloAssoApiV5CommonModelsApiNotificationsPostApiUrlNotificationBody.from_dict(hello_asso_api_v5_common_models_api_notifications_post_api_url_notification_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


