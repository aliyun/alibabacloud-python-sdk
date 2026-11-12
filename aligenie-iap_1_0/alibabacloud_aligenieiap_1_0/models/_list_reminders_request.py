# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class ListRemindersRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.ListRemindersRequestDeviceInfo = None,
        payload: main_models.ListRemindersRequestPayload = None,
        user_info: main_models.ListRemindersRequestUserInfo = None,
    ):
        # List of device identity information.
        # 
        # This parameter is required.
        self.device_info = device_info
        # Input parameters for the service request.
        # 
        # This parameter is required.
        self.payload = payload
        # List of user identity information.
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
            temp_model = main_models.ListRemindersRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Payload') is not None:
            temp_model = main_models.ListRemindersRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.ListRemindersRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class ListRemindersRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type:
        #  - When the encoding type is SKILLID, the value is the application\\"s Skill ID.
        #  - When the encoding type is PACKAGENAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identifier for Tmall Genie, and each method corresponds to a different encoding type.  
        # - PACKAGE_NAME: APK package name, used for the Android application customer ingest endpoint.  
        # - SKILL_ID: Skill ID, used for the cloud-side ingest endpoint.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User Identifier, either userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of the User ID:
        #  - OPEN_ID: The default User ID identity.
        #  - UNION_ID: The User ID identity at the organization dimension. This value is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. This parameter is required when **IdType** is configured as **UNION_ID**.
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

class ListRemindersRequestPayload(DaraModel):
    def __init__(
        self,
        is_debug: bool = None,
    ):
        # Indicates whether this invocation is for debug purposes.
        # 
        # This parameter is required.
        self.is_debug = is_debug

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')

        return self

class ListRemindersRequestDeviceInfo(DaraModel):
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
        # - When the encoding type is SKILLID, the value is the application\\"s Skill ID.  
        # - When the encoding type is PACKAGENAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device ID for Tmall Genie, and each method corresponds to a different encoding type.  
        # - PACKAGE_NAME: APK package name, used in the Android application customer flow.  
        # - SKILL_ID: Skill ID, used in the cloud-based flow.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID, either deviceOpenId or deviceUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of the device ID.  
        # - OPEN_ID: The default device ID.  
        # - UNION_ID: Organization-level device ID. This value is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required when **IdType** is set to **UNION_ID**.
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

