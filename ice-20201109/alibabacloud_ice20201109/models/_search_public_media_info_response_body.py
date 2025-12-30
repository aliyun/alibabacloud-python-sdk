# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SearchPublicMediaInfoResponseBody(DaraModel):
    def __init__(
        self,
        public_media_infos: List[main_models.SearchPublicMediaInfoResponseBodyPublicMediaInfos] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.public_media_infos = public_media_infos
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.public_media_infos:
            for v1 in self.public_media_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PublicMediaInfos'] = []
        if self.public_media_infos is not None:
            for k1 in self.public_media_infos:
                result['PublicMediaInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.public_media_infos = []
        if m.get('PublicMediaInfos') is not None:
            for k1 in m.get('PublicMediaInfos'):
                temp_model = main_models.SearchPublicMediaInfoResponseBodyPublicMediaInfos()
                self.public_media_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchPublicMediaInfoResponseBodyPublicMediaInfos(DaraModel):
    def __init__(
        self,
        authorized: bool = None,
        favorite: bool = None,
        media_info: main_models.SearchPublicMediaInfoResponseBodyPublicMediaInfosMediaInfo = None,
        remaining_auth_time: str = None,
    ):
        self.authorized = authorized
        self.favorite = favorite
        self.media_info = media_info
        self.remaining_auth_time = remaining_auth_time

    def validate(self):
        if self.media_info:
            self.media_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorized is not None:
            result['Authorized'] = self.authorized

        if self.favorite is not None:
            result['Favorite'] = self.favorite

        if self.media_info is not None:
            result['MediaInfo'] = self.media_info.to_map()

        if self.remaining_auth_time is not None:
            result['RemainingAuthTime'] = self.remaining_auth_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')

        if m.get('Favorite') is not None:
            self.favorite = m.get('Favorite')

        if m.get('MediaInfo') is not None:
            temp_model = main_models.SearchPublicMediaInfoResponseBodyPublicMediaInfosMediaInfo()
            self.media_info = temp_model.from_map(m.get('MediaInfo'))

        if m.get('RemainingAuthTime') is not None:
            self.remaining_auth_time = m.get('RemainingAuthTime')

        return self

class SearchPublicMediaInfoResponseBodyPublicMediaInfosMediaInfo(DaraModel):
    def __init__(
        self,
        dynamic_meta_data: main_models.SearchPublicMediaInfoResponseBodyPublicMediaInfosMediaInfoDynamicMetaData = None,
        media_basic_info: main_models.SearchPublicMediaInfoResponseBodyPublicMediaInfosMediaInfoMediaBasicInfo = None,
        media_id: str = None,
    ):
        self.dynamic_meta_data = dynamic_meta_data
        # BasicInfo
        self.media_basic_info = media_basic_info
        self.media_id = media_id

    def validate(self):
        if self.dynamic_meta_data:
            self.dynamic_meta_data.validate()
        if self.media_basic_info:
            self.media_basic_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_meta_data is not None:
            result['DynamicMetaData'] = self.dynamic_meta_data.to_map()

        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicMetaData') is not None:
            temp_model = main_models.SearchPublicMediaInfoResponseBodyPublicMediaInfosMediaInfoDynamicMetaData()
            self.dynamic_meta_data = temp_model.from_map(m.get('DynamicMetaData'))

        if m.get('MediaBasicInfo') is not None:
            temp_model = main_models.SearchPublicMediaInfoResponseBodyPublicMediaInfosMediaInfoMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m.get('MediaBasicInfo'))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class SearchPublicMediaInfoResponseBodyPublicMediaInfosMediaInfoMediaBasicInfo(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        category: str = None,
        cover_url: str = None,
        create_time: str = None,
        deleted_time: str = None,
        description: str = None,
        media_id: str = None,
        media_tags: str = None,
        media_type: str = None,
        modified_time: str = None,
        source: str = None,
        sprite_images: str = None,
        status: str = None,
        title: str = None,
        user_data: str = None,
    ):
        self.business_type = business_type
        self.category = category
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted_time = deleted_time
        self.description = description
        # MediaId
        self.media_id = media_id
        self.media_tags = media_tags
        self.media_type = media_type
        self.modified_time = modified_time
        self.source = source
        self.sprite_images = sprite_images
        self.status = status
        self.title = title
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.category is not None:
            result['Category'] = self.category

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time

        if self.description is not None:
            result['Description'] = self.description

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.source is not None:
            result['Source'] = self.source

        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SearchPublicMediaInfoResponseBodyPublicMediaInfosMediaInfoDynamicMetaData(DaraModel):
    def __init__(
        self,
        data: str = None,
        type: str = None,
    ):
        self.data = data
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

