# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CancelVideoTaskRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class CancelVideoTaskRequest(TeaModel):
    def __init__(
        self,
        app: CancelVideoTaskRequestApp = None,
        task_uuid: str = None,
        tenant_id: int = None,
    ):
        self.app = app
        self.task_uuid = task_uuid
        self.tenant_id = tenant_id

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = CancelVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CancelVideoTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        task_uuid: str = None,
        tenant_id: int = None,
    ):
        self.app_shrink = app_shrink
        self.task_uuid = task_uuid
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CancelVideoTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_reason: str = None,
        is_cancel: bool = None,
        task_uuid: str = None,
    ):
        self.fail_reason = fail_reason
        self.is_cancel = is_cancel
        self.task_uuid = task_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.is_cancel is not None:
            result['IsCancel'] = self.is_cancel
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('IsCancel') is not None:
            self.is_cancel = m.get('IsCancel')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class CancelVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CancelVideoTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CancelVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CancelVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClientAuthRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        device_id: str = None,
        device_info: str = None,
        device_type: str = None,
        license: str = None,
        tenant_id: int = None,
    ):
        self.app_id = app_id
        self.device_id = device_id
        self.device_info = device_info
        self.device_type = device_type
        self.license = license
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.license is not None:
            result['License'] = self.license
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceInfo') is not None:
            self.device_info = m.get('DeviceInfo')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('License') is not None:
            self.license = m.get('License')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ClientAuthResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ClientAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ClientAuthResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ClientAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClientStartRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        tenant_id: int = None,
    ):
        self.app_id = app_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ClientStartResponseBodyData(TeaModel):
    def __init__(
        self,
        im_token: str = None,
    ):
        self.im_token = im_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.im_token is not None:
            result['ImToken'] = self.im_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImToken') is not None:
            self.im_token = m.get('ImToken')
        return self


class ClientStartResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ClientStartResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ClientStartResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ClientStartResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ClientStartResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ClientStartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseTimedResetOperateRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: int = None,
    ):
        self.instance_id = instance_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CloseTimedResetOperateResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: int = None,
    ):
        self.instance_id = instance_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CloseTimedResetOperateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CloseTimedResetOperateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CloseTimedResetOperateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloseTimedResetOperateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseTimedResetOperateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CloseTimedResetOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Create2dAvatarRequest(TeaModel):
    def __init__(
        self,
        callback: bool = None,
        description: str = None,
        image: str = None,
        name: str = None,
        orientation: int = None,
        portrait: str = None,
        tenant_id: int = None,
        transparent: bool = None,
        video: str = None,
    ):
        self.callback = callback
        self.description = description
        self.image = image
        self.name = name
        self.orientation = orientation
        self.portrait = portrait
        self.tenant_id = tenant_id
        self.transparent = transparent
        self.video = video

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.description is not None:
            result['Description'] = self.description
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.portrait is not None:
            result['Portrait'] = self.portrait
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.transparent is not None:
            result['Transparent'] = self.transparent
        if self.video is not None:
            result['Video'] = self.video
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('Portrait') is not None:
            self.portrait = m.get('Portrait')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Transparent') is not None:
            self.transparent = m.get('Transparent')
        if m.get('Video') is not None:
            self.video = m.get('Video')
        return self


class Create2dAvatarResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class Create2dAvatarResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Create2dAvatarResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = Create2dAvatarResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class Create2dAvatarResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Create2dAvatarResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = Create2dAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAvatarRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        tenant_id: int = None,
    ):
        self.code = code
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DeleteAvatarResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAvatarResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAvatarResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DuplexDecisionRequestDialogContextHistories(TeaModel):
    def __init__(
        self,
        robot: str = None,
        user: str = None,
    ):
        self.robot = robot
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.robot is not None:
            result['Robot'] = self.robot
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Robot') is not None:
            self.robot = m.get('Robot')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DuplexDecisionRequestDialogContext(TeaModel):
    def __init__(
        self,
        cur_utterance_idx: int = None,
        histories: List[DuplexDecisionRequestDialogContextHistories] = None,
    ):
        self.cur_utterance_idx = cur_utterance_idx
        self.histories = histories

    def validate(self):
        if self.histories:
            for k in self.histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_utterance_idx is not None:
            result['CurUtteranceIdx'] = self.cur_utterance_idx
        result['Histories'] = []
        if self.histories is not None:
            for k in self.histories:
                result['Histories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurUtteranceIdx') is not None:
            self.cur_utterance_idx = m.get('CurUtteranceIdx')
        self.histories = []
        if m.get('Histories') is not None:
            for k in m.get('Histories'):
                temp_model = DuplexDecisionRequestDialogContextHistories()
                self.histories.append(temp_model.from_map(k))
        return self


class DuplexDecisionRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        biz_request_id: str = None,
        call_time: int = None,
        custom_keywords: List[str] = None,
        dialog_context: DuplexDecisionRequestDialogContext = None,
        dialog_status: str = None,
        interrupt_type: int = None,
        session_id: str = None,
        tenant_id: int = None,
        text: str = None,
    ):
        self.app_id = app_id
        self.biz_request_id = biz_request_id
        self.call_time = call_time
        self.custom_keywords = custom_keywords
        self.dialog_context = dialog_context
        self.dialog_status = dialog_status
        self.interrupt_type = interrupt_type
        self.session_id = session_id
        self.tenant_id = tenant_id
        self.text = text

    def validate(self):
        if self.dialog_context:
            self.dialog_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_request_id is not None:
            result['BizRequestId'] = self.biz_request_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.custom_keywords is not None:
            result['CustomKeywords'] = self.custom_keywords
        if self.dialog_context is not None:
            result['DialogContext'] = self.dialog_context.to_map()
        if self.dialog_status is not None:
            result['DialogStatus'] = self.dialog_status
        if self.interrupt_type is not None:
            result['InterruptType'] = self.interrupt_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizRequestId') is not None:
            self.biz_request_id = m.get('BizRequestId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CustomKeywords') is not None:
            self.custom_keywords = m.get('CustomKeywords')
        if m.get('DialogContext') is not None:
            temp_model = DuplexDecisionRequestDialogContext()
            self.dialog_context = temp_model.from_map(m['DialogContext'])
        if m.get('DialogStatus') is not None:
            self.dialog_status = m.get('DialogStatus')
        if m.get('InterruptType') is not None:
            self.interrupt_type = m.get('InterruptType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DuplexDecisionShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        biz_request_id: str = None,
        call_time: int = None,
        custom_keywords_shrink: str = None,
        dialog_context_shrink: str = None,
        dialog_status: str = None,
        interrupt_type: int = None,
        session_id: str = None,
        tenant_id: int = None,
        text: str = None,
    ):
        self.app_id = app_id
        self.biz_request_id = biz_request_id
        self.call_time = call_time
        self.custom_keywords_shrink = custom_keywords_shrink
        self.dialog_context_shrink = dialog_context_shrink
        self.dialog_status = dialog_status
        self.interrupt_type = interrupt_type
        self.session_id = session_id
        self.tenant_id = tenant_id
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_request_id is not None:
            result['BizRequestId'] = self.biz_request_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.custom_keywords_shrink is not None:
            result['CustomKeywords'] = self.custom_keywords_shrink
        if self.dialog_context_shrink is not None:
            result['DialogContext'] = self.dialog_context_shrink
        if self.dialog_status is not None:
            result['DialogStatus'] = self.dialog_status
        if self.interrupt_type is not None:
            result['InterruptType'] = self.interrupt_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizRequestId') is not None:
            self.biz_request_id = m.get('BizRequestId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CustomKeywords') is not None:
            self.custom_keywords_shrink = m.get('CustomKeywords')
        if m.get('DialogContext') is not None:
            self.dialog_context_shrink = m.get('DialogContext')
        if m.get('DialogStatus') is not None:
            self.dialog_status = m.get('DialogStatus')
        if m.get('InterruptType') is not None:
            self.interrupt_type = m.get('InterruptType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DuplexDecisionResponseBodyData(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        grab_type: str = None,
        output_text: str = None,
    ):
        self.action_type = action_type
        self.grab_type = grab_type
        self.output_text = output_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.grab_type is not None:
            result['GrabType'] = self.grab_type
        if self.output_text is not None:
            result['OutputText'] = self.output_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('GrabType') is not None:
            self.grab_type = m.get('GrabType')
        if m.get('OutputText') is not None:
            self.output_text = m.get('OutputText')
        return self


class DuplexDecisionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DuplexDecisionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DuplexDecisionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DuplexDecisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DuplexDecisionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DuplexDecisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoTaskInfoRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetVideoTaskInfoRequest(TeaModel):
    def __init__(
        self,
        app: GetVideoTaskInfoRequestApp = None,
        task_uuid: str = None,
        tenant_id: int = None,
    ):
        self.app = app
        self.task_uuid = task_uuid
        self.tenant_id = tenant_id

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = GetVideoTaskInfoRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetVideoTaskInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        task_uuid: str = None,
        tenant_id: int = None,
    ):
        self.app_shrink = app_shrink
        self.task_uuid = task_uuid
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetVideoTaskInfoResponseBodyDataTaskResult(TeaModel):
    def __init__(
        self,
        alpha_url: str = None,
        fail_code: str = None,
        fail_reason: str = None,
        preview_pic: str = None,
        subtitles_url: str = None,
        video_duration: int = None,
        video_url: str = None,
        word_subtitles_url: str = None,
    ):
        self.alpha_url = alpha_url
        self.fail_code = fail_code
        self.fail_reason = fail_reason
        self.preview_pic = preview_pic
        self.subtitles_url = subtitles_url
        self.video_duration = video_duration
        self.video_url = video_url
        # 字粒度的时间戳文件，特定任务支持
        self.word_subtitles_url = word_subtitles_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_url is not None:
            result['AlphaUrl'] = self.alpha_url
        if self.fail_code is not None:
            result['FailCode'] = self.fail_code
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.preview_pic is not None:
            result['PreviewPic'] = self.preview_pic
        if self.subtitles_url is not None:
            result['SubtitlesUrl'] = self.subtitles_url
        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.word_subtitles_url is not None:
            result['WordSubtitlesUrl'] = self.word_subtitles_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlphaUrl') is not None:
            self.alpha_url = m.get('AlphaUrl')
        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('PreviewPic') is not None:
            self.preview_pic = m.get('PreviewPic')
        if m.get('SubtitlesUrl') is not None:
            self.subtitles_url = m.get('SubtitlesUrl')
        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('WordSubtitlesUrl') is not None:
            self.word_subtitles_url = m.get('WordSubtitlesUrl')
        return self


class GetVideoTaskInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        process: str = None,
        status: str = None,
        task_result: GetVideoTaskInfoResponseBodyDataTaskResult = None,
        task_uuid: str = None,
        type: str = None,
    ):
        self.process = process
        self.status = status
        self.task_result = task_result
        self.task_uuid = task_uuid
        self.type = type

    def validate(self):
        if self.task_result:
            self.task_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.process is not None:
            result['Process'] = self.process
        if self.status is not None:
            result['Status'] = self.status
        if self.task_result is not None:
            result['TaskResult'] = self.task_result.to_map()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskResult') is not None:
            temp_model = GetVideoTaskInfoResponseBodyDataTaskResult()
            self.task_result = temp_model.from_map(m['TaskResult'])
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetVideoTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetVideoTaskInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetVideoTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVideoTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVideoTaskInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetVideoTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LicenseAuthRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        license: str = None,
        tenant_id: int = None,
    ):
        self.app_id = app_id
        self.license = license
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.license is not None:
            result['License'] = self.license
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('License') is not None:
            self.license = m.get('License')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class LicenseAuthResponseBodyData(TeaModel):
    def __init__(
        self,
        token: str = None,
    ):
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class LicenseAuthResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: LicenseAuthResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = LicenseAuthResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LicenseAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LicenseAuthResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = LicenseAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAvatarRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        tenant_id: int = None,
    ):
        self.code = code
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryAvatarResponseBodyDataSupportedResolutionsOffline(TeaModel):
    def __init__(
        self,
        desc: str = None,
        height: int = None,
        width: int = None,
    ):
        self.desc = desc
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class QueryAvatarResponseBodyDataSupportedResolutionsOnline(TeaModel):
    def __init__(
        self,
        desc: str = None,
        height: int = None,
        width: int = None,
    ):
        self.desc = desc
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class QueryAvatarResponseBodyDataSupportedResolutions(TeaModel):
    def __init__(
        self,
        offline: List[QueryAvatarResponseBodyDataSupportedResolutionsOffline] = None,
        online: List[QueryAvatarResponseBodyDataSupportedResolutionsOnline] = None,
    ):
        self.offline = offline
        self.online = online

    def validate(self):
        if self.offline:
            for k in self.offline:
                if k:
                    k.validate()
        if self.online:
            for k in self.online:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Offline'] = []
        if self.offline is not None:
            for k in self.offline:
                result['Offline'].append(k.to_map() if k else None)
        result['Online'] = []
        if self.online is not None:
            for k in self.online:
                result['Online'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.offline = []
        if m.get('Offline') is not None:
            for k in m.get('Offline'):
                temp_model = QueryAvatarResponseBodyDataSupportedResolutionsOffline()
                self.offline.append(temp_model.from_map(k))
        self.online = []
        if m.get('Online') is not None:
            for k in m.get('Online'):
                temp_model = QueryAvatarResponseBodyDataSupportedResolutionsOnline()
                self.online.append(temp_model.from_map(k))
        return self


class QueryAvatarResponseBodyData(TeaModel):
    def __init__(
        self,
        all_locate_images: Dict[str, Any] = None,
        avatar_type: str = None,
        description: str = None,
        image: str = None,
        make_fail_reason: str = None,
        make_stage: str = None,
        make_status: str = None,
        model_type: str = None,
        name: str = None,
        portrait: str = None,
        supported_resolutions: QueryAvatarResponseBodyDataSupportedResolutions = None,
    ):
        self.all_locate_images = all_locate_images
        self.avatar_type = avatar_type
        self.description = description
        self.image = image
        self.make_fail_reason = make_fail_reason
        self.make_stage = make_stage
        self.make_status = make_status
        self.model_type = model_type
        self.name = name
        self.portrait = portrait
        self.supported_resolutions = supported_resolutions

    def validate(self):
        if self.supported_resolutions:
            self.supported_resolutions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_locate_images is not None:
            result['AllLocateImages'] = self.all_locate_images
        if self.avatar_type is not None:
            result['AvatarType'] = self.avatar_type
        if self.description is not None:
            result['Description'] = self.description
        if self.image is not None:
            result['Image'] = self.image
        if self.make_fail_reason is not None:
            result['MakeFailReason'] = self.make_fail_reason
        if self.make_stage is not None:
            result['MakeStage'] = self.make_stage
        if self.make_status is not None:
            result['MakeStatus'] = self.make_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.name is not None:
            result['Name'] = self.name
        if self.portrait is not None:
            result['Portrait'] = self.portrait
        if self.supported_resolutions is not None:
            result['SupportedResolutions'] = self.supported_resolutions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllLocateImages') is not None:
            self.all_locate_images = m.get('AllLocateImages')
        if m.get('AvatarType') is not None:
            self.avatar_type = m.get('AvatarType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('MakeFailReason') is not None:
            self.make_fail_reason = m.get('MakeFailReason')
        if m.get('MakeStage') is not None:
            self.make_stage = m.get('MakeStage')
        if m.get('MakeStatus') is not None:
            self.make_status = m.get('MakeStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Portrait') is not None:
            self.portrait = m.get('Portrait')
        if m.get('SupportedResolutions') is not None:
            temp_model = QueryAvatarResponseBodyDataSupportedResolutions()
            self.supported_resolutions = temp_model.from_map(m['SupportedResolutions'])
        return self


class QueryAvatarResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryAvatarResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryAvatarResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAvatarResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAvatarResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAvatarListRequest(TeaModel):
    def __init__(
        self,
        model_type: str = None,
        page_no: int = None,
        page_size: int = None,
        tenant_id: int = None,
    ):
        self.model_type = model_type
        self.page_no = page_no
        self.page_size = page_size
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryAvatarListResponseBodyDataListSupportedResolutionsOffline(TeaModel):
    def __init__(
        self,
        desc: str = None,
        height: int = None,
        width: int = None,
    ):
        self.desc = desc
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class QueryAvatarListResponseBodyDataListSupportedResolutionsOnline(TeaModel):
    def __init__(
        self,
        desc: str = None,
        height: int = None,
        width: int = None,
    ):
        self.desc = desc
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class QueryAvatarListResponseBodyDataListSupportedResolutions(TeaModel):
    def __init__(
        self,
        offline: List[QueryAvatarListResponseBodyDataListSupportedResolutionsOffline] = None,
        online: List[QueryAvatarListResponseBodyDataListSupportedResolutionsOnline] = None,
    ):
        self.offline = offline
        self.online = online

    def validate(self):
        if self.offline:
            for k in self.offline:
                if k:
                    k.validate()
        if self.online:
            for k in self.online:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Offline'] = []
        if self.offline is not None:
            for k in self.offline:
                result['Offline'].append(k.to_map() if k else None)
        result['Online'] = []
        if self.online is not None:
            for k in self.online:
                result['Online'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.offline = []
        if m.get('Offline') is not None:
            for k in m.get('Offline'):
                temp_model = QueryAvatarListResponseBodyDataListSupportedResolutionsOffline()
                self.offline.append(temp_model.from_map(k))
        self.online = []
        if m.get('Online') is not None:
            for k in m.get('Online'):
                temp_model = QueryAvatarListResponseBodyDataListSupportedResolutionsOnline()
                self.online.append(temp_model.from_map(k))
        return self


class QueryAvatarListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        avatar_type: str = None,
        code: str = None,
        description: str = None,
        image: str = None,
        make_fail_reason: str = None,
        make_stage: str = None,
        make_status: str = None,
        model_type: str = None,
        name: str = None,
        portrait: str = None,
        supported_resolutions: QueryAvatarListResponseBodyDataListSupportedResolutions = None,
    ):
        self.avatar_type = avatar_type
        self.code = code
        self.description = description
        self.image = image
        self.make_fail_reason = make_fail_reason
        self.make_stage = make_stage
        self.make_status = make_status
        self.model_type = model_type
        self.name = name
        self.portrait = portrait
        self.supported_resolutions = supported_resolutions

    def validate(self):
        if self.supported_resolutions:
            self.supported_resolutions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_type is not None:
            result['AvatarType'] = self.avatar_type
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.image is not None:
            result['Image'] = self.image
        if self.make_fail_reason is not None:
            result['MakeFailReason'] = self.make_fail_reason
        if self.make_stage is not None:
            result['MakeStage'] = self.make_stage
        if self.make_status is not None:
            result['MakeStatus'] = self.make_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.name is not None:
            result['Name'] = self.name
        if self.portrait is not None:
            result['Portrait'] = self.portrait
        if self.supported_resolutions is not None:
            result['SupportedResolutions'] = self.supported_resolutions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarType') is not None:
            self.avatar_type = m.get('AvatarType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('MakeFailReason') is not None:
            self.make_fail_reason = m.get('MakeFailReason')
        if m.get('MakeStage') is not None:
            self.make_stage = m.get('MakeStage')
        if m.get('MakeStatus') is not None:
            self.make_status = m.get('MakeStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Portrait') is not None:
            self.portrait = m.get('Portrait')
        if m.get('SupportedResolutions') is not None:
            temp_model = QueryAvatarListResponseBodyDataListSupportedResolutions()
            self.supported_resolutions = temp_model.from_map(m['SupportedResolutions'])
        return self


class QueryAvatarListResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryAvatarListResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryAvatarListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class QueryAvatarListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryAvatarListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryAvatarListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAvatarListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAvatarListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryAvatarListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRunningInstanceRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class QueryRunningInstanceRequest(TeaModel):
    def __init__(
        self,
        app: QueryRunningInstanceRequestApp = None,
        session_id: str = None,
        tenant_id: int = None,
    ):
        self.app = app
        self.session_id = session_id
        self.tenant_id = tenant_id

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = QueryRunningInstanceRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryRunningInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        session_id: str = None,
        tenant_id: int = None,
    ):
        self.app_shrink = app_shrink
        self.session_id = session_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryRunningInstanceResponseBodyDataChannel(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        expired_time: str = None,
        gslb: List[str] = None,
        nonce: str = None,
        token: str = None,
        type: str = None,
        user_id: str = None,
        user_info_in_channel: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.expired_time = expired_time
        self.gslb = gslb
        self.nonce = nonce
        self.token = token
        self.type = type
        self.user_id = user_id
        self.user_info_in_channel = user_info_in_channel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gslb is not None:
            result['Gslb'] = self.gslb
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.token is not None:
            result['Token'] = self.token
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_info_in_channel is not None:
            result['UserInfoInChannel'] = self.user_info_in_channel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserInfoInChannel') is not None:
            self.user_info_in_channel = m.get('UserInfoInChannel')
        return self


class QueryRunningInstanceResponseBodyDataUser(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryRunningInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        channel: QueryRunningInstanceResponseBodyDataChannel = None,
        session_id: str = None,
        user: QueryRunningInstanceResponseBodyDataUser = None,
    ):
        self.channel = channel
        self.session_id = session_id
        self.user = user

    def validate(self):
        if self.channel:
            self.channel.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel.to_map()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            temp_model = QueryRunningInstanceResponseBodyDataChannel()
            self.channel = temp_model.from_map(m['Channel'])
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('User') is not None:
            temp_model = QueryRunningInstanceResponseBodyDataUser()
            self.user = temp_model.from_map(m['User'])
        return self


class QueryRunningInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryRunningInstanceResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryRunningInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRunningInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRunningInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryRunningInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTimedResetOperateStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: int = None,
    ):
        self.instance_id = instance_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryTimedResetOperateStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        status: int = None,
        status_str: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.status = status
        self.status_str = status_str
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryTimedResetOperateStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryTimedResetOperateStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryTimedResetOperateStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTimedResetOperateStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTimedResetOperateStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryTimedResetOperateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVideoTaskInfoRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class QueryVideoTaskInfoRequest(TeaModel):
    def __init__(
        self,
        app: QueryVideoTaskInfoRequestApp = None,
        order_by_id: str = None,
        page_no: int = None,
        page_size: int = None,
        status: int = None,
        task_uuid: str = None,
        tenant_id: int = None,
        title: str = None,
        type: int = None,
    ):
        self.app = app
        self.order_by_id = order_by_id
        self.page_no = page_no
        self.page_size = page_size
        self.status = status
        self.task_uuid = task_uuid
        self.tenant_id = tenant_id
        self.title = title
        self.type = type

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.order_by_id is not None:
            result['OrderById'] = self.order_by_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = QueryVideoTaskInfoRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('OrderById') is not None:
            self.order_by_id = m.get('OrderById')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryVideoTaskInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        order_by_id: str = None,
        page_no: int = None,
        page_size: int = None,
        status: int = None,
        task_uuid: str = None,
        tenant_id: int = None,
        title: str = None,
        type: int = None,
    ):
        self.app_shrink = app_shrink
        self.order_by_id = order_by_id
        self.page_no = page_no
        self.page_size = page_size
        self.status = status
        self.task_uuid = task_uuid
        self.tenant_id = tenant_id
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.order_by_id is not None:
            result['OrderById'] = self.order_by_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('OrderById') is not None:
            self.order_by_id = m.get('OrderById')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryVideoTaskInfoResponseBodyDataListTaskResult(TeaModel):
    def __init__(
        self,
        alpha_url: str = None,
        fail_code: str = None,
        fail_reason: str = None,
        preview_pic: str = None,
        subtitles_url: str = None,
        video_duration: int = None,
        video_url: str = None,
        word_subtitles_url: str = None,
    ):
        self.alpha_url = alpha_url
        self.fail_code = fail_code
        self.fail_reason = fail_reason
        self.preview_pic = preview_pic
        self.subtitles_url = subtitles_url
        self.video_duration = video_duration
        self.video_url = video_url
        self.word_subtitles_url = word_subtitles_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_url is not None:
            result['AlphaUrl'] = self.alpha_url
        if self.fail_code is not None:
            result['FailCode'] = self.fail_code
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.preview_pic is not None:
            result['PreviewPic'] = self.preview_pic
        if self.subtitles_url is not None:
            result['SubtitlesUrl'] = self.subtitles_url
        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.word_subtitles_url is not None:
            result['WordSubtitlesUrl'] = self.word_subtitles_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlphaUrl') is not None:
            self.alpha_url = m.get('AlphaUrl')
        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('PreviewPic') is not None:
            self.preview_pic = m.get('PreviewPic')
        if m.get('SubtitlesUrl') is not None:
            self.subtitles_url = m.get('SubtitlesUrl')
        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('WordSubtitlesUrl') is not None:
            self.word_subtitles_url = m.get('WordSubtitlesUrl')
        return self


class QueryVideoTaskInfoResponseBodyDataList(TeaModel):
    def __init__(
        self,
        status: int = None,
        task_result: QueryVideoTaskInfoResponseBodyDataListTaskResult = None,
        task_uuid: str = None,
        title: str = None,
        type: int = None,
    ):
        self.status = status
        self.task_result = task_result
        self.task_uuid = task_uuid
        self.title = title
        self.type = type

    def validate(self):
        if self.task_result:
            self.task_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.task_result is not None:
            result['TaskResult'] = self.task_result.to_map()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskResult') is not None:
            temp_model = QueryVideoTaskInfoResponseBodyDataListTaskResult()
            self.task_result = temp_model.from_map(m['TaskResult'])
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryVideoTaskInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryVideoTaskInfoResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryVideoTaskInfoResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryVideoTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryVideoTaskInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryVideoTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryVideoTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryVideoTaskInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryVideoTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Render3dAvatarRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        code: str = None,
        tenant_id: int = None,
    ):
        self.app_id = app_id
        self.code = code
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class Render3dAvatarResponseBodyData(TeaModel):
    def __init__(
        self,
        render_data: str = None,
    ):
        self.render_data = render_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.render_data is not None:
            result['RenderData'] = self.render_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderData') is not None:
            self.render_data = m.get('RenderData')
        return self


