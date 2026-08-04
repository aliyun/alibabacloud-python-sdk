# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListMusicRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.ListMusicRequestDeviceInfo = None,
        payload: main_models.ListMusicRequestPayload = None,
        user_info: main_models.ListMusicRequestUserInfo = None,
    ):
        # Device ID information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Input parameters for the service request
        # 
        # This parameter is required.
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
            temp_model = main_models.ListMusicRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Payload') is not None:
            temp_model = main_models.ListMusicRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.ListMusicRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class ListMusicRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type. When the encoding type is SKILL_ID, the value is the application\\"s SkillID. When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identifier for Maojing, and each method corresponds to a different encoding type: PACKAGE_NAME: APK package name, used for Android application customer links; SKILL_ID: skill ID, used for cloud-based links
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User Identifier (userOpenId or userUnionId)
        # 
        # This parameter is required.
        self.id = id
        # Type of user ID: OPEN_ID: default user ID identifier; UNION_ID: organization-dimension user ID identifier, available only after an organization has been requested on the Maojing Skill Application Open Platform
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID, required if IdType is UNION_ID
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

class ListMusicRequestPayload(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        music_id: int = None,
        music_name: str = None,
        music_type: int = None,
        music_type_name: str = None,
        page_size: int = None,
    ):
        # Current page
        self.current_page = current_page
        # Ringtone ID, an extension field; currently not required
        self.music_id = music_id
        # Ringtone name, an extension field; currently not required to be passed.
        self.music_name = music_name
        # Ringtone category ID, returned by the queryMusicType API
        # 
        # This parameter is required.
        self.music_type = music_type
        # Ringtone category name, returned by the queryMusicType API
        # 
        # This parameter is required.
        self.music_type_name = music_type_name
        # Number of entries per page: maximum value is 100
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.music_id is not None:
            result['MusicId'] = self.music_id

        if self.music_name is not None:
            result['MusicName'] = self.music_name

        if self.music_type is not None:
            result['MusicType'] = self.music_type

        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')

        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')

        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')

        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListMusicRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type: when the encoding type is SKILL_ID, the value is the application\\"s SkillID; when the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device ID for Maojing, and each method corresponds to a different encoding type: PACKAGE_NAME refers to the APK package name, used in the Android application customer link; SKILL_ID refers to the skill ID, used in the cloud link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID (deviceOpenId or deviceUnionId)
        # 
        # This parameter is required.
        self.id = id
        # Type of the device ID: OPEN_ID indicates the default device ID; UNION_ID indicates the organization-dimension device ID, which is available only after an organization has been requested on the Maojing Skill Application Open Platform.
        # 
        # This parameter is required.
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

