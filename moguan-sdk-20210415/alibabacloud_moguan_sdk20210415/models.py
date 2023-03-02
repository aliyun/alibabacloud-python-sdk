# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any


class RegisterDeviceRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        device_id: str = None,
        extend: Dict[str, Any] = None,
        sdk_code: str = None,
        user_device_id: str = None,
    ):
        self.app_key = app_key
        self.device_id = device_id
        self.extend = extend
        self.sdk_code = sdk_code
        self.user_device_id = user_device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.sdk_code is not None:
            result['SdkCode'] = self.sdk_code
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('SdkCode') is not None:
            self.sdk_code = m.get('SdkCode')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class RegisterDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        device_id: str = None,
        extend_shrink: str = None,
        sdk_code: str = None,
        user_device_id: str = None,
    ):
        self.app_key = app_key
        self.device_id = device_id
        self.extend_shrink = extend_shrink
        self.sdk_code = sdk_code
        self.user_device_id = user_device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.extend_shrink is not None:
            result['Extend'] = self.extend_shrink
        if self.sdk_code is not None:
            result['SdkCode'] = self.sdk_code
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Extend') is not None:
            self.extend_shrink = m.get('Extend')
        if m.get('SdkCode') is not None:
            self.sdk_code = m.get('SdkCode')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class RegisterDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        license: str = None,
        public_key: str = None,
        rid: str = None,
        signature: str = None,
    ):
        self.license = license
        self.public_key = public_key
        self.rid = rid
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license is not None:
            result['License'] = self.license
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('License') is not None:
            self.license = m.get('License')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class RegisterDeviceResponseBody(TeaModel):
    def __init__(
        self,
        data: RegisterDeviceResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RegisterDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterDeviceResponseBody = None,
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
            temp_model = RegisterDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


