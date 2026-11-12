# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class SendNotificationsRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.SendNotificationsRequestDeviceInfo = None,
        notification_unicast_request: main_models.SendNotificationsRequestNotificationUnicastRequest = None,
        tenant_info: main_models.SendNotificationsRequestTenantInfo = None,
        user_info: main_models.SendNotificationsRequestUserInfo = None,
    ):
        # Device identity information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Input parameter object for message push.
        # 
        # This parameter is required.
        self.notification_unicast_request = notification_unicast_request
        # Identity information.
        self.tenant_info = tenant_info
        # User Identifier information
        # 
        # This parameter is required.
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.SendNotificationsRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('NotificationUnicastRequest') is not None:
            temp_model = main_models.SendNotificationsRequestNotificationUnicastRequest()
            self.notification_unicast_request = temp_model.from_map(m.get('NotificationUnicastRequest'))

        if m.get('TenantInfo') is not None:
            temp_model = main_models.SendNotificationsRequestTenantInfo()
            self.tenant_info = temp_model.from_map(m.get('TenantInfo'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.SendNotificationsRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class SendNotificationsRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type. If the encoding type is SKILL_ID, the value is the application\\"s Skill ID. If the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the Maojing User Identifier, and each method corresponds to a different encoding type:  
        # - PACKAGE_NAME: APK package name, used for the Android application customer link  
        # - SKILL_ID: Skill ID, used for the cloud-based link
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User Identifier (userOpenId or userUnionId)
        # 
        # This parameter is required.
        self.id = id
        # Type of the User ID:  
        # - OPEN_ID: Default User ID identifier  
        # - UNION_ID: Organization-dimension User ID identifier, available only after an organization has been requested on the Maojing Skill Application Open Platform
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required if IdType is UNION_ID.
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

class SendNotificationsRequestTenantInfo(DaraModel):
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

class SendNotificationsRequestNotificationUnicastRequest(DaraModel):
    def __init__(
        self,
        is_debug: bool = None,
        message_template_id: str = None,
        place_holder: Dict[str, str] = None,
        send_target: main_models.SendNotificationsRequestNotificationUnicastRequestSendTarget = None,
    ):
        # Debug flag. When the skill application is in the debugging phase, setting this flag determines whether the retrieved skill application information is from the editing state or the online state.
        self.is_debug = is_debug
        # Message template ID obtained when requesting a message template in the Tmall Genie Application Platform.
        # 
        # This parameter is required.
        self.message_template_id = message_template_id
        # Placeholder information. For example, for the template ["Hello, {nick}!"], this can be: {"nick":"Xiao Tian Tian"}. Additionally, within the placeholder parameters, you can append parameters to the application launch link to support hyperlinking to a specific address, such as: `{"nick":"Xiao Tian Tian","_URL_SUFFIX_":"xxx"}`. The hyperlink address in the message pop-up will then be: application launch link + `${_URL_SUFFIX_}`. This feature is only effective for applications that have configured a launch link.
        self.place_holder = place_holder
        # Target information for message push.
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
            temp_model = main_models.SendNotificationsRequestNotificationUnicastRequestSendTarget()
            self.send_target = temp_model.from_map(m.get('SendTarget'))

        return self

class SendNotificationsRequestNotificationUnicastRequestSendTarget(DaraModel):
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

class SendNotificationsRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type. If the encoding type is SKILL_ID, the value is the application\\"s Skill ID. If the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device ID for Maojing, and each method corresponds to a different encoding type:  
        #  - PACKAGE_NAME: APK package name, used for the Android application customer link  
        #  - SKILL_ID: Skill ID, used for the cloud link
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID (deviceOpenId or deviceUnionId)
        # 
        # This parameter is required.
        self.id = id
        # Type of device ID:  
        #  - OPEN_ID: Default device ID  
        #  - UNION_ID: Organization-dimension device ID, available only after an organization has been requested on the Maojing Skill Application Open Platform
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required if IdType is UNION_ID.
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