class Render3dAvatarResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Render3dAvatarResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = Render3dAvatarResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class Render3dAvatarResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Render3dAvatarResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = Render3dAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCommandRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        content: Dict[str, Any] = None,
        feedback: bool = None,
        session_id: str = None,
        tenant_id: int = None,
        unique_code: str = None,
    ):
        self.code = code
        self.content = content
        self.feedback = feedback
        self.session_id = session_id
        self.tenant_id = tenant_id
        self.unique_code = unique_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendCommandShrinkRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        content_shrink: str = None,
        feedback: bool = None,
        session_id: str = None,
        tenant_id: int = None,
        unique_code: str = None,
    ):
        self.code = code
        self.content_shrink = content_shrink
        self.feedback = feedback
        self.session_id = session_id
        self.tenant_id = tenant_id
        self.unique_code = unique_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendCommandResponseBodyData(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        unique_code: str = None,
    ):
        self.session_id = session_id
        self.unique_code = unique_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendCommandResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendCommandResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendCommandResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendCommandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SendCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequestStreamExtension(TeaModel):
    def __init__(
        self,
        index: int = None,
        is_stream: bool = None,
        position: str = None,
    ):
        self.index = index
        self.is_stream = is_stream
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.is_stream is not None:
            result['IsStream'] = self.is_stream
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('IsStream') is not None:
            self.is_stream = m.get('IsStream')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class SendMessageRequestTextRequest(TeaModel):
    def __init__(
        self,
        command_type: str = None,
        id: str = None,
        speech_text: str = None,
        interrupt: bool = None,
    ):
        self.command_type = command_type
        self.id = id
        self.speech_text = speech_text
        self.interrupt = interrupt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.id is not None:
            result['Id'] = self.id
        if self.speech_text is not None:
            result['SpeechText'] = self.speech_text
        if self.interrupt is not None:
            result['interrupt'] = self.interrupt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SpeechText') is not None:
            self.speech_text = m.get('SpeechText')
        if m.get('interrupt') is not None:
            self.interrupt = m.get('interrupt')
        return self


class SendMessageRequestVAMLRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        vaml: str = None,
    ):
        self.code = code
        self.vaml = vaml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.vaml is not None:
            result['Vaml'] = self.vaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Vaml') is not None:
            self.vaml = m.get('Vaml')
        return self


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        feedback: bool = None,
        session_id: str = None,
        stream_extension: SendMessageRequestStreamExtension = None,
        tenant_id: int = None,
        text_request: SendMessageRequestTextRequest = None,
        vamlrequest: SendMessageRequestVAMLRequest = None,
    ):
        self.feedback = feedback
        self.session_id = session_id
        self.stream_extension = stream_extension
        self.tenant_id = tenant_id
        self.text_request = text_request
        self.vamlrequest = vamlrequest

    def validate(self):
        if self.stream_extension:
            self.stream_extension.validate()
        if self.text_request:
            self.text_request.validate()
        if self.vamlrequest:
            self.vamlrequest.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.stream_extension is not None:
            result['StreamExtension'] = self.stream_extension.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text_request is not None:
            result['TextRequest'] = self.text_request.to_map()
        if self.vamlrequest is not None:
            result['VAMLRequest'] = self.vamlrequest.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StreamExtension') is not None:
            temp_model = SendMessageRequestStreamExtension()
            self.stream_extension = temp_model.from_map(m['StreamExtension'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TextRequest') is not None:
            temp_model = SendMessageRequestTextRequest()
            self.text_request = temp_model.from_map(m['TextRequest'])
        if m.get('VAMLRequest') is not None:
            temp_model = SendMessageRequestVAMLRequest()
            self.vamlrequest = temp_model.from_map(m['VAMLRequest'])
        return self


class SendMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        feedback: bool = None,
        session_id: str = None,
        stream_extension_shrink: str = None,
        tenant_id: int = None,
        text_request_shrink: str = None,
        vamlrequest_shrink: str = None,
    ):
        self.feedback = feedback
        self.session_id = session_id
        self.stream_extension_shrink = stream_extension_shrink
        self.tenant_id = tenant_id
        self.text_request_shrink = text_request_shrink
        self.vamlrequest_shrink = vamlrequest_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.stream_extension_shrink is not None:
            result['StreamExtension'] = self.stream_extension_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text_request_shrink is not None:
            result['TextRequest'] = self.text_request_shrink
        if self.vamlrequest_shrink is not None:
            result['VAMLRequest'] = self.vamlrequest_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StreamExtension') is not None:
            self.stream_extension_shrink = m.get('StreamExtension')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TextRequest') is not None:
            self.text_request_shrink = m.get('TextRequest')
        if m.get('VAMLRequest') is not None:
            self.vamlrequest_shrink = m.get('VAMLRequest')
        return self


class SendMessageResponseBodyData(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        session_id: str = None,
    ):
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendMessageResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        # Id of the request
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendMessageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendTextRequestStreamExtension(TeaModel):
    def __init__(
        self,
        index: int = None,
        is_stream: bool = None,
        position: str = None,
    ):
        self.index = index
        self.is_stream = is_stream
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.is_stream is not None:
            result['IsStream'] = self.is_stream
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('IsStream') is not None:
            self.is_stream = m.get('IsStream')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class SendTextRequest(TeaModel):
    def __init__(
        self,
        feedback: bool = None,
        interrupt: bool = None,
        session_id: str = None,
        stream_extension: SendTextRequestStreamExtension = None,
        tenant_id: int = None,
        text: str = None,
        unique_code: str = None,
    ):
        self.feedback = feedback
        self.interrupt = interrupt
        self.session_id = session_id
        self.stream_extension = stream_extension
        self.tenant_id = tenant_id
        self.text = text
        self.unique_code = unique_code

    def validate(self):
        if self.stream_extension:
            self.stream_extension.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.stream_extension is not None:
            result['StreamExtension'] = self.stream_extension.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StreamExtension') is not None:
            temp_model = SendTextRequestStreamExtension()
            self.stream_extension = temp_model.from_map(m['StreamExtension'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendTextShrinkRequest(TeaModel):
    def __init__(
        self,
        feedback: bool = None,
        interrupt: bool = None,
        session_id: str = None,
        stream_extension_shrink: str = None,
        tenant_id: int = None,
        text: str = None,
        unique_code: str = None,
    ):
        self.feedback = feedback
        self.interrupt = interrupt
        self.session_id = session_id
        self.stream_extension_shrink = stream_extension_shrink
        self.tenant_id = tenant_id
        self.text = text
        self.unique_code = unique_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.stream_extension_shrink is not None:
            result['StreamExtension'] = self.stream_extension_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StreamExtension') is not None:
            self.stream_extension_shrink = m.get('StreamExtension')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendTextResponseBodyData(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        unique_code: str = None,
    ):
        self.session_id = session_id
        self.unique_code = unique_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendTextResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendTextResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendTextResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendTextResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SendTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVamlRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        tenant_id: int = None,
        vaml: str = None,
    ):
        self.session_id = session_id
        self.tenant_id = tenant_id
        self.vaml = vaml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vaml is not None:
            result['Vaml'] = self.vaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Vaml') is not None:
            self.vaml = m.get('Vaml')
        return self


class SendVamlResponseBodyData(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        unique_code: str = None,
    ):
        self.session_id = session_id
        self.unique_code = unique_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendVamlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendVamlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendVamlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendVamlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendVamlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SendVamlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class StartInstanceRequestChannel(TeaModel):
    def __init__(
        self,
        req_config: Dict[str, Any] = None,
        type: str = None,
    ):
        self.req_config = req_config
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_config is not None:
            result['ReqConfig'] = self.req_config
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqConfig') is not None:
            self.req_config = m.get('ReqConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class StartInstanceRequestCommandRequest(TeaModel):
    def __init__(
        self,
        alpha_switch: bool = None,
    ):
        self.alpha_switch = alpha_switch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_switch is not None:
            result['AlphaSwitch'] = self.alpha_switch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlphaSwitch') is not None:
            self.alpha_switch = m.get('AlphaSwitch')
        return self


class StartInstanceRequestUser(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        app: StartInstanceRequestApp = None,
        channel: StartInstanceRequestChannel = None,
        command_request: StartInstanceRequestCommandRequest = None,
        tenant_id: int = None,
        user: StartInstanceRequestUser = None,
    ):
        self.app = app
        self.channel = channel
        self.command_request = command_request
        self.tenant_id = tenant_id
        self.user = user

    def validate(self):
        if self.app:
            self.app.validate()
        if self.channel:
            self.channel.validate()
        if self.command_request:
            self.command_request.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.channel is not None:
            result['Channel'] = self.channel.to_map()
        if self.command_request is not None:
            result['CommandRequest'] = self.command_request.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = StartInstanceRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('Channel') is not None:
            temp_model = StartInstanceRequestChannel()
            self.channel = temp_model.from_map(m['Channel'])
        if m.get('CommandRequest') is not None:
            temp_model = StartInstanceRequestCommandRequest()
            self.command_request = temp_model.from_map(m['CommandRequest'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('User') is not None:
            temp_model = StartInstanceRequestUser()
            self.user = temp_model.from_map(m['User'])
        return self


class StartInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        channel_shrink: str = None,
        command_request_shrink: str = None,
        tenant_id: int = None,
        user_shrink: str = None,
    ):
        self.app_shrink = app_shrink
        self.channel_shrink = channel_shrink
        self.command_request_shrink = command_request_shrink
        self.tenant_id = tenant_id
        self.user_shrink = user_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.channel_shrink is not None:
            result['Channel'] = self.channel_shrink
        if self.command_request_shrink is not None:
            result['CommandRequest'] = self.command_request_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('Channel') is not None:
            self.channel_shrink = m.get('Channel')
        if m.get('CommandRequest') is not None:
            self.command_request_shrink = m.get('CommandRequest')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('User') is not None:
            self.user_shrink = m.get('User')
        return self


class StartInstanceResponseBodyDataChannel(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        expired_time: str = None,
        gslb: List[str] = None,
        nonce: str = None,
        token: str = None,
        type: str = None,
        user_id: str = None,
        user_info_in_channel: str = None,
    ):
        self.app_id = app_id
        self.channel_id = channel_id
        self.expired_time = expired_time
        self.gslb = gslb
        self.nonce = nonce
        self.token = token
        self.type = type
        self.user_id = user_id
        self.user_info_in_channel = user_info_in_channel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gslb is not None:
            result['Gslb'] = self.gslb
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.token is not None:
            result['Token'] = self.token
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_info_in_channel is not None:
            result['UserInfoInChannel'] = self.user_info_in_channel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserInfoInChannel') is not None:
            self.user_info_in_channel = m.get('UserInfoInChannel')
        return self


class StartInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        channel: StartInstanceResponseBodyDataChannel = None,
        request_id: str = None,
        session_id: str = None,
        token: str = None,
    ):
        self.channel = channel
        self.request_id = request_id
        self.session_id = session_id
        self.token = token

    def validate(self):
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            temp_model = StartInstanceResponseBodyDataChannel()
            self.channel = temp_model.from_map(m['Channel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StartInstanceResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StartInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTimedResetOperateRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: int = None,
    ):
        self.instance_id = instance_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class StartTimedResetOperateResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: int = None,
    ):
        self.instance_id = instance_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class StartTimedResetOperateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StartTimedResetOperateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StartTimedResetOperateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartTimedResetOperateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartTimedResetOperateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StartTimedResetOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        tenant_id: int = None,
    ):
        self.session_id = session_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class StopInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        session_id: str = None,
    ):
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StopInstanceResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StopInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAudioTo2DAvatarVideoTaskRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class SubmitAudioTo2DAvatarVideoTaskRequestAvatarInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class SubmitAudioTo2DAvatarVideoTaskRequestVideoInfo(TeaModel):
    def __init__(
        self,
        alpha_format: int = None,
        background_image_url: str = None,
        is_alpha: bool = None,
        resolution: int = None,
    ):
        self.alpha_format = alpha_format
        self.background_image_url = background_image_url
        self.is_alpha = is_alpha
        self.resolution = resolution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_format is not None:
            result['AlphaFormat'] = self.alpha_format
        if self.background_image_url is not None:
            result['BackgroundImageUrl'] = self.background_image_url
        if self.is_alpha is not None:
            result['IsAlpha'] = self.is_alpha
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlphaFormat') is not None:
            self.alpha_format = m.get('AlphaFormat')
        if m.get('BackgroundImageUrl') is not None:
            self.background_image_url = m.get('BackgroundImageUrl')
        if m.get('IsAlpha') is not None:
            self.is_alpha = m.get('IsAlpha')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        return self


class SubmitAudioTo2DAvatarVideoTaskRequest(TeaModel):
    def __init__(
        self,
        app: SubmitAudioTo2DAvatarVideoTaskRequestApp = None,
        avatar_info: SubmitAudioTo2DAvatarVideoTaskRequestAvatarInfo = None,
        callback: bool = None,
        callback_params: str = None,
        ext_params: str = None,
        tenant_id: int = None,
        title: str = None,
        url: str = None,
        video_info: SubmitAudioTo2DAvatarVideoTaskRequestVideoInfo = None,
    ):
        self.app = app
        self.avatar_info = avatar_info
        self.callback = callback
        self.callback_params = callback_params
        self.ext_params = ext_params
        self.tenant_id = tenant_id
        self.title = title
        self.url = url
        self.video_info = video_info

    def validate(self):
        if self.app:
            self.app.validate()
        if self.avatar_info:
            self.avatar_info.validate()
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.avatar_info is not None:
            result['AvatarInfo'] = self.avatar_info.to_map()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = SubmitAudioTo2DAvatarVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('AvatarInfo') is not None:
            temp_model = SubmitAudioTo2DAvatarVideoTaskRequestAvatarInfo()
            self.avatar_info = temp_model.from_map(m['AvatarInfo'])
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('VideoInfo') is not None:
            temp_model = SubmitAudioTo2DAvatarVideoTaskRequestVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class SubmitAudioTo2DAvatarVideoTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        avatar_info_shrink: str = None,
        callback: bool = None,
        callback_params: str = None,
        ext_params: str = None,
        tenant_id: int = None,
        title: str = None,
        url: str = None,
        video_info_shrink: str = None,
    ):
        self.app_shrink = app_shrink
        self.avatar_info_shrink = avatar_info_shrink
        self.callback = callback
        self.callback_params = callback_params
        self.ext_params = ext_params
        self.tenant_id = tenant_id
        self.title = title
        self.url = url
        self.video_info_shrink = video_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.avatar_info_shrink is not None:
            result['AvatarInfo'] = self.avatar_info_shrink
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.video_info_shrink is not None:
            result['VideoInfo'] = self.video_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('AvatarInfo') is not None:
            self.avatar_info_shrink = m.get('AvatarInfo')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('VideoInfo') is not None:
            self.video_info_shrink = m.get('VideoInfo')
        return self


