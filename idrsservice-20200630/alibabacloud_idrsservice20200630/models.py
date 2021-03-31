# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CheckServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CheckServiceLinkedRoleResponseBodyData(TeaModel):
    def __init__(
        self,
        has_role: bool = None,
    ):
        self.has_role = has_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_role is not None:
            result['HasRole'] = self.has_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasRole') is not None:
            self.has_role = m.get('HasRole')
        return self


class CheckServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CheckServiceLinkedRoleResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CheckServiceLinkedRoleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CheckServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckServiceLinkedRoleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CheckServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        package_name: str = None,
        department_id: str = None,
        client_token: str = None,
    ):
        self.name = name
        self.package_name = package_name
        self.department_id = department_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateAppResponseBodyData(TeaModel):
    def __init__(
        self,
        creator_name: str = None,
        disabled: bool = None,
        created_at: str = None,
        name: str = None,
        id: str = None,
    ):
        self.creator_name = creator_name
        self.disabled = disabled
        self.created_at = created_at
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateAppResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDepartmentRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        name: str = None,
        client_token: str = None,
    ):
        self.description = description
        self.label = label
        self.name = name
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDepartmentResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        created_at: str = None,
        name: str = None,
        id: str = None,
    ):
        self.description = description
        self.created_at = created_at
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateDepartmentResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateDepartmentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDepartmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDetectProcessRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        draft: str = None,
        content: str = None,
    ):
        self.name = name
        self.draft = draft
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class CreateDetectProcessResponseBodyData(TeaModel):
    def __init__(
        self,
        draft: str = None,
        created_at: str = None,
        disabled: bool = None,
        md_5: str = None,
        name: str = None,
        content: str = None,
        id: str = None,
    ):
        self.draft = draft
        self.created_at = created_at
        self.disabled = disabled
        self.md_5 = md_5
        self.name = name
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateDetectProcessResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateDetectProcessResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateDetectProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateDetectProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDetectProcessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateDetectProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLiveRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        rtc_code: str = None,
        user_id: str = None,
        client_token: str = None,
        app_id: str = None,
    ):
        self.name = name
        self.rtc_code = rtc_code
        self.user_id = user_id
        self.client_token = client_token
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class CreateLiveResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        channel: str = None,
        name: str = None,
        id: str = None,
    ):
        self.created_at = created_at
        self.channel = channel
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateLiveResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateLiveResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateLiveResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLiveResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLiveDetectionRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        user_id: str = None,
        rule_id: str = None,
        meta_url: str = None,
        client_token: str = None,
    ):
        self.live_id = live_id
        self.user_id = user_id
        self.rule_id = rule_id
        self.meta_url = meta_url
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateLiveDetectionResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateLiveDetectionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateLiveDetectionResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateLiveDetectionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateLiveDetectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLiveDetectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateLiveDetectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLiveRecordTemplateRequestBackgrounds(TeaModel):
    def __init__(
        self,
        display: int = None,
        url: str = None,
        width: float = None,
        height: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.display = display
        self.url = url
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class CreateLiveRecordTemplateRequestWatermarks(TeaModel):
    def __init__(
        self,
        alpha: float = None,
        display: int = None,
        url: str = None,
        width: float = None,
        height: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.alpha = alpha
        self.display = display
        self.url = url
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.display is not None:
            result['Display'] = self.display
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class CreateLiveRecordTemplateRequestClockWidgets(TeaModel):
    def __init__(
        self,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class CreateLiveRecordTemplateRequest(TeaModel):
    def __init__(
        self,
        rtc_code: str = None,
        name: str = None,
        background_color: int = None,
        backgrounds: List[CreateLiveRecordTemplateRequestBackgrounds] = None,
        watermarks: List[CreateLiveRecordTemplateRequestWatermarks] = None,
        clock_widgets: List[CreateLiveRecordTemplateRequestClockWidgets] = None,
    ):
        self.rtc_code = rtc_code
        self.name = name
        self.background_color = background_color
        self.backgrounds = backgrounds
        self.watermarks = watermarks
        self.clock_widgets = clock_widgets

    def validate(self):
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        if self.name is not None:
            result['Name'] = self.name
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = CreateLiveRecordTemplateRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = CreateLiveRecordTemplateRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = CreateLiveRecordTemplateRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        return self


class CreateLiveRecordTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        rtc_code: str = None,
        name: str = None,
        background_color: int = None,
        backgrounds_shrink: str = None,
        watermarks_shrink: str = None,
        clock_widgets_shrink: str = None,
    ):
        self.rtc_code = rtc_code
        self.name = name
        self.background_color = background_color
        self.backgrounds_shrink = backgrounds_shrink
        self.watermarks_shrink = watermarks_shrink
        self.clock_widgets_shrink = clock_widgets_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        if self.name is not None:
            result['Name'] = self.name
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.backgrounds_shrink is not None:
            result['Backgrounds'] = self.backgrounds_shrink
        if self.watermarks_shrink is not None:
            result['Watermarks'] = self.watermarks_shrink
        if self.clock_widgets_shrink is not None:
            result['ClockWidgets'] = self.clock_widgets_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('Backgrounds') is not None:
            self.backgrounds_shrink = m.get('Backgrounds')
        if m.get('Watermarks') is not None:
            self.watermarks_shrink = m.get('Watermarks')
        if m.get('ClockWidgets') is not None:
            self.clock_widgets_shrink = m.get('ClockWidgets')
        return self


class CreateLiveRecordTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
    ):
        self.created_at = created_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateLiveRecordTemplateResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateLiveRecordTemplateResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateLiveRecordTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateLiveRecordTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLiveRecordTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateLiveRecordTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        content: str = None,
        client_token: str = None,
    ):
        self.name = name
        self.content = content
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        content: str = None,
        id: str = None,
    ):
        self.name = name
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateRuleResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStatisticsRecordRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        app_id: str = None,
        device_type: int = None,
        begin_at: str = None,
        end_at: str = None,
        client_token: str = None,
    ):
        self.device_id = device_id
        self.app_id = app_id
        self.device_type = device_type
        self.begin_at = begin_at
        self.end_at = end_at
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.begin_at is not None:
            result['BeginAt'] = self.begin_at
        if self.end_at is not None:
            result['EndAt'] = self.end_at
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('BeginAt') is not None:
            self.begin_at = m.get('BeginAt')
        if m.get('EndAt') is not None:
            self.end_at = m.get('EndAt')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateStatisticsRecordResponseBody(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStatisticsRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateStatisticsRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateStatisticsRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStatisticsTaskRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        client_token: str = None,
        department_id: List[str] = None,
    ):
        self.date_from = date_from
        self.date_to = date_to
        self.client_token = client_token
        self.department_id = department_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['DateFrom'] = self.date_from
        if self.date_to is not None:
            result['DateTo'] = self.date_to
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateFrom') is not None:
            self.date_from = m.get('DateFrom')
        if m.get('DateTo') is not None:
            self.date_to = m.get('DateTo')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        return self


