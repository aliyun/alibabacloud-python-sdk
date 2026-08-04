# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class AddAndRemoveFavoriteContentRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.AddAndRemoveFavoriteContentRequestDeviceInfo = None,
        open_add_and_remove_favorite_content_request: main_models.AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequest = None,
        user_info: main_models.AddAndRemoveFavoriteContentRequestUserInfo = None,
    ):
        # Device identification information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Business parameters
        # 
        # This parameter is required.
        self.open_add_and_remove_favorite_content_request = open_add_and_remove_favorite_content_request
        # User identification information
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_add_and_remove_favorite_content_request:
            self.open_add_and_remove_favorite_content_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.open_add_and_remove_favorite_content_request is not None:
            result['OpenAddAndRemoveFavoriteContentRequest'] = self.open_add_and_remove_favorite_content_request.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = main_models.AddAndRemoveFavoriteContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('OpenAddAndRemoveFavoriteContentRequest') is not None:
            temp_model = main_models.AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequest()
            self.open_add_and_remove_favorite_content_request = temp_model.from_map(m.get('OpenAddAndRemoveFavoriteContentRequest'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.AddAndRemoveFavoriteContentRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class AddAndRemoveFavoriteContentRequestUserInfo(DaraModel):
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
        # When the encoding type is `SKILL_ID`, the value is the Skill ID of the application. When the encoding type is `PACKAGE_NAME`, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identifier for Tmall Genie, and each method corresponds to a different encoding type.
        # 
        # `PACKAGE_NAME`: APK package name, used for the Android application customer link. `SKILL_ID`: Skill ID, used for the cloud-based link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User Identifier, set to userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # The type of User ID.
        # 
        # `OPEN_ID`: The default User ID identity. `UNION_ID`: The organization-dimension User ID identity. This value is available only after an organization has been requested on the Tmall Genie Skills Open Platform.
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

class AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequest(DaraModel):
    def __init__(
        self,
        favorite_cmd: str = None,
        open_source_raw_id_pair: main_models.AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequestOpenSourceRawIdPair = None,
        package_type: str = None,
    ):
        # Operation Type
        # 
        # ADD for collect; REMOVE for remove from favorites
        # 
        # This parameter is required.
        self.favorite_cmd = favorite_cmd
        # Object to collect or remove from favorites
        # 
        # This parameter is required.
        self.open_source_raw_id_pair = open_source_raw_id_pair
        # Content type
        # 
        # Content: CONTENT; Album: ALBUM; Playlist: COLLECT.
        # 
        # This parameter is required.
        self.package_type = package_type

    def validate(self):
        if self.open_source_raw_id_pair:
            self.open_source_raw_id_pair.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.favorite_cmd is not None:
            result['FavoriteCmd'] = self.favorite_cmd

        if self.open_source_raw_id_pair is not None:
            result['OpenSourceRawIdPair'] = self.open_source_raw_id_pair.to_map()

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FavoriteCmd') is not None:
            self.favorite_cmd = m.get('FavoriteCmd')

        if m.get('OpenSourceRawIdPair') is not None:
            temp_model = main_models.AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequestOpenSourceRawIdPair()
            self.open_source_raw_id_pair = temp_model.from_map(m.get('OpenSourceRawIdPair'))

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        return self

class AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequestOpenSourceRawIdPair(DaraModel):
    def __init__(
        self,
        extend_info: Dict[str, Any] = None,
        raw_id: str = None,
        source: str = None,
    ):
        # Extension information
        self.extend_info = extend_info
        # Third-party ID
        # 
        # This parameter is required.
        self.raw_id = raw_id
        # Source
        # 
        # This parameter is required.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.raw_id is not None:
            result['RawId'] = self.raw_id

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

class AddAndRemoveFavoriteContentRequestDeviceInfo(DaraModel):
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
        # When the encoding type is `SKILL_ID`, the value is the Skill ID of the application. When the encoding type is `PACKAGE_NAME`, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device ID for Tmall Genie, and each method corresponds to a different encoding type.
        # 
        # `PACKAGE_NAME`: APK package name, used for the Android application customer link. `SKILL_ID`: Skill ID, used for the cloud-based link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID, set to deviceOpenId or deviceUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of device ID
        # 
        # `OPEN_ID`: Default device ID identifier. `UNION_ID`: Device ID identifier at the organization dimension. This value is available only after an organization has been registered on the Tmall Genie Skill Application Open Platform.
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

