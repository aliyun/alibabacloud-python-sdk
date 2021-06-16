# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DeleteSessionResponseBodyData(TeaModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        # session ID
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class DeleteSessionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteSessionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 错误码
        self.code = code
        self.data = data
        # 错误详情
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 是否成功
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
            temp_model = DeleteSessionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSessionResponseBody = None,
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
            temp_model = DeleteSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        desc: str = None,
        instance_id: str = None,
        params: str = None,
        proxy_ip: str = None,
        proxy_private_key: str = None,
        proxy_remote_port: str = None,
        remote_private_key: str = None,
        remote_pub_key: str = None,
        session_id: str = None,
        source: str = None,
        status: str = None,
        type: str = None,
    ):
        # 描述说明
        self.desc = desc
        # 实例 ID
        self.instance_id = instance_id
        # 自定义参数
        self.params = params
        # 代理实例 IP
        self.proxy_ip = proxy_ip
        # 代理实例私钥
        self.proxy_private_key = proxy_private_key
        # 代理实例端口
        self.proxy_remote_port = proxy_remote_port
        # 远端实例私钥
        self.remote_private_key = remote_private_key
        # 远端实例公钥
        self.remote_pub_key = remote_pub_key
        # session ID
        self.session_id = session_id
        # 来源
        self.source = source
        # session状态
        self.status = status
        # 实例类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.params is not None:
            result['params'] = self.params
        if self.proxy_ip is not None:
            result['proxyIp'] = self.proxy_ip
        if self.proxy_private_key is not None:
            result['proxyPrivateKey'] = self.proxy_private_key
        if self.proxy_remote_port is not None:
            result['proxyRemotePort'] = self.proxy_remote_port
        if self.remote_private_key is not None:
            result['remotePrivateKey'] = self.remote_private_key
        if self.remote_pub_key is not None:
            result['remotePubKey'] = self.remote_pub_key
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.source is not None:
            result['source'] = self.source
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('proxyIp') is not None:
            self.proxy_ip = m.get('proxyIp')
        if m.get('proxyPrivateKey') is not None:
            self.proxy_private_key = m.get('proxyPrivateKey')
        if m.get('proxyRemotePort') is not None:
            self.proxy_remote_port = m.get('proxyRemotePort')
        if m.get('remotePrivateKey') is not None:
            self.remote_private_key = m.get('remotePrivateKey')
        if m.get('remotePubKey') is not None:
            self.remote_pub_key = m.get('remotePubKey')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 错误码
        self.code = code
        self.data = data
        # 错误详情
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 是否成功
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
            temp_model = GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceResponseBody = None,
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HeartBeatRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        session_status: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.session_status = session_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.session_status is not None:
            result['sessionStatus'] = self.session_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('sessionStatus') is not None:
            self.session_status = m.get('sessionStatus')
        return self


class HeartBeatResponseBodyData(TeaModel):
    def __init__(
        self,
        session_status: str = None,
    ):
        # session 状态
        self.session_status = session_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_status is not None:
            result['sessionStatus'] = self.session_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionStatus') is not None:
            self.session_status = m.get('sessionStatus')
        return self


class HeartBeatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HeartBeatResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 错误码
        self.code = code
        self.data = data
        # 错误详情
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 是否成功
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
            temp_model = HeartBeatResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class HeartBeatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HeartBeatResponseBody = None,
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
            temp_model = HeartBeatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnRegisterInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class UnRegisterInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UnRegisterInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 错误码
        self.code = code
        self.data = data
        # 错误详情
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 是否成功
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
            temp_model = UnRegisterInstanceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UnRegisterInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnRegisterInstanceResponseBody = None,
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
            temp_model = UnRegisterInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSessionRequest(TeaModel):
    def __init__(
        self,
        session_name: str = None,
    ):
        self.session_name = session_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_name is not None:
            result['sessionName'] = self.session_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionName') is not None:
            self.session_name = m.get('sessionName')
        return self


