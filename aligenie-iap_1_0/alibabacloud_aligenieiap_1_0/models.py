# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateReminderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateReminderRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 设备标识（deviceOpenId或deviceUnionId）
        self.id = id
        # 设备Id的类型 - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateReminderRequestPayloadRecurrenceRule(TeaModel):
    def __init__(
        self,
        day: int = None,
        days_of_month: List[int] = None,
        days_of_week: List[int] = None,
        end_date_time: int = None,
        freq: str = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        second: int = None,
        start_date_time: int = None,
        year: int = None,
    ):
        # 触发时间的日
        self.day = day
        # 月循环相关，表示每月的几号的集合,数值范围为1-31
        self.days_of_month = days_of_month
        # 周循环相关，表示每周几触发，数值范围为1-7
        self.days_of_week = days_of_week
        # 结束时间，时间戳毫秒
        self.end_date_time = end_date_time
        # 循环类型:支持单次ONCE、每天DAILY、每周WEEKLY、每月MONTHLY
        self.freq = freq
        # 触发时间的时
        self.hour = hour
        # 触发时间的分
        self.minute = minute
        # 触发时间的月
        self.month = month
        # 触发时间的秒
        self.second = second
        # 开始时间，时间戳毫秒
        self.start_date_time = start_date_time
        # 触发时间的年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class CreateReminderRequestPayload(TeaModel):
    def __init__(
        self,
        content: str = None,
        is_debug: bool = None,
        recurrence_rule: CreateReminderRequestPayloadRecurrenceRule = None,
    ):
        # 提醒内容
        self.content = content
        # 调试标识
        self.is_debug = is_debug
        # 提醒调度信息
        self.recurrence_rule = recurrence_rule

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('RecurrenceRule') is not None:
            temp_model = CreateReminderRequestPayloadRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        return self


class CreateReminderRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的用户标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 用户标识（userOpenId或userUnionId）
        self.id = id
        # 用户Id的类型 - OPEN_ID：默认的用户ID标识 - UNION_ID: 组织维度的用户ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateReminderRequest(TeaModel):
    def __init__(
        self,
        device_info: CreateReminderRequestDeviceInfo = None,
        payload: CreateReminderRequestPayload = None,
        user_info: CreateReminderRequestUserInfo = None,
    ):
        # 设备标识信息
        self.device_info = device_info
        # 服务请求入参
        self.payload = payload
        # 用户标识信息
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = CreateReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = CreateReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = CreateReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CreateReminderShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # 设备标识信息
        self.device_info_shrink = device_info_shrink
        # 服务请求入参
        self.payload_shrink = payload_shrink
        # 用户标识信息
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CreateReminderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        model: int = None,
        success: bool = None,
    ):
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 创建的提醒id
        self.model = model
        # 服务成功标识
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateReminderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateReminderResponseBody = None,
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
            temp_model = CreateReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReminderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteReminderRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 设备标识（deviceOpenId或deviceUnionId）
        self.id = id
        # 设备Id的类型 - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteReminderRequestPayload(TeaModel):
    def __init__(
        self,
        id: int = None,
        is_debug: bool = None,
    ):
        # 提醒的唯一id
        self.id = id
        # 调试标识
        self.is_debug = is_debug

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        return self


class DeleteReminderRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的用户标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 用户标识（userOpenId或userUnionId）
        self.id = id
        # 用户Id的类型 - OPEN_ID：默认的用户ID标识 - UNION_ID: 组织维度的用户ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteReminderRequest(TeaModel):
    def __init__(
        self,
        device_info: DeleteReminderRequestDeviceInfo = None,
        payload: DeleteReminderRequestPayload = None,
        user_info: DeleteReminderRequestUserInfo = None,
    ):
        # 设备标识信息
        self.device_info = device_info
        # 服务请求入参
        self.payload = payload
        # 用户标识信息
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = DeleteReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = DeleteReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = DeleteReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class DeleteReminderShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # 设备标识信息
        self.device_info_shrink = device_info_shrink
        # 服务请求入参
        self.payload_shrink = payload_shrink
        # 用户标识信息
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class DeleteReminderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_msg: str = None,
        success: bool = None,
    ):
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 服务成功标识
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteReminderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteReminderResponseBody = None,
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
            temp_model = DeleteReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneNumberHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetPhoneNumberRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 设备标识（deviceOpenId或deviceUnionId）
        self.id = id
        # 设备Id的类型  - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetPhoneNumberRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的用户标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 用户标识（userOpenId或userUnionId）
        self.id = id
        # 用户Id的类型  - OPEN_ID：默认的用户ID标识 - UNION_ID: 组织维度的用户ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetPhoneNumberRequest(TeaModel):
    def __init__(
        self,
        device_info: GetPhoneNumberRequestDeviceInfo = None,
        user_info: GetPhoneNumberRequestUserInfo = None,
    ):
        # 设备标识信息
        self.device_info = device_info
        # 用户标识信息
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetPhoneNumberRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = GetPhoneNumberRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetPhoneNumberShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # 设备标识信息
        self.device_info_shrink = device_info_shrink
        # 用户标识信息
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetPhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
    ):
        # 用户手机号
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')
        return self


class GetPhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPhoneNumberResponseBody = None,
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
            temp_model = GetPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReminderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetReminderRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 设备标识（deviceOpenId或deviceUnionId）
        self.id = id
        # 设备Id的类型 - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetReminderRequestPayload(TeaModel):
    def __init__(
        self,
        id: int = None,
        is_debug: bool = None,
    ):
        # 提醒的唯一id
        self.id = id
        # 调试标识
        self.is_debug = is_debug

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        return self


class GetReminderRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的用户标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 用户标识（userOpenId或userUnionId）
        self.id = id
        # 用户Id的类型 - OPEN_ID：默认的用户ID标识 - UNION_ID: 组织维度的用户ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetReminderRequest(TeaModel):
    def __init__(
        self,
        device_info: GetReminderRequestDeviceInfo = None,
        payload: GetReminderRequestPayload = None,
        user_info: GetReminderRequestUserInfo = None,
    ):
        # 设备标识信息
        self.device_info = device_info
        # 服务请求入参
        self.payload = payload
        # 用户标识信息
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetReminderShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # 设备标识信息
        self.device_info_shrink = device_info_shrink
        # 服务请求入参
        self.payload_shrink = payload_shrink
        # 用户标识信息
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetReminderResponseBodyModelRemindResponsesRecurrenceRule(TeaModel):
    def __init__(
        self,
        day: int = None,
        days_of_month: List[int] = None,
        days_of_week: List[int] = None,
        end_date_time: str = None,
        freq: str = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        second: int = None,
        start_date_time: str = None,
        year: int = None,
    ):
        # 天
        self.day = day
        # 月的第几天 可用作月循环
        self.days_of_month = days_of_month
        # 周循环字段，取值范围：1-7
        self.days_of_week = days_of_week
        # 调度结束时间
        self.end_date_time = end_date_time
        # 调度类型
        self.freq = freq
        # 小时
        self.hour = hour
        # 分
        self.minute = minute
        # 月
        self.month = month
        # 秒
        self.second = second
        # 调度开始时间
        self.start_date_time = start_date_time
        # 年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class GetReminderResponseBodyModelRemindResponses(TeaModel):
    def __init__(
        self,
        action_topic: str = None,
        day_desc: str = None,
        recurrence_rule: GetReminderResponseBodyModelRemindResponsesRecurrenceRule = None,
        remind_id: int = None,
        remind_time: str = None,
        repeat_count: int = None,
        week: str = None,
    ):
        # 执行动作topic
        self.action_topic = action_topic
        # 触发条件描述
        self.day_desc = day_desc
        # 调度信息
        self.recurrence_rule = recurrence_rule
        # 提醒id
        self.remind_id = remind_id
        # 下次提醒时间
        self.remind_time = remind_time
        # 重复次数
        self.repeat_count = repeat_count
        # 触发为周几
        self.week = week

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_topic is not None:
            result['ActionTopic'] = self.action_topic
        if self.day_desc is not None:
            result['DayDesc'] = self.day_desc
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        if self.remind_id is not None:
            result['RemindId'] = self.remind_id
        if self.remind_time is not None:
            result['RemindTime'] = self.remind_time
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.week is not None:
            result['Week'] = self.week
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionTopic') is not None:
            self.action_topic = m.get('ActionTopic')
        if m.get('DayDesc') is not None:
            self.day_desc = m.get('DayDesc')
        if m.get('RecurrenceRule') is not None:
            temp_model = GetReminderResponseBodyModelRemindResponsesRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')
        if m.get('RemindTime') is not None:
            self.remind_time = m.get('RemindTime')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('Week') is not None:
            self.week = m.get('Week')
        return self


