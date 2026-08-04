# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListRecommendContentRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.ListRecommendContentRequestDeviceInfo = None,
        request: main_models.ListRecommendContentRequestRequest = None,
        user_info: main_models.ListRecommendContentRequestUserInfo = None,
    ):
        # Device identification information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Request Parameters
        # 
        # This parameter is required.
        self.request = request
        # User identification information
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.request:
            self.request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.request is not None:
            result['Request'] = self.request.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = main_models.ListRecommendContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Request') is not None:
            temp_model = main_models.ListRecommendContentRequestRequest()
            self.request = temp_model.from_map(m.get('Request'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.ListRecommendContentRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class ListRecommendContentRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type.
        # 
        # When the encoding type is SKILL_ID, the value is the Skill ID of the application.  
        # When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identifier for Tmall Genie, and each method corresponds to a different encoding type.
        # 
        # PACKAGE_NAME: APK package name, used for the Android application client path.
        # SKILL_ID: Skill ID, used for the cloud-based path.
        self.encode_type = encode_type
        # User Identifier, set to userOpenId or userUnionId.
        self.id = id
        # Type of User ID.
        # 
        # OPEN_ID: The default User ID identifier.  
        # UNION_ID: The organization-dimension User ID identifier. This value is available only after an organization has been requested on the Tmall Genie Skills Application Open Platform.
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

class ListRecommendContentRequestRequest(DaraModel):
    def __init__(
        self,
        count: int = None,
        type: str = None,
    ):
        # Quantity of recommendations
        self.count = count
        # Default value: song (currently, the extension field supports only song)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListRecommendContentRequestDeviceInfo(DaraModel):
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
        # When the encoding type is SKILL_ID, the value is the application\\"s Skill ID.
        # When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device ID for Tmall Genie, and each method corresponds to a different encoding type.
        # 
        # PACKAGE_NAME: APK package name, used for the Android application client path.
        # SKILL_ID: Skill ID, used for the cloud-based path.
        self.encode_type = encode_type
        # Device ID, set to deviceOpenId or deviceUnionId.
        self.id = id
        # Type of device ID
        # 
        # OPEN_ID: Default device ID identity.
        # UNION_ID: Organization-dimension device ID identity. This value is available only after an organization has been registered on the Tmall Genie Skill Application Open Platform.
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

