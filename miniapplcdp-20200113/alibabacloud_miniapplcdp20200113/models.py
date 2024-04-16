# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class DataItemsModelDataValue(TeaModel):
    def __init__(
        self,
        id: str = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        sub_type: str = None,
        module_id: str = None,
        content: str = None,
        app_id: str = None,
        linked: bool = None,
        link_module_id: str = None,
        link_model_id: str = None,
        schema_version: str = None,
        description: str = None,
        props: str = None,
        visibility: str = None,
        model_digest: str = None,
    ):
        self.id = id
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.sub_type = sub_type
        self.module_id = module_id
        self.content = content
        self.app_id = app_id
        self.linked = linked
        self.link_module_id = link_module_id
        self.link_model_id = link_model_id
        self.schema_version = schema_version
        self.description = description
        self.props = props
        self.visibility = visibility
        self.model_digest = model_digest

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.content is not None:
            result['Content'] = self.content
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.description is not None:
            result['Description'] = self.description
        if self.props is not None:
            result['Props'] = self.props
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        return self


class DataItemsResourceDataValue(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        description: str = None,
        schema_version: str = None,
        module_id: str = None,
        content: Dict[str, Any] = None,
        app_id: str = None,
        visibility: str = None,
    ):
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.description = description
        self.schema_version = schema_version
        self.module_id = module_id
        self.content = content
        self.app_id = app_id
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.description is not None:
            result['Description'] = self.description
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.content is not None:
            result['Content'] = self.content
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class BatchCreateModelRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        model_data_json: str = None,
        module_id: str = None,
        schema_version: str = None,
        source: str = None,
        sub_type: str = None,
    ):
        self.app_id = app_id
        self.model_data_json = model_data_json
        self.module_id = module_id
        self.schema_version = schema_version
        self.source = source
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_data_json is not None:
            result['ModelDataJson'] = self.model_data_json
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelDataJson') is not None:
            self.model_data_json = m.get('ModelDataJson')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class BatchCreateModelResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_digest: str = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_digest = model_digest
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class BatchCreateModelResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[BatchCreateModelResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = BatchCreateModelResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class BatchCreateModelResponseBody(TeaModel):
    def __init__(
        self,
        data: BatchCreateModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = BatchCreateModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchCreateModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCreateModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchCreateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteModelRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        model_id_list: str = None,
        module_id: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.model_id_list = model_id_list
        self.module_id = module_id
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id_list is not None:
            result['ModelIdList'] = self.model_id_list
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelIdList') is not None:
            self.model_id_list = m.get('ModelIdList')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class BatchDeleteModelResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class BatchDeleteModelResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[BatchDeleteModelResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = BatchDeleteModelResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class BatchDeleteModelResponseBody(TeaModel):
    def __init__(
        self,
        data: BatchDeleteModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = BatchDeleteModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDeleteModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchDeleteModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteResourcesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        module_id: str = None,
        resource_id_list: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.module_id = module_id
        self.resource_id_list = resource_id_list
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id_list is not None:
            result['ResourceIdList'] = self.resource_id_list
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceIdList') is not None:
            self.resource_id_list = m.get('ResourceIdList')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class BatchDeleteResourcesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        revision: int = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.revision = revision
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class BatchDeleteResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[BatchDeleteResourcesResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = BatchDeleteResourcesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class BatchDeleteResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: BatchDeleteResourcesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = BatchDeleteResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDeleteResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchDeleteResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchRestoreModelRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        model_id_list: str = None,
        module_id: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.model_id_list = model_id_list
        self.module_id = module_id
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id_list is not None:
            result['ModelIdList'] = self.model_id_list
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelIdList') is not None:
            self.model_id_list = m.get('ModelIdList')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class BatchRestoreModelResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class BatchRestoreModelResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[BatchRestoreModelResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = BatchRestoreModelResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class BatchRestoreModelResponseBody(TeaModel):
    def __init__(
        self,
        data: BatchRestoreModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = BatchRestoreModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchRestoreModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchRestoreModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchRestoreModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain: str = None,
        domain_type: str = None,
        env_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.domain = domain
        self.domain_type = domain_type
        self.env_id = env_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CheckDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        valid: bool = None,
    ):
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class CheckDomainResponseBody(TeaModel):
    def __init__(
        self,
        data: CheckDomainResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CheckDomainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        description: str = None,
        icon: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.description = description
        self.icon = icon
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CloneAppResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_status: str = None,
        app_type: str = None,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        is_template: bool = None,
        last_edit_time: str = None,
        main_module_id: str = None,
        modified_time: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_status = app_status
        self.app_type = app_type
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.is_template = is_template
        self.last_edit_time = last_edit_time
        self.main_module_id = main_module_id
        self.modified_time = modified_time
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CloneAppResponseBody(TeaModel):
    def __init__(
        self,
        data: CloneAppResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CloneAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneModelFromCommitRequest(TeaModel):
    def __init__(
        self,
        model_id: str = None,
        source: str = None,
        source_commit_id: str = None,
        source_module_id: str = None,
        sub_type: str = None,
        target_module_id: str = None,
        target_name: str = None,
        target_sub_type: str = None,
    ):
        self.model_id = model_id
        self.source = source
        self.source_commit_id = source_commit_id
        self.source_module_id = source_module_id
        self.sub_type = sub_type
        self.target_module_id = target_module_id
        self.target_name = target_name
        self.target_sub_type = target_sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_commit_id is not None:
            result['SourceCommitId'] = self.source_commit_id
        if self.source_module_id is not None:
            result['SourceModuleId'] = self.source_module_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.target_module_id is not None:
            result['TargetModuleId'] = self.target_module_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_sub_type is not None:
            result['TargetSubType'] = self.target_sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceCommitId') is not None:
            self.source_commit_id = m.get('SourceCommitId')
        if m.get('SourceModuleId') is not None:
            self.source_module_id = m.get('SourceModuleId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('TargetModuleId') is not None:
            self.target_module_id = m.get('TargetModuleId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetSubType') is not None:
            self.target_sub_type = m.get('TargetSubType')
        return self


class CloneModelFromCommitResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CloneModelFromCommitResponseBody(TeaModel):
    def __init__(
        self,
        data: CloneModelFromCommitResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CloneModelFromCommitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneModelFromCommitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneModelFromCommitResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneModelFromCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneModelInModuleRequest(TeaModel):
    def __init__(
        self,
        model_id: str = None,
        module_id: str = None,
        source: str = None,
        target_name: str = None,
        target_sub_type: str = None,
    ):
        self.model_id = model_id
        self.module_id = module_id
        self.source = source
        self.target_name = target_name
        self.target_sub_type = target_sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_sub_type is not None:
            result['TargetSubType'] = self.target_sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetSubType') is not None:
            self.target_sub_type = m.get('TargetSubType')
        return self


class CloneModelInModuleResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CloneModelInModuleResponseBody(TeaModel):
    def __init__(
        self,
        data: CloneModelInModuleResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CloneModelInModuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneModelInModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneModelInModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneModelInModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        asynchronous: bool = None,
        category_id: str = None,
        client_token: str = None,
        description: str = None,
        icon: str = None,
        platform_version: str = None,
        schema_version: str = None,
        source: str = None,
        source_commit_id: str = None,
        template_id: str = None,
        templated: bool = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.asynchronous = asynchronous
        self.category_id = category_id
        self.client_token = client_token
        self.description = description
        self.icon = icon
        self.platform_version = platform_version
        self.schema_version = schema_version
        self.source = source
        self.source_commit_id = source_commit_id
        self.template_id = template_id
        self.templated = templated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.asynchronous is not None:
            result['Asynchronous'] = self.asynchronous
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.source_commit_id is not None:
            result['SourceCommitId'] = self.source_commit_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.templated is not None:
            result['Templated'] = self.templated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Asynchronous') is not None:
            self.asynchronous = m.get('Asynchronous')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceCommitId') is not None:
            self.source_commit_id = m.get('SourceCommitId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Templated') is not None:
            self.templated = m.get('Templated')
        return self


class CreateAppResponseBodyDataCategories(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        category_name: str = None,
        parent_category_id: str = None,
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class CreateAppResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_status: str = None,
        app_type: str = None,
        categories: List[CreateAppResponseBodyDataCategories] = None,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        is_template: bool = None,
        last_edit_time: str = None,
        main_module_id: str = None,
        modified_time: str = None,
        platform_version: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_status = app_status
        self.app_type = app_type
        self.categories = categories
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.is_template = is_template
        self.last_edit_time = last_edit_time
        self.main_module_id = main_module_id
        self.modified_time = modified_time
        self.platform_version = platform_version
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = CreateAppResponseBodyDataCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateAppResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCommitRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        commit_log: str = None,
        commit_type: str = None,
        main_module_commit_id: str = None,
        module_id: str = None,
        rollback_to_commit_id: str = None,
        rollback_type: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.client_token = client_token
        self.commit_log = commit_log
        self.commit_type = commit_type
        self.main_module_commit_id = main_module_commit_id
        self.module_id = module_id
        self.rollback_to_commit_id = rollback_to_commit_id
        self.rollback_type = rollback_type
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateCommitResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_id: str = None,
        commit_log: str = None,
        commit_type: str = None,
        create_time: str = None,
        main_module_commit_id: str = None,
        main_module_id: str = None,
        model_data_path: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_data_path: str = None,
        resource_digest: Dict[str, str] = None,
        rollback_to_commit_id: str = None,
        rollback_type: str = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.commit_id = commit_id
        self.commit_log = commit_log
        self.commit_type = commit_type
        self.create_time = create_time
        self.main_module_commit_id = main_module_commit_id
        self.main_module_id = main_module_id
        self.model_data_path = model_data_path
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_data_path = resource_data_path
        self.resource_digest = resource_digest
        self.rollback_to_commit_id = rollback_to_commit_id
        self.rollback_type = rollback_type
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class CreateCommitResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateCommitResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateCommitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCommitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCommitResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        domain: str = None,
        domain_type: str = None,
        env_id: str = None,
        path: str = None,
        private_key: str = None,
        public_key: str = None,
        source: str = None,
        with_certificate: bool = None,
    ):
        self.app_id = app_id
        self.client_token = client_token
        self.domain = domain
        self.domain_type = domain_type
        self.env_id = env_id
        self.path = path
        self.private_key = private_key
        self.public_key = public_key
        self.source = source
        self.with_certificate = with_certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.path is not None:
            result['Path'] = self.path
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.source is not None:
            result['Source'] = self.source
        if self.with_certificate is not None:
            result['WithCertificate'] = self.with_certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WithCertificate') is not None:
            self.with_certificate = m.get('WithCertificate')
        return self


class CreateDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        applied: bool = None,
        checked: bool = None,
        cname: str = None,
        deleted: bool = None,
        domain: str = None,
        domain_type: str = None,
        env_id: str = None,
        path: str = None,
        with_certificate: bool = None,
    ):
        self.app_id = app_id
        self.applied = applied
        self.checked = checked
        self.cname = cname
        self.deleted = deleted
        self.domain = domain
        self.domain_type = domain_type
        self.env_id = env_id
        self.path = path
        self.with_certificate = with_certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.applied is not None:
            result['Applied'] = self.applied
        if self.checked is not None:
            result['Checked'] = self.checked
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.path is not None:
            result['Path'] = self.path
        if self.with_certificate is not None:
            result['WithCertificate'] = self.with_certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Applied') is not None:
            self.applied = m.get('Applied')
        if m.get('Checked') is not None:
            self.checked = m.get('Checked')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('WithCertificate') is not None:
            self.with_certificate = m.get('WithCertificate')
        return self


class CreateDomainResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateDomainResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateDomainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLinkEntityAndAssociationRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        model_data: str = None,
        source: str = None,
    ):
        self.client_token = client_token
        self.model_data = model_data
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.model_data is not None:
            result['ModelData'] = self.model_data
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ModelData') is not None:
            self.model_data = m.get('ModelData')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateLinkEntityAndAssociationResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CreateLinkEntityAndAssociationResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[CreateLinkEntityAndAssociationResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = CreateLinkEntityAndAssociationResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class CreateLinkEntityAndAssociationResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateLinkEntityAndAssociationResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateLinkEntityAndAssociationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLinkEntityAndAssociationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLinkEntityAndAssociationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLinkEntityAndAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        content: str = None,
        description: str = None,
        encode_type: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_id: str = None,
        model_name: str = None,
        model_type: str = None,
        module_id: str = None,
        schema_version: str = None,
        source: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.client_token = client_token
        self.content = content
        self.description = description
        self.encode_type = encode_type
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_id = model_id
        self.model_name = model_name
        self.model_type = model_type
        self.module_id = module_id
        self.schema_version = schema_version
        self.source = source
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CreateModelResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_digest: str = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_digest = model_digest
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CreateModelResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        icon: str = None,
        minimum_platform_version: str = None,
        module_name: str = None,
        module_type: str = None,
        platform: str = None,
        source: str = None,
        source_module_id: str = None,
        target_app_source: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.icon = icon
        self.minimum_platform_version = minimum_platform_version
        self.module_name = module_name
        self.module_type = module_type
        self.platform = platform
        self.source = source
        self.source_module_id = source_module_id
        self.target_app_source = target_app_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source is not None:
            result['Source'] = self.source
        if self.source_module_id is not None:
            result['SourceModuleId'] = self.source_module_id
        if self.target_app_source is not None:
            result['TargetAppSource'] = self.target_app_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceModuleId') is not None:
            self.source_module_id = m.get('SourceModuleId')
        if m.get('TargetAppSource') is not None:
            self.target_app_source = m.get('TargetAppSource')
        return self


class CreateModuleResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        latest_published_commit: str = None,
        latest_published_version: str = None,
        minimum_platform_version: str = None,
        modified_time: str = None,
        module_id: str = None,
        module_name: str = None,
        module_type: str = None,
        owner_app_id: str = None,
        owner_user_id: str = None,
        platform: str = None,
        platform_version: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.latest_published_commit = latest_published_commit
        self.latest_published_version = latest_published_version
        self.minimum_platform_version = minimum_platform_version
        self.modified_time = modified_time
        self.module_id = module_id
        self.module_name = module_name
        self.module_type = module_type
        self.owner_app_id = owner_app_id
        self.owner_user_id = owner_user_id
        self.platform = platform
        self.platform_version = platform_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        return self


class CreateModuleResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateModuleResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateModuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModulePublishRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        module_id: str = None,
        publish_version: str = None,
        source: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.module_id = module_id
        self.publish_version = publish_version
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.publish_version is not None:
            result['PublishVersion'] = self.publish_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PublishVersion') is not None:
            self.publish_version = m.get('PublishVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateModulePublishResponseBodyData(TeaModel):
    def __init__(
        self,
        commit_id: str = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        module_id: str = None,
        publish_id: str = None,
        version: str = None,
    ):
        self.commit_id = commit_id
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.module_id = module_id
        self.publish_id = publish_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateModulePublishResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateModulePublishResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateModulePublishResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModulePublishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModulePublishResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModulePublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePublishRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        commit_id: str = None,
        description: str = None,
        env_type: str = None,
        publish_type: str = None,
        source: str = None,
        version_number: str = None,
    ):
        self.app_id = app_id
        self.client_token = client_token
        self.commit_id = commit_id
        self.description = description
        self.env_type = env_type
        self.publish_type = publish_type
        self.source = source
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.description is not None:
            result['Description'] = self.description
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.source is not None:
            result['Source'] = self.source
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class CreatePublishResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_id: str = None,
        completion_time: str = None,
        create_time: str = None,
        description: str = None,
        env_id: str = None,
        modified_time: str = None,
        publish_id: str = None,
        publish_status: str = None,
        publish_type: str = None,
        reason: str = None,
        start_time: str = None,
        sub_tasks: List[Dict[str, str]] = None,
        version_number: str = None,
    ):
        self.app_id = app_id
        self.commit_id = commit_id
        self.completion_time = completion_time
        self.create_time = create_time
        self.description = description
        self.env_id = env_id
        self.modified_time = modified_time
        self.publish_id = publish_id
        self.publish_status = publish_status
        self.publish_type = publish_type
        self.reason = reason
        self.start_time = start_time
        self.sub_tasks = sub_tasks
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_tasks is not None:
            result['SubTasks'] = self.sub_tasks
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubTasks') is not None:
            self.sub_tasks = m.get('SubTasks')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class CreatePublishResponseBody(TeaModel):
    def __init__(
        self,
        data: CreatePublishResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreatePublishResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePublishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePublishResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        content: str = None,
        description: str = None,
        module_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        schema_version: str = None,
        source: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.client_token = client_token
        self.content = content
        self.description = description
        self.module_id = module_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.schema_version = schema_version
        self.source = source
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CreateResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_digest: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        revision: int = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_digest = resource_digest
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.revision = revision
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class CreateResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateResourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteAppResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_status: str = None,
        app_type: str = None,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        is_template: bool = None,
        last_edit_time: str = None,
        main_module_id: str = None,
        modified_time: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_status = app_status
        self.app_type = app_type
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.is_template = is_template
        self.last_edit_time = last_edit_time
        self.main_module_id = main_module_id
        self.modified_time = modified_time
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteAppResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCommitRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_id: str = None,
        module_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.commit_id = commit_id
        self.module_id = module_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteCommitResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_id: str = None,
        commit_log: str = None,
        commit_type: str = None,
        create_time: str = None,
        main_module_commit_id: str = None,
        main_module_id: str = None,
        model_data_path: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_data_path: str = None,
        resource_digest: Dict[str, str] = None,
        rollback_to_commit_id: str = None,
        rollback_type: str = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.commit_id = commit_id
        self.commit_log = commit_log
        self.commit_type = commit_type
        self.create_time = create_time
        self.main_module_commit_id = main_module_commit_id
        self.main_module_id = main_module_id
        self.model_data_path = model_data_path
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_data_path = resource_data_path
        self.resource_digest = resource_digest
        self.rollback_to_commit_id = rollback_to_commit_id
        self.rollback_type = rollback_type
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class DeleteCommitResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteCommitResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteCommitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCommitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCommitResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain: str = None,
        env_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.domain = domain
        self.env_id = env_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        applied: bool = None,
        deleted: bool = None,
        domain: str = None,
        domain_type: str = None,
        env_id: str = None,
        path: str = None,
    ):
        self.app_id = app_id
        self.applied = applied
        self.deleted = deleted
        self.domain = domain
        self.domain_type = domain_type
        self.env_id = env_id
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.applied is not None:
            result['Applied'] = self.applied
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Applied') is not None:
            self.applied = m.get('Applied')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteDomainResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteDomainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        model_id: str = None,
        module_id: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.model_id = model_id
        self.module_id = module_id
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteModelResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DeleteModelResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModuleRequest(TeaModel):
    def __init__(
        self,
        module_id: str = None,
        source: str = None,
    ):
        self.module_id = module_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteModuleResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        latest_published_commit: str = None,
        latest_published_version: str = None,
        minimum_platform_version: str = None,
        modified_time: str = None,
        module_id: str = None,
        module_name: str = None,
        owner_app_id: str = None,
        owner_user_id: str = None,
        platform: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.latest_published_commit = latest_published_commit
        self.latest_published_version = latest_published_version
        self.minimum_platform_version = minimum_platform_version
        self.modified_time = modified_time
        self.module_id = module_id
        self.module_name = module_name
        self.owner_app_id = owner_app_id
        self.owner_user_id = owner_user_id
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class DeleteModuleResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteModuleResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteModuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        module_id: str = None,
        resource_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.module_id = module_id
        self.resource_id = resource_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DeleteResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        revision: int = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.revision = revision
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class DeleteResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteResourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAppUserPasswordRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env_id: str = None,
        source: str = None,
        user_name: str = None,
    ):
        self.app_id = app_id
        self.env_id = env_id
        self.source = source
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GenerateAppUserPasswordResponseBodyData(TeaModel):
    def __init__(
        self,
        password: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GenerateAppUserPasswordResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateAppUserPasswordResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GenerateAppUserPasswordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAppUserPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateAppUserPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateAppUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAuthTokenRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        module_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.module_id = module_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GenerateAuthTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
    ):
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class GenerateAuthTokenResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateAuthTokenResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GenerateAuthTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAuthTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateAuthTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadTokenRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        material_id: str = None,
        module_id: str = None,
        source: str = None,
        upload_token_type: str = None,
    ):
        self.app_id = app_id
        self.material_id = material_id
        self.module_id = module_id
        self.source = source
        self.upload_token_type = upload_token_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        if self.upload_token_type is not None:
            result['UploadTokenType'] = self.upload_token_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UploadTokenType') is not None:
            self.upload_token_type = m.get('UploadTokenType')
        return self


class GenerateUploadTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        key: str = None,
        oss_access_key_id: str = None,
        policy: str = None,
        server_url: str = None,
        signature: str = None,
        x_amz_algorithm: str = None,
        x_amz_credential: str = None,
        x_amz_date: str = None,
        x_amz_signature: str = None,
    ):
        self.key = key
        self.oss_access_key_id = oss_access_key_id
        self.policy = policy
        self.server_url = server_url
        self.signature = signature
        self.x_amz_algorithm = x_amz_algorithm
        self.x_amz_credential = x_amz_credential
        self.x_amz_date = x_amz_date
        self.x_amz_signature = x_amz_signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.oss_access_key_id is not None:
            result['OssAccessKeyId'] = self.oss_access_key_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.server_url is not None:
            result['ServerURL'] = self.server_url
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.x_amz_algorithm is not None:
            result['X-Amz-Algorithm'] = self.x_amz_algorithm
        if self.x_amz_credential is not None:
            result['X-Amz-Credential'] = self.x_amz_credential
        if self.x_amz_date is not None:
            result['X-Amz-Date'] = self.x_amz_date
        if self.x_amz_signature is not None:
            result['X-Amz-Signature'] = self.x_amz_signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OssAccessKeyId') is not None:
            self.oss_access_key_id = m.get('OssAccessKeyId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('ServerURL') is not None:
            self.server_url = m.get('ServerURL')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('X-Amz-Algorithm') is not None:
            self.x_amz_algorithm = m.get('X-Amz-Algorithm')
        if m.get('X-Amz-Credential') is not None:
            self.x_amz_credential = m.get('X-Amz-Credential')
        if m.get('X-Amz-Date') is not None:
            self.x_amz_date = m.get('X-Amz-Date')
        if m.get('X-Amz-Signature') is not None:
            self.x_amz_signature = m.get('X-Amz-Signature')
        return self


class GenerateUploadTokenResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateUploadTokenResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GenerateUploadTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateUploadTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateUploadTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateUploadTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetAppResponseBodyDataCategories(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        category_name: str = None,
        parent_category_id: str = None,
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class GetAppResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_status: str = None,
        app_type: str = None,
        categories: List[GetAppResponseBodyDataCategories] = None,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        is_template: bool = None,
        last_edit_time: str = None,
        main_module_id: str = None,
        modified_time: str = None,
        platform_version: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_status = app_status
        self.app_type = app_type
        self.categories = categories
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.is_template = is_template
        self.last_edit_time = last_edit_time
        self.main_module_id = main_module_id
        self.modified_time = modified_time
        self.platform_version = platform_version
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = GetAppResponseBodyDataCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAppResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppModelRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        schema_version: str = None,
        source: str = None,
        sub_type: str = None,
    ):
        self.app_id = app_id
        self.schema_version = schema_version
        self.source = source
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class GetAppModelResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_digest: str = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_digest = model_digest
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class GetAppModelResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAppModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetAppModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppSecretRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetAppSecretResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        return self


class GetAppSecretResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAppSecretResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetAppSecretResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppSecretResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        artifact_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.artifact_id = artifact_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetArtifactResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        artifact_id: str = None,
        artifact_type: str = None,
        available: bool = None,
        create_time: str = None,
        modified_time: str = None,
        url: str = None,
    ):
        self.app_id = app_id
        self.artifact_id = artifact_id
        self.artifact_type = artifact_type
        self.available = available
        self.create_time = create_time
        self.modified_time = modified_time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.available is not None:
            result['Available'] = self.available
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetArtifactResponseBody(TeaModel):
    def __init__(
        self,
        data: GetArtifactResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetArtifactResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArtifactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCommitRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_id: str = None,
        module_id: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.commit_id = commit_id
        self.module_id = module_id
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetCommitResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_digest: str = None,
        commit_id: str = None,
        commit_log: str = None,
        commit_type: str = None,
        create_time: str = None,
        main_module_commit_id: str = None,
        main_module_id: str = None,
        model_data_path: str = None,
        model_digest: Dict[str, str] = None,
        model_pack: List[Any] = None,
        modified_time: str = None,
        module_id: str = None,
        resource_data_path: str = None,
        resource_digest: Dict[str, str] = None,
        resource_pack: List[Dict[str, str]] = None,
        rollback_to_commit_id: str = None,
        rollback_type: str = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.commit_digest = commit_digest
        self.commit_id = commit_id
        self.commit_log = commit_log
        self.commit_type = commit_type
        self.create_time = create_time
        self.main_module_commit_id = main_module_commit_id
        self.main_module_id = main_module_id
        self.model_data_path = model_data_path
        self.model_digest = model_digest
        self.model_pack = model_pack
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_data_path = resource_data_path
        self.resource_digest = resource_digest
        self.resource_pack = resource_pack
        self.rollback_to_commit_id = rollback_to_commit_id
        self.rollback_type = rollback_type
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_digest is not None:
            result['CommitDigest'] = self.commit_digest
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_pack is not None:
            result['ModelPack'] = self.model_pack
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_pack is not None:
            result['ResourcePack'] = self.resource_pack
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitDigest') is not None:
            self.commit_digest = m.get('CommitDigest')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelPack') is not None:
            self.model_pack = m.get('ModelPack')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourcePack') is not None:
            self.resource_pack = m.get('ResourcePack')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class GetCommitResponseBody(TeaModel):
    def __init__(
        self,
        data: GetCommitResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetCommitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCommitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCommitResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultAppUserRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.env_id = env_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetDefaultAppUserResponseBodyData(TeaModel):
    def __init__(
        self,
        has_password: bool = None,
        user_name: str = None,
    ):
        self.has_password = has_password
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetDefaultAppUserResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDefaultAppUserResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDefaultAppUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultAppUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDefaultAppUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDefaultAppUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainCnameRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain: str = None,
        domain_type: str = None,
        env_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.domain = domain
        self.domain_type = domain_type
        self.env_id = env_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetDomainCnameResponseBodyData(TeaModel):
    def __init__(
        self,
        cname: str = None,
    ):
        self.cname = cname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        return self


class GetDomainCnameResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDomainCnameResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDomainCnameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDomainCnameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDomainCnameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDomainCnameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainOverviewRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain: str = None,
        env_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.domain = domain
        self.env_id = env_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetDomainOverviewResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        applied: bool = None,
        certificate: Dict[str, str] = None,
        cname: str = None,
        deleted: bool = None,
        domain: str = None,
        domain_type: str = None,
        env_id: str = None,
        path: str = None,
        with_certificate: bool = None,
    ):
        self.app_id = app_id
        self.applied = applied
        self.certificate = certificate
        self.cname = cname
        self.deleted = deleted
        self.domain = domain
        self.domain_type = domain_type
        self.env_id = env_id
        self.path = path
        self.with_certificate = with_certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.applied is not None:
            result['Applied'] = self.applied
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.path is not None:
            result['Path'] = self.path
        if self.with_certificate is not None:
            result['WithCertificate'] = self.with_certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Applied') is not None:
            self.applied = m.get('Applied')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('WithCertificate') is not None:
            self.with_certificate = m.get('WithCertificate')
        return self


class GetDomainOverviewResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDomainOverviewResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDomainOverviewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDomainOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDomainOverviewResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDomainOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.env_id = env_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetEnvironmentResponseBodyData(TeaModel):
    def __init__(
        self,
        account_ops_endpoint: str = None,
        app_id: str = None,
        create_time: str = None,
        current_publish_id: str = None,
        endpoint: str = None,
        env_id: str = None,
        env_type: str = None,
        modified_time: str = None,
        publishing_id: str = None,
    ):
        self.account_ops_endpoint = account_ops_endpoint
        self.app_id = app_id
        self.create_time = create_time
        self.current_publish_id = current_publish_id
        self.endpoint = endpoint
        self.env_id = env_id
        self.env_type = env_type
        self.modified_time = modified_time
        self.publishing_id = publishing_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ops_endpoint is not None:
            result['AccountOpsEndpoint'] = self.account_ops_endpoint
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_publish_id is not None:
            result['CurrentPublishId'] = self.current_publish_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publishing_id is not None:
            result['PublishingId'] = self.publishing_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountOpsEndpoint') is not None:
            self.account_ops_endpoint = m.get('AccountOpsEndpoint')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentPublishId') is not None:
            self.current_publish_id = m.get('CurrentPublishId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishingId') is not None:
            self.publishing_id = m.get('PublishingId')
        return self


class GetEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        data: GetEnvironmentResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistoryStatsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: str = None,
        source: str = None,
        start_date: str = None,
    ):
        self.app_id = app_id
        self.end_date = end_date
        self.source = source
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.source is not None:
            result['Source'] = self.source
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetHistoryStatsResponseBodyData(TeaModel):
    def __init__(
        self,
        history_pv: Dict[str, str] = None,
        history_uv: Dict[str, str] = None,
    ):
        self.history_pv = history_pv
        self.history_uv = history_uv

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_pv is not None:
            result['HistoryPv'] = self.history_pv
        if self.history_uv is not None:
            result['HistoryUv'] = self.history_uv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoryPv') is not None:
            self.history_pv = m.get('HistoryPv')
        if m.get('HistoryUv') is not None:
            self.history_uv = m.get('HistoryUv')
        return self


class GetHistoryStatsResponseBody(TeaModel):
    def __init__(
        self,
        data: GetHistoryStatsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetHistoryStatsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHistoryStatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHistoryStatsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHistoryStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLatestCommitRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        module_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.module_id = module_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetLatestCommitResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_id: str = None,
        commit_log: str = None,
        commit_type: str = None,
        create_time: str = None,
        main_module_commit_id: str = None,
        main_module_id: str = None,
        model_data_path: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_data_path: str = None,
        resource_digest: Dict[str, str] = None,
        rollback_to_commit_id: str = None,
        rollback_type: str = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.commit_id = commit_id
        self.commit_log = commit_log
        self.commit_type = commit_type
        self.create_time = create_time
        self.main_module_commit_id = main_module_commit_id
        self.main_module_id = main_module_id
        self.model_data_path = model_data_path
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_data_path = resource_data_path
        self.resource_digest = resource_digest
        self.rollback_to_commit_id = rollback_to_commit_id
        self.rollback_type = rollback_type
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class GetLatestCommitResponseBody(TeaModel):
    def __init__(
        self,
        data: GetLatestCommitResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetLatestCommitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLatestCommitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLatestCommitResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLatestCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        model_id: str = None,
        module_id: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.model_id = model_id
        self.module_id = module_id
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetModelResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class GetModelResponseBody(TeaModel):
    def __init__(
        self,
        data: GetModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModuleRequest(TeaModel):
    def __init__(
        self,
        module_id: str = None,
        module_type: str = None,
        source: str = None,
    ):
        self.module_id = module_id
        self.module_type = module_type
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetModuleResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        latest_published_commit: str = None,
        latest_published_version: str = None,
        minimum_platform_version: str = None,
        modified_time: str = None,
        module_id: str = None,
        module_name: str = None,
        owner_app_id: str = None,
        owner_user_id: str = None,
        platform: str = None,
        platform_version: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.latest_published_commit = latest_published_commit
        self.latest_published_version = latest_published_version
        self.minimum_platform_version = minimum_platform_version
        self.modified_time = modified_time
        self.module_id = module_id
        self.module_name = module_name
        self.owner_app_id = owner_app_id
        self.owner_user_id = owner_user_id
        self.platform = platform
        self.platform_version = platform_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        return self


class GetModuleResponseBody(TeaModel):
    def __init__(
        self,
        data: GetModuleResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetModuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublishRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        publish_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.publish_id = publish_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetPublishResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_id: str = None,
        completion_time: str = None,
        create_time: str = None,
        description: str = None,
        env_id: str = None,
        modified_time: str = None,
        publish_id: str = None,
        publish_status: str = None,
        publish_type: str = None,
        reason: str = None,
        start_time: str = None,
        sub_tasks: List[Dict[str, str]] = None,
        version_number: str = None,
    ):
        self.app_id = app_id
        self.commit_id = commit_id
        self.completion_time = completion_time
        self.create_time = create_time
        self.description = description
        self.env_id = env_id
        self.modified_time = modified_time
        self.publish_id = publish_id
        self.publish_status = publish_status
        self.publish_type = publish_type
        self.reason = reason
        self.start_time = start_time
        self.sub_tasks = sub_tasks
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_tasks is not None:
            result['SubTasks'] = self.sub_tasks
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubTasks') is not None:
            self.sub_tasks = m.get('SubTasks')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class GetPublishResponseBody(TeaModel):
    def __init__(
        self,
        data: GetPublishResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetPublishResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPublishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPublishResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRealtimeStatsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetRealtimeStatsResponseBodyData(TeaModel):
    def __init__(
        self,
        today_pv_count: Dict[str, str] = None,
        today_uv_count: Dict[str, str] = None,
        total_pv_count: Dict[str, str] = None,
        total_uv_count: Dict[str, str] = None,
    ):
        self.today_pv_count = today_pv_count
        self.today_uv_count = today_uv_count
        self.total_pv_count = total_pv_count
        self.total_uv_count = total_uv_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.today_pv_count is not None:
            result['TodayPvCount'] = self.today_pv_count
        if self.today_uv_count is not None:
            result['TodayUvCount'] = self.today_uv_count
        if self.total_pv_count is not None:
            result['TotalPvCount'] = self.total_pv_count
        if self.total_uv_count is not None:
            result['TotalUvCount'] = self.total_uv_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TodayPvCount') is not None:
            self.today_pv_count = m.get('TodayPvCount')
        if m.get('TodayUvCount') is not None:
            self.today_uv_count = m.get('TodayUvCount')
        if m.get('TotalPvCount') is not None:
            self.total_pv_count = m.get('TotalPvCount')
        if m.get('TotalUvCount') is not None:
            self.total_uv_count = m.get('TotalUvCount')
        return self


class GetRealtimeStatsResponseBody(TeaModel):
    def __init__(
        self,
        data: GetRealtimeStatsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetRealtimeStatsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRealtimeStatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRealtimeStatsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRealtimeStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        image_process_parameter: str = None,
        module_id: str = None,
        resource_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.image_process_parameter = image_process_parameter
        self.module_id = module_id
        self.resource_id = resource_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.image_process_parameter is not None:
            result['ImageProcessParameter'] = self.image_process_parameter
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ImageProcessParameter') is not None:
            self.image_process_parameter = m.get('ImageProcessParameter')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_digest: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        revision: int = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_digest = resource_digest
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.revision = revision
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class GetResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: GetResourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        source: str = None,
    ):
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetUserResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        platform_version: str = None,
        user_secret: str = None,
        user_status: str = None,
        user_type: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.platform_version = platform_version
        self.user_secret = user_secret
        self.user_status = user_status
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.user_secret is not None:
            result['UserSecret'] = self.user_secret
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('UserSecret') is not None:
            self.user_secret = m.get('UserSecret')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        data: GetUserResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppModulesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        recursive: bool = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.recursive = recursive
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListAppModulesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        commit_id: str = None,
        description: str = None,
        direct_dependency: bool = None,
        icon: str = None,
        minimum_platform_version: str = None,
        module_id: str = None,
        module_name: str = None,
        owner_user_id: str = None,
        platform: str = None,
        version: str = None,
    ):
        self.commit_id = commit_id
        self.description = description
        self.direct_dependency = direct_dependency
        self.icon = icon
        self.minimum_platform_version = minimum_platform_version
        self.module_id = module_id
        self.module_name = module_name
        self.owner_user_id = owner_user_id
        self.platform = platform
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.description is not None:
            result['Description'] = self.description
        if self.direct_dependency is not None:
            result['DirectDependency'] = self.direct_dependency
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectDependency') is not None:
            self.direct_dependency = m.get('DirectDependency')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAppModulesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListAppModulesResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListAppModulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListAppModulesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListAppModulesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListAppModulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppModulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppModulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppTemplatesRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        source: str = None,
        template_type: str = None,
    ):
        self.app_type = app_type
        self.source = source
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.source is not None:
            result['Source'] = self.source
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListAppTemplatesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        category_name: str = None,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        last_edit_time: str = None,
        main_module_id: str = None,
        modified_time: str = None,
        schema_version: str = None,
        source: str = None,
        template_id: str = None,
        template_type: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.category_name = category_name
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.last_edit_time = last_edit_time
        self.main_module_id = main_module_id
        self.modified_time = modified_time
        self.schema_version = schema_version
        self.source = source
        self.template_id = template_id
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListAppTemplatesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListAppTemplatesResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListAppTemplatesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListAppTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListAppTemplatesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListAppTemplatesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_status: str = None,
        app_type: str = None,
        custom_parent_id: str = None,
        description: str = None,
        main_module_id: str = None,
        page_number: int = None,
        page_size: int = None,
        source: str = None,
        template: bool = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_status = app_status
        self.app_type = app_type
        self.custom_parent_id = custom_parent_id
        self.description = description
        self.main_module_id = main_module_id
        self.page_number = page_number
        self.page_size = page_size
        self.source = source
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.custom_parent_id is not None:
            result['CustomParentId'] = self.custom_parent_id
        if self.description is not None:
            result['Description'] = self.description
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CustomParentId') is not None:
            self.custom_parent_id = m.get('CustomParentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class ListAppsResponseBodyDataItemsCategories(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        category_name: str = None,
        parent_category_id: str = None,
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class ListAppsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_status: str = None,
        app_type: str = None,
        categories: List[ListAppsResponseBodyDataItemsCategories] = None,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        is_template: bool = None,
        last_edit_time: str = None,
        main_module_id: str = None,
        modified_time: str = None,
        platform_version: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_status = app_status
        self.app_type = app_type
        self.categories = categories
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.is_template = is_template
        self.last_edit_time = last_edit_time
        self.main_module_id = main_module_id
        self.modified_time = modified_time
        self.platform_version = platform_version
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = ListAppsResponseBodyDataItemsCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListAppsResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListAppsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListAppsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        publish_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.publish_id = publish_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListArtifactsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        artifact_id: str = None,
        artifact_type: str = None,
        available: bool = None,
        create_time: str = None,
        modified_time: str = None,
        url: str = None,
    ):
        self.app_id = app_id
        self.artifact_id = artifact_id
        self.artifact_type = artifact_type
        self.available = available
        self.create_time = create_time
        self.modified_time = modified_time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.available is not None:
            result['Available'] = self.available
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListArtifactsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListArtifactsResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListArtifactsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListArtifactsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListArtifactsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListArtifactsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListArtifactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListArtifactsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListArtifactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommitsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_log: str = None,
        custom_parent_id: str = None,
        module_id: str = None,
        page_number: int = None,
        page_size: int = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.commit_log = commit_log
        self.custom_parent_id = custom_parent_id
        self.module_id = module_id
        self.page_number = page_number
        self.page_size = page_size
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.custom_parent_id is not None:
            result['CustomParentId'] = self.custom_parent_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CustomParentId') is not None:
            self.custom_parent_id = m.get('CustomParentId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListCommitsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_digest: str = None,
        commit_id: str = None,
        commit_log: str = None,
        commit_type: str = None,
        create_time: str = None,
        main_module_commit_id: str = None,
        main_module_id: str = None,
        model_data_path: str = None,
        model_digest: Dict[str, str] = None,
        modified_time: str = None,
        module_id: str = None,
        resource_data_path: str = None,
        resource_digest: Dict[str, str] = None,
        rollback_to_commit_id: str = None,
        rollback_type: str = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.commit_digest = commit_digest
        self.commit_id = commit_id
        self.commit_log = commit_log
        self.commit_type = commit_type
        self.create_time = create_time
        self.main_module_commit_id = main_module_commit_id
        self.main_module_id = main_module_id
        self.model_data_path = model_data_path
        self.model_digest = model_digest
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_data_path = resource_data_path
        self.resource_digest = resource_digest
        self.rollback_to_commit_id = rollback_to_commit_id
        self.rollback_type = rollback_type
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_digest is not None:
            result['CommitDigest'] = self.commit_digest
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.commit_log is not None:
            result['CommitLog'] = self.commit_log
        if self.commit_type is not None:
            result['CommitType'] = self.commit_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.main_module_commit_id is not None:
            result['MainModuleCommitId'] = self.main_module_commit_id
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.rollback_to_commit_id is not None:
            result['RollbackToCommitId'] = self.rollback_to_commit_id
        if self.rollback_type is not None:
            result['RollbackType'] = self.rollback_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitDigest') is not None:
            self.commit_digest = m.get('CommitDigest')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CommitLog') is not None:
            self.commit_log = m.get('CommitLog')
        if m.get('CommitType') is not None:
            self.commit_type = m.get('CommitType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MainModuleCommitId') is not None:
            self.main_module_commit_id = m.get('MainModuleCommitId')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('RollbackToCommitId') is not None:
            self.rollback_to_commit_id = m.get('RollbackToCommitId')
        if m.get('RollbackType') is not None:
            self.rollback_type = m.get('RollbackType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class ListCommitsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListCommitsResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListCommitsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCommitsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListCommitsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListCommitsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCommitsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCommitsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCommitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.env_id = env_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListDomainsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        applied: bool = None,
        checked: bool = None,
        cname: str = None,
        deleted: bool = None,
        domain: str = None,
        domain_type: str = None,
        env_id: str = None,
        path: str = None,
        with_certificate: bool = None,
    ):
        self.app_id = app_id
        self.applied = applied
        self.checked = checked
        self.cname = cname
        self.deleted = deleted
        self.domain = domain
        self.domain_type = domain_type
        self.env_id = env_id
        self.path = path
        self.with_certificate = with_certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.applied is not None:
            result['Applied'] = self.applied
        if self.checked is not None:
            result['Checked'] = self.checked
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.path is not None:
            result['Path'] = self.path
        if self.with_certificate is not None:
            result['WithCertificate'] = self.with_certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Applied') is not None:
            self.applied = m.get('Applied')
        if m.get('Checked') is not None:
            self.checked = m.get('Checked')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('WithCertificate') is not None:
            self.with_certificate = m.get('WithCertificate')
        return self


class ListDomainsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListDomainsResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListDomainsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListDomainsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListDomainsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListDomainsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDomainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentOverviewsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListEnvironmentOverviewsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        config: Dict[str, str] = None,
        create_time: str = None,
        current_publish: Dict[str, str] = None,
        endpoint: str = None,
        env_id: str = None,
        env_status: str = None,
        env_type: str = None,
        latest_app_access_time: str = None,
        modified_time: str = None,
        ops_record: Dict[str, str] = None,
        publishing: Dict[str, str] = None,
    ):
        self.app_id = app_id
        self.config = config
        self.create_time = create_time
        self.current_publish = current_publish
        self.endpoint = endpoint
        self.env_id = env_id
        self.env_status = env_status
        self.env_type = env_type
        self.latest_app_access_time = latest_app_access_time
        self.modified_time = modified_time
        self.ops_record = ops_record
        self.publishing = publishing

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.config is not None:
            result['Config'] = self.config
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_publish is not None:
            result['CurrentPublish'] = self.current_publish
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_status is not None:
            result['EnvStatus'] = self.env_status
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.latest_app_access_time is not None:
            result['LatestAppAccessTime'] = self.latest_app_access_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.ops_record is not None:
            result['OpsRecord'] = self.ops_record
        if self.publishing is not None:
            result['Publishing'] = self.publishing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentPublish') is not None:
            self.current_publish = m.get('CurrentPublish')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvStatus') is not None:
            self.env_status = m.get('EnvStatus')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('LatestAppAccessTime') is not None:
            self.latest_app_access_time = m.get('LatestAppAccessTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OpsRecord') is not None:
            self.ops_record = m.get('OpsRecord')
        if m.get('Publishing') is not None:
            self.publishing = m.get('Publishing')
        return self


class ListEnvironmentOverviewsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListEnvironmentOverviewsResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListEnvironmentOverviewsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListEnvironmentOverviewsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListEnvironmentOverviewsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListEnvironmentOverviewsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEnvironmentOverviewsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnvironmentOverviewsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnvironmentOverviewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env_type: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.env_type = env_type
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListEnvironmentsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        account_ops_endpoint: str = None,
        app_id: str = None,
        create_time: str = None,
        current_publish_id: str = None,
        endpoint: str = None,
        env_id: str = None,
        env_type: str = None,
        modified_time: str = None,
        publishing_id: str = None,
    ):
        self.account_ops_endpoint = account_ops_endpoint
        self.app_id = app_id
        self.create_time = create_time
        self.current_publish_id = current_publish_id
        self.endpoint = endpoint
        self.env_id = env_id
        self.env_type = env_type
        self.modified_time = modified_time
        self.publishing_id = publishing_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ops_endpoint is not None:
            result['AccountOpsEndpoint'] = self.account_ops_endpoint
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_publish_id is not None:
            result['CurrentPublishId'] = self.current_publish_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publishing_id is not None:
            result['PublishingId'] = self.publishing_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountOpsEndpoint') is not None:
            self.account_ops_endpoint = m.get('AccountOpsEndpoint')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentPublishId') is not None:
            self.current_publish_id = m.get('CurrentPublishId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishingId') is not None:
            self.publishing_id = m.get('PublishingId')
        return self


class ListEnvironmentsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListEnvironmentsResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListEnvironmentsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListEnvironmentsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListEnvironmentsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnvironmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        model_id: str = None,
        model_name: str = None,
        model_type: str = None,
        module_id: str = None,
        schema_version: str = None,
        source: str = None,
        sub_type: str = None,
        with_content: bool = None,
    ):
        self.app_id = app_id
        self.model_id = model_id
        self.model_name = model_name
        self.model_type = model_type
        self.module_id = module_id
        self.schema_version = schema_version
        self.source = source
        self.sub_type = sub_type
        self.with_content = with_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListModelsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_digest: str = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_digest = model_digest
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class ListModelsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListModelsResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModelsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListModelsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListModelsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListModelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelsByPageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        model_name: str = None,
        model_type: str = None,
        module_id: str = None,
        page_number: int = None,
        page_size: int = None,
        schema_version: str = None,
        source: str = None,
        sub_type: str = None,
        with_content: bool = None,
    ):
        self.app_id = app_id
        self.model_name = model_name
        self.model_type = model_type
        self.module_id = module_id
        self.page_number = page_number
        self.page_size = page_size
        self.schema_version = schema_version
        self.source = source
        self.sub_type = sub_type
        self.with_content = with_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListModelsByPageResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class ListModelsByPageResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListModelsByPageResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModelsByPageResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListModelsByPageResponseBody(TeaModel):
    def __init__(
        self,
        data: ListModelsByPageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListModelsByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModelsByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModelsByPageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModelsByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModuleDependenciesRequest(TeaModel):
    def __init__(
        self,
        module_id: str = None,
        recursive: bool = None,
        source: str = None,
    ):
        self.module_id = module_id
        self.recursive = recursive
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListModuleDependenciesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        commit_id: str = None,
        description: str = None,
        direct_dependency: bool = None,
        icon: str = None,
        minimum_platform_version: str = None,
        module_id: str = None,
        module_name: str = None,
        origin: str = None,
        owner_user_id: str = None,
        platform: str = None,
        version: str = None,
    ):
        self.commit_id = commit_id
        self.description = description
        self.direct_dependency = direct_dependency
        self.icon = icon
        self.minimum_platform_version = minimum_platform_version
        self.module_id = module_id
        self.module_name = module_name
        self.origin = origin
        self.owner_user_id = owner_user_id
        self.platform = platform
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.description is not None:
            result['Description'] = self.description
        if self.direct_dependency is not None:
            result['DirectDependency'] = self.direct_dependency
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectDependency') is not None:
            self.direct_dependency = m.get('DirectDependency')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListModuleDependenciesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListModuleDependenciesResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModuleDependenciesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListModuleDependenciesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListModuleDependenciesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListModuleDependenciesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModuleDependenciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModuleDependenciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModuleDependenciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModuleModelsRequest(TeaModel):
    def __init__(
        self,
        module_list: str = None,
        source: str = None,
        sub_types: str = None,
        with_content: bool = None,
    ):
        self.module_list = module_list
        self.source = source
        self.sub_types = sub_types
        self.with_content = with_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_list is not None:
            result['ModuleList'] = self.module_list
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_types is not None:
            result['SubTypes'] = self.sub_types
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleList') is not None:
            self.module_list = m.get('ModuleList')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubTypes') is not None:
            self.sub_types = m.get('SubTypes')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListModuleModelsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        commit_id: str = None,
        model_data: Dict[str, List[DataItemsModelDataValue]] = None,
        model_data_path: Dict[str, str] = None,
        model_digest: Dict[str, str] = None,
        module_id: str = None,
        resource_data: Dict[str, str] = None,
        resource_data_path: Dict[str, str] = None,
    ):
        self.commit_id = commit_id
        self.model_data = model_data
        self.model_data_path = model_data_path
        self.model_digest = model_digest
        self.module_id = module_id
        self.resource_data = resource_data
        self.resource_data_path = resource_data_path

    def validate(self):
        if self.model_data:
            for v in self.model_data.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        result['ModelData'] = {}
        if self.model_data is not None:
            for k, v in self.model_data.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['ModelData'][k] = l1
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_data is not None:
            result['ResourceData'] = self.resource_data
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        self.model_data = {}
        if m.get('ModelData') is not None:
            for k, v in m.get('ModelData').items():
                l1 = []
                for k1 in v:
                    temp_model = DataItemsModelDataValue()
                    l1.append(temp_model.from_map(k1))
                self.model_data['k'] = l1
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceData') is not None:
            self.resource_data = m.get('ResourceData')
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        return self


class ListModuleModelsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListModuleModelsResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModuleModelsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListModuleModelsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListModuleModelsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListModuleModelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModuleModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModuleModelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModuleModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModulePublishVersionsRequest(TeaModel):
    def __init__(
        self,
        custom_parent_id: str = None,
        module_id: str = None,
        module_version: str = None,
        page_number: int = None,
        page_size: int = None,
        source: str = None,
    ):
        self.custom_parent_id = custom_parent_id
        self.module_id = module_id
        self.module_version = module_version
        self.page_number = page_number
        self.page_size = page_size
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_parent_id is not None:
            result['CustomParentId'] = self.custom_parent_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_version is not None:
            result['ModuleVersion'] = self.module_version
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomParentId') is not None:
            self.custom_parent_id = m.get('CustomParentId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleVersion') is not None:
            self.module_version = m.get('ModuleVersion')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListModulePublishVersionsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        commit_id: str = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        module_id: str = None,
        platform_version: str = None,
        publish_id: str = None,
        version: str = None,
    ):
        self.commit_id = commit_id
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.module_id = module_id
        self.platform_version = platform_version
        self.publish_id = publish_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListModulePublishVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListModulePublishVersionsResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModulePublishVersionsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListModulePublishVersionsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListModulePublishVersionsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListModulePublishVersionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModulePublishVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModulePublishVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModulePublishVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModuleResourcesRequest(TeaModel):
    def __init__(
        self,
        module_list: str = None,
        source: str = None,
        types: str = None,
        with_content: bool = None,
    ):
        self.module_list = module_list
        self.source = source
        self.types = types
        self.with_content = with_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_list is not None:
            result['ModuleList'] = self.module_list
        if self.source is not None:
            result['Source'] = self.source
        if self.types is not None:
            result['Types'] = self.types
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleList') is not None:
            self.module_list = m.get('ModuleList')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListModuleResourcesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        commit_id: str = None,
        model_data: Dict[str, str] = None,
        model_data_path: Dict[str, str] = None,
        module_id: str = None,
        resource_data: Dict[str, List[DataItemsResourceDataValue]] = None,
        resource_data_path: Dict[str, str] = None,
    ):
        self.commit_id = commit_id
        self.model_data = model_data
        self.model_data_path = model_data_path
        self.module_id = module_id
        self.resource_data = resource_data
        self.resource_data_path = resource_data_path

    def validate(self):
        if self.resource_data:
            for v in self.resource_data.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.model_data is not None:
            result['ModelData'] = self.model_data
        if self.model_data_path is not None:
            result['ModelDataPath'] = self.model_data_path
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        result['ResourceData'] = {}
        if self.resource_data is not None:
            for k, v in self.resource_data.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['ResourceData'][k] = l1
        if self.resource_data_path is not None:
            result['ResourceDataPath'] = self.resource_data_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('ModelData') is not None:
            self.model_data = m.get('ModelData')
        if m.get('ModelDataPath') is not None:
            self.model_data_path = m.get('ModelDataPath')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        self.resource_data = {}
        if m.get('ResourceData') is not None:
            for k, v in m.get('ResourceData').items():
                l1 = []
                for k1 in v:
                    temp_model = DataItemsResourceDataValue()
                    l1.append(temp_model.from_map(k1))
                self.resource_data['k'] = l1
        if m.get('ResourceDataPath') is not None:
            self.resource_data_path = m.get('ResourceDataPath')
        return self


class ListModuleResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListModuleResourcesResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModuleResourcesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListModuleResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListModuleResourcesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListModuleResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModuleResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModuleResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModuleResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModulesRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        has_owner_app: bool = None,
        module_id: str = None,
        module_name: str = None,
        platform: str = None,
        source: str = None,
    ):
        self.description = description
        self.has_owner_app = has_owner_app
        self.module_id = module_id
        self.module_name = module_name
        self.platform = platform
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.has_owner_app is not None:
            result['HasOwnerApp'] = self.has_owner_app
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasOwnerApp') is not None:
            self.has_owner_app = m.get('HasOwnerApp')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListModulesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        latest_published_commit: str = None,
        latest_published_version: str = None,
        minimum_platform_version: str = None,
        modified_time: str = None,
        module_id: str = None,
        module_name: str = None,
        owner_app_id: str = None,
        owner_user_id: str = None,
        platform: str = None,
        platform_version: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.latest_published_commit = latest_published_commit
        self.latest_published_version = latest_published_version
        self.minimum_platform_version = minimum_platform_version
        self.modified_time = modified_time
        self.module_id = module_id
        self.module_name = module_name
        self.owner_app_id = owner_app_id
        self.owner_user_id = owner_user_id
        self.platform = platform
        self.platform_version = platform_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        return self


class ListModulesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListModulesResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListModulesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListModulesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListModulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModulesByPageRequest(TeaModel):
    def __init__(
        self,
        custom_parent_id: str = None,
        description: str = None,
        has_owner_app: bool = None,
        module_id: str = None,
        module_name: str = None,
        module_type: str = None,
        page_number: int = None,
        page_size: int = None,
        platform: str = None,
        source: str = None,
    ):
        self.custom_parent_id = custom_parent_id
        self.description = description
        self.has_owner_app = has_owner_app
        self.module_id = module_id
        self.module_name = module_name
        self.module_type = module_type
        self.page_number = page_number
        self.page_size = page_size
        self.platform = platform
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_parent_id is not None:
            result['CustomParentId'] = self.custom_parent_id
        if self.description is not None:
            result['Description'] = self.description
        if self.has_owner_app is not None:
            result['HasOwnerApp'] = self.has_owner_app
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomParentId') is not None:
            self.custom_parent_id = m.get('CustomParentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasOwnerApp') is not None:
            self.has_owner_app = m.get('HasOwnerApp')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListModulesByPageResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        latest_published_commit: str = None,
        latest_published_version: str = None,
        minimum_platform_version: str = None,
        modified_time: str = None,
        module_id: str = None,
        module_name: str = None,
        module_type: str = None,
        owner_app_id: str = None,
        owner_user_id: str = None,
        platform: str = None,
        platform_version: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.latest_published_commit = latest_published_commit
        self.latest_published_version = latest_published_version
        self.minimum_platform_version = minimum_platform_version
        self.modified_time = modified_time
        self.module_id = module_id
        self.module_name = module_name
        self.module_type = module_type
        self.owner_app_id = owner_app_id
        self.owner_user_id = owner_user_id
        self.platform = platform
        self.platform_version = platform_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        return self


class ListModulesByPageResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListModulesByPageResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListModulesByPageResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListModulesByPageResponseBody(TeaModel):
    def __init__(
        self,
        data: ListModulesByPageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListModulesByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListModulesByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModulesByPageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModulesByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishVersionsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env_id: str = None,
        page_number: int = None,
        page_size: int = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.env_id = env_id
        self.page_number = page_number
        self.page_size = page_size
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListPublishVersionsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_id: str = None,
        completion_time: str = None,
        create_time: str = None,
        description: str = None,
        env_id: str = None,
        modified_time: str = None,
        publish_id: str = None,
        publish_status: str = None,
        publish_type: str = None,
        reason: str = None,
        start_time: str = None,
        sub_tasks: List[Dict[str, str]] = None,
        version_number: str = None,
    ):
        self.app_id = app_id
        self.commit_id = commit_id
        self.completion_time = completion_time
        self.create_time = create_time
        self.description = description
        self.env_id = env_id
        self.modified_time = modified_time
        self.publish_id = publish_id
        self.publish_status = publish_status
        self.publish_type = publish_type
        self.reason = reason
        self.start_time = start_time
        self.sub_tasks = sub_tasks
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_tasks is not None:
            result['SubTasks'] = self.sub_tasks
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubTasks') is not None:
            self.sub_tasks = m.get('SubTasks')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class ListPublishVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListPublishVersionsResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListPublishVersionsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublishVersionsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListPublishVersionsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListPublishVersionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPublishVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPublishVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPublishVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishedModulesRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        exclude_app_id: str = None,
        exclude_module_id: str = None,
        has_owner_app: bool = None,
        module_id: str = None,
        module_name: str = None,
        module_type: str = None,
        page_number: int = None,
        page_size: int = None,
        platform: str = None,
        source: str = None,
    ):
        self.description = description
        self.exclude_app_id = exclude_app_id
        self.exclude_module_id = exclude_module_id
        self.has_owner_app = has_owner_app
        self.module_id = module_id
        self.module_name = module_name
        self.module_type = module_type
        self.page_number = page_number
        self.page_size = page_size
        self.platform = platform
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_app_id is not None:
            result['ExcludeAppId'] = self.exclude_app_id
        if self.exclude_module_id is not None:
            result['ExcludeModuleId'] = self.exclude_module_id
        if self.has_owner_app is not None:
            result['HasOwnerApp'] = self.has_owner_app
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeAppId') is not None:
            self.exclude_app_id = m.get('ExcludeAppId')
        if m.get('ExcludeModuleId') is not None:
            self.exclude_module_id = m.get('ExcludeModuleId')
        if m.get('HasOwnerApp') is not None:
            self.has_owner_app = m.get('HasOwnerApp')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListPublishedModulesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        latest_published_commit: str = None,
        latest_published_version: str = None,
        minimum_platform_version: str = None,
        modified_time: str = None,
        module_id: str = None,
        module_name: str = None,
        module_type: str = None,
        owner_app_id: str = None,
        owner_user_id: str = None,
        platform: str = None,
        platform_version: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.latest_published_commit = latest_published_commit
        self.latest_published_version = latest_published_version
        self.minimum_platform_version = minimum_platform_version
        self.modified_time = modified_time
        self.module_id = module_id
        self.module_name = module_name
        self.module_type = module_type
        self.owner_app_id = owner_app_id
        self.owner_user_id = owner_user_id
        self.platform = platform
        self.platform_version = platform_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        return self


class ListPublishedModulesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListPublishedModulesResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListPublishedModulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublishedModulesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListPublishedModulesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListPublishedModulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPublishedModulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPublishedModulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPublishedModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env_id: str = None,
        page_number: int = None,
        page_size: int = None,
        publish_status: str = None,
        publish_type: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.env_id = env_id
        self.page_number = page_number
        self.page_size = page_size
        self.publish_status = publish_status
        self.publish_type = publish_type
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListPublishesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_id: str = None,
        completion_time: str = None,
        create_time: str = None,
        description: str = None,
        env_id: str = None,
        modified_time: str = None,
        publish_id: str = None,
        publish_status: str = None,
        publish_type: str = None,
        reason: str = None,
        start_time: str = None,
        version_number: str = None,
    ):
        self.app_id = app_id
        self.commit_id = commit_id
        self.completion_time = completion_time
        self.create_time = create_time
        self.description = description
        self.env_id = env_id
        self.modified_time = modified_time
        self.publish_id = publish_id
        self.publish_status = publish_status
        self.publish_type = publish_type
        self.reason = reason
        self.start_time = start_time
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.publish_id is not None:
            result['PublishId'] = self.publish_id
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PublishId') is not None:
            self.publish_id = m.get('PublishId')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class ListPublishesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListPublishesResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListPublishesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublishesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListPublishesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListPublishesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPublishesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPublishesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPublishesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        description: str = None,
        image_process_parameter: str = None,
        module_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        source: str = None,
        with_content: bool = None,
    ):
        self.app_id = app_id
        self.description = description
        self.image_process_parameter = image_process_parameter
        self.module_id = module_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.source = source
        self.with_content = with_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.image_process_parameter is not None:
            result['ImageProcessParameter'] = self.image_process_parameter
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source is not None:
            result['Source'] = self.source
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageProcessParameter') is not None:
            self.image_process_parameter = m.get('ImageProcessParameter')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListResourcesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: Any = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_digest: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        revision: int = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_digest = resource_digest
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.revision = revision
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class ListResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListResourcesResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListResourcesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListResourcesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesByPageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        description: str = None,
        image_process_parameter: str = None,
        module_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        source: str = None,
        with_content: bool = None,
    ):
        self.app_id = app_id
        self.description = description
        self.image_process_parameter = image_process_parameter
        self.module_id = module_id
        self.page_number = page_number
        self.page_size = page_size
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.source = source
        self.with_content = with_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.image_process_parameter is not None:
            result['ImageProcessParameter'] = self.image_process_parameter
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source is not None:
            result['Source'] = self.source
        if self.with_content is not None:
            result['WithContent'] = self.with_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageProcessParameter') is not None:
            self.image_process_parameter = m.get('ImageProcessParameter')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WithContent') is not None:
            self.with_content = m.get('WithContent')
        return self


class ListResourcesByPageResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_digest: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        revision: int = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_digest = resource_digest
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.revision = revision
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class ListResourcesByPageResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListResourcesByPageResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListResourcesByPageResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourcesByPageResponseBody(TeaModel):
    def __init__(
        self,
        data: ListResourcesByPageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListResourcesByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListResourcesByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcesByPageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourcesByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAppUserPasswordRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env_id: str = None,
        source: str = None,
        user_name: str = None,
    ):
        self.app_id = app_id
        self.env_id = env_id
        self.source = source
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ResetAppUserPasswordResponseBodyData(TeaModel):
    def __init__(
        self,
        password: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ResetAppUserPasswordResponseBody(TeaModel):
    def __init__(
        self,
        data: ResetAppUserPasswordResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ResetAppUserPasswordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetAppUserPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAppUserPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetAppUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreModelRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        model_id: str = None,
        module_id: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.model_id = model_id
        self.module_id = module_id
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class RestoreModelResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class RestoreModelResponseBody(TeaModel):
    def __init__(
        self,
        data: RestoreModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RestoreModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestoreModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestoreModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestoreModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunLogicModelRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        commit_id: str = None,
        content: str = None,
        encode_type: str = None,
        module_id: str = None,
        parameters: str = None,
        schema_version: str = None,
        source: str = None,
        sub_type: str = None,
    ):
        self.app_id = app_id
        self.commit_id = commit_id
        self.content = content
        self.encode_type = encode_type
        self.module_id = module_id
        self.parameters = parameters
        self.schema_version = schema_version
        self.source = source
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.content is not None:
            result['Content'] = self.content
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class RunLogicModelResponseBodyData(TeaModel):
    def __init__(
        self,
        body: str = None,
        headers: Dict[str, str] = None,
        status: int = None,
    ):
        self.body = body
        self.headers = headers
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class RunLogicModelResponseBody(TeaModel):
    def __init__(
        self,
        data: RunLogicModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RunLogicModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunLogicModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunLogicModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunLogicModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetEnvironmentDefaultDomainRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        domain: str = None,
        domain_type: str = None,
        env_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.domain = domain
        self.domain_type = domain_type
        self.env_id = env_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class SetEnvironmentDefaultDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        config_changed: bool = None,
        default_master_domain: str = None,
        default_static_domain: str = None,
        master_domain: str = None,
        master_domain_applied: bool = None,
        static_domain: str = None,
        static_domain_applied: bool = None,
    ):
        self.config_changed = config_changed
        self.default_master_domain = default_master_domain
        self.default_static_domain = default_static_domain
        self.master_domain = master_domain
        self.master_domain_applied = master_domain_applied
        self.static_domain = static_domain
        self.static_domain_applied = static_domain_applied

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_changed is not None:
            result['ConfigChanged'] = self.config_changed
        if self.default_master_domain is not None:
            result['DefaultMasterDomain'] = self.default_master_domain
        if self.default_static_domain is not None:
            result['DefaultStaticDomain'] = self.default_static_domain
        if self.master_domain is not None:
            result['MasterDomain'] = self.master_domain
        if self.master_domain_applied is not None:
            result['MasterDomainApplied'] = self.master_domain_applied
        if self.static_domain is not None:
            result['StaticDomain'] = self.static_domain
        if self.static_domain_applied is not None:
            result['StaticDomainApplied'] = self.static_domain_applied
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigChanged') is not None:
            self.config_changed = m.get('ConfigChanged')
        if m.get('DefaultMasterDomain') is not None:
            self.default_master_domain = m.get('DefaultMasterDomain')
        if m.get('DefaultStaticDomain') is not None:
            self.default_static_domain = m.get('DefaultStaticDomain')
        if m.get('MasterDomain') is not None:
            self.master_domain = m.get('MasterDomain')
        if m.get('MasterDomainApplied') is not None:
            self.master_domain_applied = m.get('MasterDomainApplied')
        if m.get('StaticDomain') is not None:
            self.static_domain = m.get('StaticDomain')
        if m.get('StaticDomainApplied') is not None:
            self.static_domain_applied = m.get('StaticDomainApplied')
        return self


class SetEnvironmentDefaultDomainResponseBody(TeaModel):
    def __init__(
        self,
        data: SetEnvironmentDefaultDomainResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SetEnvironmentDefaultDomainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetEnvironmentDefaultDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetEnvironmentDefaultDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetEnvironmentDefaultDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAppServerRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.env_id = env_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class StartAppServerResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_server_status: str = None,
        env_id: str = None,
    ):
        self.app_id = app_id
        self.app_server_status = app_server_status
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_server_status is not None:
            result['AppServerStatus'] = self.app_server_status
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppServerStatus') is not None:
            self.app_server_status = m.get('AppServerStatus')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class StartAppServerResponseBody(TeaModel):
    def __init__(
        self,
        data: StartAppServerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StartAppServerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartAppServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartAppServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartAppServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAppServerRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        env_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.env_id = env_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class StopAppServerResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_server_status: str = None,
        env_id: str = None,
    ):
        self.app_id = app_id
        self.app_server_status = app_server_status
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_server_status is not None:
            result['AppServerStatus'] = self.app_server_status
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppServerStatus') is not None:
            self.app_server_status = m.get('AppServerStatus')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class StopAppServerResponseBody(TeaModel):
    def __init__(
        self,
        data: StopAppServerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StopAppServerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAppServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopAppServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopAppServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        description: str = None,
        icon: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.description = description
        self.icon = icon
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateAppResponseBodyDataCategories(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        category_name: str = None,
        parent_category_id: str = None,
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class UpdateAppResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_status: str = None,
        app_type: str = None,
        categories: List[UpdateAppResponseBodyDataCategories] = None,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        is_template: bool = None,
        last_edit_time: str = None,
        main_module_id: str = None,
        modified_time: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_status = app_status
        self.app_type = app_type
        self.categories = categories
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.is_template = is_template
        self.last_edit_time = last_edit_time
        self.main_module_id = main_module_id
        self.modified_time = modified_time
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time
        if self.main_module_id is not None:
            result['MainModuleId'] = self.main_module_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = UpdateAppResponseBodyDataCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')
        if m.get('MainModuleId') is not None:
            self.main_module_id = m.get('MainModuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateAppResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateAppResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppModelRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: str = None,
        encode_type: str = None,
        schema_version: str = None,
        source: str = None,
        sub_type: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.encode_type = encode_type
        self.schema_version = schema_version
        self.source = source
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class UpdateAppModelResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_digest: str = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_digest = model_digest
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class UpdateAppModelResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateAppModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateAppModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAppModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModelRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: str = None,
        description: str = None,
        encode_type: str = None,
        model_id: str = None,
        model_name: str = None,
        module_id: str = None,
        schema_version: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.description = description
        self.encode_type = encode_type
        self.model_id = model_id
        self.model_name = model_name
        self.module_id = module_id
        self.schema_version = schema_version
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateModelResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        attributes: List[Dict[str, str]] = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        id: str = None,
        link_model_id: str = None,
        link_module_id: str = None,
        linked: bool = None,
        model_digest: str = None,
        model_id: str = None,
        model_name: str = None,
        model_status: str = None,
        model_type: str = None,
        modified_time: str = None,
        module_id: str = None,
        props: Dict[str, str] = None,
        revision: int = None,
        schema_version: str = None,
        sub_type: str = None,
        visibility: str = None,
    ):
        self.app_id = app_id
        self.attributes = attributes
        self.content = content
        self.create_time = create_time
        self.description = description
        self.id = id
        self.link_model_id = link_model_id
        self.link_module_id = link_module_id
        self.linked = linked
        self.model_digest = model_digest
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.model_type = model_type
        self.modified_time = modified_time
        self.module_id = module_id
        self.props = props
        self.revision = revision
        self.schema_version = schema_version
        self.sub_type = sub_type
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.link_model_id is not None:
            result['LinkModelId'] = self.link_model_id
        if self.link_module_id is not None:
            result['LinkModuleId'] = self.link_module_id
        if self.linked is not None:
            result['Linked'] = self.linked
        if self.model_digest is not None:
            result['ModelDigest'] = self.model_digest
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.props is not None:
            result['Props'] = self.props
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LinkModelId') is not None:
            self.link_model_id = m.get('LinkModelId')
        if m.get('LinkModuleId') is not None:
            self.link_module_id = m.get('LinkModuleId')
        if m.get('Linked') is not None:
            self.linked = m.get('Linked')
        if m.get('ModelDigest') is not None:
            self.model_digest = m.get('ModelDigest')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class UpdateModelResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModuleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        module_id: str = None,
        module_name: str = None,
        source: str = None,
    ):
        self.description = description
        self.module_id = module_id
        self.module_name = module_name
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateModuleResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        latest_published_commit: str = None,
        latest_published_version: str = None,
        minimum_platform_version: str = None,
        modified_time: str = None,
        module_id: str = None,
        module_name: str = None,
        owner_app_id: str = None,
        owner_user_id: str = None,
        platform: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.icon = icon
        self.latest_published_commit = latest_published_commit
        self.latest_published_version = latest_published_version
        self.minimum_platform_version = minimum_platform_version
        self.modified_time = modified_time
        self.module_id = module_id
        self.module_name = module_name
        self.owner_app_id = owner_app_id
        self.owner_user_id = owner_user_id
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.latest_published_commit is not None:
            result['LatestPublishedCommit'] = self.latest_published_commit
        if self.latest_published_version is not None:
            result['LatestPublishedVersion'] = self.latest_published_version
        if self.minimum_platform_version is not None:
            result['MinimumPlatformVersion'] = self.minimum_platform_version
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.owner_app_id is not None:
            result['OwnerAppId'] = self.owner_app_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LatestPublishedCommit') is not None:
            self.latest_published_commit = m.get('LatestPublishedCommit')
        if m.get('LatestPublishedVersion') is not None:
            self.latest_published_version = m.get('LatestPublishedVersion')
        if m.get('MinimumPlatformVersion') is not None:
            self.minimum_platform_version = m.get('MinimumPlatformVersion')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('OwnerAppId') is not None:
            self.owner_app_id = m.get('OwnerAppId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class UpdateModuleResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateModuleResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateModuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: str = None,
        description: str = None,
        module_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.description = description
        self.module_id = module_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_digest: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        revision: int = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_digest = resource_digest
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.revision = revision
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_digest is not None:
            result['ResourceDigest'] = self.resource_digest
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceDigest') is not None:
            self.resource_digest = m.get('ResourceDigest')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class UpdateResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateResourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceContentRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: str = None,
        module_id: str = None,
        resource_id: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.module_id = module_id
        self.resource_id = resource_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateResourceContentResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        revision: int = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.revision = revision
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class UpdateResourceContentResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateResourceContentResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateResourceContentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateResourceContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceContentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceInfoRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        description: str = None,
        module_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        source: str = None,
    ):
        self.app_id = app_id
        self.description = description
        self.module_id = module_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateResourceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: Dict[str, str] = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
        module_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        revision: int = None,
        schema_version: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.module_id = module_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.revision = revision
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        return self


class UpdateResourceInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateResourceInfoResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateResourceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateResourceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


