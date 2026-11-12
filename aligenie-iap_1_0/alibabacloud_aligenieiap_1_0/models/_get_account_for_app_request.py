# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class GetAccountForAppRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.GetAccountForAppRequestDeviceInfo = None,
        payload: main_models.GetAccountForAppRequestPayload = None,
        user_info: main_models.GetAccountForAppRequestUserInfo = None,
    ):
        # Device ID information
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
            temp_model = main_models.GetAccountForAppRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Payload') is not None:
            temp_model = main_models.GetAccountForAppRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.GetAccountForAppRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class GetAccountForAppRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type:  
        # - When the encoding type is SKILL_ID, the value is the application\\"s Skill ID.  
        # - When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identifier for Tmall Genie, and each way corresponds to a different encoding type:  
        # - PACKAGE_NAME: APK package name, used for the Android application customer link.  
        # - SKILL_ID: Skill ID, used for the cloud-based link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User identifier, which can be set to userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of User ID:  
        # - OPEN_ID: The default user ID identity.  
        # - UNION_ID: Organization-dimension user ID identity. This value is available only after an organization has been requested on the Tmall Genie Skill Application Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. This field is required if IdType is set to UNION_ID.
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

class GetAccountForAppRequestPayload(DaraModel):
    def __init__(
        self,
        phone: str = None,
        origin_uuid: str = None,
    ):
        # Phone number of the authorized membership user.
        self.phone = phone
        # Plaintext UUID
        self.origin_uuid = origin_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phone is not None:
            result['Phone'] = self.phone

        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')

        return self

class GetAccountForAppRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type:  
        # - When the encoding type is SKILL_ID, the value is the application\\"s Skill ID.  
        # - When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device ID for Tmall Genie, and each method corresponds to a different encoding type.
        # - PACKAGE_NAME: APK package name, used in the Android application customer flow.
        # - SKILL_ID: Skill ID, used in the cloud-based flow.
        self.encode_type = encode_type
        # Device ID, set to deviceOpenId or deviceUnionId.
        self.id = id
        # Type of the device ID:  
        # - OPEN_ID: Default device ID identifier  
        # - UNION_ID: Device ID identifier at the organization dimension. This value is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
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

