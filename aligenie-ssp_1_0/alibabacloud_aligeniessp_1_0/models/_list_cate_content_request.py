# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListCateContentRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.ListCateContentRequestDeviceInfo = None,
        request: main_models.ListCateContentRequestRequest = None,
        user_info: main_models.ListCateContentRequestUserInfo = None,
    ):
        # Device identifier information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Request Parameters
        # 
        # This parameter is required.
        self.request = request
        # User identifier information
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
            temp_model = main_models.ListCateContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Request') is not None:
            temp_model = main_models.ListCateContentRequestRequest()
            self.request = temp_model.from_map(m.get('Request'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.ListCateContentRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class ListCateContentRequestUserInfo(DaraModel):
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
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identifier for Tmall Genie, and each method corresponds to a different encoding type.
        # 
        # PACKAGE_NAME: APK package name, used for the Android application customer link.  
        # SKILL_ID: Skill ID, used for the cloud-based link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User Identifier, set to userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of User ID.
        # 
        # OPEN_ID: The default User ID identifier.  
        # UNION_ID: The organization-dimension User ID identifier. This value is available only after an organization has been registered on the Tmall Genie Skills Application Open Platform.
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

class ListCateContentRequestRequest(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        is_album: bool = None,
        page_num: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # Category ID
        # 
        # This parameter is required.
        self.cate_id = cate_id
        # Indicates whether to query albums
        # 
        # This parameter is required.
        self.is_album = is_album
        # Page number
        # 
        # This parameter is required.
        self.page_num = page_num
        # Number of records per page
        # 
        # This parameter is required.
        self.page_size = page_size
        # Sorting field
        self.sort_by = sort_by
        # Sorting order
        # 
        # This parameter is required.
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.is_album is not None:
            result['IsAlbum'] = self.is_album

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('IsAlbum') is not None:
            self.is_album = m.get('IsAlbum')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

class ListCateContentRequestDeviceInfo(DaraModel):
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
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device identifier for Tmall Genie, and each method corresponds to a different encoding type.
        # 
        # PACKAGE_NAME: APK package name, used for the Android application customer link.
        # SKILL_ID: Skill ID, used for the cloud-based link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device identifier, set to deviceOpenId or deviceUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of device ID
        # 
        # OPEN_ID: Default device ID identifier.  
        # UNION_ID: Organization-level device ID identifier. This value is available only after an organization has been registered on the Tmall Genie Skill Application Open Platform.
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