class GetReminderResponseBodyModel(TeaModel):
    def __init__(
        self,
        remind_responses: List[GetReminderResponseBodyModelRemindResponses] = None,
    ):
        # 提醒信息
        self.remind_responses = remind_responses

    def validate(self):
        if self.remind_responses:
            for k in self.remind_responses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RemindResponses'] = []
        if self.remind_responses is not None:
            for k in self.remind_responses:
                result['RemindResponses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remind_responses = []
        if m.get('RemindResponses') is not None:
            for k in m.get('RemindResponses'):
                temp_model = GetReminderResponseBodyModelRemindResponses()
                self.remind_responses.append(temp_model.from_map(k))
        return self


class GetReminderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_msg: str = None,
        model: GetReminderResponseBodyModel = None,
        success: bool = None,
    ):
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 提醒信息
        self.model = model
        # 服务成功标识
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            temp_model = GetReminderResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetReminderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetReminderResponseBody = None,
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
            temp_model = GetReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRemindersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListRemindersRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 设备标识（deviceOpenId或deviceUnionId）
        self.id = id
        # 设备Id的类型 - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListRemindersRequestPayload(TeaModel):
    def __init__(
        self,
        is_debug: bool = None,
    ):
        # 调试标识
        self.is_debug = is_debug

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        return self


class ListRemindersRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的用户标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 用户标识（userOpenId或userUnionId）
        self.id = id
        # 用户Id的类型 - OPEN_ID：默认的用户ID标识 - UNION_ID: 组织维度的用户ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListRemindersRequest(TeaModel):
    def __init__(
        self,
        device_info: ListRemindersRequestDeviceInfo = None,
        payload: ListRemindersRequestPayload = None,
        user_info: ListRemindersRequestUserInfo = None,
    ):
        # 设备标识信息
        self.device_info = device_info
        # 服务请求入参
        self.payload = payload
        # 用户标识信息
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListRemindersRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = ListRemindersRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = ListRemindersRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListRemindersShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # 设备标识信息
        self.device_info_shrink = device_info_shrink
        # 服务请求入参
        self.payload_shrink = payload_shrink
        # 用户标识信息
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListRemindersResponseBodyModelRemindResponsesRecurrenceRule(TeaModel):
    def __init__(
        self,
        day: int = None,
        days_of_month: List[int] = None,
        days_of_week: List[int] = None,
        end_date_time: str = None,
        freq: str = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        second: int = None,
        start_date_time: str = None,
        year: int = None,
    ):
        # 天
        self.day = day
        # 月的第几天 可用作月循环
        self.days_of_month = days_of_month
        # 周循环字段，取值范围：1-7
        self.days_of_week = days_of_week
        # 调度结束时间
        self.end_date_time = end_date_time
        # 调度类型
        self.freq = freq
        # 小时
        self.hour = hour
        # 分
        self.minute = minute
        # 月
        self.month = month
        # 秒
        self.second = second
        # 调度开始时间
        self.start_date_time = start_date_time
        # 年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class ListRemindersResponseBodyModelRemindResponses(TeaModel):
    def __init__(
        self,
        action_topic: str = None,
        day_desc: str = None,
        recurrence_rule: ListRemindersResponseBodyModelRemindResponsesRecurrenceRule = None,
        remind_id: int = None,
        remind_time: str = None,
        repeat_count: int = None,
        week: str = None,
    ):
        # 执行动作topic
        self.action_topic = action_topic
        # 触发条件描述
        self.day_desc = day_desc
        # 调度信息
        self.recurrence_rule = recurrence_rule
        # 提醒id
        self.remind_id = remind_id
        # 下次提醒时间
        self.remind_time = remind_time
        # 重复次数
        self.repeat_count = repeat_count
        # 触发为周几
        self.week = week

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_topic is not None:
            result['ActionTopic'] = self.action_topic
        if self.day_desc is not None:
            result['DayDesc'] = self.day_desc
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        if self.remind_id is not None:
            result['RemindId'] = self.remind_id
        if self.remind_time is not None:
            result['RemindTime'] = self.remind_time
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.week is not None:
            result['Week'] = self.week
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionTopic') is not None:
            self.action_topic = m.get('ActionTopic')
        if m.get('DayDesc') is not None:
            self.day_desc = m.get('DayDesc')
        if m.get('RecurrenceRule') is not None:
            temp_model = ListRemindersResponseBodyModelRemindResponsesRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')
        if m.get('RemindTime') is not None:
            self.remind_time = m.get('RemindTime')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('Week') is not None:
            self.week = m.get('Week')
        return self


