# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class VideoAppReportRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.VideoAppReportRequestDeviceInfo = None,
        payload: main_models.VideoAppReportRequestPayload = None,
        user_info: main_models.VideoAppReportRequestUserInfo = None,
    ):
        # Device identity information
        self.device_info = device_info
        # 业务参数
        self.payload = payload
        # 用户标识信息
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.VideoAppReportRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Payload') is not None:
            temp_model = main_models.VideoAppReportRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.VideoAppReportRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class VideoAppReportRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值
        # 
        # - 编码类型是SKILL_ID时，其值为应用的Skill ID。
        # - 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # 编码类型，获取天猫精灵的用户标识的途径有多种，不同途径对应不同的编码类型。
        # - PACKAGE_NAME：apk包名，Android应用客户链路的编码类型。
        # - SKILL_ID：技能ID，云端链路的编码类型。
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # 用户标识，设置为userOpenId或userUnionId。
        # 
        # This parameter is required.
        self.id = id
        # 用户Id的类型  
        # - OPEN_ID：默认的用户ID标识。
        # - UNION_ID: 组织维度的用户ID标识，在天猫精灵技能应用开放平台申请过组织后才会有该值。
        # 
        # This parameter is required.
        self.id_type = id_type
        # 组织ID，如果IdType为UNION_ID时必填。
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class VideoAppReportRequestPayload(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        is_login: bool = None,
        is_vip: bool = None,
        login_nick: str = None,
        origin_uuid: str = None,
        phone: str = None,
        pkg_name: str = None,
        start_time: int = None,
    ):
        # 会员的结束时间。
        # 
        # This parameter is required.
        self.end_time = end_time
        # 会员是否登录。
        # 
        # This parameter is required.
        self.is_login = is_login
        # 该账号是否为会员。
        # 
        # This parameter is required.
        self.is_vip = is_vip
        # 账号的昵称。
        self.login_nick = login_nick
        # 明文uuid
        self.origin_uuid = origin_uuid
        # 账户的手机号码。
        self.phone = phone
        # 应用包名。
        # 
        # This parameter is required.
        self.pkg_name = pkg_name
        # 会员的开始时间。
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.is_login is not None:
            result['isLogin'] = self.is_login

        if self.is_vip is not None:
            result['isVip'] = self.is_vip

        if self.login_nick is not None:
            result['loginNick'] = self.login_nick

        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid

        if self.phone is not None:
            result['phone'] = self.phone

        if self.pkg_name is not None:
            result['pkgName'] = self.pkg_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('isLogin') is not None:
            self.is_login = m.get('isLogin')

        if m.get('isVip') is not None:
            self.is_vip = m.get('isVip')

        if m.get('loginNick') is not None:
            self.login_nick = m.get('loginNick')

        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('pkgName') is not None:
            self.pkg_name = m.get('pkgName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

class VideoAppReportRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # 编码类型对应的值
        # 
        # - 编码类型是SKILL_ID时，其值为应用的Skill ID。
        # - 编码类型是PACKAGE_NAME时，其值为对应客户端App的packageName。
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device ID from Tmall Genie, and each method corresponds to a different encoding type.
        # - PACKAGE_NAME: APK package name, used for Android application customer flows.
        # - SKILL_ID: Skill ID, used for cloud-based flows.
        self.encode_type = encode_type
        # Device ID, set to either deviceOpenId or deviceUnionId.
        self.id = id
        # Type of the device ID.
        # - OPEN_ID: The default device ID.
        # - UNION_ID: Organization-level device ID. This value is available only after an organization has been registered on the Tmall Genie Skill Application Open Platform.
        self.id_type = id_type
        # Organization ID. Required when IdType is UNION_ID.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

