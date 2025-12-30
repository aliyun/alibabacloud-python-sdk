# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLiveTranscodeTemplatesRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        key_word: str = None,
        page_no: int = None,
        page_size: int = None,
        sort_by: str = None,
        type: str = None,
        video_codec: str = None,
    ):
        # The category of the template. Valid values:
        # 
        # *   system
        # *   customized
        self.category = category
        # The search keyword. You can use the template ID or name as the keyword to search for templates. If you search for templates by name, fuzzy match is supported.
        self.key_word = key_word
        # The page number of the page to return. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The sorting order. By default, the query results are sorted by creation time in descending order. Valid values:
        # 
        # *   asc
        # *   desc
        self.sort_by = sort_by
        # The type of the template. Valid values:
        # 
        # *   normal
        # *   narrow-band
        # *   audio-only
        # *   origin
        self.type = type
        # The video codec. Valid values:
        # 
        # *   H.264
        # *   H.265
        self.video_codec = video_codec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.type is not None:
            result['Type'] = self.type

        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')

        return self