class SubmitAudioTo2DAvatarVideoTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uuid: str = None,
    ):
        self.task_uuid = task_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class SubmitAudioTo2DAvatarVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitAudioTo2DAvatarVideoTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SubmitAudioTo2DAvatarVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitAudioTo2DAvatarVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitAudioTo2DAvatarVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SubmitAudioTo2DAvatarVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAudioTo3DAvatarVideoTaskRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class SubmitAudioTo3DAvatarVideoTaskRequestAvatarInfo(TeaModel):
    def __init__(
        self,
        angle: int = None,
        code: str = None,
        industry_code: str = None,
        locate: int = None,
    ):
        self.angle = angle
        self.code = code
        self.industry_code = industry_code
        self.locate = locate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.code is not None:
            result['Code'] = self.code
        if self.industry_code is not None:
            result['IndustryCode'] = self.industry_code
        if self.locate is not None:
            result['Locate'] = self.locate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IndustryCode') is not None:
            self.industry_code = m.get('IndustryCode')
        if m.get('Locate') is not None:
            self.locate = m.get('Locate')
        return self


class SubmitAudioTo3DAvatarVideoTaskRequestVideoInfo(TeaModel):
    def __init__(
        self,
        alpha_format: int = None,
        background_image_url: str = None,
        is_alpha: bool = None,
        resolution: int = None,
    ):
        self.alpha_format = alpha_format
        self.background_image_url = background_image_url
        self.is_alpha = is_alpha
        self.resolution = resolution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_format is not None:
            result['AlphaFormat'] = self.alpha_format
        if self.background_image_url is not None:
            result['BackgroundImageUrl'] = self.background_image_url
        if self.is_alpha is not None:
            result['IsAlpha'] = self.is_alpha
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlphaFormat') is not None:
            self.alpha_format = m.get('AlphaFormat')
        if m.get('BackgroundImageUrl') is not None:
            self.background_image_url = m.get('BackgroundImageUrl')
        if m.get('IsAlpha') is not None:
            self.is_alpha = m.get('IsAlpha')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        return self


