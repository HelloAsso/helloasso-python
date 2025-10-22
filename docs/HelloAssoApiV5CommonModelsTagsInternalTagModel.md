# HelloAssoApiV5CommonModelsTagsInternalTagModel

InternalTagModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Tag Id | [optional] 
**name** | **str** | Name tag | [optional] 
**form_count** | **int** | Count of times Tag is used by forms | [optional] 
**organization_count** | **int** | Count of times Tag is used by Organizations | [optional] 
**tag_type** | [**HelloAssoApiV5CommonModelsEnumsTagType**](HelloAssoApiV5CommonModelsEnumsTagType.md) |  | [optional] 
**tag_parent** | [**HelloAssoApiV5CommonModelsTagsInternalTagModel**](HelloAssoApiV5CommonModelsTagsInternalTagModel.md) |  | [optional] 
**amount_collected** | **int** | Amount collected by all forms linked to this tag (in cents) | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_tags_internal_tag_model import HelloAssoApiV5CommonModelsTagsInternalTagModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsTagsInternalTagModel from a JSON string
hello_asso_api_v5_common_models_tags_internal_tag_model_instance = HelloAssoApiV5CommonModelsTagsInternalTagModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsTagsInternalTagModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_tags_internal_tag_model_dict = hello_asso_api_v5_common_models_tags_internal_tag_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsTagsInternalTagModel from a dict
hello_asso_api_v5_common_models_tags_internal_tag_model_from_dict = HelloAssoApiV5CommonModelsTagsInternalTagModel.from_dict(hello_asso_api_v5_common_models_tags_internal_tag_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


