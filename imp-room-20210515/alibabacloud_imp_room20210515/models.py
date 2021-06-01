# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GetLoginTokenRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        app_key: str = None,
        device_id: str = None,
    ):
        # 用户ID
        self.app_uid = app_uid
        # AppKey
        self.app_key = app_key
        # 设备ID
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class GetLoginTokenRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: GetLoginTokenRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetLoginTokenRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetLoginTokenShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetLoginTokenResponseBodyResult(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        refresh_token: str = None,
        access_token_expired_time: int = None,
    ):
        # 登录Tokon
        self.access_token = access_token
        # 更新Token
        self.refresh_token = refresh_token
        # 登录Token过期时间
        self.access_token_expired_time = access_token_expired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        return self


class GetLoginTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result: GetLoginTokenResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetLoginTokenResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLoginTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLoginTokenResponseBody = None,
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
            temp_model = GetLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoomRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        biz_type: str = None,
        template_id: str = None,
        room_id: str = None,
        title: str = None,
        notice: str = None,
        owner_id: str = None,
        extension: Dict[str, str] = None,
    ):
        # 租户名
        self.domain = domain
        # 业务类型
        self.biz_type = biz_type
        # 模板id
        self.template_id = template_id
        # 房间id
        self.room_id = room_id
        # 房间标题
        self.title = title
        # 房间公告
        self.notice = notice
        # 房主id
        self.owner_id = owner_id
        # 拓展字段
        self.extension = extension

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class CreateRoomRequest(TeaModel):
    def __init__(
        self,
        request: CreateRoomRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = CreateRoomRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class CreateRoomResponseBodyResult(TeaModel):
    def __init__(
        self,
        room_id: str = None,
    ):
        # 房间id
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class CreateRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateRoomResponseBodyResult = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class CreateRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRoomResponseBody = None,
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
            temp_model = CreateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DestroyRoomRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        room_id: str = None,
    ):
        # 租户名
        self.domain = domain
        # 房间id
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class DestroyRoomRequest(TeaModel):
    def __init__(
        self,
        request: DestroyRoomRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = DestroyRoomRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class DestroyRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class DestroyRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DestroyRoomResponseBody = None,
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
            temp_model = DestroyRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        room_id: str = None,
        plugin_id: str = None,
        extension: Dict[str, str] = None,
    ):
        # 租户名
        self.domain = domain
        # 房间id
        self.room_id = room_id
        # 插件ID
        self.plugin_id = plugin_id
        # 拓展字段
        self.extension = extension

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        request: CreateInstanceRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = CreateInstanceRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class CreateInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        extension: Dict[str, str] = None,
    ):
        # 插件实例ID
        self.instance_id = instance_id
        # 扩展信息
        self.extension = extension

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateInstanceResponseBodyResult = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoomDetailRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        room_id: str = None,
    ):
        # 租户名
        self.domain = domain
        # 房间id
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class GetRoomDetailRequest(TeaModel):
    def __init__(
        self,
        request: GetRoomDetailRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = GetRoomDetailRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class GetRoomDetailResponseBodyResultPluginInstanceInfoList(TeaModel):
    def __init__(
        self,
        plugin_id: str = None,
        instance_id: str = None,
        create_time: int = None,
        extension: Dict[str, str] = None,
    ):
        # 插件id
        self.plugin_id = plugin_id
        # 对应实例id
        self.instance_id = instance_id
        # 创建时间戳
        self.create_time = create_time
        # 拓展字段
        self.extension = extension

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class GetRoomDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        room_id: str = None,
        title: str = None,
        notice: str = None,
        owner_id: str = None,
        uv: int = None,
        online_count: int = None,
        plugin_instance_info_list: List[GetRoomDetailResponseBodyResultPluginInstanceInfoList] = None,
    ):
        # 房间id
        self.room_id = room_id
        # 房间标题
        self.title = title
        # 房间公告
        self.notice = notice
        # 房主id
        self.owner_id = owner_id
        # uv
        self.uv = uv
        # 在线数
        self.online_count = online_count
        # 活跃插件列表
        self.plugin_instance_info_list = plugin_instance_info_list

    def validate(self):
        if self.plugin_instance_info_list:
            for k in self.plugin_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.uv is not None:
            result['Uv'] = self.uv
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = GetRoomDetailResponseBodyResultPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        return self


class GetRoomDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetRoomDetailResponseBodyResult = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetRoomDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class GetRoomDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRoomDetailResponseBody = None,
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
            temp_model = GetRoomDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoomListRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        biz_type: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # 租户名
        self.domain = domain
        # 业务类型
        self.biz_type = biz_type
        # 查询第几页的房间列表
        self.page_num = page_num
        # 该页面房间数量(最大支持50)
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetRoomListRequest(TeaModel):
    def __init__(
        self,
        request: GetRoomListRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = GetRoomListRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class GetRoomListResponseBodyResultRoomInfoList(TeaModel):
    def __init__(
        self,
        room_id: str = None,
        title: str = None,
        owner_id: str = None,
        biz_type: str = None,
        domain: str = None,
    ):
        # 房间id
        self.room_id = room_id
        # 房间标题名字
        self.title = title
        # 房主的用户id
        self.owner_id = owner_id
        # 业务类型
        self.biz_type = biz_type
        # 应用id，同appId
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class GetRoomListResponseBodyResult(TeaModel):
    def __init__(
        self,
        total: int = None,
        has_more: bool = None,
        room_info_list: List[GetRoomListResponseBodyResultRoomInfoList] = None,
    ):
        # 租户下的房间列表总数
        self.total = total
        # 是否还有下一页房间列表
        self.has_more = has_more
        # 租户下的房间列表基础信息
        self.room_info_list = room_info_list

    def validate(self):
        if self.room_info_list:
            for k in self.room_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['RoomInfoList'] = []
        if self.room_info_list is not None:
            for k in self.room_info_list:
                result['RoomInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.room_info_list = []
        if m.get('RoomInfoList') is not None:
            for k in m.get('RoomInfoList'):
                temp_model = GetRoomListResponseBodyResultRoomInfoList()
                self.room_info_list.append(temp_model.from_map(k))
        return self


class GetRoomListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetRoomListResponseBodyResult = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 业务结果
        self.result = result
        # 请求是否成功
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetRoomListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class GetRoomListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRoomListResponseBody = None,
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
            temp_model = GetRoomListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


