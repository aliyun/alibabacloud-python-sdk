# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class PushNotificationsRequest(DaraModel):
    def __init__(
        self,
        notification_unicast_request: main_models.PushNotificationsRequestNotificationUnicastRequest = None,
        tenant_info: main_models.PushNotificationsRequestTenantInfo = None,
    ):
        # Input parameter object for message push.
        # 
        # This parameter is required.
        self.notification_unicast_request = notification_unicast_request
        # Identity information.
        self.tenant_info = tenant_info

    def validate(self):
        if self.notification_unicast_request:
            self.notification_unicast_request.validate()
        if self.tenant_info:
            self.tenant_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notification_unicast_request is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request.to_map()

        if self.tenant_info is not None:
            result['TenantInfo'] = self.tenant_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationUnicastRequest') is not None:
            temp_model = main_models.PushNotificationsRequestNotificationUnicastRequest()
            self.notification_unicast_request = temp_model.from_map(m.get('NotificationUnicastRequest'))

        if m.get('TenantInfo') is not None:
            temp_model = main_models.PushNotificationsRequestTenantInfo()
            self.tenant_info = temp_model.from_map(m.get('TenantInfo'))

        return self

class PushNotificationsRequestTenantInfo(DaraModel):
    def __init__(self):
        pass
    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self

class PushNotificationsRequestNotificationUnicastRequest(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        is_debug: bool = None,
        message_template_id: str = None,
        organization_id: str = None,
        place_holder: Dict[str, str] = None,
        send_target: main_models.PushNotificationsRequestNotificationUnicastRequestSendTarget = None,
    ):
        # The value corresponding to the encoding type.  
        # - When the encoding type is SKILL_ID, the value is the skill ID obtained from the webhook service.  
        # - When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the Tmall Genie device ID, and each method corresponds to a different encoding type:  
        # - PACKAGE_NAME: APK package name  
        # - SKILL_ID: Skill ID
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Debug flag. When the skill application is in the debug phase, setting this flag determines whether the retrieved skill application information is from the editing state or the online state.
        self.is_debug = is_debug
        # Message template ID obtained when applying for a message template on the Tmall Genie Application Platform.
        # 
        # This parameter is required.
        self.message_template_id = message_template_id
        # Organization Identifier. This parameter is required only when the push type is `XX_UNION_XX`. If you obtain CatGenie device or user identifiers through multiple channels and need interoperability among them, you must request an organization from the platform. After approval, the platform will assign an organization identifier.
        self.organization_id = organization_id
        # Placeholder information. For example, for the template ["Hello, {nick}!"], this could be {"nick":"Sweetie"}. Additionally, within the placeholder parameters, you can append parameters to the application launch link to support hyperlinking to a specific address, such as: `{"nick":"Sweetie","_URL_SUFFIX_":"xxx"}`. The hyperlink address in the message pop-up will then be: application launch link + `${_URL_SUFFIX_}`. This feature only works for applications that have configured a launch link.
        self.place_holder = place_holder
        # The target information for message push.
        # 
        # This parameter is required.
        self.send_target = send_target

    def validate(self):
        if self.send_target:
            self.send_target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.PushNotificationsRequestNotificationUnicastRequestSendTarget()
            self.send_target = temp_model.from_map(m.get('SendTarget'))

        return self

class PushNotificationsRequestNotificationUnicastRequestSendTarget(DaraModel):
    def __init__(
        self,
        target_identity: str = None,
        target_type: str = None,
    ):
        # The identity value corresponding to the Push Target Type.
        self.target_identity = target_identity
        # The type of the Push Target, indicating the type when obtaining the corresponding device or User Identifier:  
        # - `DEVICE_UNION_ID`: device unionId  
        # - `DEVICE_OPEN_ID`: device openId  
        # - `USER_UNION_ID`: user unionId  
        # - `USER_OPEN_ID`: user openId
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