class CreateStatisticsTaskResponseBody(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStatisticsTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateStatisticsTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateStatisticsTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskGroupRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        expire_at: str = None,
        group_name: str = None,
        rule_id: str = None,
        runnable_time_from: str = None,
        runnable_time_to: str = None,
        trigger_period: str = None,
        client_token: str = None,
        day: List[int] = None,
        video_url: List[str] = None,
    ):
        self.app_id = app_id
        self.expire_at = expire_at
        self.group_name = group_name
        self.rule_id = rule_id
        self.runnable_time_from = runnable_time_from
        self.runnable_time_to = runnable_time_to
        self.trigger_period = trigger_period
        self.client_token = client_token
        self.day = day
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.runnable_time_from is not None:
            result['RunnableTimeFrom'] = self.runnable_time_from
        if self.runnable_time_to is not None:
            result['RunnableTimeTo'] = self.runnable_time_to
        if self.trigger_period is not None:
            result['TriggerPeriod'] = self.trigger_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.day is not None:
            result['Day'] = self.day
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RunnableTimeFrom') is not None:
            self.runnable_time_from = m.get('RunnableTimeFrom')
        if m.get('RunnableTimeTo') is not None:
            self.runnable_time_to = m.get('RunnableTimeTo')
        if m.get('TriggerPeriod') is not None:
            self.trigger_period = m.get('TriggerPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class CreateTaskGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        completed_tasks: int = None,
        total_tasks: int = None,
        created_at: str = None,
        name: str = None,
        task_ids: List[str] = None,
        id: str = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        self.status = status
        self.completed_tasks = completed_tasks
        self.total_tasks = total_tasks
        self.created_at = created_at
        self.name = name
        self.task_ids = task_ids
        self.id = id
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.completed_tasks is not None:
            result['CompletedTasks'] = self.completed_tasks
        if self.total_tasks is not None:
            result['TotalTasks'] = self.total_tasks
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CompletedTasks') is not None:
            self.completed_tasks = m.get('CompletedTasks')
        if m.get('TotalTasks') is not None:
            self.total_tasks = m.get('TotalTasks')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class CreateTaskGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateTaskGroupResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateTaskGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateTaskGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTaskGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateTaskGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserDepartmentsRequest(TeaModel):
    def __init__(
        self,
        user_id: List[str] = None,
        department_id: List[str] = None,
        client_token: str = None,
    ):
        self.user_id = user_id
        self.department_id = department_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateUserDepartmentsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateUserDepartmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserDepartmentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateUserDepartmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDepartmentRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDepartmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDetectProcessRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteDetectProcessResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteDetectProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDetectProcessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteDetectProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLiveRecordTemplateRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteLiveRecordTemplateResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteLiveRecordTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLiveRecordTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteLiveRecordTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        name: str = None,
        content: str = None,
        id: str = None,
    ):
        self.created_at = created_at
        self.name = name
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DeleteRuleResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeleteRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteUserResponseBodyErrors(TeaModel):
    def __init__(
        self,
        message: str = None,
        field: str = None,
    ):
        self.message = message
        self.field = field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.field is not None:
            result['Field'] = self.field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        errors: List[DeleteUserResponseBodyErrors] = None,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: str = None,
    ):
        self.errors = errors
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = DeleteUserResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserDepartmentsRequest(TeaModel):
    def __init__(
        self,
        user_id: List[str] = None,
        department_id: List[str] = None,
    ):
        self.user_id = user_id
        self.department_id = department_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        return self


class DeleteUserDepartmentsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteUserDepartmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserDepartmentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteUserDepartmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExitLiveRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        user_id: str = None,
        rtc_code: str = None,
    ):
        self.channel = channel
        self.user_id = user_id
        self.rtc_code = rtc_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        return self


class ExitLiveResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
    ):
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ExitLiveResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ExitLiveResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ExitLiveResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ExitLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExitLiveResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ExitLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        package_name: str = None,
        device_id: str = None,
    ):
        self.id = id
        self.package_name = package_name
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class GetAppResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        disabled: str = None,
        name: str = None,
    ):
        self.created_at = created_at
        self.disabled = disabled
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetAppResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBatchSignedUrlRequest(TeaModel):
    def __init__(
        self,
        file_url_list: List[str] = None,
    ):
        self.file_url_list = file_url_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url_list is not None:
            result['FileUrlList'] = self.file_url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrlList') is not None:
            self.file_url_list = m.get('FileUrlList')
        return self


class GetBatchSignedUrlResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[str] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetBatchSignedUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBatchSignedUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetBatchSignedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDepartmentRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDepartmentResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        created_at: str = None,
        updated_at: str = None,
        name: str = None,
        id: str = None,
    ):
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetDepartmentResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetDepartmentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDepartmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectEvaluationRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetDetectEvaluationResponseBodyDataEvaluationItemList(TeaModel):
    def __init__(
        self,
        success_rate: str = None,
        handle_count: int = None,
        name: str = None,
        success_count: int = None,
    ):
        self.success_rate = success_rate
        self.handle_count = handle_count
        self.name = name
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_rate is not None:
            result['SuccessRate'] = self.success_rate
        if self.handle_count is not None:
            result['HandleCount'] = self.handle_count
        if self.name is not None:
            result['Name'] = self.name
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuccessRate') is not None:
            self.success_rate = m.get('SuccessRate')
        if m.get('HandleCount') is not None:
            self.handle_count = m.get('HandleCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class GetDetectEvaluationResponseBodyData(TeaModel):
    def __init__(
        self,
        day: str = None,
        evaluation_item_list: List[GetDetectEvaluationResponseBodyDataEvaluationItemList] = None,
    ):
        self.day = day
        self.evaluation_item_list = evaluation_item_list

    def validate(self):
        if self.evaluation_item_list:
            for k in self.evaluation_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        result['EvaluationItemList'] = []
        if self.evaluation_item_list is not None:
            for k in self.evaluation_item_list:
                result['EvaluationItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        self.evaluation_item_list = []
        if m.get('EvaluationItemList') is not None:
            for k in m.get('EvaluationItemList'):
                temp_model = GetDetectEvaluationResponseBodyDataEvaluationItemList()
                self.evaluation_item_list.append(temp_model.from_map(k))
        return self


class GetDetectEvaluationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetDetectEvaluationResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetDetectEvaluationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetDetectEvaluationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDetectEvaluationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetDetectEvaluationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDetectionResponseBodyDataTasks(TeaModel):
    def __init__(
        self,
        status: str = None,
        video_meta_url: str = None,
        created_at: str = None,
        id: str = None,
        video_url: str = None,
    ):
        self.status = status
        self.video_meta_url = video_meta_url
        self.created_at = created_at
        self.id = id
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.video_meta_url is not None:
            result['VideoMetaUrl'] = self.video_meta_url
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoMetaUrl') is not None:
            self.video_meta_url = m.get('VideoMetaUrl')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetDetectionResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        department_name: str = None,
        tasks: List[GetDetectionResponseBodyDataTasks] = None,
        recording_type: str = None,
        created_at: str = None,
        department_id: str = None,
        id: str = None,
        rule_name: str = None,
        rule_id: str = None,
    ):
        self.status = status
        self.department_name = department_name
        self.tasks = tasks
        self.recording_type = recording_type
        self.created_at = created_at
        self.department_id = department_id
        self.id = id
        self.rule_name = rule_name
        self.rule_id = rule_id

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.recording_type is not None:
            result['RecordingType'] = self.recording_type
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = GetDetectionResponseBodyDataTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('RecordingType') is not None:
            self.recording_type = m.get('RecordingType')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetDetectionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetDetectionResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetDetectionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetDetectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDetectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetDetectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectProcessRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDetectProcessResponseBodyData(TeaModel):
    def __init__(
        self,
        draft: str = None,
        created_at: str = None,
        md_5: str = None,
        updated_at: str = None,
        name: str = None,
        new_version: bool = None,
        content: str = None,
        id: str = None,
    ):
        self.draft = draft
        self.created_at = created_at
        self.md_5 = md_5
        self.updated_at = updated_at
        self.name = name
        self.new_version = new_version
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.new_version is not None:
            result['NewVersion'] = self.new_version
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewVersion') is not None:
            self.new_version = m.get('NewVersion')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDetectProcessResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetDetectProcessResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetDetectProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetDetectProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDetectProcessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetDetectProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectProcessJsonFileRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDetectProcessJsonFileResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetDetectProcessJsonFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDetectProcessJsonFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetDetectProcessJsonFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectProcessTemplateResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetDetectProcessTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDetectProcessTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetDetectProcessTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGlobalConfigRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetGlobalConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetGlobalConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGlobalConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetGlobalConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRecordTemplateRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetLiveRecordTemplateResponseBodyDataBackgrounds(TeaModel):
    def __init__(
        self,
        display: int = None,
        x: float = None,
        y: float = None,
        width: float = None,
        height: float = None,
        zorder: int = None,
    ):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class GetLiveRecordTemplateResponseBodyDataWatermarks(TeaModel):
    def __init__(
        self,
        url: str = None,
        alpha: float = None,
        display: int = None,
        x: float = None,
        y: float = None,
        width: float = None,
        height: float = None,
        zorder: int = None,
    ):
        self.url = url
        self.alpha = alpha
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.display is not None:
            result['Display'] = self.display
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class GetLiveRecordTemplateResponseBodyDataClockWidgets(TeaModel):
    def __init__(
        self,
        font_type: int = None,
        font_size: int = None,
        font_color: int = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.font_type = font_type
        self.font_size = font_size
        self.font_color = font_color
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class GetLiveRecordTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        disabled: str = None,
        name: str = None,
        id: str = None,
        rtc_code: str = None,
        description: str = None,
        backgrounds: List[GetLiveRecordTemplateResponseBodyDataBackgrounds] = None,
        watermarks: List[GetLiveRecordTemplateResponseBodyDataWatermarks] = None,
        clock_widgets: List[GetLiveRecordTemplateResponseBodyDataClockWidgets] = None,
    ):
        self.created_at = created_at
        self.disabled = disabled
        self.name = name
        self.id = id
        self.rtc_code = rtc_code
        self.description = description
        self.backgrounds = backgrounds
        self.watermarks = watermarks
        self.clock_widgets = clock_widgets

    def validate(self):
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        if self.description is not None:
            result['Description'] = self.description
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = GetLiveRecordTemplateResponseBodyDataBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = GetLiveRecordTemplateResponseBodyDataWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = GetLiveRecordTemplateResponseBodyDataClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        return self


class GetLiveRecordTemplateResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetLiveRecordTemplateResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetLiveRecordTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetLiveRecordTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLiveRecordTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetLiveRecordTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelSignedUrlRequest(TeaModel):
    def __init__(
        self,
        model_path: List[str] = None,
    ):
        self.model_path = model_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_path is not None:
            result['ModelPath'] = self.model_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelPath') is not None:
            self.model_path = m.get('ModelPath')
        return self


class GetModelSignedUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        public_url: str = None,
        md_5: str = None,
        model_path: str = None,
    ):
        self.public_url = public_url
        self.md_5 = md_5
        self.model_path = model_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public_url is not None:
            result['PublicUrl'] = self.public_url
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.model_path is not None:
            result['ModelPath'] = self.model_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('ModelPath') is not None:
            self.model_path = m.get('ModelPath')
        return self


class GetModelSignedUrlResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetModelSignedUrlResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetModelSignedUrlResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetModelSignedUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetModelSignedUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetModelSignedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPreSignedUrlRequest(TeaModel):
    def __init__(
        self,
        prefix: str = None,
    ):
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class GetPreSignedUrlResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetPreSignedUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPreSignedUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetPreSignedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        name: str = None,
        content: str = None,
        id: str = None,
    ):
        self.created_at = created_at
        self.name = name
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetRuleResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceConfigurationRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetServiceConfigurationResponseBodyData(TeaModel):
    def __init__(
        self,
        live_record_all: bool = None,
        live_record_layout: int = None,
        live_record_max_client: int = None,
        live_record_every_one: bool = None,
        live_record_task_profile: str = None,
        live_record_video_resolution: int = None,
        task_item_queue_size: int = None,
        client_queue_size: int = None,
    ):
        self.live_record_all = live_record_all
        self.live_record_layout = live_record_layout
        self.live_record_max_client = live_record_max_client
        self.live_record_every_one = live_record_every_one
        self.live_record_task_profile = live_record_task_profile
        self.live_record_video_resolution = live_record_video_resolution
        self.task_item_queue_size = task_item_queue_size
        self.client_queue_size = client_queue_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_record_all is not None:
            result['LiveRecordAll'] = self.live_record_all
        if self.live_record_layout is not None:
            result['LiveRecordLayout'] = self.live_record_layout
        if self.live_record_max_client is not None:
            result['LiveRecordMaxClient'] = self.live_record_max_client
        if self.live_record_every_one is not None:
            result['LiveRecordEveryOne'] = self.live_record_every_one
        if self.live_record_task_profile is not None:
            result['LiveRecordTaskProfile'] = self.live_record_task_profile
        if self.live_record_video_resolution is not None:
            result['LiveRecordVideoResolution'] = self.live_record_video_resolution
        if self.task_item_queue_size is not None:
            result['TaskItemQueueSize'] = self.task_item_queue_size
        if self.client_queue_size is not None:
            result['ClientQueueSize'] = self.client_queue_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveRecordAll') is not None:
            self.live_record_all = m.get('LiveRecordAll')
        if m.get('LiveRecordLayout') is not None:
            self.live_record_layout = m.get('LiveRecordLayout')
        if m.get('LiveRecordMaxClient') is not None:
            self.live_record_max_client = m.get('LiveRecordMaxClient')
        if m.get('LiveRecordEveryOne') is not None:
            self.live_record_every_one = m.get('LiveRecordEveryOne')
        if m.get('LiveRecordTaskProfile') is not None:
            self.live_record_task_profile = m.get('LiveRecordTaskProfile')
        if m.get('LiveRecordVideoResolution') is not None:
            self.live_record_video_resolution = m.get('LiveRecordVideoResolution')
        if m.get('TaskItemQueueSize') is not None:
            self.task_item_queue_size = m.get('TaskItemQueueSize')
        if m.get('ClientQueueSize') is not None:
            self.client_queue_size = m.get('ClientQueueSize')
        return self


class GetServiceConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetServiceConfigurationResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetServiceConfigurationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetServiceConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetServiceConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetServiceConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSignedUrlRequest(TeaModel):
    def __init__(
        self,
        file_url: str = None,
    ):
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class GetSignedUrlResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetSignedUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSignedUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetSignedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSlrConfigurationRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetSlrConfigurationResponseBodyData(TeaModel):
    def __init__(
        self,
        mq_group_id: str = None,
        mq_topic: str = None,
        mq_instance_id: str = None,
        mq_event_list: List[str] = None,
        mq_topic_test: str = None,
        mq_group_id_test: str = None,
        mq_endpoint: str = None,
        mq_subscribe: bool = None,
    ):
        self.mq_group_id = mq_group_id
        self.mq_topic = mq_topic
        self.mq_instance_id = mq_instance_id
        self.mq_event_list = mq_event_list
        self.mq_topic_test = mq_topic_test
        self.mq_group_id_test = mq_group_id_test
        self.mq_endpoint = mq_endpoint
        self.mq_subscribe = mq_subscribe

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mq_group_id is not None:
            result['MqGroupId'] = self.mq_group_id
        if self.mq_topic is not None:
            result['MqTopic'] = self.mq_topic
        if self.mq_instance_id is not None:
            result['MqInstanceId'] = self.mq_instance_id
        if self.mq_event_list is not None:
            result['MqEventList'] = self.mq_event_list
        if self.mq_topic_test is not None:
            result['MqTopicTest'] = self.mq_topic_test
        if self.mq_group_id_test is not None:
            result['MqGroupIdTest'] = self.mq_group_id_test
        if self.mq_endpoint is not None:
            result['MqEndpoint'] = self.mq_endpoint
        if self.mq_subscribe is not None:
            result['MqSubscribe'] = self.mq_subscribe
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqGroupId') is not None:
            self.mq_group_id = m.get('MqGroupId')
        if m.get('MqTopic') is not None:
            self.mq_topic = m.get('MqTopic')
        if m.get('MqInstanceId') is not None:
            self.mq_instance_id = m.get('MqInstanceId')
        if m.get('MqEventList') is not None:
            self.mq_event_list = m.get('MqEventList')
        if m.get('MqTopicTest') is not None:
            self.mq_topic_test = m.get('MqTopicTest')
        if m.get('MqGroupIdTest') is not None:
            self.mq_group_id_test = m.get('MqGroupIdTest')
        if m.get('MqEndpoint') is not None:
            self.mq_endpoint = m.get('MqEndpoint')
        if m.get('MqSubscribe') is not None:
            self.mq_subscribe = m.get('MqSubscribe')
        return self


class GetSlrConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetSlrConfigurationResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetSlrConfigurationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetSlrConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSlrConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetSlrConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStatisticsRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        department_id: List[str] = None,
    ):
        self.date_from = date_from
        self.date_to = date_to
        self.department_id = department_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['DateFrom'] = self.date_from
        if self.date_to is not None:
            result['DateTo'] = self.date_to
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateFrom') is not None:
            self.date_from = m.get('DateFrom')
        if m.get('DateTo') is not None:
            self.date_to = m.get('DateTo')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        return self


class GetStatisticsResponseBodyDataItemsDetail(TeaModel):
    def __init__(
        self,
        department_name: str = None,
        cloud_count: int = None,
        department_id: str = None,
        month: int = None,
        client_count: int = None,
    ):
        self.department_name = department_name
        self.cloud_count = cloud_count
        self.department_id = department_id
        self.month = month
        self.client_count = client_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.cloud_count is not None:
            result['CloudCount'] = self.cloud_count
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.month is not None:
            result['Month'] = self.month
        if self.client_count is not None:
            result['ClientCount'] = self.client_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('CloudCount') is not None:
            self.cloud_count = m.get('CloudCount')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('ClientCount') is not None:
            self.client_count = m.get('ClientCount')
        return self


class GetStatisticsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        department_name: str = None,
        cloud_count: int = None,
        month: str = None,
        client_count: int = None,
        detail: List[GetStatisticsResponseBodyDataItemsDetail] = None,
    ):
        self.department_name = department_name
        self.cloud_count = cloud_count
        self.month = month
        self.client_count = client_count
        self.detail = detail

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.cloud_count is not None:
            result['CloudCount'] = self.cloud_count
        if self.month is not None:
            result['Month'] = self.month
        if self.client_count is not None:
            result['ClientCount'] = self.client_count
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('CloudCount') is not None:
            self.cloud_count = m.get('CloudCount')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('ClientCount') is not None:
            self.client_count = m.get('ClientCount')
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = GetStatisticsResponseBodyDataItemsDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class GetStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[GetStatisticsResponseBodyDataItems] = None,
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
                temp_model = GetStatisticsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class GetStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetStatisticsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        created_at: str = None,
        id: str = None,
        video_url: str = None,
    ):
        self.status = status
        self.created_at = created_at
        self.id = id
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetTaskResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskGroupRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        completed_tasks: int = None,
        total_tasks: int = None,
        created_at: str = None,
        name: str = None,
        task_ids: List[str] = None,
        id: str = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        self.status = status
        self.completed_tasks = completed_tasks
        self.total_tasks = total_tasks
        self.created_at = created_at
        self.name = name
        self.task_ids = task_ids
        self.id = id
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.completed_tasks is not None:
            result['CompletedTasks'] = self.completed_tasks
        if self.total_tasks is not None:
            result['TotalTasks'] = self.total_tasks
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CompletedTasks') is not None:
            self.completed_tasks = m.get('CompletedTasks')
        if m.get('TotalTasks') is not None:
            self.total_tasks = m.get('TotalTasks')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetTaskGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetTaskGroupResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetTaskGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetTaskGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTaskGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetTaskGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetUserResponseBodyDataDepartments(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: str = None,
        name: str = None,
        gmt_modified: str = None,
        id: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.name = name
        self.gmt_modified = gmt_modified
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetUserResponseBodyData(TeaModel):
    def __init__(
        self,
        email: str = None,
        phone_number: str = None,
        departments: List[GetUserResponseBodyDataDepartments] = None,
        created_at: str = None,
        updated_at: str = None,
        source: str = None,
        role: str = None,
        name: str = None,
        id: str = None,
        username: str = None,
    ):
        self.email = email
        self.phone_number = phone_number
        self.departments = departments
        self.created_at = created_at
        self.updated_at = updated_at
        self.source = source
        self.role = role
        self.name = name
        self.id = id
        self.username = username

    def validate(self):
        if self.departments:
            for k in self.departments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        result['Departments'] = []
        if self.departments is not None:
            for k in self.departments:
                result['Departments'].append(k.to_map() if k else None)
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.source is not None:
            result['Source'] = self.source
        if self.role is not None:
            result['Role'] = self.role
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        self.departments = []
        if m.get('Departments') is not None:
            for k in m.get('Departments'):
                temp_model = GetUserResponseBodyDataDepartments()
                self.departments.append(temp_model.from_map(k))
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetUserResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class InitializeServiceLinkedRoleResponseBodyData(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        create_success: bool = None,
    ):
        self.error_message = error_message
        self.create_success = create_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.create_success is not None:
            result['CreateSuccess'] = self.create_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('CreateSuccess') is not None:
            self.create_success = m.get('CreateSuccess')
        return self


class InitializeServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: InitializeServiceLinkedRoleResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = InitializeServiceLinkedRoleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class InitializeServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitializeServiceLinkedRoleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = InitializeServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinLiveRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        channel: str = None,
        rtc_code: str = None,
    ):
        self.user_id = user_id
        self.channel = channel
        self.rtc_code = rtc_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        return self


class JoinLiveResponseBodyDataTokenDataTurn(TeaModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class JoinLiveResponseBodyDataTokenData(TeaModel):
    def __init__(
        self,
        turn: JoinLiveResponseBodyDataTokenDataTurn = None,
        token: str = None,
        app_id: str = None,
        nonce: str = None,
        gslb: List[str] = None,
        live_id: str = None,
        user_id: str = None,
        timestamp: int = None,
    ):
        self.turn = turn
        self.token = token
        self.app_id = app_id
        self.nonce = nonce
        self.gslb = gslb
        self.live_id = live_id
        self.user_id = user_id
        self.timestamp = timestamp

    def validate(self):
        if self.turn:
            self.turn.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.turn is not None:
            result['Turn'] = self.turn.to_map()
        if self.token is not None:
            result['Token'] = self.token
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.gslb is not None:
            result['Gslb'] = self.gslb
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Turn') is not None:
            temp_model = JoinLiveResponseBodyDataTokenDataTurn()
            self.turn = temp_model.from_map(m['Turn'])
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class JoinLiveResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        token_data: JoinLiveResponseBodyDataTokenData = None,
    ):
        self.code = code
        self.token_data = token_data

    def validate(self):
        if self.token_data:
            self.token_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.token_data is not None:
            result['TokenData'] = self.token_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('TokenData') is not None:
            temp_model = JoinLiveResponseBodyDataTokenData()
            self.token_data = temp_model.from_map(m['TokenData'])
        return self


class JoinLiveResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: JoinLiveResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = JoinLiveResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class JoinLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinLiveResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = JoinLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        department_name: str = None,
        package_name: str = None,
        created_at: str = None,
        department_id: str = None,
        disabled: bool = None,
        name: str = None,
        id: str = None,
    ):
        self.department_name = department_name
        self.package_name = package_name
        self.created_at = created_at
        self.department_id = department_id
        self.disabled = disabled
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListAppsResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListAppsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListAppsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDepartmentsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_index: int = None,
        page_size: int = None,
        user_id: str = None,
    ):
        self.name = name
        self.page_index = page_index
        self.page_size = page_size
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListDepartmentsResponseBodyDataItemsAdministrators(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
    ):
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDepartmentsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        description: str = None,
        administrators: List[ListDepartmentsResponseBodyDataItemsAdministrators] = None,
        created_at: str = None,
        updated_at: str = None,
        name: str = None,
        id: str = None,
    ):
        self.description = description
        self.administrators = administrators
        self.created_at = created_at
        self.updated_at = updated_at
        self.name = name
        self.id = id

    def validate(self):
        if self.administrators:
            for k in self.administrators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Administrators'] = []
        if self.administrators is not None:
            for k in self.administrators:
                result['Administrators'].append(k.to_map() if k else None)
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.administrators = []
        if m.get('Administrators') is not None:
            for k in m.get('Administrators'):
                temp_model = ListDepartmentsResponseBodyDataItemsAdministrators()
                self.administrators.append(temp_model.from_map(k))
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDepartmentsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListDepartmentsResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListDepartmentsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListDepartmentsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListDepartmentsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListDepartmentsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDepartmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDepartmentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListDepartmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDetectionsRequest(TeaModel):
    def __init__(
        self,
        create_date_from: str = None,
        create_date_to: str = None,
        department_id: str = None,
        page_index: int = None,
        page_size: int = None,
        recording_type: str = None,
        rule_id: str = None,
    ):
        self.create_date_from = create_date_from
        self.create_date_to = create_date_to
        self.department_id = department_id
        self.page_index = page_index
        self.page_size = page_size
        self.recording_type = recording_type
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date_from is not None:
            result['CreateDateFrom'] = self.create_date_from
        if self.create_date_to is not None:
            result['CreateDateTo'] = self.create_date_to
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.recording_type is not None:
            result['RecordingType'] = self.recording_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDateFrom') is not None:
            self.create_date_from = m.get('CreateDateFrom')
        if m.get('CreateDateTo') is not None:
            self.create_date_to = m.get('CreateDateTo')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecordingType') is not None:
            self.recording_type = m.get('RecordingType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListDetectionsResponseBodyErrors(TeaModel):
    def __init__(
        self,
        message: str = None,
        field: str = None,
    ):
        self.message = message
        self.field = field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.field is not None:
            result['Field'] = self.field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        return self


class ListDetectionsResponseBodyDataItemsTasks(TeaModel):
    def __init__(
        self,
        status: str = None,
        video_meta_url: str = None,
        created_at: str = None,
        id: str = None,
        video_url: str = None,
    ):
        self.status = status
        self.video_meta_url = video_meta_url
        self.created_at = created_at
        self.id = id
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.video_meta_url is not None:
            result['VideoMetaUrl'] = self.video_meta_url
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoMetaUrl') is not None:
            self.video_meta_url = m.get('VideoMetaUrl')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class ListDetectionsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        status: str = None,
        department_name: str = None,
        tasks: List[ListDetectionsResponseBodyDataItemsTasks] = None,
        recording_type: str = None,
        created_at: str = None,
        department_id: str = None,
        id: str = None,
        rule_name: str = None,
        rule_id: str = None,
    ):
        self.status = status
        self.department_name = department_name
        self.tasks = tasks
        self.recording_type = recording_type
        self.created_at = created_at
        self.department_id = department_id
        self.id = id
        self.rule_name = rule_name
        self.rule_id = rule_id

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.recording_type is not None:
            result['RecordingType'] = self.recording_type
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListDetectionsResponseBodyDataItemsTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('RecordingType') is not None:
            self.recording_type = m.get('RecordingType')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListDetectionsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListDetectionsResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListDetectionsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListDetectionsResponseBody(TeaModel):
    def __init__(
        self,
        errors: List[ListDetectionsResponseBodyErrors] = None,
        message: str = None,
        request_id: str = None,
        data: ListDetectionsResponseBodyData = None,
        code: str = None,
    ):
        self.errors = errors
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = ListDetectionsResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListDetectionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDetectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDetectionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListDetectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDetectProcessesRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        name: str = None,
        publish_status: bool = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.name = name
        self.publish_status = publish_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        return self


class ListDetectProcessesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        draft: str = None,
        file_url: str = None,
        created_at: str = None,
        md_5: str = None,
        updated_at: str = None,
        new_version: bool = None,
        name: str = None,
        content: str = None,
        id: str = None,
    ):
        self.draft = draft
        self.file_url = file_url
        self.created_at = created_at
        self.md_5 = md_5
        self.updated_at = updated_at
        self.new_version = new_version
        self.name = name
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.new_version is not None:
            result['NewVersion'] = self.new_version
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('NewVersion') is not None:
            self.new_version = m.get('NewVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDetectProcessesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListDetectProcessesResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListDetectProcessesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListDetectProcessesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListDetectProcessesResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListDetectProcessesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDetectProcessesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDetectProcessesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListDetectProcessesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFilesRequest(TeaModel):
    def __init__(
        self,
        prefix: str = None,
        limit: int = None,
    ):
        self.prefix = prefix
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListFilesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[str] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLiveAppsRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListLiveAppsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        rtc_code: str = None,
        name: str = None,
        id: str = None,
    ):
        self.created_at = created_at
        self.rtc_code = rtc_code
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListLiveAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListLiveAppsResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListLiveAppsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListLiveAppsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListLiveAppsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListLiveAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListLiveAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLiveAppsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListLiveAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLiveRecordTemplatesRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListLiveRecordTemplatesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        updated_at: str = None,
        name: str = None,
        id: str = None,
        rtc_code: str = None,
    ):
        self.created_at = created_at
        self.updated_at = updated_at
        self.name = name
        self.id = id
        self.rtc_code = rtc_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        return self


class ListLiveRecordTemplatesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListLiveRecordTemplatesResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListLiveRecordTemplatesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListLiveRecordTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListLiveRecordTemplatesResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListLiveRecordTemplatesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListLiveRecordTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLiveRecordTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListLiveRecordTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLivesRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListLivesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        status: str = None,
        user_id: str = None,
        created_at: str = None,
        channel: str = None,
        name: str = None,
        id: str = None,
        public_id: str = None,
    ):
        self.status = status
        self.user_id = user_id
        self.created_at = created_at
        self.channel = channel
        self.name = name
        self.id = id
        self.public_id = public_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.public_id is not None:
            result['PublicId'] = self.public_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PublicId') is not None:
            self.public_id = m.get('PublicId')
        return self


class ListLivesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListLivesResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListLivesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListLivesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListLivesResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListLivesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListLivesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLivesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListLivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[str] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRolesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRulesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        name: str = None,
        content: str = None,
        id: str = None,
    ):
        self.created_at = created_at
        self.name = name
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListRulesResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListRulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListRulesResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListStatisticsTaskRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListStatisticsTaskResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        status: int = None,
        file_url: str = None,
        created_at: str = None,
        name: str = None,
    ):
        self.status = status
        self.file_url = file_url
        self.created_at = created_at
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListStatisticsTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListStatisticsTaskResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListStatisticsTaskResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListStatisticsTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListStatisticsTaskResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListStatisticsTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListStatisticsTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListStatisticsTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListStatisticsTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskGroupsRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListTaskGroupsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        status: str = None,
        completed_tasks: int = None,
        total_tasks: int = None,
        created_at: str = None,
        name: str = None,
        task_ids: List[str] = None,
        id: str = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        self.status = status
        self.completed_tasks = completed_tasks
        self.total_tasks = total_tasks
        self.created_at = created_at
        self.name = name
        self.task_ids = task_ids
        self.id = id
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.completed_tasks is not None:
            result['CompletedTasks'] = self.completed_tasks
        if self.total_tasks is not None:
            result['TotalTasks'] = self.total_tasks
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CompletedTasks') is not None:
            self.completed_tasks = m.get('CompletedTasks')
        if m.get('TotalTasks') is not None:
            self.total_tasks = m.get('TotalTasks')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListTaskGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListTaskGroupsResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListTaskGroupsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListTaskGroupsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListTaskGroupsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListTaskGroupsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListTaskGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTaskGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListTaskGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskItemsRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListTaskItemsResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        created_at: str = None,
        message: str = None,
        output: str = None,
        name: str = None,
        segment_seq: int = None,
    ):
        self.status = status
        self.created_at = created_at
        self.message = message
        self.output = output
        self.name = name
        self.segment_seq = segment_seq

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.output is not None:
            result['Output'] = self.output
        if self.name is not None:
            result['Name'] = self.name
        if self.segment_seq is not None:
            result['SegmentSeq'] = self.segment_seq
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SegmentSeq') is not None:
            self.segment_seq = m.get('SegmentSeq')
        return self


class ListTaskItemsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[ListTaskItemsResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTaskItemsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListTaskItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTaskItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListTaskItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        task_group_id: str = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.task_group_id = task_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_group_id is not None:
            result['TaskGroupId'] = self.task_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')
        return self


class ListTasksResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        status: str = None,
        video_meta_url: str = None,
        created_at: str = None,
        id: str = None,
        video_url: str = None,
    ):
        self.status = status
        self.video_meta_url = video_meta_url
        self.created_at = created_at
        self.id = id
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.video_meta_url is not None:
            result['VideoMetaUrl'] = self.video_meta_url
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoMetaUrl') is not None:
            self.video_meta_url = m.get('VideoMetaUrl')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class ListTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListTasksResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListTasksResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListTasksResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        page_index: int = None,
        page_size: int = None,
        username: str = None,
    ):
        self.department_id = department_id
        self.page_index = page_index
        self.page_size = page_size
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListUsersResponseBodyDataItemsDepartments(TeaModel):
    def __init__(
        self,
        description: str = None,
        created_at: str = None,
        updated_at: str = None,
        name: str = None,
        id: str = None,
    ):
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUsersResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        ram_username: str = None,
        email: str = None,
        phone_number: str = None,
        departments: List[ListUsersResponseBodyDataItemsDepartments] = None,
        created_at: str = None,
        updated_at: str = None,
        source: str = None,
        role: str = None,
        name: str = None,
        id: str = None,
        username: str = None,
    ):
        self.ram_username = ram_username
        self.email = email
        self.phone_number = phone_number
        self.departments = departments
        self.created_at = created_at
        self.updated_at = updated_at
        self.source = source
        self.role = role
        self.name = name
        self.id = id
        self.username = username

    def validate(self):
        if self.departments:
            for k in self.departments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ram_username is not None:
            result['RamUsername'] = self.ram_username
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        result['Departments'] = []
        if self.departments is not None:
            for k in self.departments:
                result['Departments'].append(k.to_map() if k else None)
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.source is not None:
            result['Source'] = self.source
        if self.role is not None:
            result['Role'] = self.role
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RamUsername') is not None:
            self.ram_username = m.get('RamUsername')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        self.departments = []
        if m.get('Departments') is not None:
            for k in m.get('Departments'):
                temp_model = ListUsersResponseBodyDataItemsDepartments()
                self.departments.append(temp_model.from_map(k))
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListUsersResponseBodyDataItems] = None,
        total_pages: int = None,
        total_elements: int = None,
    ):
        self.items = items
        self.total_pages = total_pages
        self.total_elements = total_elements

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
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListUsersResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListUsersResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListUsersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameDetectProcessRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class RenameDetectProcessResponseBodyData(TeaModel):
    def __init__(
        self,
        draft: str = None,
        created_at: str = None,
        md_5: str = None,
        name: str = None,
        content: str = None,
        id: str = None,
    ):
        self.draft = draft
        self.created_at = created_at
        self.md_5 = md_5
        self.name = name
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class RenameDetectProcessResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: RenameDetectProcessResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RenameDetectProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RenameDetectProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenameDetectProcessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = RenameDetectProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartLiveRecordTaskRequestClockWidgets(TeaModel):
    def __init__(
        self,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class StartLiveRecordTaskRequestUserPanesImages(TeaModel):
    def __init__(
        self,
        display: int = None,
        height: float = None,
        url: str = None,
        width: float = None,
        x: float = None,
        zorder: int = None,
        y: float = None,
    ):
        self.display = display
        self.height = height
        self.url = url
        self.width = width
        self.x = x
        self.zorder = zorder
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class StartLiveRecordTaskRequestUserPanesTexts(TeaModel):
    def __init__(
        self,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        text: str = None,
        x: float = None,
        zorder: int = None,
        y: float = None,
    ):
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.text = text
        self.x = x
        self.zorder = zorder
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.text is not None:
            result['Text'] = self.text
        if self.x is not None:
            result['X'] = self.x
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class StartLiveRecordTaskRequestUserPanes(TeaModel):
    def __init__(
        self,
        images: List[StartLiveRecordTaskRequestUserPanesImages] = None,
        pane_id: int = None,
        source_type: str = None,
        texts: List[StartLiveRecordTaskRequestUserPanesTexts] = None,
        user_id: str = None,
    ):
        self.images = images
        self.pane_id = pane_id
        self.source_type = source_type
        self.texts = texts
        self.user_id = user_id

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = StartLiveRecordTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k))
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = StartLiveRecordTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class StartLiveRecordTaskRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        user_id: str = None,
        rtc_code: str = None,
        name: str = None,
        template_id: str = None,
        background_color: int = None,
        clock_widgets: List[StartLiveRecordTaskRequestClockWidgets] = None,
        user_panes: List[StartLiveRecordTaskRequestUserPanes] = None,
    ):
        self.live_id = live_id
        self.user_id = user_id
        self.rtc_code = rtc_code
        self.name = name
        self.template_id = template_id
        self.background_color = background_color
        self.clock_widgets = clock_widgets
        self.user_panes = user_panes

    def validate(self):
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()
        if self.user_panes:
            for k in self.user_panes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k in self.user_panes:
                result['UserPanes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = StartLiveRecordTaskRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k in m.get('UserPanes'):
                temp_model = StartLiveRecordTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k))
        return self


class StartLiveRecordTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        user_id: str = None,
        rtc_code: str = None,
        name: str = None,
        template_id: str = None,
        background_color: int = None,
        clock_widgets_shrink: str = None,
        user_panes_shrink: str = None,
    ):
        self.live_id = live_id
        self.user_id = user_id
        self.rtc_code = rtc_code
        self.name = name
        self.template_id = template_id
        self.background_color = background_color
        self.clock_widgets_shrink = clock_widgets_shrink
        self.user_panes_shrink = user_panes_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.clock_widgets_shrink is not None:
            result['ClockWidgets'] = self.clock_widgets_shrink
        if self.user_panes_shrink is not None:
            result['UserPanes'] = self.user_panes_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('ClockWidgets') is not None:
            self.clock_widgets_shrink = m.get('ClockWidgets')
        if m.get('UserPanes') is not None:
            self.user_panes_shrink = m.get('UserPanes')
        return self


class StartLiveRecordTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
    ):
        self.created_at = created_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StartLiveRecordTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: StartLiveRecordTaskResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = StartLiveRecordTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class StartLiveRecordTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartLiveRecordTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = StartLiveRecordTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLiveRecordTaskRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        user_id: str = None,
    ):
        self.live_id = live_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class StopLiveRecordTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StopLiveRecordTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: StopLiveRecordTaskResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = StopLiveRecordTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class StopLiveRecordTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopLiveRecordTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = StopLiveRecordTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        disabled: bool = None,
        package_name: str = None,
        department_id: str = None,
    ):
        self.id = id
        self.name = name
        self.disabled = disabled
        self.package_name = package_name
        self.department_id = department_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        return self


class UpdateAppResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDepartmentRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        name: str = None,
        id: str = None,
    ):
        self.description = description
        self.label = label
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDepartmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDetectProcessRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        draft: str = None,
        content: str = None,
    ):
        self.id = id
        self.name = name
        self.draft = draft
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class UpdateDetectProcessResponseBodyData(TeaModel):
    def __init__(
        self,
        draft: str = None,
        created_at: str = None,
        md_5: str = None,
        name: str = None,
        content: str = None,
        id: str = None,
    ):
        self.draft = draft
        self.created_at = created_at
        self.md_5 = md_5
        self.name = name
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateDetectProcessResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: UpdateDetectProcessResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = UpdateDetectProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateDetectProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDetectProcessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateDetectProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLiveRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        status: str = None,
        user_id: str = None,
    ):
        self.live_id = live_id
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateLiveResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
    ):
        self.created_at = created_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateLiveResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: UpdateLiveResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = UpdateLiveResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLiveResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLiveRecordTaskRequestClockWidgets(TeaModel):
    def __init__(
        self,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateLiveRecordTaskRequestUserPanesImages(TeaModel):
    def __init__(
        self,
        display: int = None,
        height: float = None,
        url: str = None,
        width: float = None,
        x: float = None,
        zorder: int = None,
        y: float = None,
    ):
        self.display = display
        self.height = height
        self.url = url
        self.width = width
        self.x = x
        self.zorder = zorder
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class UpdateLiveRecordTaskRequestUserPanesTexts(TeaModel):
    def __init__(
        self,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        text: str = None,
        x: float = None,
        zorder: int = None,
        y: float = None,
    ):
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.text = text
        self.x = x
        self.zorder = zorder
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.text is not None:
            result['Text'] = self.text
        if self.x is not None:
            result['X'] = self.x
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class UpdateLiveRecordTaskRequestUserPanes(TeaModel):
    def __init__(
        self,
        images: List[UpdateLiveRecordTaskRequestUserPanesImages] = None,
        pane_id: int = None,
        source_type: str = None,
        texts: List[UpdateLiveRecordTaskRequestUserPanesTexts] = None,
        user_id: str = None,
    ):
        self.images = images
        self.pane_id = pane_id
        self.source_type = source_type
        self.texts = texts
        self.user_id = user_id

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.pane_id is not None:
            result['PaneId'] = self.pane_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = UpdateLiveRecordTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k))
        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = UpdateLiveRecordTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateLiveRecordTaskRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        user_id: str = None,
        rtc_code: str = None,
        name: str = None,
        template_id: str = None,
        background_color: int = None,
        clock_widgets: List[UpdateLiveRecordTaskRequestClockWidgets] = None,
        user_panes: List[UpdateLiveRecordTaskRequestUserPanes] = None,
    ):
        self.live_id = live_id
        self.user_id = user_id
        self.rtc_code = rtc_code
        self.name = name
        self.template_id = template_id
        self.background_color = background_color
        self.clock_widgets = clock_widgets
        self.user_panes = user_panes

    def validate(self):
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()
        if self.user_panes:
            for k in self.user_panes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        result['UserPanes'] = []
        if self.user_panes is not None:
            for k in self.user_panes:
                result['UserPanes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = UpdateLiveRecordTaskRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k in m.get('UserPanes'):
                temp_model = UpdateLiveRecordTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k))
        return self


class UpdateLiveRecordTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        user_id: str = None,
        rtc_code: str = None,
        name: str = None,
        template_id: str = None,
        background_color: int = None,
        clock_widgets_shrink: str = None,
        user_panes_shrink: str = None,
    ):
        self.live_id = live_id
        self.user_id = user_id
        self.rtc_code = rtc_code
        self.name = name
        self.template_id = template_id
        self.background_color = background_color
        self.clock_widgets_shrink = clock_widgets_shrink
        self.user_panes_shrink = user_panes_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.clock_widgets_shrink is not None:
            result['ClockWidgets'] = self.clock_widgets_shrink
        if self.user_panes_shrink is not None:
            result['UserPanes'] = self.user_panes_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('ClockWidgets') is not None:
            self.clock_widgets_shrink = m.get('ClockWidgets')
        if m.get('UserPanes') is not None:
            self.user_panes_shrink = m.get('UserPanes')
        return self


class UpdateLiveRecordTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
    ):
        self.created_at = created_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateLiveRecordTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: UpdateLiveRecordTaskResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = UpdateLiveRecordTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateLiveRecordTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLiveRecordTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateLiveRecordTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLiveRecordTemplateRequestBackgrounds(TeaModel):
    def __init__(
        self,
        display: int = None,
        url: str = None,
        width: float = None,
        height: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.display = display
        self.url = url
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateLiveRecordTemplateRequestWatermarks(TeaModel):
    def __init__(
        self,
        alpha: float = None,
        display: int = None,
        url: str = None,
        width: float = None,
        height: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.alpha = alpha
        self.display = display
        self.url = url
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha is not None:
            result['Alpha'] = self.alpha
        if self.display is not None:
            result['Display'] = self.display
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateLiveRecordTemplateRequestClockWidgets(TeaModel):
    def __init__(
        self,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.font_type is not None:
            result['FontType'] = self.font_type
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.zorder is not None:
            result['ZOrder'] = self.zorder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')
        return self


class UpdateLiveRecordTemplateRequest(TeaModel):
    def __init__(
        self,
        rtc_code: str = None,
        name: str = None,
        id: str = None,
        background_color: int = None,
        backgrounds: List[UpdateLiveRecordTemplateRequestBackgrounds] = None,
        watermarks: List[UpdateLiveRecordTemplateRequestWatermarks] = None,
        clock_widgets: List[UpdateLiveRecordTemplateRequestClockWidgets] = None,
    ):
        self.rtc_code = rtc_code
        self.name = name
        self.id = id
        self.background_color = background_color
        self.backgrounds = backgrounds
        self.watermarks = watermarks
        self.clock_widgets = clock_widgets

    def validate(self):
        if self.backgrounds:
            for k in self.backgrounds:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()
        if self.clock_widgets:
            for k in self.clock_widgets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k in self.backgrounds:
                result['Backgrounds'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k in self.clock_widgets:
                result['ClockWidgets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k in m.get('Backgrounds'):
                temp_model = UpdateLiveRecordTemplateRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = UpdateLiveRecordTemplateRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k in m.get('ClockWidgets'):
                temp_model = UpdateLiveRecordTemplateRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k))
        return self


class UpdateLiveRecordTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        rtc_code: str = None,
        name: str = None,
        id: str = None,
        background_color: int = None,
        backgrounds_shrink: str = None,
        watermarks_shrink: str = None,
        clock_widgets_shrink: str = None,
    ):
        self.rtc_code = rtc_code
        self.name = name
        self.id = id
        self.background_color = background_color
        self.backgrounds_shrink = backgrounds_shrink
        self.watermarks_shrink = watermarks_shrink
        self.clock_widgets_shrink = clock_widgets_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rtc_code is not None:
            result['RtcCode'] = self.rtc_code
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.backgrounds_shrink is not None:
            result['Backgrounds'] = self.backgrounds_shrink
        if self.watermarks_shrink is not None:
            result['Watermarks'] = self.watermarks_shrink
        if self.clock_widgets_shrink is not None:
            result['ClockWidgets'] = self.clock_widgets_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RtcCode') is not None:
            self.rtc_code = m.get('RtcCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('Backgrounds') is not None:
            self.backgrounds_shrink = m.get('Backgrounds')
        if m.get('Watermarks') is not None:
            self.watermarks_shrink = m.get('Watermarks')
        if m.get('ClockWidgets') is not None:
            self.clock_widgets_shrink = m.get('ClockWidgets')
        return self


class UpdateLiveRecordTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
    ):
        self.created_at = created_at
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateLiveRecordTemplateResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: UpdateLiveRecordTemplateResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = UpdateLiveRecordTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateLiveRecordTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLiveRecordTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateLiveRecordTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        content: str = None,
    ):
        self.id = id
        self.name = name
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class UpdateRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        name: str = None,
        content: str = None,
        id: str = None,
    ):
        self.created_at = created_at
        self.name = name
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: UpdateRuleResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = UpdateRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceConfigurationRequest(TeaModel):
    def __init__(
        self,
        task_item_queue_size: int = None,
        client_queue_size: int = None,
        live_record_every_one: bool = None,
        live_record_all: bool = None,
        live_record_layout: int = None,
        live_record_task_profile: str = None,
        live_record_max_client: int = None,
        live_record_video_resolution: int = None,
    ):
        self.task_item_queue_size = task_item_queue_size
        self.client_queue_size = client_queue_size
        self.live_record_every_one = live_record_every_one
        self.live_record_all = live_record_all
        self.live_record_layout = live_record_layout
        self.live_record_task_profile = live_record_task_profile
        self.live_record_max_client = live_record_max_client
        self.live_record_video_resolution = live_record_video_resolution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_item_queue_size is not None:
            result['TaskItemQueueSize'] = self.task_item_queue_size
        if self.client_queue_size is not None:
            result['ClientQueueSize'] = self.client_queue_size
        if self.live_record_every_one is not None:
            result['LiveRecordEveryOne'] = self.live_record_every_one
        if self.live_record_all is not None:
            result['LiveRecordAll'] = self.live_record_all
        if self.live_record_layout is not None:
            result['LiveRecordLayout'] = self.live_record_layout
        if self.live_record_task_profile is not None:
            result['LiveRecordTaskProfile'] = self.live_record_task_profile
        if self.live_record_max_client is not None:
            result['LiveRecordMaxClient'] = self.live_record_max_client
        if self.live_record_video_resolution is not None:
            result['LiveRecordVideoResolution'] = self.live_record_video_resolution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskItemQueueSize') is not None:
            self.task_item_queue_size = m.get('TaskItemQueueSize')
        if m.get('ClientQueueSize') is not None:
            self.client_queue_size = m.get('ClientQueueSize')
        if m.get('LiveRecordEveryOne') is not None:
            self.live_record_every_one = m.get('LiveRecordEveryOne')
        if m.get('LiveRecordAll') is not None:
            self.live_record_all = m.get('LiveRecordAll')
        if m.get('LiveRecordLayout') is not None:
            self.live_record_layout = m.get('LiveRecordLayout')
        if m.get('LiveRecordTaskProfile') is not None:
            self.live_record_task_profile = m.get('LiveRecordTaskProfile')
        if m.get('LiveRecordMaxClient') is not None:
            self.live_record_max_client = m.get('LiveRecordMaxClient')
        if m.get('LiveRecordVideoResolution') is not None:
            self.live_record_video_resolution = m.get('LiveRecordVideoResolution')
        return self


class UpdateServiceConfigurationResponseBody(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateServiceConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServiceConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateServiceConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSlrConfigurationRequest(TeaModel):
    def __init__(
        self,
        mq_subscribe: bool = None,
        mq_endpoint: str = None,
        mq_instance_id: str = None,
        mq_topic: str = None,
        mq_group_id: str = None,
        mq_topic_test: str = None,
        mq_group_id_test: str = None,
        mq_event: List[str] = None,
    ):
        self.mq_subscribe = mq_subscribe
        self.mq_endpoint = mq_endpoint
        self.mq_instance_id = mq_instance_id
        self.mq_topic = mq_topic
        self.mq_group_id = mq_group_id
        self.mq_topic_test = mq_topic_test
        self.mq_group_id_test = mq_group_id_test
        self.mq_event = mq_event

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mq_subscribe is not None:
            result['MqSubscribe'] = self.mq_subscribe
        if self.mq_endpoint is not None:
            result['MqEndpoint'] = self.mq_endpoint
        if self.mq_instance_id is not None:
            result['MqInstanceId'] = self.mq_instance_id
        if self.mq_topic is not None:
            result['MqTopic'] = self.mq_topic
        if self.mq_group_id is not None:
            result['MqGroupId'] = self.mq_group_id
        if self.mq_topic_test is not None:
            result['MqTopicTest'] = self.mq_topic_test
        if self.mq_group_id_test is not None:
            result['MqGroupIdTest'] = self.mq_group_id_test
        if self.mq_event is not None:
            result['MqEvent'] = self.mq_event
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqSubscribe') is not None:
            self.mq_subscribe = m.get('MqSubscribe')
        if m.get('MqEndpoint') is not None:
            self.mq_endpoint = m.get('MqEndpoint')
        if m.get('MqInstanceId') is not None:
            self.mq_instance_id = m.get('MqInstanceId')
        if m.get('MqTopic') is not None:
            self.mq_topic = m.get('MqTopic')
        if m.get('MqGroupId') is not None:
            self.mq_group_id = m.get('MqGroupId')
        if m.get('MqTopicTest') is not None:
            self.mq_topic_test = m.get('MqTopicTest')
        if m.get('MqGroupIdTest') is not None:
            self.mq_group_id_test = m.get('MqGroupIdTest')
        if m.get('MqEvent') is not None:
            self.mq_event = m.get('MqEvent')
        return self


class UpdateSlrConfigurationResponseBody(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateSlrConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSlrConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateSlrConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        email: str = None,
        name: str = None,
        phone_number: str = None,
        role: str = None,
        id: str = None,
    ):
        self.email = email
        self.name = name
        self.phone_number = phone_number
        self.role = role
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.role is not None:
            result['Role'] = self.role
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


