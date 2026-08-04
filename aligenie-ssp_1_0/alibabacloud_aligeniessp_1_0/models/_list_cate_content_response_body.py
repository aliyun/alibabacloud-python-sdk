# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListCateContentResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.ListCateContentResponseBodyResult = None,
    ):
        # code encoding
        self.code = code
        # message information
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Return Result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListCateContentResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListCateContentResponseBodyResult(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        open_data_item_list: List[main_models.ListCateContentResponseBodyResultOpenDataItemList] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # Current page number
        self.current_page_num = current_page_num
        # Data information
        self.open_data_item_list = open_data_item_list
        # Number of records per page
        self.page_size = page_size
        # Total number of records
        self.total_size = total_size

    def validate(self):
        if self.open_data_item_list:
            for v1 in self.open_data_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['OpenDataItemList'] = []
        if self.open_data_item_list is not None:
            for k1 in self.open_data_item_list:
                result['OpenDataItemList'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        self.open_data_item_list = []
        if m.get('OpenDataItemList') is not None:
            for k1 in m.get('OpenDataItemList'):
                temp_model = main_models.ListCateContentResponseBodyResultOpenDataItemList()
                self.open_data_item_list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListCateContentResponseBodyResultOpenDataItemList(DaraModel):
    def __init__(
        self,
        alias: List[str] = None,
        audition: bool = None,
        authors: List[main_models.ListCateContentResponseBodyResultOpenDataItemListAuthors] = None,
        category: str = None,
        charge: bool = None,
        comm_cate_id: str = None,
        cover: main_models.ListCateContentResponseBodyResultOpenDataItemListCover = None,
        description: str = None,
        hot_score: float = None,
        item_type: str = None,
        raw_id: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        valid: str = None,
        id: int = None,
    ):
        # Alias
        self.alias = alias
        # Is audition available
        self.audition = audition
        # author information
        self.authors = authors
        # Transform controlType based on the assigned public category
        self.category = category
        # Whether it is charged
        self.charge = charge
        # Category ID
        self.comm_cate_id = comm_cate_id
        # Album thumbnail image
        self.cover = cover
        # Content description
        self.description = description
        # Popularity score
        self.hot_score = hot_score
        # Type of content, such as music, audio, radio, jokes, etc.
        self.item_type = item_type
        # Third-party ID of the album
        self.raw_id = raw_id
        # Source
        self.source = source
        # Title
        self.title = title
        # Transform favoriteType based on the associated public category.
        self.type = type
        # Indicates whether the content is playable.
        self.valid = valid
        # Primary key ID
        self.id = id

    def validate(self):
        if self.authors:
            for v1 in self.authors:
                 if v1:
                    v1.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.audition is not None:
            result['Audition'] = self.audition

        result['Authors'] = []
        if self.authors is not None:
            for k1 in self.authors:
                result['Authors'].append(k1.to_map() if k1 else None)

        if self.category is not None:
            result['Category'] = self.category

        if self.charge is not None:
            result['Charge'] = self.charge

        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id

        if self.cover is not None:
            result['Cover'] = self.cover.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.hot_score is not None:
            result['HotScore'] = self.hot_score

        if self.item_type is not None:
            result['ItemType'] = self.item_type

        if self.raw_id is not None:
            result['RawId'] = self.raw_id

        if self.source is not None:
            result['Source'] = self.source

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        if self.valid is not None:
            result['Valid'] = self.valid

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Audition') is not None:
            self.audition = m.get('Audition')

        self.authors = []
        if m.get('Authors') is not None:
            for k1 in m.get('Authors'):
                temp_model = main_models.ListCateContentResponseBodyResultOpenDataItemListAuthors()
                self.authors.append(temp_model.from_map(k1))

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Charge') is not None:
            self.charge = m.get('Charge')

        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')

        if m.get('Cover') is not None:
            temp_model = main_models.ListCateContentResponseBodyResultOpenDataItemListCover()
            self.cover = temp_model.from_map(m.get('Cover'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')

        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')

        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

class ListCateContentResponseBodyResultOpenDataItemListCover(DaraModel):
    def __init__(
        self,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
        can_resize: bool = None,
    ):
        # Default image
        self.img = img
        # Large image
        self.large = large
        # Medium image (Deprecated)
        self.mediam = mediam
        # Medium image
        self.medium = medium
        # Small image
        self.small = small
        # Indicates whether cropping can be performed using OSS rules.
        self.can_resize = can_resize

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.img is not None:
            result['Img'] = self.img

        if self.large is not None:
            result['Large'] = self.large

        if self.mediam is not None:
            result['Mediam'] = self.mediam

        if self.medium is not None:
            result['Medium'] = self.medium

        if self.small is not None:
            result['Small'] = self.small

        if self.can_resize is not None:
            result['canResize'] = self.can_resize

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Img') is not None:
            self.img = m.get('Img')

        if m.get('Large') is not None:
            self.large = m.get('Large')

        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')

        if m.get('Medium') is not None:
            self.medium = m.get('Medium')

        if m.get('Small') is not None:
            self.small = m.get('Small')

        if m.get('canResize') is not None:
            self.can_resize = m.get('canResize')

        return self

class ListCateContentResponseBodyResultOpenDataItemListAuthors(DaraModel):
    def __init__(
        self,
        author_types: List[str] = None,
        cover: main_models.ListCateContentResponseBodyResultOpenDataItemListAuthorsCover = None,
        description: str = None,
        gender: str = None,
        id: int = None,
        online: bool = None,
        raw_id: str = None,
        source: str = None,
        title: str = None,
    ):
        # Author type
        self.author_types = author_types
        # profile picture
        self.cover = cover
        # Author description
        self.description = description
        # Gender
        self.gender = gender
        # Primary key ID of the author information
        self.id = id
        # Whether it is online
        self.online = online
        # third-party author ID
        self.raw_id = raw_id
        # Source
        self.source = source
        # Author title
        self.title = title

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types

        if self.cover is not None:
            result['Cover'] = self.cover.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.id is not None:
            result['Id'] = self.id

        if self.online is not None:
            result['Online'] = self.online

        if self.raw_id is not None:
            result['RawId'] = self.raw_id

        if self.source is not None:
            result['Source'] = self.source

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')

        if m.get('Cover') is not None:
            temp_model = main_models.ListCateContentResponseBodyResultOpenDataItemListAuthorsCover()
            self.cover = temp_model.from_map(m.get('Cover'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class ListCateContentResponseBodyResultOpenDataItemListAuthorsCover(DaraModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        # Indicates whether the image can be cropped using OSS rules.
        self.can_resize = can_resize
        # default image
        self.img = img
        # Large image
        self.large = large
        # Medium image (Deprecated)
        self.mediam = mediam
        # medium image
        self.medium = medium
        # small image
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize

        if self.img is not None:
            result['Img'] = self.img

        if self.large is not None:
            result['Large'] = self.large

        if self.mediam is not None:
            result['Mediam'] = self.mediam

        if self.medium is not None:
            result['Medium'] = self.medium

        if self.small is not None:
            result['Small'] = self.small

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')

        if m.get('Img') is not None:
            self.img = m.get('Img')

        if m.get('Large') is not None:
            self.large = m.get('Large')

        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')

        if m.get('Medium') is not None:
            self.medium = m.get('Medium')

        if m.get('Small') is not None:
            self.small = m.get('Small')

        return self