class SubmitAudioTo3DAvatarVideoTaskRequest(TeaModel):
    def __init__(
        self,
        app: SubmitAudioTo3DAvatarVideoTaskRequestApp = None,
        avatar_info: SubmitAudioTo3DAvatarVideoTaskRequestAvatarInfo = None,
        callback: bool = None,
        callback_params: str = None,
        ext_params: str = None,
        tenant_id: int = None,
        title: str = None,
        url: str = None,
        video_info: SubmitAudioTo3DAvatarVideoTaskRequestVideoInfo = None,
    ):
        self.app = app
        self.avatar_info = avatar_info
        self.callback = callback
        self.callback_params = callback_params
        self.ext_params = ext_params
        self.tenant_id = tenant_id
        self.title = title
        self.url = url
        self.video_info = video_info

    def validate(self):
        if self.app:
            self.app.validate()
        if self.avatar_info:
            self.avatar_info.validate()
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.avatar_info is not None:
            result['AvatarInfo'] = self.avatar_info.to_map()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = SubmitAudioTo3DAvatarVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('AvatarInfo') is not None:
            temp_model = SubmitAudioTo3DAvatarVideoTaskRequestAvatarInfo()
            self.avatar_info = temp_model.from_map(m['AvatarInfo'])
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('VideoInfo') is not None:
            temp_model = SubmitAudioTo3DAvatarVideoTaskRequestVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class SubmitAudioTo3DAvatarVideoTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        avatar_info_shrink: str = None,
        callback: bool = None,
        callback_params: str = None,
        ext_params: str = None,
        tenant_id: int = None,
        title: str = None,
        url: str = None,
        video_info_shrink: str = None,
    ):
        self.app_shrink = app_shrink
        self.avatar_info_shrink = avatar_info_shrink
        self.callback = callback
        self.callback_params = callback_params
        self.ext_params = ext_params
        self.tenant_id = tenant_id
        self.title = title
        self.url = url
        self.video_info_shrink = video_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.avatar_info_shrink is not None:
            result['AvatarInfo'] = self.avatar_info_shrink
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.video_info_shrink is not None:
            result['VideoInfo'] = self.video_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('AvatarInfo') is not None:
            self.avatar_info_shrink = m.get('AvatarInfo')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('VideoInfo') is not None:
            self.video_info_shrink = m.get('VideoInfo')
        return self


class SubmitAudioTo3DAvatarVideoTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uuid: str = None,
    ):
        self.task_uuid = task_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class SubmitAudioTo3DAvatarVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitAudioTo3DAvatarVideoTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SubmitAudioTo3DAvatarVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitAudioTo3DAvatarVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitAudioTo3DAvatarVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SubmitAudioTo3DAvatarVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTextTo2DAvatarVideoTaskRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class SubmitTextTo2DAvatarVideoTaskRequestAudioInfo(TeaModel):
    def __init__(
        self,
        pitch_rate: int = None,
        speech_rate: int = None,
        voice: str = None,
        volume: int = None,
    ):
        self.pitch_rate = pitch_rate
        self.speech_rate = speech_rate
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class SubmitTextTo2DAvatarVideoTaskRequestAvatarInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class SubmitTextTo2DAvatarVideoTaskRequestVideoInfo(TeaModel):
    def __init__(
        self,
        alpha_format: int = None,
        background_image_url: str = None,
        is_alpha: bool = None,
        is_subtitles: bool = None,
        resolution: int = None,
        subtitle_embedded: bool = None,
    ):
        self.alpha_format = alpha_format
        self.background_image_url = background_image_url
        self.is_alpha = is_alpha
        self.is_subtitles = is_subtitles
        self.resolution = resolution
        self.subtitle_embedded = subtitle_embedded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_format is not None:
            result['AlphaFormat'] = self.alpha_format
        if self.background_image_url is not None:
            result['BackgroundImageUrl'] = self.background_image_url
        if self.is_alpha is not None:
            result['IsAlpha'] = self.is_alpha
        if self.is_subtitles is not None:
            result['IsSubtitles'] = self.is_subtitles
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.subtitle_embedded is not None:
            result['SubtitleEmbedded'] = self.subtitle_embedded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlphaFormat') is not None:
            self.alpha_format = m.get('AlphaFormat')
        if m.get('BackgroundImageUrl') is not None:
            self.background_image_url = m.get('BackgroundImageUrl')
        if m.get('IsAlpha') is not None:
            self.is_alpha = m.get('IsAlpha')
        if m.get('IsSubtitles') is not None:
            self.is_subtitles = m.get('IsSubtitles')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('SubtitleEmbedded') is not None:
            self.subtitle_embedded = m.get('SubtitleEmbedded')
        return self


class SubmitTextTo2DAvatarVideoTaskRequest(TeaModel):
    def __init__(
        self,
        app: SubmitTextTo2DAvatarVideoTaskRequestApp = None,
        audio_info: SubmitTextTo2DAvatarVideoTaskRequestAudioInfo = None,
        avatar_info: SubmitTextTo2DAvatarVideoTaskRequestAvatarInfo = None,
        callback: bool = None,
        callback_params: str = None,
        ext_params: str = None,
        tenant_id: int = None,
        text: str = None,
        title: str = None,
        video_info: SubmitTextTo2DAvatarVideoTaskRequestVideoInfo = None,
    ):
        self.app = app
        self.audio_info = audio_info
        self.avatar_info = avatar_info
        self.callback = callback
        self.callback_params = callback_params
        self.ext_params = ext_params
        self.tenant_id = tenant_id
        self.text = text
        self.title = title
        self.video_info = video_info

    def validate(self):
        if self.app:
            self.app.validate()
        if self.audio_info:
            self.audio_info.validate()
        if self.avatar_info:
            self.avatar_info.validate()
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.audio_info is not None:
            result['AudioInfo'] = self.audio_info.to_map()
        if self.avatar_info is not None:
            result['AvatarInfo'] = self.avatar_info.to_map()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('AudioInfo') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskRequestAudioInfo()
            self.audio_info = temp_model.from_map(m['AudioInfo'])
        if m.get('AvatarInfo') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskRequestAvatarInfo()
            self.avatar_info = temp_model.from_map(m['AvatarInfo'])
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskRequestVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class SubmitTextTo2DAvatarVideoTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        audio_info_shrink: str = None,
        avatar_info_shrink: str = None,
        callback: bool = None,
        callback_params: str = None,
        ext_params: str = None,
        tenant_id: int = None,
        text: str = None,
        title: str = None,
        video_info_shrink: str = None,
    ):
        self.app_shrink = app_shrink
        self.audio_info_shrink = audio_info_shrink
        self.avatar_info_shrink = avatar_info_shrink
        self.callback = callback
        self.callback_params = callback_params
        self.ext_params = ext_params
        self.tenant_id = tenant_id
        self.text = text
        self.title = title
        self.video_info_shrink = video_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.audio_info_shrink is not None:
            result['AudioInfo'] = self.audio_info_shrink
        if self.avatar_info_shrink is not None:
            result['AvatarInfo'] = self.avatar_info_shrink
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info_shrink is not None:
            result['VideoInfo'] = self.video_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('AudioInfo') is not None:
            self.audio_info_shrink = m.get('AudioInfo')
        if m.get('AvatarInfo') is not None:
            self.avatar_info_shrink = m.get('AvatarInfo')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            self.video_info_shrink = m.get('VideoInfo')
        return self


