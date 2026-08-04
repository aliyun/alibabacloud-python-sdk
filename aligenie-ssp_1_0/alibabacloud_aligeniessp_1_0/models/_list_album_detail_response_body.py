# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListAlbumDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.ListAlbumDetailResponseBodyResult = None,
    ):
        # Code encoding
        self.code = code
        # Message information
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
            temp_model = main_models.ListAlbumDetailResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListAlbumDetailResponseBodyResult(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        open_data_item_list: List[main_models.ListAlbumDetailResponseBodyResultOpenDataItemList] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # Current page number
        self.current_page_num = current_page_num
        # Data information
        self.open_data_item_list = open_data_item_list
        # Number of records per page
        self.page_size = page_size
        # total number of records
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
                temp_model = main_models.ListAlbumDetailResponseBodyResultOpenDataItemList()
                self.open_data_item_list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListAlbumDetailResponseBodyResultOpenDataItemList(DaraModel):
    def __init__(
        self,
        alias: List[str] = None,
        audition: bool = None,
        authors: List[main_models.ListAlbumDetailResponseBodyResultOpenDataItemListAuthors] = None,
        category: str = None,
        charge: bool = None,
        comm_cate_id: int = None,
        cover: main_models.ListAlbumDetailResponseBodyResultOpenDataItemListCover = None,
        description: str = None,
        duration: int = None,
        hot_score: float = None,
        id: int = None,
        item_type: str = None,
        order_index: int = None,
        raw_id: str = None,
        source: str = None,
        styles: List[str] = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        # Alias
        self.alias = alias
        # Indicates whether the content is available for audition
        self.audition = audition
        # Author of the content
        self.authors = authors
        # Transform controlType based on the associated public category
        self.category = category
        # Is charged
        self.charge = charge
        # category ID
        self.comm_cate_id = comm_cate_id
        # Content thumbnail
        self.cover = cover
        # Content description
        self.description = description
        # Duration
        self.duration = duration
        # popularity score
        self.hot_score = hot_score
        # content ID
        self.id = id
        # Type of content, such as music, audio, radio, jokes, etc.
        self.item_type = item_type
        # OrderIndex sequence
        self.order_index = order_index
        # Third-party ID
        self.raw_id = raw_id
        # Source
        self.source = source
        # style
        self.styles = styles
        # Title
        self.title = title
        # Transform favoriteType based on the associated public category
        self.type = type
        # Indicates whether the content is playable
        self.valid = valid

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

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.hot_score is not None:
            result['HotScore'] = self.hot_score

        if self.id is not None:
            result['Id'] = self.id

        if self.item_type is not None:
            result['ItemType'] = self.item_type

        if self.order_index is not None:
            result['OrderIndex'] = self.order_index

        if self.raw_id is not None:
            result['RawId'] = self.raw_id

        if self.source is not None:
            result['Source'] = self.source

        if self.styles is not None:
            result['Styles'] = self.styles

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        if self.valid is not None:
            result['Valid'] = self.valid

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
                temp_model = main_models.ListAlbumDetailResponseBodyResultOpenDataItemListAuthors()
                self.authors.append(temp_model.from_map(k1))

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Charge') is not None:
            self.charge = m.get('Charge')

        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')

        if m.get('Cover') is not None:
            temp_model = main_models.ListAlbumDetailResponseBodyResultOpenDataItemListCover()
            self.cover = temp_model.from_map(m.get('Cover'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')

        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')

        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Styles') is not None:
            self.styles = m.get('Styles')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        return self

class ListAlbumDetailResponseBodyResultOpenDataItemListCover(DaraModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        medium: str = None,
        small: str = None,
    ):
        # Indicates whether OSS rules can be used for cropping
        self.can_resize = can_resize
        # Default image
        self.img = img
        # Large image
        self.large = large
        # Medium image
        self.medium = medium
        # Small image
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

        if m.get('Medium') is not None:
            self.medium = m.get('Medium')

        if m.get('Small') is not None:
            self.small = m.get('Small')

        return self

class ListAlbumDetailResponseBodyResultOpenDataItemListAuthors(DaraModel):
    def __init__(
        self,
        author_types: List[str] = None,
        gender: str = None,
        id: int = None,
        online: bool = None,
        source: str = None,
        title: str = None,
    ):
        # Author type
        self.author_types = author_types
        # Gender
        self.gender = gender
        # Primary key ID of the author
        self.id = id
        # Whether the author is online
        self.online = online
        # Source
        self.source = source
        # Author title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.id is not None:
            result['Id'] = self.id

        if self.online is not None:
            result['Online'] = self.online

        if self.source is not None:
            result['Source'] = self.source

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

