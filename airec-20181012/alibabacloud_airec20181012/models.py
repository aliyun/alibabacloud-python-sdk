# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AttachDatasetResponseBodyResult(TeaModel):
    def __init__(
        self,
        state: str = None,
        gmt_create: int = None,
        version_id: str = None,
        instance_id: str = None,
        gmt_modified: int = None,
    ):
        self.state = state
        self.gmt_create = gmt_create
        self.version_id = version_id
        self.instance_id = instance_id
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class AttachDatasetResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: AttachDatasetResponseBodyResult = None,
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
            temp_model = AttachDatasetResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class AttachDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachDatasetResponseBody = None,
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
            temp_model = AttachDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDiversifyResponseBodyResultParameter(TeaModel):
    def __init__(
        self,
        window: int = None,
        category_index: int = None,
    ):
        self.window = window
        self.category_index = category_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.window is not None:
            result['Window'] = self.window
        if self.category_index is not None:
            result['CategoryIndex'] = self.category_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Window') is not None:
            self.window = m.get('Window')
        if m.get('CategoryIndex') is not None:
            self.category_index = m.get('CategoryIndex')
        return self


class CreateDiversifyResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        gmt_modified: str = None,
        parameter: CreateDiversifyResponseBodyResultParameter = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Parameter') is not None:
            temp_model = CreateDiversifyResponseBodyResultParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class CreateDiversifyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: CreateDiversifyResponseBodyResult = None,
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
            temp_model = CreateDiversifyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateDiversifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDiversifyResponseBody = None,
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
            temp_model = CreateDiversifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: CreateInstanceResponseBodyResult = None,
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
            temp_model = CreateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceResponseBody = None,
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMixResponseBodyResultParameterSettings(TeaModel):
    def __init__(
        self,
        value: int = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateMixResponseBodyResultParameter(TeaModel):
    def __init__(
        self,
        settings: List[CreateMixResponseBodyResultParameterSettings] = None,
    ):
        self.settings = settings

    def validate(self):
        if self.settings:
            for k in self.settings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Settings'] = []
        if self.settings is not None:
            for k in self.settings:
                result['Settings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.settings = []
        if m.get('Settings') is not None:
            for k in m.get('Settings'):
                temp_model = CreateMixResponseBodyResultParameterSettings()
                self.settings.append(temp_model.from_map(k))
        return self


class CreateMixResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        gmt_modified: str = None,
        parameter: CreateMixResponseBodyResultParameter = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Parameter') is not None:
            temp_model = CreateMixResponseBodyResultParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class CreateMixResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: CreateMixResponseBodyResult = None,
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
            temp_model = CreateMixResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateMixResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMixResponseBody = None,
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
            temp_model = CreateMixResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        rule_id: str = None,
    ):
        self.status = status
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateRuleResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateRuleResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRuleResponseBody = None,
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
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSceneRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class CreateSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        gmt_create: str = None,
        scene_id: str = None,
        gmt_modified: str = None,
    ):
        self.status = status
        self.gmt_create = gmt_create
        self.scene_id = scene_id
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class CreateSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateSceneResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateSceneResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSceneResponseBody = None,
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
            temp_model = CreateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSetResponseBodyResult(TeaModel):
    def __init__(
        self,
        state: str = None,
        gmt_create: int = None,
        version_id: str = None,
        instance_id: str = None,
        gmt_modified: int = None,
    ):
        self.state = state
        self.gmt_create = gmt_create
        self.version_id = version_id
        self.instance_id = instance_id
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class DeleteDataSetResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: DeleteDataSetResponseBodyResult = None,
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
            temp_model = DeleteDataSetResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDataSetResponseBody = None,
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
            temp_model = DeleteDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDiversifyResponseBodyResultParameter(TeaModel):
    def __init__(
        self,
        window: int = None,
        category_index: int = None,
    ):
        self.window = window
        self.category_index = category_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.window is not None:
            result['Window'] = self.window
        if self.category_index is not None:
            result['CategoryIndex'] = self.category_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Window') is not None:
            self.window = m.get('Window')
        if m.get('CategoryIndex') is not None:
            self.category_index = m.get('CategoryIndex')
        return self


class DeleteDiversifyResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        gmt_modified: str = None,
        parameter: DeleteDiversifyResponseBodyResultParameter = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Parameter') is not None:
            temp_model = DeleteDiversifyResponseBodyResultParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class DeleteDiversifyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: DeleteDiversifyResponseBodyResult = None,
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
            temp_model = DeleteDiversifyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteDiversifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDiversifyResponseBody = None,
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
            temp_model = DeleteDiversifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMixResponseBodyResultParameterSettings(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteMixResponseBodyResultParameter(TeaModel):
    def __init__(
        self,
        settings: List[DeleteMixResponseBodyResultParameterSettings] = None,
    ):
        self.settings = settings

    def validate(self):
        if self.settings:
            for k in self.settings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Settings'] = []
        if self.settings is not None:
            for k in self.settings:
                result['Settings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.settings = []
        if m.get('Settings') is not None:
            for k in m.get('Settings'):
                temp_model = DeleteMixResponseBodyResultParameterSettings()
                self.settings.append(temp_model.from_map(k))
        return self


class DeleteMixResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        gmt_modified: str = None,
        parameter: DeleteMixResponseBodyResultParameter = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Parameter') is not None:
            temp_model = DeleteMixResponseBodyResultParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class DeleteMixResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: DeleteMixResponseBodyResult = None,
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
            temp_model = DeleteMixResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteMixResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMixResponseBody = None,
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
            temp_model = DeleteMixResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class DeleteSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DeleteSceneResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteSceneResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSceneResponseBody = None,
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
            temp_model = DeleteSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataSetMessageResponseBodyResult(TeaModel):
    def __init__(
        self,
        error_level: str = None,
        message: str = None,
        timestamp: str = None,
        error_type: str = None,
    ):
        self.error_level = error_level
        self.message = message
        self.timestamp = timestamp
        self.error_type = error_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.error_level is not None:
            result['ErrorLevel'] = self.error_level
        if self.message is not None:
            result['Message'] = self.message
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.error_type is not None:
            result['ErrorType'] = self.error_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorLevel') is not None:
            self.error_level = m.get('ErrorLevel')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')
        return self


class DescribeDataSetMessageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[DescribeDataSetMessageResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeDataSetMessageResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeDataSetMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataSetMessageResponseBody = None,
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
            temp_model = DescribeDataSetMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataSetReportResponseBodyResultOverall(TeaModel):
    def __init__(
        self,
        user_repetitive_rate: float = None,
        user_user_count: int = None,
        bhv_count: int = None,
        bhv_legal_rate: float = None,
        user_complete_rate: float = None,
        user_login_rate: float = None,
        item_complete_rate: float = None,
        item_repetitive_rate: float = None,
        item_item_count: int = None,
        user_legal_rate: float = None,
        item_legal_rate: float = None,
        item_login_rate: float = None,
    ):
        self.user_repetitive_rate = user_repetitive_rate
        self.user_user_count = user_user_count
        self.bhv_count = bhv_count
        self.bhv_legal_rate = bhv_legal_rate
        self.user_complete_rate = user_complete_rate
        self.user_login_rate = user_login_rate
        self.item_complete_rate = item_complete_rate
        self.item_repetitive_rate = item_repetitive_rate
        self.item_item_count = item_item_count
        self.user_legal_rate = user_legal_rate
        self.item_legal_rate = item_legal_rate
        self.item_login_rate = item_login_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_repetitive_rate is not None:
            result['UserRepetitiveRate'] = self.user_repetitive_rate
        if self.user_user_count is not None:
            result['UserUserCount'] = self.user_user_count
        if self.bhv_count is not None:
            result['BhvCount'] = self.bhv_count
        if self.bhv_legal_rate is not None:
            result['BhvLegalRate'] = self.bhv_legal_rate
        if self.user_complete_rate is not None:
            result['UserCompleteRate'] = self.user_complete_rate
        if self.user_login_rate is not None:
            result['UserLoginRate'] = self.user_login_rate
        if self.item_complete_rate is not None:
            result['ItemCompleteRate'] = self.item_complete_rate
        if self.item_repetitive_rate is not None:
            result['ItemRepetitiveRate'] = self.item_repetitive_rate
        if self.item_item_count is not None:
            result['ItemItemCount'] = self.item_item_count
        if self.user_legal_rate is not None:
            result['UserLegalRate'] = self.user_legal_rate
        if self.item_legal_rate is not None:
            result['ItemLegalRate'] = self.item_legal_rate
        if self.item_login_rate is not None:
            result['ItemLoginRate'] = self.item_login_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserRepetitiveRate') is not None:
            self.user_repetitive_rate = m.get('UserRepetitiveRate')
        if m.get('UserUserCount') is not None:
            self.user_user_count = m.get('UserUserCount')
        if m.get('BhvCount') is not None:
            self.bhv_count = m.get('BhvCount')
        if m.get('BhvLegalRate') is not None:
            self.bhv_legal_rate = m.get('BhvLegalRate')
        if m.get('UserCompleteRate') is not None:
            self.user_complete_rate = m.get('UserCompleteRate')
        if m.get('UserLoginRate') is not None:
            self.user_login_rate = m.get('UserLoginRate')
        if m.get('ItemCompleteRate') is not None:
            self.item_complete_rate = m.get('ItemCompleteRate')
        if m.get('ItemRepetitiveRate') is not None:
            self.item_repetitive_rate = m.get('ItemRepetitiveRate')
        if m.get('ItemItemCount') is not None:
            self.item_item_count = m.get('ItemItemCount')
        if m.get('UserLegalRate') is not None:
            self.user_legal_rate = m.get('UserLegalRate')
        if m.get('ItemLegalRate') is not None:
            self.item_legal_rate = m.get('ItemLegalRate')
        if m.get('ItemLoginRate') is not None:
            self.item_login_rate = m.get('ItemLoginRate')
        return self


class DescribeDataSetReportResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        uv_ctr: float = None,
        biz_date: int = None,
        per_uv_click: float = None,
        pv: int = None,
        active_item: int = None,
        ctr: float = None,
        per_uv_bhv: float = None,
        click: int = None,
        uv: int = None,
        click_user: int = None,
    ):
        self.uv_ctr = uv_ctr
        self.biz_date = biz_date
        self.per_uv_click = per_uv_click
        self.pv = pv
        self.active_item = active_item
        self.ctr = ctr
        self.per_uv_bhv = per_uv_bhv
        self.click = click
        self.uv = uv
        self.click_user = click_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uv_ctr is not None:
            result['UvCtr'] = self.uv_ctr
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.per_uv_click is not None:
            result['PerUvClick'] = self.per_uv_click
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.active_item is not None:
            result['ActiveItem'] = self.active_item
        if self.ctr is not None:
            result['Ctr'] = self.ctr
        if self.per_uv_bhv is not None:
            result['PerUvBhv'] = self.per_uv_bhv
        if self.click is not None:
            result['Click'] = self.click
        if self.uv is not None:
            result['Uv'] = self.uv
        if self.click_user is not None:
            result['ClickUser'] = self.click_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UvCtr') is not None:
            self.uv_ctr = m.get('UvCtr')
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('PerUvClick') is not None:
            self.per_uv_click = m.get('PerUvClick')
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('ActiveItem') is not None:
            self.active_item = m.get('ActiveItem')
        if m.get('Ctr') is not None:
            self.ctr = m.get('Ctr')
        if m.get('PerUvBhv') is not None:
            self.per_uv_bhv = m.get('PerUvBhv')
        if m.get('Click') is not None:
            self.click = m.get('Click')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        if m.get('ClickUser') is not None:
            self.click_user = m.get('ClickUser')
        return self


class DescribeDataSetReportResponseBodyResult(TeaModel):
    def __init__(
        self,
        overall: DescribeDataSetReportResponseBodyResultOverall = None,
        detail: List[DescribeDataSetReportResponseBodyResultDetail] = None,
    ):
        self.overall = overall
        self.detail = detail

    def validate(self):
        if self.overall:
            self.overall.validate()
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.overall is not None:
            result['Overall'] = self.overall.to_map()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Overall') is not None:
            temp_model = DescribeDataSetReportResponseBodyResultOverall()
            self.overall = temp_model.from_map(m['Overall'])
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeDataSetReportResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class DescribeDataSetReportResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: DescribeDataSetReportResponseBodyResult = None,
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
            temp_model = DescribeDataSetReportResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeDataSetReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataSetReportResponseBody = None,
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
            temp_model = DescribeDataSetReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiversifyResponseBodyResultParameter(TeaModel):
    def __init__(
        self,
        window: int = None,
        category_index: int = None,
    ):
        self.window = window
        self.category_index = category_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.window is not None:
            result['Window'] = self.window
        if self.category_index is not None:
            result['CategoryIndex'] = self.category_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Window') is not None:
            self.window = m.get('Window')
        if m.get('CategoryIndex') is not None:
            self.category_index = m.get('CategoryIndex')
        return self


class DescribeDiversifyResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        gmt_modified: str = None,
        parameter: DescribeDiversifyResponseBodyResultParameter = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Parameter') is not None:
            temp_model = DescribeDiversifyResponseBodyResultParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class DescribeDiversifyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: DescribeDiversifyResponseBodyResult = None,
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
            temp_model = DescribeDiversifyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeDiversifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDiversifyResponseBody = None,
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
            temp_model = DescribeDiversifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExposureSettingsResponseBodyResult(TeaModel):
    def __init__(
        self,
        duration_seconds: int = None,
        scenario_based: bool = None,
    ):
        self.duration_seconds = duration_seconds
        self.scenario_based = scenario_based

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.scenario_based is not None:
            result['ScenarioBased'] = self.scenario_based
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('ScenarioBased') is not None:
            self.scenario_based = m.get('ScenarioBased')
        return self


class DescribeExposureSettingsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: DescribeExposureSettingsResponseBodyResult = None,
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
            temp_model = DescribeExposureSettingsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeExposureSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExposureSettingsResponseBody = None,
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
            temp_model = DescribeExposureSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        commodity_code: str = None,
        charge_type: str = None,
        instance_id: str = None,
        gmt_modified: str = None,
        lock_mode: str = None,
        region_id: str = None,
        data_set_version: str = None,
        industry: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        name: str = None,
        scene: str = None,
    ):
        self.status = status
        self.type = type
        self.commodity_code = commodity_code
        self.charge_type = charge_type
        self.instance_id = instance_id
        self.gmt_modified = gmt_modified
        self.lock_mode = lock_mode
        self.region_id = region_id
        self.data_set_version = data_set_version
        self.industry = industry
        self.expired_time = expired_time
        self.gmt_create = gmt_create
        self.name = name
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.data_set_version is not None:
            result['DataSetVersion'] = self.data_set_version
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DataSetVersion') is not None:
            self.data_set_version = m.get('DataSetVersion')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: DescribeInstanceResponseBodyResult = None,
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
            temp_model = DescribeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceResponseBody = None,
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
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMixResponseBodyResultParameterSettings(TeaModel):
    def __init__(
        self,
        value: int = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeMixResponseBodyResultParameter(TeaModel):
    def __init__(
        self,
        settings: List[DescribeMixResponseBodyResultParameterSettings] = None,
    ):
        self.settings = settings

    def validate(self):
        if self.settings:
            for k in self.settings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Settings'] = []
        if self.settings is not None:
            for k in self.settings:
                result['Settings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.settings = []
        if m.get('Settings') is not None:
            for k in m.get('Settings'):
                temp_model = DescribeMixResponseBodyResultParameterSettings()
                self.settings.append(temp_model.from_map(k))
        return self


class DescribeMixResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        gmt_modified: str = None,
        parameter: DescribeMixResponseBodyResultParameter = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Parameter') is not None:
            temp_model = DescribeMixResponseBodyResultParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class DescribeMixResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: DescribeMixResponseBodyResult = None,
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
            temp_model = DescribeMixResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeMixResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMixResponseBody = None,
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
            temp_model = DescribeMixResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQuotaResponseBodyResult(TeaModel):
    def __init__(
        self,
        qps: int = None,
        item_count: int = None,
        current_qps: int = None,
        user_count: int = None,
        user_count_used: int = None,
        item_count_used: int = None,
    ):
        self.qps = qps
        self.item_count = item_count
        self.current_qps = current_qps
        self.user_count = user_count
        self.user_count_used = user_count_used
        self.item_count_used = item_count_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.item_count is not None:
            result['ItemCount'] = self.item_count
        if self.current_qps is not None:
            result['CurrentQps'] = self.current_qps
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.user_count_used is not None:
            result['UserCountUsed'] = self.user_count_used
        if self.item_count_used is not None:
            result['ItemCountUsed'] = self.item_count_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('ItemCount') is not None:
            self.item_count = m.get('ItemCount')
        if m.get('CurrentQps') is not None:
            self.current_qps = m.get('CurrentQps')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('UserCountUsed') is not None:
            self.user_count_used = m.get('UserCountUsed')
        if m.get('ItemCountUsed') is not None:
            self.item_count_used = m.get('ItemCountUsed')
        return self


class DescribeQuotaResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: DescribeQuotaResponseBodyResult = None,
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
            temp_model = DescribeQuotaResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeQuotaResponseBody = None,
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
            temp_model = DescribeQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        console_url: str = None,
        local_name: str = None,
        endpoint: str = None,
        region_id: str = None,
    ):
        self.status = status
        self.console_url = console_url
        self.local_name = local_name
        self.endpoint = endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.console_url is not None:
            result['ConsoleUrl'] = self.console_url
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConsoleUrl') is not None:
            self.console_url = m.get('ConsoleUrl')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[DescribeRegionsResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRuleRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        rule_type: str = None,
    ):
        self.scene_id = scene_id
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class DescribeRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        rule_id: str = None,
    ):
        self.status = status
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeRuleResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeRuleResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRuleResponseBody = None,
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
            temp_model = DescribeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        gmt_create: str = None,
        scene_id: str = None,
        gmt_modified: str = None,
    ):
        self.status = status
        self.gmt_create = gmt_create
        self.scene_id = scene_id
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class DescribeSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeSceneResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeSceneResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSceneResponseBody = None,
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
            temp_model = DescribeSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneThroughputResponseBodyResult(TeaModel):
    def __init__(
        self,
        pv_count: int = None,
    ):
        self.pv_count = pv_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pv_count is not None:
            result['PvCount'] = self.pv_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PvCount') is not None:
            self.pv_count = m.get('PvCount')
        return self


class DescribeSceneThroughputResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeSceneThroughputResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeSceneThroughputResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeSceneThroughputResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSceneThroughputResponseBody = None,
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
            temp_model = DescribeSceneThroughputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSyncReportDetailRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        type: str = None,
        level_type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.type = type
        self.level_type = level_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.type is not None:
            result['Type'] = self.type
        if self.level_type is not None:
            result['LevelType'] = self.level_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('LevelType') is not None:
            self.level_type = m.get('LevelType')
        return self


class DescribeSyncReportDetailResponseBodyResultHistoryData(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        error_percent: float = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.error_percent = error_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.error_percent is not None:
            result['ErrorPercent'] = self.error_percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ErrorPercent') is not None:
            self.error_percent = m.get('ErrorPercent')
        return self


class DescribeSyncReportDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: str = None,
        error_count: int = None,
        sample_display: bool = None,
        history_data: List[DescribeSyncReportDetailResponseBodyResultHistoryData] = None,
        default_display: bool = None,
        error_percent: float = None,
    ):
        self.type = type
        self.error_count = error_count
        self.sample_display = sample_display
        self.history_data = history_data
        self.default_display = default_display
        self.error_percent = error_percent

    def validate(self):
        if self.history_data:
            for k in self.history_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.sample_display is not None:
            result['SampleDisplay'] = self.sample_display
        result['HistoryData'] = []
        if self.history_data is not None:
            for k in self.history_data:
                result['HistoryData'].append(k.to_map() if k else None)
        if self.default_display is not None:
            result['DefaultDisplay'] = self.default_display
        if self.error_percent is not None:
            result['ErrorPercent'] = self.error_percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('SampleDisplay') is not None:
            self.sample_display = m.get('SampleDisplay')
        self.history_data = []
        if m.get('HistoryData') is not None:
            for k in m.get('HistoryData'):
                temp_model = DescribeSyncReportDetailResponseBodyResultHistoryData()
                self.history_data.append(temp_model.from_map(k))
        if m.get('DefaultDisplay') is not None:
            self.default_display = m.get('DefaultDisplay')
        if m.get('ErrorPercent') is not None:
            self.error_percent = m.get('ErrorPercent')
        return self


class DescribeSyncReportDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[DescribeSyncReportDetailResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeSyncReportDetailResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeSyncReportDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSyncReportDetailResponseBody = None,
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
            temp_model = DescribeSyncReportDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSyncReportOutliersRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        key: str = None,
        type: str = None,
        end_time: int = None,
        level_type: str = None,
    ):
        self.start_time = start_time
        self.key = key
        self.type = type
        self.end_time = end_time
        self.level_type = level_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.level_type is not None:
            result['LevelType'] = self.level_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LevelType') is not None:
            self.level_type = m.get('LevelType')
        return self


class DescribeSyncReportOutliersResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: Dict[str, Any] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class DescribeSyncReportOutliersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSyncReportOutliersResponseBody = None,
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
            temp_model = DescribeSyncReportOutliersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserMetricsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        metric_type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class DescribeUserMetricsResponseBodyResultDataPoints(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        val: float = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.val is not None:
            result['Val'] = self.val
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        return self


class DescribeUserMetricsResponseBodyResult(TeaModel):
    def __init__(
        self,
        data_points: List[DescribeUserMetricsResponseBodyResultDataPoints] = None,
        scene_id: str = None,
    ):
        self.data_points = data_points
        self.scene_id = scene_id

    def validate(self):
        if self.data_points:
            for k in self.data_points:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataPoints'] = []
        if self.data_points is not None:
            for k in self.data_points:
                result['DataPoints'].append(k.to_map() if k else None)
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_points = []
        if m.get('DataPoints') is not None:
            for k in m.get('DataPoints'):
                temp_model = DescribeUserMetricsResponseBodyResultDataPoints()
                self.data_points.append(temp_model.from_map(k))
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class DescribeUserMetricsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[DescribeUserMetricsResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeUserMetricsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeUserMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserMetricsResponseBody = None,
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
            temp_model = DescribeUserMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DowngradeInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DowngradeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: DowngradeInstanceResponseBodyResult = None,
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
            temp_model = DowngradeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DowngradeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DowngradeInstanceResponseBody = None,
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
            temp_model = DowngradeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardRequest(TeaModel):
    def __init__(
        self,
        start_date: int = None,
        end_date: int = None,
        trace_id: str = None,
        scene_id: str = None,
        page: int = None,
        size: int = None,
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.trace_id = trace_id
        self.scene_id = scene_id
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListDashboardResponseBodyResultList(TeaModel):
    def __init__(
        self,
        uv_ctr: float = None,
        biz_date: int = None,
        active_item: int = None,
        per_uv_bhv: float = None,
        uv: int = None,
        per_uv_click: float = None,
        pv: int = None,
        ctr: float = None,
        scene_id: str = None,
        trace_id: str = None,
        click: int = None,
        click_user: int = None,
    ):
        self.uv_ctr = uv_ctr
        self.biz_date = biz_date
        self.active_item = active_item
        self.per_uv_bhv = per_uv_bhv
        self.uv = uv
        self.per_uv_click = per_uv_click
        self.pv = pv
        self.ctr = ctr
        self.scene_id = scene_id
        self.trace_id = trace_id
        self.click = click
        self.click_user = click_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uv_ctr is not None:
            result['UvCtr'] = self.uv_ctr
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.active_item is not None:
            result['ActiveItem'] = self.active_item
        if self.per_uv_bhv is not None:
            result['PerUvBhv'] = self.per_uv_bhv
        if self.uv is not None:
            result['Uv'] = self.uv
        if self.per_uv_click is not None:
            result['PerUvClick'] = self.per_uv_click
        if self.pv is not None:
            result['Pv'] = self.pv
        if self.ctr is not None:
            result['Ctr'] = self.ctr
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.click is not None:
            result['Click'] = self.click
        if self.click_user is not None:
            result['ClickUser'] = self.click_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UvCtr') is not None:
            self.uv_ctr = m.get('UvCtr')
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('ActiveItem') is not None:
            self.active_item = m.get('ActiveItem')
        if m.get('PerUvBhv') is not None:
            self.per_uv_bhv = m.get('PerUvBhv')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        if m.get('PerUvClick') is not None:
            self.per_uv_click = m.get('PerUvClick')
        if m.get('Pv') is not None:
            self.pv = m.get('Pv')
        if m.get('Ctr') is not None:
            self.ctr = m.get('Ctr')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('Click') is not None:
            self.click = m.get('Click')
        if m.get('ClickUser') is not None:
            self.click_user = m.get('ClickUser')
        return self


class ListDashboardResponseBodyResult(TeaModel):
    def __init__(
        self,
        list: List[ListDashboardResponseBodyResultList] = None,
        num: int = None,
    ):
        self.list = list
        self.num = num

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.num is not None:
            result['Num'] = self.num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListDashboardResponseBodyResultList()
                self.list.append(temp_model.from_map(k))
        if m.get('Num') is not None:
            self.num = m.get('Num')
        return self


class ListDashboardResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: ListDashboardResponseBodyResult = None,
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
            temp_model = ListDashboardResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardResponseBody = None,
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
            temp_model = ListDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardDetailsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        trace_ids: str = None,
        scene_ids: str = None,
        metric_type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.trace_ids = trace_ids
        self.scene_ids = scene_ids
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.trace_ids is not None:
            result['TraceIds'] = self.trace_ids
        if self.scene_ids is not None:
            result['SceneIds'] = self.scene_ids
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TraceIds') is not None:
            self.trace_ids = m.get('TraceIds')
        if m.get('SceneIds') is not None:
            self.scene_ids = m.get('SceneIds')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class ListDashboardDetailsResponseBodyResultMetricRes(TeaModel):
    def __init__(
        self,
        total: Dict[str, Any] = None,
        detail: Dict[str, Any] = None,
    ):
        self.total = total
        self.detail = detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        if self.detail is not None:
            result['Detail'] = self.detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        return self


class ListDashboardDetailsResponseBodyResult(TeaModel):
    def __init__(
        self,
        metric_res: ListDashboardDetailsResponseBodyResultMetricRes = None,
        scene_id: str = None,
        trace_id: str = None,
    ):
        self.metric_res = metric_res
        self.scene_id = scene_id
        self.trace_id = trace_id

    def validate(self):
        if self.metric_res:
            self.metric_res.validate()

    def to_map(self):
        result = dict()
        if self.metric_res is not None:
            result['MetricRes'] = self.metric_res.to_map()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricRes') is not None:
            temp_model = ListDashboardDetailsResponseBodyResultMetricRes()
            self.metric_res = temp_model.from_map(m['MetricRes'])
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListDashboardDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDashboardDetailsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDashboardDetailsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDashboardDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardDetailsResponseBody = None,
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
            temp_model = ListDashboardDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardDetailsFlowsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        trace_ids: str = None,
        scene_ids: str = None,
        metric_type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.trace_ids = trace_ids
        self.scene_ids = scene_ids
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.trace_ids is not None:
            result['TraceIds'] = self.trace_ids
        if self.scene_ids is not None:
            result['SceneIds'] = self.scene_ids
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TraceIds') is not None:
            self.trace_ids = m.get('TraceIds')
        if m.get('SceneIds') is not None:
            self.scene_ids = m.get('SceneIds')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class ListDashboardDetailsFlowsResponseBodyResultMetricData(TeaModel):
    def __init__(
        self,
        metric_res: Dict[str, Any] = None,
        scene_id: str = None,
        trace_id: str = None,
    ):
        self.metric_res = metric_res
        self.scene_id = scene_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.metric_res is not None:
            result['MetricRes'] = self.metric_res
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricRes') is not None:
            self.metric_res = m.get('MetricRes')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListDashboardDetailsFlowsResponseBodyResult(TeaModel):
    def __init__(
        self,
        metric_data: List[ListDashboardDetailsFlowsResponseBodyResultMetricData] = None,
        metric_type: str = None,
    ):
        self.metric_data = metric_data
        self.metric_type = metric_type

    def validate(self):
        if self.metric_data:
            for k in self.metric_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['MetricData'] = []
        if self.metric_data is not None:
            for k in self.metric_data:
                result['MetricData'].append(k.to_map() if k else None)
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_data = []
        if m.get('MetricData') is not None:
            for k in m.get('MetricData'):
                temp_model = ListDashboardDetailsFlowsResponseBodyResultMetricData()
                self.metric_data.append(temp_model.from_map(k))
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class ListDashboardDetailsFlowsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListDashboardDetailsFlowsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListDashboardDetailsFlowsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListDashboardDetailsFlowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardDetailsFlowsResponseBody = None,
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
            temp_model = ListDashboardDetailsFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardMetricsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        metric_type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class ListDashboardMetricsResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        val: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.val is not None:
            result['Val'] = self.val
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        return self


class ListDashboardMetricsResponseBodyResult(TeaModel):
    def __init__(
        self,
        total: Dict[str, Any] = None,
        detail: List[ListDashboardMetricsResponseBodyResultDetail] = None,
    ):
        self.total = total
        self.detail = detail

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = ListDashboardMetricsResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class ListDashboardMetricsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDashboardMetricsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDashboardMetricsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDashboardMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardMetricsResponseBody = None,
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
            temp_model = ListDashboardMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardMetricsFlowsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        metric_type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class ListDashboardMetricsFlowsResponseBodyResult(TeaModel):
    def __init__(
        self,
        metric_data: Dict[str, Any] = None,
        metric_type: str = None,
    ):
        self.metric_data = metric_data
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.metric_data is not None:
            result['MetricData'] = self.metric_data
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricData') is not None:
            self.metric_data = m.get('MetricData')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class ListDashboardMetricsFlowsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDashboardMetricsFlowsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDashboardMetricsFlowsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDashboardMetricsFlowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardMetricsFlowsResponseBody = None,
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
            temp_model = ListDashboardMetricsFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardParametersResponseBodyResult(TeaModel):
    def __init__(
        self,
        scene_id: List[str] = None,
        trace_id: List[str] = None,
    ):
        self.scene_id = scene_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListDashboardParametersResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: ListDashboardParametersResponseBodyResult = None,
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
            temp_model = ListDashboardParametersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListDashboardParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardParametersResponseBody = None,
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
            temp_model = ListDashboardParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardUidResponseBodyResult(TeaModel):
    def __init__(
        self,
        num: int = None,
        uid: List[str] = None,
    ):
        self.num = num
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.num is not None:
            result['Num'] = self.num
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListDashboardUidResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: ListDashboardUidResponseBodyResult = None,
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
            temp_model = ListDashboardUidResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListDashboardUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardUidResponseBody = None,
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
            temp_model = ListDashboardUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSetResponseBodyResult(TeaModel):
    def __init__(
        self,
        state: str = None,
        gmt_create: int = None,
        version_id: str = None,
        instance_id: str = None,
        gmt_modified: int = None,
    ):
        self.state = state
        self.gmt_create = gmt_create
        self.version_id = version_id
        self.instance_id = instance_id
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class ListDataSetResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[ListDataSetResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDataSetResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataSetResponseBody = None,
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
            temp_model = ListDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        type: str = None,
        table_name: str = None,
        project_name: str = None,
        bucket_name: str = None,
        path: str = None,
        partition: str = None,
        timestamp: int = None,
        access_key_id: str = None,
    ):
        self.type = type
        self.table_name = table_name
        self.project_name = project_name
        self.bucket_name = bucket_name
        self.path = path
        self.partition = partition
        self.timestamp = timestamp
        self.access_key_id = access_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.path is not None:
            result['Path'] = self.path
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        return self


class ListDataSourceResponseBodyResult(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        meta: ListDataSourceResponseBodyResultMeta = None,
        gmt_create: str = None,
        gmt_modified: str = None,
    ):
        self.table_name = table_name
        self.meta = meta
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Meta') is not None:
            temp_model = ListDataSourceResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['Meta'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class ListDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[ListDataSourceResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDataSourceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataSourceResponseBody = None,
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
            temp_model = ListDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiversifyResponseBodyResultParameter(TeaModel):
    def __init__(
        self,
        window: int = None,
        category_index: int = None,
    ):
        self.window = window
        self.category_index = category_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.window is not None:
            result['Window'] = self.window
        if self.category_index is not None:
            result['CategoryIndex'] = self.category_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Window') is not None:
            self.window = m.get('Window')
        if m.get('CategoryIndex') is not None:
            self.category_index = m.get('CategoryIndex')
        return self


class ListDiversifyResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        gmt_modified: str = None,
        parameter: ListDiversifyResponseBodyResultParameter = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Parameter') is not None:
            temp_model = ListDiversifyResponseBodyResultParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class ListDiversifyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[ListDiversifyResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDiversifyResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDiversifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDiversifyResponseBody = None,
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
            temp_model = ListDiversifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        status: str = None,
        name: str = None,
        expired_time: str = None,
    ):
        self.page = page
        self.size = size
        self.status = status
        self.name = name
        self.expired_time = expired_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.name is not None:
            result['Name'] = self.name
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        return self


class ListInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        commodity_code: str = None,
        charge_type: str = None,
        instance_id: str = None,
        gmt_modified: str = None,
        lock_mode: str = None,
        region_id: str = None,
        data_set_version: str = None,
        industry: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        name: str = None,
        scene: str = None,
    ):
        self.status = status
        self.type = type
        self.commodity_code = commodity_code
        self.charge_type = charge_type
        self.instance_id = instance_id
        self.gmt_modified = gmt_modified
        self.lock_mode = lock_mode
        self.region_id = region_id
        self.data_set_version = data_set_version
        self.industry = industry
        self.expired_time = expired_time
        self.gmt_create = gmt_create
        self.name = name
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.data_set_version is not None:
            result['DataSetVersion'] = self.data_set_version
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DataSetVersion') is not None:
            self.data_set_version = m.get('DataSetVersion')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[ListInstanceResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListInstanceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceResponseBody = None,
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceTaskResponseBodyResultSubProgressInfos(TeaModel):
    def __init__(
        self,
        type: str = None,
        progress: int = None,
        finished_num: int = None,
        total_num: int = None,
        detail: str = None,
    ):
        self.type = type
        self.progress = progress
        self.finished_num = finished_num
        self.total_num = total_num
        self.detail = detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.finished_num is not None:
            result['FinishedNum'] = self.finished_num
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.detail is not None:
            result['Detail'] = self.detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('FinishedNum') is not None:
            self.finished_num = m.get('FinishedNum')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        return self


class ListInstanceTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        sub_progress_infos: List[ListInstanceTaskResponseBodyResultSubProgressInfos] = None,
        name: str = None,
        total_progress: int = None,
    ):
        self.sub_progress_infos = sub_progress_infos
        self.name = name
        self.total_progress = total_progress

    def validate(self):
        if self.sub_progress_infos:
            for k in self.sub_progress_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SubProgressInfos'] = []
        if self.sub_progress_infos is not None:
            for k in self.sub_progress_infos:
                result['SubProgressInfos'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.total_progress is not None:
            result['TotalProgress'] = self.total_progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_progress_infos = []
        if m.get('SubProgressInfos') is not None:
            for k in m.get('SubProgressInfos'):
                temp_model = ListInstanceTaskResponseBodyResultSubProgressInfos()
                self.sub_progress_infos.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TotalProgress') is not None:
            self.total_progress = m.get('TotalProgress')
        return self


class ListInstanceTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[ListInstanceTaskResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListInstanceTaskResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInstanceTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceTaskResponseBody = None,
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
            temp_model = ListInstanceTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListItemsRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
    ):
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListItemsResponseBodyResultTotal(TeaModel):
    def __init__(
        self,
        weight_item: int = None,
        instance_recommend_item: int = None,
        query_count: int = None,
        total_count: int = None,
        scene_recommend_item: int = None,
        scene_weight_item: int = None,
    ):
        self.weight_item = weight_item
        self.instance_recommend_item = instance_recommend_item
        self.query_count = query_count
        self.total_count = total_count
        self.scene_recommend_item = scene_recommend_item
        self.scene_weight_item = scene_weight_item

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.weight_item is not None:
            result['WeightItem'] = self.weight_item
        if self.instance_recommend_item is not None:
            result['InstanceRecommendItem'] = self.instance_recommend_item
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.scene_recommend_item is not None:
            result['SceneRecommendItem'] = self.scene_recommend_item
        if self.scene_weight_item is not None:
            result['SceneWeightItem'] = self.scene_weight_item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WeightItem') is not None:
            self.weight_item = m.get('WeightItem')
        if m.get('InstanceRecommendItem') is not None:
            self.instance_recommend_item = m.get('InstanceRecommendItem')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('SceneRecommendItem') is not None:
            self.scene_recommend_item = m.get('SceneRecommendItem')
        if m.get('SceneWeightItem') is not None:
            self.scene_weight_item = m.get('SceneWeightItem')
        return self


class ListItemsResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        status: str = None,
        pub_time: str = None,
        expire_time: str = None,
        item_type: str = None,
        author: str = None,
        category_path: str = None,
        item_id: str = None,
        shop_id: str = None,
        brand_id: str = None,
        channel: str = None,
        duration: str = None,
        title: str = None,
    ):
        self.status = status
        self.pub_time = pub_time
        self.expire_time = expire_time
        self.item_type = item_type
        self.author = author
        self.category_path = category_path
        self.item_id = item_id
        self.shop_id = shop_id
        self.brand_id = brand_id
        self.channel = channel
        self.duration = duration
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.author is not None:
            result['Author'] = self.author
        if self.category_path is not None:
            result['CategoryPath'] = self.category_path
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.brand_id is not None:
            result['BrandId'] = self.brand_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('CategoryPath') is not None:
            self.category_path = m.get('CategoryPath')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('BrandId') is not None:
            self.brand_id = m.get('BrandId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListItemsResponseBodyResult(TeaModel):
    def __init__(
        self,
        total: ListItemsResponseBodyResultTotal = None,
        detail: List[ListItemsResponseBodyResultDetail] = None,
    ):
        self.total = total
        self.detail = detail

    def validate(self):
        if self.total:
            self.total.validate()
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total is not None:
            result['Total'] = self.total.to_map()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            temp_model = ListItemsResponseBodyResultTotal()
            self.total = temp_model.from_map(m['Total'])
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = ListItemsResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class ListItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListItemsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListItemsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListItemsResponseBody = None,
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
            temp_model = ListItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogsRequest(TeaModel):
    def __init__(
        self,
        query_params: str = None,
        start_time: int = None,
        end_time: int = None,
        page: int = None,
        size: int = None,
    ):
        self.query_params = query_params
        self.start_time = start_time
        self.end_time = end_time
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.query_params is not None:
            result['QueryParams'] = self.query_params
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryParams') is not None:
            self.query_params = m.get('QueryParams')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListLogsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        headers: ListLogsResponseBodyHeaders = None,
        result: List[Dict[str, Any]] = None,
    ):
        self.request_id = request_id
        self.headers = headers
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListLogsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ListLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLogsResponseBody = None,
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
            temp_model = ListLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMixResponseBodyResultParameterSettings(TeaModel):
    def __init__(
        self,
        value: int = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListMixResponseBodyResultParameter(TeaModel):
    def __init__(
        self,
        settings: List[ListMixResponseBodyResultParameterSettings] = None,
    ):
        self.settings = settings

    def validate(self):
        if self.settings:
            for k in self.settings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Settings'] = []
        if self.settings is not None:
            for k in self.settings:
                result['Settings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.settings = []
        if m.get('Settings') is not None:
            for k in m.get('Settings'):
                temp_model = ListMixResponseBodyResultParameterSettings()
                self.settings.append(temp_model.from_map(k))
        return self


class ListMixResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        gmt_modified: str = None,
        parameter: ListMixResponseBodyResultParameter = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Parameter') is not None:
            temp_model = ListMixResponseBodyResultParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class ListMixResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[ListMixResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListMixResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListMixResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMixResponseBody = None,
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
            temp_model = ListMixResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRuleConditionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        selection_operation: str = None,
        select_value: str = None,
        select_type: str = None,
    ):
        self.selection_operation = selection_operation
        self.select_value = select_value
        self.select_type = select_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.selection_operation is not None:
            result['SelectionOperation'] = self.selection_operation
        if self.select_value is not None:
            result['SelectValue'] = self.select_value
        if self.select_type is not None:
            result['SelectType'] = self.select_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SelectionOperation') is not None:
            self.selection_operation = m.get('SelectionOperation')
        if m.get('SelectValue') is not None:
            self.select_value = m.get('SelectValue')
        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')
        return self


class ListRuleConditionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListRuleConditionsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRuleConditionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRuleConditionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRuleConditionsResponseBody = None,
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
            temp_model = ListRuleConditionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        rule_type: str = None,
        status: str = None,
        page: int = None,
        size: int = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.scene_id = scene_id
        self.rule_type = rule_type
        self.status = status
        self.page = page
        self.size = size
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ListRulesResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        rule_id: str = None,
    ):
        self.status = status
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListRulesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRulesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRulesResponseBody = None,
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
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRuleTasksRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListRuleTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        finish_time: int = None,
        finish_rate: int = None,
    ):
        self.finish_time = finish_time
        self.finish_rate = finish_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.finish_rate is not None:
            result['FinishRate'] = self.finish_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('FinishRate') is not None:
            self.finish_rate = m.get('FinishRate')
        return self


class ListRuleTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListRuleTasksResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListRuleTasksResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRuleTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRuleTasksResponseBody = None,
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
            temp_model = ListRuleTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSceneItemsRequest(TeaModel):
    def __init__(
        self,
        operation_rule_id: str = None,
        selection_rule_id: str = None,
        page: int = None,
        size: int = None,
        preview_type: str = None,
        query_count: int = None,
    ):
        self.operation_rule_id = operation_rule_id
        self.selection_rule_id = selection_rule_id
        self.page = page
        self.size = size
        self.preview_type = preview_type
        self.query_count = query_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operation_rule_id is not None:
            result['OperationRuleId'] = self.operation_rule_id
        if self.selection_rule_id is not None:
            result['SelectionRuleId'] = self.selection_rule_id
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.preview_type is not None:
            result['PreviewType'] = self.preview_type
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationRuleId') is not None:
            self.operation_rule_id = m.get('OperationRuleId')
        if m.get('SelectionRuleId') is not None:
            self.selection_rule_id = m.get('SelectionRuleId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('PreviewType') is not None:
            self.preview_type = m.get('PreviewType')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        return self


class ListSceneItemsResponseBodyResultTotal(TeaModel):
    def __init__(
        self,
        weight_item: int = None,
        instance_recommend_item: int = None,
        total_count: int = None,
        scene_recommend_item: int = None,
        scene_weight_item: int = None,
    ):
        self.weight_item = weight_item
        self.instance_recommend_item = instance_recommend_item
        self.total_count = total_count
        self.scene_recommend_item = scene_recommend_item
        self.scene_weight_item = scene_weight_item

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.weight_item is not None:
            result['WeightItem'] = self.weight_item
        if self.instance_recommend_item is not None:
            result['InstanceRecommendItem'] = self.instance_recommend_item
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.scene_recommend_item is not None:
            result['SceneRecommendItem'] = self.scene_recommend_item
        if self.scene_weight_item is not None:
            result['SceneWeightItem'] = self.scene_weight_item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WeightItem') is not None:
            self.weight_item = m.get('WeightItem')
        if m.get('InstanceRecommendItem') is not None:
            self.instance_recommend_item = m.get('InstanceRecommendItem')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('SceneRecommendItem') is not None:
            self.scene_recommend_item = m.get('SceneRecommendItem')
        if m.get('SceneWeightItem') is not None:
            self.scene_weight_item = m.get('SceneWeightItem')
        return self


class ListSceneItemsResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        status: str = None,
        pub_time: str = None,
        expire_time: str = None,
        item_type: str = None,
        author: str = None,
        category_path: str = None,
        item_id: str = None,
        shop_id: str = None,
        brand_id: str = None,
        channel: str = None,
        duration: str = None,
        title: str = None,
    ):
        self.status = status
        self.pub_time = pub_time
        self.expire_time = expire_time
        self.item_type = item_type
        self.author = author
        self.category_path = category_path
        self.item_id = item_id
        self.shop_id = shop_id
        self.brand_id = brand_id
        self.channel = channel
        self.duration = duration
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.author is not None:
            result['Author'] = self.author
        if self.category_path is not None:
            result['CategoryPath'] = self.category_path
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.brand_id is not None:
            result['BrandId'] = self.brand_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('CategoryPath') is not None:
            self.category_path = m.get('CategoryPath')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('BrandId') is not None:
            self.brand_id = m.get('BrandId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListSceneItemsResponseBodyResult(TeaModel):
    def __init__(
        self,
        total: ListSceneItemsResponseBodyResultTotal = None,
        detail: List[ListSceneItemsResponseBodyResultDetail] = None,
    ):
        self.total = total
        self.detail = detail

    def validate(self):
        if self.total:
            self.total.validate()
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total is not None:
            result['Total'] = self.total.to_map()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            temp_model = ListSceneItemsResponseBodyResultTotal()
            self.total = temp_model.from_map(m['Total'])
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = ListSceneItemsResponseBodyResultDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class ListSceneItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListSceneItemsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListSceneItemsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListSceneItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSceneItemsResponseBody = None,
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
            temp_model = ListSceneItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenesRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListScenesResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        gmt_create: str = None,
        scene_id: str = None,
        gmt_modified: str = None,
    ):
        self.status = status
        self.gmt_create = gmt_create
        self.scene_id = scene_id
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class ListScenesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListScenesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListScenesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListScenesResponseBody = None,
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
            temp_model = ListScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUmengAppkeysResponseBodyResult(TeaModel):
    def __init__(
        self,
        platform: str = None,
        name: str = None,
        appkey: str = None,
    ):
        self.platform = platform
        self.name = name
        self.appkey = appkey

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.name is not None:
            result['Name'] = self.name
        if self.appkey is not None:
            result['Appkey'] = self.appkey
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Appkey') is not None:
            self.appkey = m.get('Appkey')
        return self


class ListUmengAppkeysResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[ListUmengAppkeysResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListUmengAppkeysResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListUmengAppkeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUmengAppkeysResponseBody = None,
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
            temp_model = ListUmengAppkeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceResponseBodyResultMeta(TeaModel):
    def __init__(
        self,
        type: str = None,
        table_name: str = None,
        project_name: str = None,
        bucket_name: str = None,
        path: str = None,
        partition: str = None,
        timestamp: int = None,
        access_key_id: str = None,
    ):
        self.type = type
        self.table_name = table_name
        self.project_name = project_name
        self.bucket_name = bucket_name
        self.path = path
        self.partition = partition
        self.timestamp = timestamp
        self.access_key_id = access_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.path is not None:
            result['Path'] = self.path
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        return self


class ModifyDataSourceResponseBodyResult(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        meta: ModifyDataSourceResponseBodyResultMeta = None,
        gmt_create: str = None,
        gmt_modified: str = None,
    ):
        self.table_name = table_name
        self.meta = meta
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Meta') is not None:
            temp_model = ModifyDataSourceResponseBodyResultMeta()
            self.meta = temp_model.from_map(m['Meta'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class ModifyDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: ModifyDataSourceResponseBodyResult = None,
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
            temp_model = ModifyDataSourceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifyDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDataSourceResponseBody = None,
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
            temp_model = ModifyDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiversifyResponseBodyResultParameter(TeaModel):
    def __init__(
        self,
        window: int = None,
        category_index: int = None,
    ):
        self.window = window
        self.category_index = category_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.window is not None:
            result['Window'] = self.window
        if self.category_index is not None:
            result['CategoryIndex'] = self.category_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Window') is not None:
            self.window = m.get('Window')
        if m.get('CategoryIndex') is not None:
            self.category_index = m.get('CategoryIndex')
        return self


class ModifyDiversifyResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        gmt_modified: str = None,
        parameter: ModifyDiversifyResponseBodyResultParameter = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Parameter') is not None:
            temp_model = ModifyDiversifyResponseBodyResultParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class ModifyDiversifyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: ModifyDiversifyResponseBodyResult = None,
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
            temp_model = ModifyDiversifyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifyDiversifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDiversifyResponseBody = None,
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
            temp_model = ModifyDiversifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyExposureSettingsResponseBodyResult(TeaModel):
    def __init__(
        self,
        duration_seconds: int = None,
        scenario_based: bool = None,
    ):
        self.duration_seconds = duration_seconds
        self.scenario_based = scenario_based

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.scenario_based is not None:
            result['ScenarioBased'] = self.scenario_based
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('ScenarioBased') is not None:
            self.scenario_based = m.get('ScenarioBased')
        return self


class ModifyExposureSettingsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: ModifyExposureSettingsResponseBodyResult = None,
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
            temp_model = ModifyExposureSettingsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifyExposureSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyExposureSettingsResponseBody = None,
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
            temp_model = ModifyExposureSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        commodity_code: str = None,
        charge_type: str = None,
        instance_id: str = None,
        gmt_modified: str = None,
        lock_mode: str = None,
        region_id: str = None,
        data_set_version: str = None,
        industry: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        name: str = None,
        scene: str = None,
    ):
        self.status = status
        self.type = type
        self.commodity_code = commodity_code
        self.charge_type = charge_type
        self.instance_id = instance_id
        self.gmt_modified = gmt_modified
        self.lock_mode = lock_mode
        self.region_id = region_id
        self.data_set_version = data_set_version
        self.industry = industry
        self.expired_time = expired_time
        self.gmt_create = gmt_create
        self.name = name
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.data_set_version is not None:
            result['DataSetVersion'] = self.data_set_version
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DataSetVersion') is not None:
            self.data_set_version = m.get('DataSetVersion')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class ModifyInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: ModifyInstanceResponseBodyResult = None,
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
            temp_model = ModifyInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifyInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceResponseBody = None,
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
            temp_model = ModifyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ModifyItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyItemsResponseBody = None,
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
            temp_model = ModifyItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMixResponseBodyResultParameterSettings(TeaModel):
    def __init__(
        self,
        value: int = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyMixResponseBodyResultParameter(TeaModel):
    def __init__(
        self,
        settings: List[ModifyMixResponseBodyResultParameterSettings] = None,
    ):
        self.settings = settings

    def validate(self):
        if self.settings:
            for k in self.settings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Settings'] = []
        if self.settings is not None:
            for k in self.settings:
                result['Settings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.settings = []
        if m.get('Settings') is not None:
            for k in m.get('Settings'):
                temp_model = ModifyMixResponseBodyResultParameterSettings()
                self.settings.append(temp_model.from_map(k))
        return self


class ModifyMixResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        gmt_modified: str = None,
        parameter: ModifyMixResponseBodyResultParameter = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Parameter') is not None:
            temp_model = ModifyMixResponseBodyResultParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class ModifyMixResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: ModifyMixResponseBodyResult = None,
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
            temp_model = ModifyMixResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifyMixResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyMixResponseBody = None,
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
            temp_model = ModifyMixResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        gmt_create: str = None,
        rule_meta: Dict[str, Any] = None,
        gmt_modified: str = None,
        rule_id: str = None,
    ):
        self.status = status
        self.gmt_create = gmt_create
        self.rule_meta = rule_meta
        self.gmt_modified = gmt_modified
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.rule_meta is not None:
            result['RuleMeta'] = self.rule_meta
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('RuleMeta') is not None:
            self.rule_meta = m.get('RuleMeta')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ModifyRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifyRuleResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ModifyRuleResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRuleResponseBody = None,
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
            temp_model = ModifyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySceneResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        gmt_create: str = None,
        scene_id: str = None,
        gmt_modified: str = None,
    ):
        self.status = status
        self.gmt_create = gmt_create
        self.scene_id = scene_id
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class ModifySceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifySceneResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ModifySceneResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifySceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySceneResponseBody = None,
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
            temp_model = ModifySceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishRuleRequest(TeaModel):
    def __init__(
        self,
        rule_type: str = None,
        scene_id: str = None,
    ):
        self.rule_type = rule_type
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class PublishRuleResponseBodyResult(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class PublishRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: PublishRuleResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = PublishRuleResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class PublishRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishRuleResponseBody = None,
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
            temp_model = PublishRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushDocumentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class PushDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushDocumentResponseBody = None,
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
            temp_model = PushDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushInterventionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class PushInterventionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushInterventionResponseBody = None,
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
            temp_model = PushInterventionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataMessageRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        cmd_type: str = None,
        item_id: str = None,
        item_type: str = None,
        user_id: str = None,
        user_type: str = None,
        page: int = None,
        size: int = None,
        trace_id: str = None,
        scene_id: str = None,
        bhv_type: str = None,
        message_source: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.cmd_type = cmd_type
        self.item_id = item_id
        self.item_type = item_type
        self.user_id = user_id
        self.user_type = user_type
        self.page = page
        self.size = size
        self.trace_id = trace_id
        self.scene_id = scene_id
        self.bhv_type = bhv_type
        self.message_source = message_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.cmd_type is not None:
            result['CmdType'] = self.cmd_type
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.bhv_type is not None:
            result['BhvType'] = self.bhv_type
        if self.message_source is not None:
            result['MessageSource'] = self.message_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CmdType') is not None:
            self.cmd_type = m.get('CmdType')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('BhvType') is not None:
            self.bhv_type = m.get('BhvType')
        if m.get('MessageSource') is not None:
            self.message_source = m.get('MessageSource')
        return self


class QueryDataMessageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: Dict[str, Any] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class QueryDataMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDataMessageResponseBody = None,
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
            temp_model = QueryDataMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataMessageStatisticsRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        cmd_type: str = None,
        item_id: str = None,
        item_type: str = None,
        user_id: str = None,
        user_type: str = None,
        trace_id: str = None,
        scene_id: str = None,
        bhv_type: str = None,
        message_source: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.cmd_type = cmd_type
        self.item_id = item_id
        self.item_type = item_type
        self.user_id = user_id
        self.user_type = user_type
        self.trace_id = trace_id
        self.scene_id = scene_id
        self.bhv_type = bhv_type
        self.message_source = message_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.cmd_type is not None:
            result['CmdType'] = self.cmd_type
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.bhv_type is not None:
            result['BhvType'] = self.bhv_type
        if self.message_source is not None:
            result['MessageSource'] = self.message_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CmdType') is not None:
            self.cmd_type = m.get('CmdType')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('BhvType') is not None:
            self.bhv_type = m.get('BhvType')
        if m.get('MessageSource') is not None:
            self.message_source = m.get('MessageSource')
        return self


class QueryDataMessageStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: Dict[str, Any] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class QueryDataMessageStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDataMessageStatisticsResponseBody = None,
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
            temp_model = QueryDataMessageStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExceptionHistoryRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        type: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryExceptionHistoryResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: Dict[str, Any] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class QueryExceptionHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryExceptionHistoryResponseBody = None,
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
            temp_model = QueryExceptionHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRawDataRequest(TeaModel):
    def __init__(
        self,
        item_id: str = None,
        item_type: str = None,
        user_id: str = None,
        user_type: str = None,
    ):
        self.item_id = item_id
        self.item_type = item_type
        self.user_id = user_id
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class QueryRawDataResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: Dict[str, Any] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class QueryRawDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRawDataResponseBody = None,
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
            temp_model = QueryRawDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySingleAggregationReportResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: Dict[str, Any] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class QuerySingleAggregationReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySingleAggregationReportResponseBody = None,
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
            temp_model = QuerySingleAggregationReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySingleReportRequest(TeaModel):
    def __init__(
        self,
        report_type: str = None,
    ):
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        return self


class QuerySingleReportResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: Dict[str, Any] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class QuerySingleReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySingleReportResponseBody = None,
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
            temp_model = QuerySingleReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySyncReportAggregationRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
    ):
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class QuerySyncReportAggregationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: Dict[str, Any] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class QuerySyncReportAggregationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySyncReportAggregationResponseBody = None,
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
            temp_model = QuerySyncReportAggregationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecommendHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        region_id: str = None,
    ):
        self.common_headers = common_headers
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RecommendRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        user_id: str = None,
        ip: str = None,
        imei: str = None,
        return_count: int = None,
        items: str = None,
    ):
        self.scene_id = scene_id
        self.user_id = user_id
        self.ip = ip
        self.imei = imei
        self.return_count = return_count
        self.items = items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.imei is not None:
            result['Imei'] = self.imei
        if self.return_count is not None:
            result['ReturnCount'] = self.return_count
        if self.items is not None:
            result['Items'] = self.items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Imei') is not None:
            self.imei = m.get('Imei')
        if m.get('ReturnCount') is not None:
            self.return_count = m.get('ReturnCount')
        if m.get('Items') is not None:
            self.items = m.get('Items')
        return self


class RecommendResponseBodyResult(TeaModel):
    def __init__(
        self,
        trace_info: str = None,
        weight: float = None,
        match_info: str = None,
        item_type: str = None,
        position: int = None,
        item_id: str = None,
        trace_id: str = None,
    ):
        self.trace_info = trace_info
        self.weight = weight
        self.match_info = match_info
        self.item_type = item_type
        self.position = position
        self.item_id = item_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.trace_info is not None:
            result['TraceInfo'] = self.trace_info
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.match_info is not None:
            result['MatchInfo'] = self.match_info
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.position is not None:
            result['Position'] = self.position
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TraceInfo') is not None:
            self.trace_info = m.get('TraceInfo')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('MatchInfo') is not None:
            self.match_info = m.get('MatchInfo')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RecommendResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: List[RecommendResponseBodyResult] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = RecommendResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class RecommendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecommendResponseBody = None,
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
            temp_model = RecommendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class RunInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunInstanceResponseBody = None,
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
            temp_model = RunInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDataSetResponseBodyResult(TeaModel):
    def __init__(
        self,
        state: str = None,
        gmt_create: int = None,
        version_id: str = None,
        instance_id: str = None,
        gmt_modified: int = None,
    ):
        self.state = state
        self.gmt_create = gmt_create
        self.version_id = version_id
        self.instance_id = instance_id
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class StopDataSetResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: StopDataSetResponseBodyResult = None,
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
            temp_model = StopDataSetResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class StopDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDataSetResponseBody = None,
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
            temp_model = StopDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpgradeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: UpgradeInstanceResponseBodyResult = None,
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
            temp_model = UpgradeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpgradeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeInstanceResponseBody = None,
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
            temp_model = UpgradeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class ValidateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateInstanceResponseBody = None,
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
            temp_model = ValidateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