class SubmitTextTo2DAvatarVideoTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uuid: str = None,
    ):
        self.task_uuid = task_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class SubmitTextTo2DAvatarVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitTextTo2DAvatarVideoTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitTextTo2DAvatarVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTextTo2DAvatarVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SubmitTextTo2DAvatarVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTextTo3DAvatarVideoTaskRequestApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class SubmitTextTo3DAvatarVideoTaskRequestAudioInfo(TeaModel):
    def __init__(
        self,
        pitch_rate: int = None,
        speech_rate: int = None,
        voice: str = None,
        volume: int = None,
    ):
        self.pitch_rate = pitch_rate
        self.speech_rate = speech_rate
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class SubmitTextTo3DAvatarVideoTaskRequestAvatarInfo(TeaModel):
    def __init__(
        self,
        angle: int = None,
        code: str = None,
        industry_code: str = None,
        locate: int = None,
    ):
        self.angle = angle
        self.code = code
        self.industry_code = industry_code
        self.locate = locate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.code is not None:
            result['Code'] = self.code
        if self.industry_code is not None:
            result['IndustryCode'] = self.industry_code
        if self.locate is not None:
            result['Locate'] = self.locate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IndustryCode') is not None:
            self.industry_code = m.get('IndustryCode')
        if m.get('Locate') is not None:
            self.locate = m.get('Locate')
        return self


class SubmitTextTo3DAvatarVideoTaskRequestVideoInfo(TeaModel):
    def __init__(
        self,
        alpha_format: int = None,
        background_image_url: str = None,
        is_alpha: bool = None,
        is_subtitles: bool = None,
        resolution: int = None,
        subtitle_embedded: bool = None,
    ):
        self.alpha_format = alpha_format
        self.background_image_url = background_image_url
        self.is_alpha = is_alpha
        self.is_subtitles = is_subtitles
        self.resolution = resolution
        self.subtitle_embedded = subtitle_embedded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_format is not None:
            result['AlphaFormat'] = self.alpha_format
        if self.background_image_url is not None:
            result['BackgroundImageUrl'] = self.background_image_url
        if self.is_alpha is not None:
            result['IsAlpha'] = self.is_alpha
        if self.is_subtitles is not None:
            result['IsSubtitles'] = self.is_subtitles
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.subtitle_embedded is not None:
            result['SubtitleEmbedded'] = self.subtitle_embedded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlphaFormat') is not None:
            self.alpha_format = m.get('AlphaFormat')
        if m.get('BackgroundImageUrl') is not None:
            self.background_image_url = m.get('BackgroundImageUrl')
        if m.get('IsAlpha') is not None:
            self.is_alpha = m.get('IsAlpha')
        if m.get('IsSubtitles') is not None:
            self.is_subtitles = m.get('IsSubtitles')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('SubtitleEmbedded') is not None:
            self.subtitle_embedded = m.get('SubtitleEmbedded')
        return self


class SubmitTextTo3DAvatarVideoTaskRequest(TeaModel):
    def __init__(
        self,
        app: SubmitTextTo3DAvatarVideoTaskRequestApp = None,
        audio_info: SubmitTextTo3DAvatarVideoTaskRequestAudioInfo = None,
        avatar_info: SubmitTextTo3DAvatarVideoTaskRequestAvatarInfo = None,
        callback: bool = None,
        callback_params: str = None,
        ext_params: str = None,
        tenant_id: int = None,
        text: str = None,
        title: str = None,
        video_info: SubmitTextTo3DAvatarVideoTaskRequestVideoInfo = None,
    ):
        self.app = app
        self.audio_info = audio_info
        self.avatar_info = avatar_info
        self.callback = callback
        self.callback_params = callback_params
        self.ext_params = ext_params
        self.tenant_id = tenant_id
        self.text = text
        self.title = title
        self.video_info = video_info

    def validate(self):
        if self.app:
            self.app.validate()
        if self.audio_info:
            self.audio_info.validate()
        if self.avatar_info:
            self.avatar_info.validate()
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.audio_info is not None:
            result['AudioInfo'] = self.audio_info.to_map()
        if self.avatar_info is not None:
            result['AvatarInfo'] = self.avatar_info.to_map()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('AudioInfo') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskRequestAudioInfo()
            self.audio_info = temp_model.from_map(m['AudioInfo'])
        if m.get('AvatarInfo') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskRequestAvatarInfo()
            self.avatar_info = temp_model.from_map(m['AvatarInfo'])
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskRequestVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class SubmitTextTo3DAvatarVideoTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        app_shrink: str = None,
        audio_info_shrink: str = None,
        avatar_info_shrink: str = None,
        callback: bool = None,
        callback_params: str = None,
        ext_params: str = None,
        tenant_id: int = None,
        text: str = None,
        title: str = None,
        video_info_shrink: str = None,
    ):
        self.app_shrink = app_shrink
        self.audio_info_shrink = audio_info_shrink
        self.avatar_info_shrink = avatar_info_shrink
        self.callback = callback
        self.callback_params = callback_params
        self.ext_params = ext_params
        self.tenant_id = tenant_id
        self.text = text
        self.title = title
        self.video_info_shrink = video_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.audio_info_shrink is not None:
            result['AudioInfo'] = self.audio_info_shrink
        if self.avatar_info_shrink is not None:
            result['AvatarInfo'] = self.avatar_info_shrink
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info_shrink is not None:
            result['VideoInfo'] = self.video_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('AudioInfo') is not None:
            self.audio_info_shrink = m.get('AudioInfo')
        if m.get('AvatarInfo') is not None:
            self.avatar_info_shrink = m.get('AvatarInfo')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            self.video_info_shrink = m.get('VideoInfo')
        return self


class SubmitTextTo3DAvatarVideoTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uuid: str = None,
    ):
        self.task_uuid = task_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class SubmitTextTo3DAvatarVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitTextTo3DAvatarVideoTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitTextTo3DAvatarVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTextTo3DAvatarVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SubmitTextTo3DAvatarVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Update2dAvatarRequest(TeaModel):
    def __init__(
        self,
        callback: bool = None,
        code: str = None,
        description: str = None,
        image: str = None,
        name: str = None,
        orientation: int = None,
        portrait: str = None,
        tenant_id: int = None,
        transparent: bool = None,
        video: str = None,
    ):
        self.callback = callback
        self.code = code
        self.description = description
        self.image = image
        self.name = name
        self.orientation = orientation
        self.portrait = portrait
        self.tenant_id = tenant_id
        self.transparent = transparent
        self.video = video

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.portrait is not None:
            result['Portrait'] = self.portrait
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.transparent is not None:
            result['Transparent'] = self.transparent
        if self.video is not None:
            result['Video'] = self.video
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('Portrait') is not None:
            self.portrait = m.get('Portrait')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Transparent') is not None:
            self.transparent = m.get('Transparent')
        if m.get('Video') is not None:
            self.video = m.get('Video')
        return self


class Update2dAvatarResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class Update2dAvatarResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Update2dAvatarResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = Update2dAvatarResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class Update2dAvatarResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Update2dAvatarResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = Update2dAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


