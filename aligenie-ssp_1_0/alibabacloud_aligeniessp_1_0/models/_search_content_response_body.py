# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class SearchContentResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.SearchContentResponseBodyResult] = None,
    ):
        # code encoding
        self.code = code
        # message information
        self.message = message
        # Id of the request
        self.request_id = request_id
        # return information
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

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

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.SearchContentResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class SearchContentResponseBodyResult(DaraModel):
    def __init__(
        self,
        album_id: str = None,
        alias: List[str] = None,
        audition: bool = None,
        authors: List[main_models.SearchContentResponseBodyResultAuthors] = None,
        category: str = None,
        charge: bool = None,
        comm_cate_id: int = None,
        cover: main_models.SearchContentResponseBodyResultCover = None,
        description: str = None,
        duration: int = None,
        hot_score: float = None,
        id: int = None,
        item_type: str = None,
        lyric: str = None,
        order_index: str = None,
        source: str = None,
        styles: List[str] = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        # The corresponding album ID
        self.album_id = album_id
        # Alias
        self.alias = alias
        # Is audition available
        self.audition = audition
        # Authors of the content
        self.authors = authors
        # Transform controlType based on the associated public category
        self.category = category
        # Is charged
        self.charge = charge
        # The corresponding category ID
        self.comm_cate_id = comm_cate_id
        # Album thumbnail image
        self.cover = cover
        # Content description
        self.description = description
        # Duration information
        self.duration = duration
        # Popularity score
        self.hot_score = hot_score
        # Content ID
        self.id = id
        # Type of content, such as music, audio, radio, jokes, etc.
        self.item_type = item_type
        # Lyric information
        self.lyric = lyric
        # Content sorting value
        self.order_index = order_index
        # Source
        self.source = source
        # Music styles
        self.styles = styles
        # Title
        self.title = title
        # Transform favoriteType based on the associated public category
        self.type = type
        # Indicates whether the item is playable
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
        if self.album_id is not None:
            result['AlbumId'] = self.album_id

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

        if self.lyric is not None:
            result['Lyric'] = self.lyric

        if self.order_index is not None:
            result['OrderIndex'] = self.order_index

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
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')

        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Audition') is not None:
            self.audition = m.get('Audition')

        self.authors = []
        if m.get('Authors') is not None:
            for k1 in m.get('Authors'):
                temp_model = main_models.SearchContentResponseBodyResultAuthors()
                self.authors.append(temp_model.from_map(k1))

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Charge') is not None:
            self.charge = m.get('Charge')

        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')

        if m.get('Cover') is not None:
            temp_model = main_models.SearchContentResponseBodyResultCover()
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

        if m.get('Lyric') is not None:
            self.lyric = m.get('Lyric')

        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')

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

class SearchContentResponseBodyResultCover(DaraModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        # Indicates whether OSS rules can be used to crop the image
        self.can_resize = can_resize
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

class SearchContentResponseBodyResultAuthors(DaraModel):
    def __init__(
        self,
        author_types: List[str] = None,
        cover: main_models.SearchContentResponseBodyResultAuthorsCover = None,
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
        # Profile picture
        self.cover = cover
        # Author description
        self.description = description
        # Gender
        self.gender = gender
        # Author primary key ID
        self.id = id
        # Is online
        self.online = online
        # Third-party author ID
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
            temp_model = main_models.SearchContentResponseBodyResultAuthorsCover()
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

class SearchContentResponseBodyResultAuthorsCover(DaraModel):
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

