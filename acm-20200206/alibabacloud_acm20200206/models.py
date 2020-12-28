# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class BatchExportConfigurationsRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
        data: str = None,
    ):
        self.namespace_id = namespace_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class BatchExportConfigurationsResponseBody(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.file_url = file_url
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class BatchExportConfigurationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchExportConfigurationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchExportConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchImportConfigurationsRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
        policy: str = None,
        file_url: str = None,
    ):
        self.namespace_id = namespace_id
        self.policy = policy
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class BatchImportConfigurationsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class BatchImportConfigurationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchImportConfigurationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchImportConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckConfigurationCloneRequest(TeaModel):
    def __init__(
        self,
        policy: str = None,
        namespace_from: str = None,
        namespace_to: str = None,
        data: str = None,
    ):
        self.policy = policy
        self.namespace_from = namespace_from
        self.namespace_to = namespace_to
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.namespace_from is not None:
            result['NamespaceFrom'] = self.namespace_from
        if self.namespace_to is not None:
            result['NamespaceTo'] = self.namespace_to
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('NamespaceFrom') is not None:
            self.namespace_from = m.get('NamespaceFrom')
        if m.get('NamespaceTo') is not None:
            self.namespace_to = m.get('NamespaceTo')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CheckConfigurationCloneResponseBodyResultSuccessItems(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
    ):
        self.data_id = data_id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class CheckConfigurationCloneResponseBodyResult(TeaModel):
    def __init__(
        self,
        success: bool = None,
        success_items: List[CheckConfigurationCloneResponseBodyResultSuccessItems] = None,
        total_count: int = None,
    ):
        self.success = success
        self.success_items = success_items
        self.total_count = total_count

    def validate(self):
        if self.success_items:
            for k in self.success_items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        result['SuccessItems'] = []
        if self.success_items is not None:
            for k in self.success_items:
                result['SuccessItems'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.success_items = []
        if m.get('SuccessItems') is not None:
            for k in m.get('SuccessItems'):
                temp_model = CheckConfigurationCloneResponseBodyResultSuccessItems()
                self.success_items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CheckConfigurationCloneResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: CheckConfigurationCloneResponseBodyResult = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Result') is not None:
            temp_model = CheckConfigurationCloneResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckConfigurationCloneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckConfigurationCloneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckConfigurationCloneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckConfigurationExportRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
        data: str = None,
    ):
        self.namespace_id = namespace_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CheckConfigurationExportResponseBodyResult(TeaModel):
    def __init__(
        self,
        total_count: int = None,
    ):
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CheckConfigurationExportResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: CheckConfigurationExportResponseBodyResult = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Result') is not None:
            temp_model = CheckConfigurationExportResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckConfigurationExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckConfigurationExportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckConfigurationExportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneConfigurationRequest(TeaModel):
    def __init__(
        self,
        policy: str = None,
        namespace_from: str = None,
        namespace_to: str = None,
        data: str = None,
    ):
        self.policy = policy
        self.namespace_from = namespace_from
        self.namespace_to = namespace_to
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.namespace_from is not None:
            result['NamespaceFrom'] = self.namespace_from
        if self.namespace_to is not None:
            result['NamespaceTo'] = self.namespace_to
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('NamespaceFrom') is not None:
            self.namespace_from = m.get('NamespaceFrom')
        if m.get('NamespaceTo') is not None:
            self.namespace_to = m.get('NamespaceTo')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CloneConfigurationResponseBodyResultSuccessItems(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
    ):
        self.data_id = data_id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class CloneConfigurationResponseBodyResult(TeaModel):
    def __init__(
        self,
        success: bool = None,
        success_items: List[CloneConfigurationResponseBodyResultSuccessItems] = None,
        total_count: int = None,
    ):
        self.success = success
        self.success_items = success_items
        self.total_count = total_count

    def validate(self):
        if self.success_items:
            for k in self.success_items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        result['SuccessItems'] = []
        if self.success_items is not None:
            for k in self.success_items:
                result['SuccessItems'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.success_items = []
        if m.get('SuccessItems') is not None:
            for k in m.get('SuccessItems'):
                temp_model = CloneConfigurationResponseBodyResultSuccessItems()
                self.success_items.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CloneConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: CloneConfigurationResponseBodyResult = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Result') is not None:
            temp_model = CloneConfigurationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CloneConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloneConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloneConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigurationRequest(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        app_name: str = None,
        group: str = None,
        desc: str = None,
        tags: str = None,
        content: str = None,
        type: str = None,
        namespace_id: str = None,
    ):
        self.data_id = data_id
        self.app_name = app_name
        self.group = group
        self.desc = desc
        self.tags = tags
        self.content = content
        self.type = type
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.group is not None:
            result['Group'] = self.group
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.content is not None:
            result['Content'] = self.content
        if self.type is not None:
            result['Type'] = self.type
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class CreateConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        namespace_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.namespace_id = namespace_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConfigurationRequest(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
        namespace_id: str = None,
    ):
        self.data_id = data_id
        self.group = group
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNamespaceRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
    ):
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployConfigurationRequest(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        app_name: str = None,
        group: str = None,
        desc: str = None,
        tags: str = None,
        content: str = None,
        type: str = None,
        namespace_id: str = None,
        beta_ips: str = None,
    ):
        self.data_id = data_id
        self.app_name = app_name
        self.group = group
        self.desc = desc
        self.tags = tags
        self.content = content
        self.type = type
        self.namespace_id = namespace_id
        self.beta_ips = beta_ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.group is not None:
            result['Group'] = self.group
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.content is not None:
            result['Content'] = self.content
        if self.type is not None:
            result['Type'] = self.type
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')
        return self


class DeployConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeployConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeployConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigurationRequest(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
        namespace_id: str = None,
    ):
        self.data_id = data_id
        self.group = group
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DescribeConfigurationResponseBodyConfiguration(TeaModel):
    def __init__(
        self,
        type: str = None,
        app_name: str = None,
        tags: str = None,
        md_5: str = None,
        data_id: str = None,
        content: str = None,
        group: str = None,
        desc: str = None,
    ):
        self.type = type
        self.app_name = app_name
        self.tags = tags
        self.md_5 = md_5
        self.data_id = data_id
        self.content = content
        self.group = group
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.content is not None:
            result['Content'] = self.content
        if self.group is not None:
            result['Group'] = self.group
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class DescribeConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        configuration: DescribeConfigurationResponseBodyConfiguration = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.configuration = configuration
        self.code = code

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Configuration') is not None:
            temp_model = DescribeConfigurationResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImportFileUrlRequest(TeaModel):
    def __init__(
        self,
        content_type: str = None,
    ):
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        return self


class DescribeImportFileUrlResponseBody(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.file_url = file_url
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeImportFileUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImportFileUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImportFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
    ):
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DescribeNamespaceResponseBodyNamespace(TeaModel):
    def __init__(
        self,
        secret_key: str = None,
        access_key: str = None,
        endpoint: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.secret_key = secret_key
        self.access_key = access_key
        self.endpoint = endpoint
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        namespace: DescribeNamespaceResponseBodyNamespace = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.namespace = namespace

    def validate(self):
        if self.namespace:
            self.namespace.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.namespace is not None:
            result['Namespace'] = self.namespace.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Namespace') is not None:
            temp_model = DescribeNamespaceResponseBodyNamespace()
            self.namespace = temp_model.from_map(m['Namespace'])
        return self


class DescribeNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespacesResponseBodyNamespaces(TeaModel):
    def __init__(
        self,
        type: int = None,
        quota: int = None,
        namespace_id: str = None,
        config_count: int = None,
        namespace_name: str = None,
    ):
        self.type = type
        self.quota = quota
        self.namespace_id = namespace_id
        self.config_count = config_count
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class DescribeNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        namespaces: List[DescribeNamespacesResponseBodyNamespaces] = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.namespaces = namespaces
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = DescribeNamespacesResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNamespacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespacesWithCreateResponseBodyNamespaces(TeaModel):
    def __init__(
        self,
        type: int = None,
        quota: int = None,
        namespace_id: str = None,
        config_count: int = None,
        namespace_name: str = None,
    ):
        self.type = type
        self.quota = quota
        self.namespace_id = namespace_id
        self.config_count = config_count
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class DescribeNamespacesWithCreateResponseBody(TeaModel):
    def __init__(
        self,
        namespaces: List[DescribeNamespacesWithCreateResponseBodyNamespaces] = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.namespaces = namespaces
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = DescribeNamespacesWithCreateResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeNamespacesWithCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNamespacesWithCreateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNamespacesWithCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTraceByConfigurationRequest(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
        namespace_id: str = None,
        start_ts: str = None,
        end_ts: str = None,
    ):
        self.data_id = data_id
        self.group = group
        self.namespace_id = namespace_id
        self.start_ts = start_ts
        self.end_ts = end_ts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        return self


class DescribeTraceByConfigurationResponseBodyTracesEventGroupsEventDetails(TeaModel):
    def __init__(
        self,
        type: str = None,
        delay: str = None,
        ts: str = None,
        response_ip: str = None,
        event: str = None,
        ext: str = None,
        data_id: str = None,
        request_ip: str = None,
        log_date: str = None,
        handle_ip: str = None,
        group: str = None,
    ):
        self.type = type
        self.delay = delay
        self.ts = ts
        self.response_ip = response_ip
        self.event = event
        self.ext = ext
        self.data_id = data_id
        self.request_ip = request_ip
        self.log_date = log_date
        self.handle_ip = handle_ip
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.ts is not None:
            result['Ts'] = self.ts
        if self.response_ip is not None:
            result['ResponseIp'] = self.response_ip
        if self.event is not None:
            result['Event'] = self.event
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.request_ip is not None:
            result['RequestIp'] = self.request_ip
        if self.log_date is not None:
            result['LogDate'] = self.log_date
        if self.handle_ip is not None:
            result['HandleIp'] = self.handle_ip
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        if m.get('ResponseIp') is not None:
            self.response_ip = m.get('ResponseIp')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('RequestIp') is not None:
            self.request_ip = m.get('RequestIp')
        if m.get('LogDate') is not None:
            self.log_date = m.get('LogDate')
        if m.get('HandleIp') is not None:
            self.handle_ip = m.get('HandleIp')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class DescribeTraceByConfigurationResponseBodyTracesEventGroups(TeaModel):
    def __init__(
        self,
        event_type: str = None,
        event_details: List[DescribeTraceByConfigurationResponseBodyTracesEventGroupsEventDetails] = None,
    ):
        self.event_type = event_type
        self.event_details = event_details

    def validate(self):
        if self.event_details:
            for k in self.event_details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        result['EventDetails'] = []
        if self.event_details is not None:
            for k in self.event_details:
                result['EventDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        self.event_details = []
        if m.get('EventDetails') is not None:
            for k in m.get('EventDetails'):
                temp_model = DescribeTraceByConfigurationResponseBodyTracesEventGroupsEventDetails()
                self.event_details.append(temp_model.from_map(k))
        return self


class DescribeTraceByConfigurationResponseBodyTraces(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        event_groups: List[DescribeTraceByConfigurationResponseBodyTracesEventGroups] = None,
    ):
        self.timestamp = timestamp
        self.event_groups = event_groups

    def validate(self):
        if self.event_groups:
            for k in self.event_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        result['EventGroups'] = []
        if self.event_groups is not None:
            for k in self.event_groups:
                result['EventGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        self.event_groups = []
        if m.get('EventGroups') is not None:
            for k in m.get('EventGroups'):
                temp_model = DescribeTraceByConfigurationResponseBodyTracesEventGroups()
                self.event_groups.append(temp_model.from_map(k))
        return self


class DescribeTraceByConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        traces: List[DescribeTraceByConfigurationResponseBodyTraces] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.traces = traces
        self.code = code

    def validate(self):
        if self.traces:
            for k in self.traces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Traces'] = []
        if self.traces is not None:
            for k in self.traces:
                result['Traces'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.traces = []
        if m.get('Traces') is not None:
            for k in m.get('Traces'):
                temp_model = DescribeTraceByConfigurationResponseBodyTraces()
                self.traces.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeTraceByConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTraceByConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTraceByConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
        namespace_name: str = None,
    ):
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class UpdateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


