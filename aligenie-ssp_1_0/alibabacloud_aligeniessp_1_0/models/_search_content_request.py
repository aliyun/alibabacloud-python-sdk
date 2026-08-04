# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class SearchContentRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.SearchContentRequestDeviceInfo = None,
        request: main_models.SearchContentRequestRequest = None,
        user_info: main_models.SearchContentRequestUserInfo = None,
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
            temp_model = main_models.SearchContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Request') is not None:
            temp_model = main_models.SearchContentRequestRequest()
            self.request = temp_model.from_map(m.get('Request'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.SearchContentRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class SearchContentRequestUserInfo(DaraModel):
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
        # When the encoding type is SKILL_ID, the value is the Skill ID of the application.  
        # When the encoding type is PACKAGE_NAME, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identifier for Tmall Genie, and each method corresponds to a different encoding type.  
        # 
        # `PACKAGE_NAME`: APK package name, used for the Android application customer link.  
        # `SKILL_ID`: Skill ID, used for the cloud-based link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User identifier, set to either `userOpenId` or `userUnionId`.
        # 
        # This parameter is required.
        self.id = id
        # The Type of the User ID.
        # 
        # OPEN_ID: The default User ID identity.  
        # UNION_ID: The organization-dimension User ID identity. This value is available only after an organization has been requested on the Tmall Genie Skills Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required when `IdType` is `UNION_ID`.
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

class SearchContentRequestRequest(DaraModel):
    def __init__(
        self,
        cate: str = None,
        page_num: int = None,
        page_size: int = None,
        query: str = None,
        query_album: bool = None,
        sub_cate: str = None,
    ):
        # The search scope: music or audio.  
        # Input parameter enumeration: music | program
        self.cate = cate
        # Page number
        self.page_num = page_num
        # Number of records per page
        self.page_size = page_size
        # Query keyword
        self.query = query
        # Whether to query albums
        self.query_album = query_album
        # When `cate` is `music`, `subCate` can be omitted.  
        # If `subCate` is provided, it can be one of the following:  
        # `song` (Song), `singer` (Artist), `album` (Album).  
        # 
        # When `cate` is `program`, `subCate` can be omitted.  
        # If `subCate` is provided, it can be one of the following:  
        # `album` (Album), `audio` (Program Audio), `radio` (Radio Station).
        self.sub_cate = sub_cate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate is not None:
            result['Cate'] = self.cate

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.query_album is not None:
            result['QueryAlbum'] = self.query_album

        if self.sub_cate is not None:
            result['SubCate'] = self.sub_cate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cate') is not None:
            self.cate = m.get('Cate')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('QueryAlbum') is not None:
            self.query_album = m.get('QueryAlbum')

        if m.get('SubCate') is not None:
            self.sub_cate = m.get('SubCate')

        return self

class SearchContentRequestDeviceInfo(DaraModel):
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
        # When the encoding type is `SKILL_ID`, the value is the application\\"s Skill ID.  
        # When the encoding type is `PACKAGE_NAME`, the value is the `packageName` of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device ID for Tmall Genie, and each method corresponds to a different encoding type.  
        # 
        # `PACKAGE_NAME`: APK package name, used for the Android application customer link.  
        # `SKILL_ID`: Skill ID, used for the cloud-based link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID, set to either `deviceOpenId` or `deviceUnionId`.
        # 
        # This parameter is required.
        self.id = id
        # Type of device ID.  
        # 
        # `OPEN_ID`: Default device ID identity.  
        # `UNION_ID`: Organization-dimension device ID identity. This value is available only after an organization has been registered on the Tmall Genie Skill Application Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required when `IdType` is `UNION_ID`.
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