class ListRemindersResponseBodyModel(TeaModel):
    def __init__(
        self,
        remind_responses: List[ListRemindersResponseBodyModelRemindResponses] = None,
    ):
        # 提醒信息
        self.remind_responses = remind_responses

    def validate(self):
        if self.remind_responses:
            for k in self.remind_responses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RemindResponses'] = []
        if self.remind_responses is not None:
            for k in self.remind_responses:
                result['RemindResponses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remind_responses = []
        if m.get('RemindResponses') is not None:
            for k in m.get('RemindResponses'):
                temp_model = ListRemindersResponseBodyModelRemindResponses()
                self.remind_responses.append(temp_model.from_map(k))
        return self


class ListRemindersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_msg: str = None,
        model: ListRemindersResponseBodyModel = None,
        success: bool = None,
    ):
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 提醒信息
        self.model = model
        # 服务成功标识
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            temp_model = ListRemindersResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRemindersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRemindersResponseBody = None,
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
            temp_model = ListRemindersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushNotificationsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PushNotificationsRequestNotificationUnicastRequestSendTarget(TeaModel):
    def __init__(
        self,
        target_identity: str = None,
        target_type: str = None,
    ):
        # 推送目标类型对应的标识值。
        self.target_identity = target_identity
        # 推送的目标类型，获取到对应设备或用户标识时的类型 - DEVICE_UNION_ID：设备unionId - DEVICE_OPEN_ID：设备openId - USER_UNION_ID：用户unionId - USER_OPEN_ID：用户openId
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_identity is not None:
            result['TargetIdentity'] = self.target_identity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetIdentity') is not None:
            self.target_identity = m.get('TargetIdentity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class PushNotificationsRequestNotificationUnicastRequest(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        is_debug: bool = None,
        message_template_id: str = None,
        organization_id: str = None,
        place_holder: Dict[str, str] = None,
        send_target: PushNotificationsRequestNotificationUnicastRequestSendTarget = None,
    ):
        # 编码类型对应的值，例如：编码类型是SKILLID，其值就为webhook服务中得到的skillId；编码类似是PACKAGENAME，其值就为对应客户端app的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型： PACKAGE_NAME：apk包名 SKILL_ID：技能id
        self.encode_type = encode_type
        # 调试标识
        self.is_debug = is_debug
        # 消息模板，在天猫精灵应用平台中申请消息模板时得到的模板id。
        self.message_template_id = message_template_id
        # 组织标识，推送类型是XX_UNION_XX时才需要配。当存在多种途径获取猫精设备或用户标识且又需要能互通的情况下需要找平台申请组织，申请通过后由平台分配得到。
        self.organization_id = organization_id
        # 占位符信息，例如：模板是【你好，{nick}！】这里可以是：{"nick":"小甜甜"}
        self.place_holder = place_holder
        # 消息推送的目标信息。
        self.send_target = send_target

    def validate(self):
        if self.send_target:
            self.send_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.message_template_id is not None:
            result['MessageTemplateId'] = self.message_template_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.place_holder is not None:
            result['PlaceHolder'] = self.place_holder
        if self.send_target is not None:
            result['SendTarget'] = self.send_target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('MessageTemplateId') is not None:
            self.message_template_id = m.get('MessageTemplateId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('PlaceHolder') is not None:
            self.place_holder = m.get('PlaceHolder')
        if m.get('SendTarget') is not None:
            temp_model = PushNotificationsRequestNotificationUnicastRequestSendTarget()
            self.send_target = temp_model.from_map(m['SendTarget'])
        return self


class PushNotificationsRequestTenantInfo(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PushNotificationsRequest(TeaModel):
    def __init__(
        self,
        notification_unicast_request: PushNotificationsRequestNotificationUnicastRequest = None,
        tenant_info: PushNotificationsRequestTenantInfo = None,
    ):
        # 消息推送入参对象。
        self.notification_unicast_request = notification_unicast_request
        # 身份信息。
        self.tenant_info = tenant_info

    def validate(self):
        if self.notification_unicast_request:
            self.notification_unicast_request.validate()
        if self.tenant_info:
            self.tenant_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_unicast_request is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request.to_map()
        if self.tenant_info is not None:
            result['TenantInfo'] = self.tenant_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationUnicastRequest') is not None:
            temp_model = PushNotificationsRequestNotificationUnicastRequest()
            self.notification_unicast_request = temp_model.from_map(m['NotificationUnicastRequest'])
        if m.get('TenantInfo') is not None:
            temp_model = PushNotificationsRequestTenantInfo()
            self.tenant_info = temp_model.from_map(m['TenantInfo'])
        return self


class PushNotificationsShrinkRequest(TeaModel):
    def __init__(
        self,
        notification_unicast_request_shrink: str = None,
        tenant_info_shrink: str = None,
    ):
        # 消息推送入参对象。
        self.notification_unicast_request_shrink = notification_unicast_request_shrink
        # 身份信息。
        self.tenant_info_shrink = tenant_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_unicast_request_shrink is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request_shrink
        if self.tenant_info_shrink is not None:
            result['TenantInfo'] = self.tenant_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationUnicastRequest') is not None:
            self.notification_unicast_request_shrink = m.get('NotificationUnicastRequest')
        if m.get('TenantInfo') is not None:
            self.tenant_info_shrink = m.get('TenantInfo')
        return self


class PushNotificationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class SendNotificationsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class SendNotificationsRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 设备标识（deviceOpenId或deviceUnionId）
        self.id = id
        # 设备Id的类型 - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SendNotificationsRequestNotificationUnicastRequestSendTarget(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SendNotificationsRequestNotificationUnicastRequest(TeaModel):
    def __init__(
        self,
        is_debug: bool = None,
        message_template_id: str = None,
        place_holder: Dict[str, str] = None,
        send_target: SendNotificationsRequestNotificationUnicastRequestSendTarget = None,
    ):
        # 调试标识
        self.is_debug = is_debug
        # 消息模板，在天猫精灵应用平台中申请消息模板时得到的模板id。
        self.message_template_id = message_template_id
        # 占位符信息，例如：模板是【你好，{nick}！】这里可以是：{"nick":"小甜甜"}
        self.place_holder = place_holder
        # 消息推送的目标信息。
        self.send_target = send_target

    def validate(self):
        if self.send_target:
            self.send_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.message_template_id is not None:
            result['MessageTemplateId'] = self.message_template_id
        if self.place_holder is not None:
            result['PlaceHolder'] = self.place_holder
        if self.send_target is not None:
            result['SendTarget'] = self.send_target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('MessageTemplateId') is not None:
            self.message_template_id = m.get('MessageTemplateId')
        if m.get('PlaceHolder') is not None:
            self.place_holder = m.get('PlaceHolder')
        if m.get('SendTarget') is not None:
            temp_model = SendNotificationsRequestNotificationUnicastRequestSendTarget()
            self.send_target = temp_model.from_map(m['SendTarget'])
        return self


class SendNotificationsRequestTenantInfo(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SendNotificationsRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的用户标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 用户标识（userOpenId或userUnionId）
        self.id = id
        # 用户Id的类型 - OPEN_ID：默认的用户ID标识 - UNION_ID: 组织维度的用户ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SendNotificationsRequest(TeaModel):
    def __init__(
        self,
        device_info: SendNotificationsRequestDeviceInfo = None,
        notification_unicast_request: SendNotificationsRequestNotificationUnicastRequest = None,
        tenant_info: SendNotificationsRequestTenantInfo = None,
        user_info: SendNotificationsRequestUserInfo = None,
    ):
        # 设备标识信息
        self.device_info = device_info
        # 消息推送入参对象。
        self.notification_unicast_request = notification_unicast_request
        # 身份信息。
        self.tenant_info = tenant_info
        # 用户标识信息
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.notification_unicast_request:
            self.notification_unicast_request.validate()
        if self.tenant_info:
            self.tenant_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.notification_unicast_request is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request.to_map()
        if self.tenant_info is not None:
            result['TenantInfo'] = self.tenant_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = SendNotificationsRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('NotificationUnicastRequest') is not None:
            temp_model = SendNotificationsRequestNotificationUnicastRequest()
            self.notification_unicast_request = temp_model.from_map(m['NotificationUnicastRequest'])
        if m.get('TenantInfo') is not None:
            temp_model = SendNotificationsRequestTenantInfo()
            self.tenant_info = temp_model.from_map(m['TenantInfo'])
        if m.get('UserInfo') is not None:
            temp_model = SendNotificationsRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class SendNotificationsShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        notification_unicast_request_shrink: str = None,
        tenant_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # 设备标识信息
        self.device_info_shrink = device_info_shrink
        # 消息推送入参对象。
        self.notification_unicast_request_shrink = notification_unicast_request_shrink
        # 身份信息。
        self.tenant_info_shrink = tenant_info_shrink
        # 用户标识信息
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.notification_unicast_request_shrink is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request_shrink
        if self.tenant_info_shrink is not None:
            result['TenantInfo'] = self.tenant_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('NotificationUnicastRequest') is not None:
            self.notification_unicast_request_shrink = m.get('NotificationUnicastRequest')
        if m.get('TenantInfo') is not None:
            self.tenant_info_shrink = m.get('TenantInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class SendNotificationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpdateReminderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateReminderRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 设备标识（deviceOpenId或deviceUnionId）
        self.id = id
        # 设备Id的类型 - OPEN_ID：默认的设备ID标识 - UNION_ID: 组织维度的设备ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateReminderRequestPayloadRecurrenceRule(TeaModel):
    def __init__(
        self,
        day: int = None,
        days_of_month: List[int] = None,
        days_of_week: List[int] = None,
        end_date_time: int = None,
        freq: str = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        second: int = None,
        start_date_time: int = None,
        year: int = None,
    ):
        # 触发时间的日
        self.day = day
        # 月循环相关，表示每月的几号的集合,数值范围为1-31
        self.days_of_month = days_of_month
        # 周循环相关，表示每周几触发，数值范围为1-7
        self.days_of_week = days_of_week
        # 结束时间，时间戳，毫秒
        self.end_date_time = end_date_time
        # 循环类型:支持单次ONCE、每天DAILY、每周WEEKLY、每月MONTHLY
        self.freq = freq
        # 触发时间的时
        self.hour = hour
        # 触发时间的分
        self.minute = minute
        # 触发时间的月
        self.month = month
        # 触发时间的秒
        self.second = second
        # 开始时间，时间戳，毫秒
        self.start_date_time = start_date_time
        # 触发时间的年
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class UpdateReminderRequestPayload(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: int = None,
        is_debug: bool = None,
        recurrence_rule: UpdateReminderRequestPayloadRecurrenceRule = None,
    ):
        # 提醒内容
        self.content = content
        # 提醒id
        self.id = id
        # 调试标识
        self.is_debug = is_debug
        # 提醒调度信息
        self.recurrence_rule = recurrence_rule

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('RecurrenceRule') is not None:
            temp_model = UpdateReminderRequestPayloadRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        return self


class UpdateReminderRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值，编码类型是SKILL_ID时，其值为应用的Skill ID； 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的用户标识的途径有多种，不同途径对应不同的编码类型 - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型 - SKILL_ID：技能ID，云端链路的编码类型
        self.encode_type = encode_type
        # 用户标识（userOpenId或userUnionId）
        self.id = id
        # 用户Id的类型 - OPEN_ID：默认的用户ID标识 - UNION_ID: 组织维度的用户ID标识，在猫精技能应用开放平台申请过组织后才会有
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateReminderRequest(TeaModel):
    def __init__(
        self,
        device_info: UpdateReminderRequestDeviceInfo = None,
        payload: UpdateReminderRequestPayload = None,
        user_info: UpdateReminderRequestUserInfo = None,
    ):
        # 设备标识信息
        self.device_info = device_info
        # 服务请求入参
        self.payload = payload
        # 用户标识信息
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = UpdateReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = UpdateReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = UpdateReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class UpdateReminderShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # 设备标识信息
        self.device_info_shrink = device_info_shrink
        # 服务请求入参
        self.payload_shrink = payload_shrink
        # 用户标识信息
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class UpdateReminderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_msg: str = None,
        model: int = None,
        success: bool = None,
    ):
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 更新提醒的id
        self.model = model
        # 服务成功标识
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateReminderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateReminderResponseBody = None,
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
            temp_model = UpdateReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WakeUpAppHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class WakeUpAppRequestTargetInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        organization_id: str = None,
        target_identity: str = None,
        target_type: str = None,
    ):
        # 编码类型对应的值，例如：编码类型是SKILLID，其值就为webhook服务中得到的skillId；编码类似是PACKAGENAME，其值就为对应客户端app的packageName。
        self.encode_key = encode_key
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型：  PACKAGE_NAME：apk包名 SKILL_ID：技能id
        self.encode_type = encode_type
        # 组织标识，推送类型是XX_UNION_XX时才需要配。当存在多种途径获取猫精设备标识且又需要能互通的情况下需要找平台申请组织，申请通过后由平台分配得到。
        self.organization_id = organization_id
        # 推送目标类型对应的标识值
        self.target_identity = target_identity
        # 推送目标类型，获取到对应设备标识时的类型  DEVICE_UNION_ID：设备unionId； DEVICE_OPEN_ID：设备openId
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.target_identity is not None:
            result['TargetIdentity'] = self.target_identity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('TargetIdentity') is not None:
            self.target_identity = m.get('TargetIdentity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class WakeUpAppRequest(TeaModel):
    def __init__(
        self,
        is_debug: bool = None,
        path: str = None,
        target_info: WakeUpAppRequestTargetInfo = None,
    ):
        # 是否调试
        self.is_debug = is_debug
        # 应用拉起路径，类似在技能应用控制台中填的唤起链接。
        self.path = path
        # 要拉起的目标设备信息。
        self.target_info = target_info

    def validate(self):
        if self.target_info:
            self.target_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.path is not None:
            result['Path'] = self.path
        if self.target_info is not None:
            result['TargetInfo'] = self.target_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('TargetInfo') is not None:
            temp_model = WakeUpAppRequestTargetInfo()
            self.target_info = temp_model.from_map(m['TargetInfo'])
        return self


class WakeUpAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