class CreateSessionResponseBodyData(TeaModel):
    def __init__(
        self,
        local_instance_id: str = None,
        remote_instance_id: str = None,
        session_id: str = None,
        session_name: str = None,
    ):
        # 本地实例ID
        self.local_instance_id = local_instance_id
        # 远端实例ID
        self.remote_instance_id = remote_instance_id
        # Session ID
        self.session_id = session_id
        # Session名字
        self.session_name = session_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_instance_id is not None:
            result['localInstanceId'] = self.local_instance_id
        if self.remote_instance_id is not None:
            result['remoteInstanceId'] = self.remote_instance_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.session_name is not None:
            result['sessionName'] = self.session_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('localInstanceId') is not None:
            self.local_instance_id = m.get('localInstanceId')
        if m.get('remoteInstanceId') is not None:
            self.remote_instance_id = m.get('remoteInstanceId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('sessionName') is not None:
            self.session_name = m.get('sessionName')
        return self


class CreateSessionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateSessionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # ErrorCode
        self.code = code
        self.data = data
        # 错误信息
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 是否成功
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
            temp_model = CreateSessionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSessionResponseBody = None,
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
            temp_model = CreateSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        session_id: str = None,
        instance_type: str = None,
        source: str = None,
        description: str = None,
        params: str = None,
    ):
        self.instance_id = instance_id
        self.session_id = session_id
        self.instance_type = instance_type
        self.source = source
        self.description = description
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.source is not None:
            result['source'] = self.source
        if self.description is not None:
            result['description'] = self.description
        if self.params is not None:
            result['params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('params') is not None:
            self.params = m.get('params')
        return self


class RegisterInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class RegisterInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RegisterInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 错误码
        self.code = code
        self.data = data
        # 错误详情
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 是否成功
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
            temp_model = RegisterInstanceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RegisterInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterInstanceResponseBody = None,
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
            temp_model = RegisterInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionResponseBodyData(TeaModel):
    def __init__(
        self,
        local_instance_id: str = None,
        proxy_id: str = None,
        proxy_ip: str = None,
        proxy_remote_port: str = None,
        remote_instance_id: str = None,
        session_id: str = None,
        status: str = None,
    ):
        # 本地实例ID
        self.local_instance_id = local_instance_id
        # 代理实例ID
        self.proxy_id = proxy_id
        # 代理实例公网IP
        self.proxy_ip = proxy_ip
        # 代理实例端口
        self.proxy_remote_port = proxy_remote_port
        # 远端实例ID
        self.remote_instance_id = remote_instance_id
        # session ID
        self.session_id = session_id
        # session 状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_instance_id is not None:
            result['localInstanceId'] = self.local_instance_id
        if self.proxy_id is not None:
            result['proxyId'] = self.proxy_id
        if self.proxy_ip is not None:
            result['proxyIp'] = self.proxy_ip
        if self.proxy_remote_port is not None:
            result['proxyRemotePort'] = self.proxy_remote_port
        if self.remote_instance_id is not None:
            result['remoteInstanceId'] = self.remote_instance_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('localInstanceId') is not None:
            self.local_instance_id = m.get('localInstanceId')
        if m.get('proxyId') is not None:
            self.proxy_id = m.get('proxyId')
        if m.get('proxyIp') is not None:
            self.proxy_ip = m.get('proxyIp')
        if m.get('proxyRemotePort') is not None:
            self.proxy_remote_port = m.get('proxyRemotePort')
        if m.get('remoteInstanceId') is not None:
            self.remote_instance_id = m.get('remoteInstanceId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetSessionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSessionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # ErrorCode
        self.code = code
        self.data = data
        # 错误信息
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 是否成功
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
            temp_model = GetSessionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSessionResponseBody = None,
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
            temp_model = GetSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSessionsRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListSessionsResponseBodyDataSessions(TeaModel):
    def __init__(
        self,
        local_instance_id: str = None,
        proxy_id: str = None,
        proxy_ip: str = None,
        proxy_remote_port: str = None,
        remote_instance_id: str = None,
        session_id: str = None,
        status: str = None,
        session_name: str = None,
    ):
        # 本地实例ID
        self.local_instance_id = local_instance_id
        # 代理实例ID
        self.proxy_id = proxy_id
        # 代理实例公网IP
        self.proxy_ip = proxy_ip
        # 代理实例端口
        self.proxy_remote_port = proxy_remote_port
        # 远端实例ID
        self.remote_instance_id = remote_instance_id
        # session ID
        self.session_id = session_id
        # session 状态
        self.status = status
        # session 名字
        self.session_name = session_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_instance_id is not None:
            result['localInstanceId'] = self.local_instance_id
        if self.proxy_id is not None:
            result['proxyId'] = self.proxy_id
        if self.proxy_ip is not None:
            result['proxyIp'] = self.proxy_ip
        if self.proxy_remote_port is not None:
            result['proxyRemotePort'] = self.proxy_remote_port
        if self.remote_instance_id is not None:
            result['remoteInstanceId'] = self.remote_instance_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.status is not None:
            result['status'] = self.status
        if self.session_name is not None:
            result['sessionName'] = self.session_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('localInstanceId') is not None:
            self.local_instance_id = m.get('localInstanceId')
        if m.get('proxyId') is not None:
            self.proxy_id = m.get('proxyId')
        if m.get('proxyIp') is not None:
            self.proxy_ip = m.get('proxyIp')
        if m.get('proxyRemotePort') is not None:
            self.proxy_remote_port = m.get('proxyRemotePort')
        if m.get('remoteInstanceId') is not None:
            self.remote_instance_id = m.get('remoteInstanceId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sessionName') is not None:
            self.session_name = m.get('sessionName')
        return self


class ListSessionsResponseBodyData(TeaModel):
    def __init__(
        self,
        has_next_page: bool = None,
        next_page_num: int = None,
        next_page_size: int = None,
        sessions: List[ListSessionsResponseBodyDataSessions] = None,
        total: int = None,
    ):
        # 是否有下一页
        self.has_next_page = has_next_page
        # 下一页
        self.next_page_num = next_page_num
        # 下一页的session个数限制
        self.next_page_size = next_page_size
        self.sessions = sessions
        # session 总个数
        self.total = total

    def validate(self):
        if self.sessions:
            for k in self.sessions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next_page is not None:
            result['hasNextPage'] = self.has_next_page
        if self.next_page_num is not None:
            result['nextPageNum'] = self.next_page_num
        if self.next_page_size is not None:
            result['nextPageSize'] = self.next_page_size
        result['sessions'] = []
        if self.sessions is not None:
            for k in self.sessions:
                result['sessions'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasNextPage') is not None:
            self.has_next_page = m.get('hasNextPage')
        if m.get('nextPageNum') is not None:
            self.next_page_num = m.get('nextPageNum')
        if m.get('nextPageSize') is not None:
            self.next_page_size = m.get('nextPageSize')
        self.sessions = []
        if m.get('sessions') is not None:
            for k in m.get('sessions'):
                temp_model = ListSessionsResponseBodyDataSessions()
                self.sessions.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListSessionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListSessionsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 错误码
        self.code = code
        self.data = data
        # 错误详情
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 是否成功
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
            temp_model = ListSessionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListSessionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSessionsResponseBody = None,
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
            temp_model = ListSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


