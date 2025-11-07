# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ActiveInteractionCreateRequest(TeaModel):
    def __init__(
        self,
        image: str = None,
    ):
        # This parameter is required.
        self.image = image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['image'] = self.image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        return self


class ActiveInteractionCreateResponseBodyData(TeaModel):
    def __init__(
        self,
        gesture: str = None,
        person: str = None,
        scene: str = None,
    ):
        self.gesture = gesture
        self.person = person
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gesture is not None:
            result['gesture'] = self.gesture
        if self.person is not None:
            result['person'] = self.person
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gesture') is not None:
            self.gesture = m.get('gesture')
        if m.get('person') is not None:
            self.person = m.get('person')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class ActiveInteractionCreateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ActiveInteractionCreateResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ActiveInteractionCreateResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ActiveInteractionCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActiveInteractionCreateResponseBody = None,
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
            temp_model = ActiveInteractionCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeviceRegisterRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        nonce: str = None,
        request_time: str = None,
        signature: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.nonce = nonce
        # This parameter is required.
        self.request_time = request_time
        # This parameter is required.
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.nonce is not None:
            result['nonce'] = self.nonce
        if self.request_time is not None:
            result['requestTime'] = self.request_time
        if self.signature is not None:
            result['signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')
        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        return self


class DeviceRegisterResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        device_name: str = None,
        nonce: str = None,
        response_time: str = None,
        signature: str = None,
    ):
        self.app_id = app_id
        self.device_name = device_name
        self.nonce = nonce
        self.response_time = response_time
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.nonce is not None:
            result['nonce'] = self.nonce
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        if self.signature is not None:
            result['signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        return self


class DeviceRegisterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeviceRegisterResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = DeviceRegisterResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeviceRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeviceRegisterResponseBody = None,
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
            temp_model = DeviceRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        device_name: str = None,
        nonce: str = None,
        request_time: str = None,
        signature: str = None,
        token_key: str = None,
        token_type: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.device_name = device_name
        # This parameter is required.
        self.nonce = nonce
        # This parameter is required.
        self.request_time = request_time
        # This parameter is required.
        self.signature = signature
        self.token_key = token_key
        # This parameter is required.
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.nonce is not None:
            result['nonce'] = self.nonce
        if self.request_time is not None:
            result['requestTime'] = self.request_time
        if self.signature is not None:
            result['signature'] = self.signature
        if self.token_key is not None:
            result['tokenKey'] = self.token_key
        if self.token_type is not None:
            result['tokenType'] = self.token_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')
        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('tokenKey') is not None:
            self.token_key = m.get('tokenKey')
        if m.get('tokenType') is not None:
            self.token_type = m.get('tokenType')
        return self


class GetTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        device_name: str = None,
        nonce: str = None,
        request_ip: str = None,
        response_time: str = None,
        signature: str = None,
    ):
        self.app_id = app_id
        self.device_name = device_name
        self.nonce = nonce
        self.request_ip = request_ip
        self.response_time = response_time
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.nonce is not None:
            result['nonce'] = self.nonce
        if self.request_ip is not None:
            result['requestIp'] = self.request_ip
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        if self.signature is not None:
            result['signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')
        if m.get('requestIp') is not None:
            self.request_ip = m.get('requestIp')
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTokenResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTokenResponseBody = None,
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
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModelTypeDetermineRequestHistory(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class ModelTypeDetermineRequest(TeaModel):
    def __init__(
        self,
        history: List[ModelTypeDetermineRequestHistory] = None,
        input_text: str = None,
    ):
        self.history = history
        # This parameter is required.
        self.input_text = input_text

    def validate(self):
        if self.history:
            for k in self.history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['history'] = []
        if self.history is not None:
            for k in self.history:
                result['history'].append(k.to_map() if k else None)
        if self.input_text is not None:
            result['inputText'] = self.input_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.history = []
        if m.get('history') is not None:
            for k in m.get('history'):
                temp_model = ModelTypeDetermineRequestHistory()
                self.history.append(temp_model.from_map(k))
        if m.get('inputText') is not None:
            self.input_text = m.get('inputText')
        return self


class ModelTypeDetermineShrinkRequest(TeaModel):
    def __init__(
        self,
        history_shrink: str = None,
        input_text: str = None,
    ):
        self.history_shrink = history_shrink
        # This parameter is required.
        self.input_text = input_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_shrink is not None:
            result['history'] = self.history_shrink
        if self.input_text is not None:
            result['inputText'] = self.input_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('history') is not None:
            self.history_shrink = m.get('history')
        if m.get('inputText') is not None:
            self.input_text = m.get('inputText')
        return self


class ModelTypeDetermineResponseBodyData(TeaModel):
    def __init__(
        self,
        follow_up: bool = None,
        rewrite_text: str = None,
        vl: bool = None,
    ):
        self.follow_up = follow_up
        self.rewrite_text = rewrite_text
        self.vl = vl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.follow_up is not None:
            result['followUp'] = self.follow_up
        if self.rewrite_text is not None:
            result['rewriteText'] = self.rewrite_text
        if self.vl is not None:
            result['vl'] = self.vl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('followUp') is not None:
            self.follow_up = m.get('followUp')
        if m.get('rewriteText') is not None:
            self.rewrite_text = m.get('rewriteText')
        if m.get('vl') is not None:
            self.vl = m.get('vl')
        return self


class ModelTypeDetermineResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ModelTypeDetermineResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ModelTypeDetermineResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ModelTypeDetermineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModelTypeDetermineResponseBody = None,
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
            temp_model = ModelTypeDetermineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


