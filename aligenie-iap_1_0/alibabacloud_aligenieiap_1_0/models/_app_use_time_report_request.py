# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class AppUseTimeReportRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.AppUseTimeReportRequestDeviceInfo = None,
        payload: main_models.AppUseTimeReportRequestPayload = None,
        user_info: main_models.AppUseTimeReportRequestUserInfo = None,
    ):
        # Device identity information
        self.device_info = device_info
        # Business parameters
        self.payload = payload
        # User identifier information
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
            temp_model = main_models.AppUseTimeReportRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Payload') is not None:
            temp_model = main_models.AppUseTimeReportRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.AppUseTimeReportRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class AppUseTimeReportRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type  
        # 
        # - When the encoding type is SKILL_ID, the value is the application\\"s Skill ID.  
        # - When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client application.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identifier from Tmall Genie, and each method corresponds to a different encoding type.  
        # - PACKAGE_NAME: APK package name, used for the Android application customer flow.  
        # - SKILL_ID: Skill ID, used for the cloud-based flow.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User identifier, set to either userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of User ID  
        # - OPEN_ID: Default User ID identifier.  
        # - UNION_ID: Organization-dimension User ID identifier. This value is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
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

class AppUseTimeReportRequestPayload(DaraModel):
    def __init__(
        self,
        action: str = None,
        is_privilege: int = None,
        resource_id: str = None,
        resource_type: int = None,
        step_code: str = None,
        vip_type: int = None,
        origin_uuid: str = None,
    ):
        # Action item
        # 
        # - start indicates Start
        # - end indicates End
        # 
        # This parameter is required.
        self.action = action
        # Indicates whether the benefit is exclusive to members:
        # 
        # - 1 indicates Yes  
        # - 0 indicates No
        # 
        # This parameter is required.
        self.is_privilege = is_privilege
        # Resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # Resource type:
        # 
        # - 0 indicates game
        # - 1 indicates audio
        # - 2 indicates video
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # Step code. The start and end actions must be uniquely matched.
        # 
        # This parameter is required.
        self.step_code = step_code
        # Membership type:
        # 
        # - 0 indicates Cat Spirit Membership
        # - 1 indicates third-party proprietary membership
        # 
        # This parameter is required.
        self.vip_type = vip_type
        # Plaintext UUID
        self.origin_uuid = origin_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.is_privilege is not None:
            result['IsPrivilege'] = self.is_privilege

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.step_code is not None:
            result['StepCode'] = self.step_code

        if self.vip_type is not None:
            result['VipType'] = self.vip_type

        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('IsPrivilege') is not None:
            self.is_privilege = m.get('IsPrivilege')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StepCode') is not None:
            self.step_code = m.get('StepCode')

        if m.get('VipType') is not None:
            self.vip_type = m.get('VipType')

        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')

        return self



class AppUseTimeReportRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type.
        # 
        # - When the encoding type is SKILL_ID, the value is the application\\"s Skill ID.
        # - When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client application.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device identity for Tmall Genie, and each method corresponds to a different encoding type.  
        # - PACKAGE_NAME: APK package name, used for Android application customer-side integration.  
        # - SKILL_ID: Skill ID, used for cloud-side integration.
        self.encode_type = encode_type
        # Device ID, set to deviceOpenId or deviceUnionId.
        self.id = id
        # Type of device ID  
        # - OPEN_ID: Default device ID.  
        # - UNION_ID: Organization-dimension device ID, available only after an organization has been requested in the Tmall Genie Skill Application Open Platform.
        self.id_type = id_type
        # Organization ID, required if IdType is UNION_ID.
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

