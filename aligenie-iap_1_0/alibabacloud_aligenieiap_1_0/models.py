# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any


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
        target_type: str = None,
        target_identity: str = None,
        organization_id: str = None,
        encode_type: str = None,
        encode_key: str = None,
    ):
        # 推送目标类型，获取到对应设备标识时的类型  DEVICE_UNION_ID：设备unionId； DEVICE_OPEN_ID：设备openId
        self.target_type = target_type
        # 推送目标类型对应的标识值
        self.target_identity = target_identity
        # 组织标识，推送类型是XX_UNION_XX时才需要配。当存在多种途径获取猫精设备标识且又需要能互通的情况下需要找平台申请组织，申请通过后由平台分配得到。
        self.organization_id = organization_id
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型：  PACKAGE_NAME：apk包名 SKILL_ID：技能id
        self.encode_type = encode_type
        # 编码类型对应的值，例如：编码类型是SKILLID，其值就为webhook服务中得到的skillId；编码类似是PACKAGENAME，其值就为对应客户端app的packageName。
        self.encode_key = encode_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_identity is not None:
            result['TargetIdentity'] = self.target_identity
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetIdentity') is not None:
            self.target_identity = m.get('TargetIdentity')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        return self


class WakeUpAppRequest(TeaModel):
    def __init__(
        self,
        path: str = None,
        genie_app_id: str = None,
        target_info: WakeUpAppRequestTargetInfo = None,
        is_debug: bool = None,
    ):
        # 应用拉起路径，类似在技能应用控制台中填的唤起链接。
        self.path = path
        # 猫精应用id，控制台中创建应用后得到的应用id。
        self.genie_app_id = genie_app_id
        # 要拉起的目标设备信息。
        self.target_info = target_info
        # 是否调试
        self.is_debug = is_debug

    def validate(self):
        if self.target_info:
            self.target_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.genie_app_id is not None:
            result['GenieAppId'] = self.genie_app_id
        if self.target_info is not None:
            result['TargetInfo'] = self.target_info.to_map()
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('GenieAppId') is not None:
            self.genie_app_id = m.get('GenieAppId')
        if m.get('TargetInfo') is not None:
            temp_model = WakeUpAppRequestTargetInfo()
            self.target_info = temp_model.from_map(m['TargetInfo'])
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
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
        target_type: str = None,
        target_identity: str = None,
    ):
        # 推送的目标类型，获取到对应设备或用户标识时的类型 - DEVICE_UNION_ID：设备unionId - DEVICE_OPEN_ID：设备openId - USER_UNION_ID：用户unionId - USER_OPEN_ID：用户openId
        self.target_type = target_type
        # 推送目标类型对应的标识值。
        self.target_identity = target_identity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_identity is not None:
            result['TargetIdentity'] = self.target_identity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetIdentity') is not None:
            self.target_identity = m.get('TargetIdentity')
        return self


class PushNotificationsRequestNotificationUnicastRequest(TeaModel):
    def __init__(
        self,
        send_target: PushNotificationsRequestNotificationUnicastRequestSendTarget = None,
        message_template_id: str = None,
        place_holder: Dict[str, Any] = None,
        encode_type: str = None,
        encode_key: str = None,
        organization_id: str = None,
        is_debug: bool = None,
    ):
        # 消息推送的目标信息。
        self.send_target = send_target
        # 消息模板，在天猫精灵应用平台中申请消息模板时得到的模板id。
        self.message_template_id = message_template_id
        # 占位符信息，例如：模板是【你好，{nick}！】这里可以是：{"nick":"小甜甜"}
        self.place_holder = place_holder
        # 编码类型，获取猫精的设备标识的途径有多种，不同途径对应不同的编码类型： PACKAGE_NAME：apk包名 SKILL_ID：技能id
        self.encode_type = encode_type
        # 编码类型对应的值，例如：编码类型是SKILLID，其值就为webhook服务中得到的skillId；编码类似是PACKAGENAME，其值就为对应客户端app的packageName。
        self.encode_key = encode_key
        # 组织标识，推送类型是XX_UNION_XX时才需要配。当存在多种途径获取猫精设备或用户标识且又需要能互通的情况下需要找平台申请组织，申请通过后由平台分配得到。
        self.organization_id = organization_id
        # 调试标识
        self.is_debug = is_debug

    def validate(self):
        if self.send_target:
            self.send_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.send_target is not None:
            result['SendTarget'] = self.send_target.to_map()
        if self.message_template_id is not None:
            result['MessageTemplateId'] = self.message_template_id
        if self.place_holder is not None:
            result['PlaceHolder'] = self.place_holder
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SendTarget') is not None:
            temp_model = PushNotificationsRequestNotificationUnicastRequestSendTarget()
            self.send_target = temp_model.from_map(m['SendTarget'])
        if m.get('MessageTemplateId') is not None:
            self.message_template_id = m.get('MessageTemplateId')
        if m.get('PlaceHolder') is not None:
            self.place_holder = m.get('PlaceHolder')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        return self


class PushNotificationsRequestTenantInfo(TeaModel):
    def __init__(
        self,
        genie_app_id: str = None,
    ):
        # 猫精应用id，【开发者平台-技能应用】创建应用后得到的应用id。
        self.genie_app_id = genie_app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.genie_app_id is not None:
            result['GenieAppId'] = self.genie_app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GenieAppId') is not None:
            self.genie_app_id = m.get('GenieAppId')
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


