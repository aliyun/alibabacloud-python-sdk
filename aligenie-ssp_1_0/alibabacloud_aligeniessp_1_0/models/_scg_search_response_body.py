# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ScgSearchResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        result: List[main_models.ScgSearchResponseBodyResult] = None,
    ):
        # Status code
        self.code = code
        # Response message
        self.message = message
        # Page number
        self.page_num = page_num
        # Number of records per page
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Detailed returned information.
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

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ScgSearchResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ScgSearchResponseBodyResult(DaraModel):
    def __init__(
        self,
        album: bool = None,
        album_raw_id: str = None,
        album_type: int = None,
        alias: List[str] = None,
        author_ids: List[int] = None,
        author_names: List[str] = None,
        category: str = None,
        content_type: str = None,
        cover: main_models.ScgSearchResponseBodyResultCover = None,
        is_audition: bool = None,
        is_charge: str = None,
        need_charge: bool = None,
        raw_id: str = None,
        singers: str = None,
        source: str = None,
        support_audition: bool = None,
        title: str = None,
        type: str = None,
    ):
        # Whether it is an album
        self.album = album
        # Album ID
        self.album_raw_id = album_raw_id
        # Album type
        self.album_type = album_type
        # Alias
        self.alias = alias
        # Author ID
        self.author_ids = author_ids
        # Author names
        self.author_names = author_names
        # Category
        self.category = category
        # Content type
        self.content_type = content_type
        # Thumbnail
        self.cover = cover
        # Whether audition is available
        self.is_audition = is_audition
        # Is charged
        self.is_charge = is_charge
        # Whether charging is required
        self.need_charge = need_charge
        # Third-party content ID
        self.raw_id = raw_id
        # Singer name
        self.singers = singers
        # Content source
        self.source = source
        # Whether audition is supported
        self.support_audition = support_audition
        # Content title
        self.title = title
        # Content type
        self.type = type

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.album is not None:
            result['Album'] = self.album

        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id

        if self.album_type is not None:
            result['AlbumType'] = self.album_type

        if self.alias is not None:
            result['Alias'] = self.alias

        if self.author_ids is not None:
            result['AuthorIds'] = self.author_ids

        if self.author_names is not None:
            result['AuthorNames'] = self.author_names

        if self.category is not None:
            result['Category'] = self.category

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.cover is not None:
            result['Cover'] = self.cover.to_map()

        if self.is_audition is not None:
            result['IsAudition'] = self.is_audition

        if self.is_charge is not None:
            result['IsCharge'] = self.is_charge

        if self.need_charge is not None:
            result['NeedCharge'] = self.need_charge

        if self.raw_id is not None:
            result['RawId'] = self.raw_id

        if self.singers is not None:
            result['Singers'] = self.singers

        if self.source is not None:
            result['Source'] = self.source

        if self.support_audition is not None:
            result['SupportAudition'] = self.support_audition

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Album') is not None:
            self.album = m.get('Album')

        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')

        if m.get('AlbumType') is not None:
            self.album_type = m.get('AlbumType')

        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('AuthorIds') is not None:
            self.author_ids = m.get('AuthorIds')

        if m.get('AuthorNames') is not None:
            self.author_names = m.get('AuthorNames')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Cover') is not None:
            temp_model = main_models.ScgSearchResponseBodyResultCover()
            self.cover = temp_model.from_map(m.get('Cover'))

        if m.get('IsAudition') is not None:
            self.is_audition = m.get('IsAudition')

        if m.get('IsCharge') is not None:
            self.is_charge = m.get('IsCharge')

        if m.get('NeedCharge') is not None:
            self.need_charge = m.get('NeedCharge')

        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')

        if m.get('Singers') is not None:
            self.singers = m.get('Singers')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SupportAudition') is not None:
            self.support_audition = m.get('SupportAudition')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ScgSearchResponseBodyResultCover(DaraModel):
    def __init__(
        self,
        img: str = None,
        large: str = None,
        medium: str = None,
        small: str = None,
        can_resize: bool = None,
    ):
        # Thumbnail image (Img, Large, Medium, and Small may not appear simultaneously; only one of them may be present)
        self.img = img
        # Large graph
        self.large = large
        # Medium image
        self.medium = medium
        # Small image
        self.small = small
        # Whether scaling is supported
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

        if m.get('Medium') is not None:
            self.medium = m.get('Medium')

        if m.get('Small') is not None:
            self.small = m.get('Small')

        if m.get('canResize') is not None:
            self.can_resize = m.get('canResize')

        return self

