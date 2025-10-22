# HelloAssoApiV5CommonModelsCommonDocumentModel

DocumentModel class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**file_name** | **str** | The file name of document | [optional] 
**public_url** | **str** | The public url of document | [optional] 
**state** | [**HelloAssoApiV5CommonModelsComplianceV2DocumentsDocumentState**](HelloAssoApiV5CommonModelsComplianceV2DocumentsDocumentState.md) |  | [optional] 

## Example

```python
from helloasso_python.models.hello_asso_api_v5_common_models_common_document_model import HelloAssoApiV5CommonModelsCommonDocumentModel

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoApiV5CommonModelsCommonDocumentModel from a JSON string
hello_asso_api_v5_common_models_common_document_model_instance = HelloAssoApiV5CommonModelsCommonDocumentModel.from_json(json)
# print the JSON string representation of the object
print(HelloAssoApiV5CommonModelsCommonDocumentModel.to_json())

# convert the object into a dict
hello_asso_api_v5_common_models_common_document_model_dict = hello_asso_api_v5_common_models_common_document_model_instance.to_dict()
# create an instance of HelloAssoApiV5CommonModelsCommonDocumentModel from a dict
hello_asso_api_v5_common_models_common_document_model_from_dict = HelloAssoApiV5CommonModelsCommonDocumentModel.from_dict(hello_asso_api_v5_common_models_common_document_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


