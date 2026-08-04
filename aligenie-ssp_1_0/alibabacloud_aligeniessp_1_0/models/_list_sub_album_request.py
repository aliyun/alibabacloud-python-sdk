# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListSubAlbumRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.ListSubAlbumRequestDeviceInfo = None,
        query_subscription_album_request: main_models.ListSubAlbumRequestQuerySubscriptionAlbumRequest = None,
        user_info: main_models.ListSubAlbumRequestUserInfo = None,
    ):
        # Device Information
        self.device_info = device_info
        # request
        self.query_subscription_album_request = query_subscription_album_request
        # User information
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.query_subscription_album_request:
            self.query_subscription_album_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.query_subscription_album_request is not None:
            result['QuerySubscriptionAlbumRequest'] = self.query_subscription_album_request.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = main_models.ListSubAlbumRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('QuerySubscriptionAlbumRequest') is not None:
            temp_model = main_models.ListSubAlbumRequestQuerySubscriptionAlbumRequest()
            self.query_subscription_album_request = temp_model.from_map(m.get('QuerySubscriptionAlbumRequest'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.ListSubAlbumRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class ListSubAlbumRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
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

class ListSubAlbumRequestQuerySubscriptionAlbumRequest(DaraModel):
    def __init__(
        self,
        album_id: str = None,
        category_id: int = None,
        page: main_models.ListSubAlbumRequestQuerySubscriptionAlbumRequestPage = None,
        title: str = None,
    ):
        # Album ID
        self.album_id = album_id
        # Category ID
        # 
        # This parameter is required.
        self.category_id = category_id
        # Pagination Parameters
        # 
        # This parameter is required.
        self.page = page
        # Album title
        self.title = title

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.album_id is not None:
            result['AlbumId'] = self.album_id

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Page') is not None:
            temp_model = main_models.ListSubAlbumRequestQuerySubscriptionAlbumRequestPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class ListSubAlbumRequestQuerySubscriptionAlbumRequestPage(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        # Page number
        self.page_num = page_num
        # Number of entries per page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListSubAlbumRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
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

