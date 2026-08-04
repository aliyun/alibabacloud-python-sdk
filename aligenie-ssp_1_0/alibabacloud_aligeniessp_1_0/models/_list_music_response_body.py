# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListMusicResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.ListMusicResponseBodyResult = None,
    ):
        # Status code returned by the alarm service
        self.code = code
        # error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # collection of ringtone query results
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
            temp_model = main_models.ListMusicResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListMusicResponseBodyResult(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        model: List[main_models.ListMusicResponseBodyResultModel] = None,
        page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Current page
        self.current_page = current_page
        # List of ringtones
        self.model = model
        # Total number of pages
        self.page_count = page_count
        # Number of entries per page: maximum value is 100; values exceeding 100 are treated as 100
        self.page_size = page_size
        # Total number of entries
        self.total_count = total_count

    def validate(self):
        if self.model:
            for v1 in self.model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Model'] = []
        if self.model is not None:
            for k1 in self.model:
                result['Model'].append(k1.to_map() if k1 else None)

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.model = []
        if m.get('Model') is not None:
            for k1 in m.get('Model'):
                temp_model = main_models.ListMusicResponseBodyResultModel()
                self.model.append(temp_model.from_map(k1))

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMusicResponseBodyResultModel(DaraModel):
    def __init__(
        self,
        music_id: int = None,
        music_name: str = None,
        music_type: int = None,
        music_type_name: str = None,
        music_url: str = None,
    ):
        # Ringtone ID
        self.music_id = music_id
        # Ringtone name
        self.music_name = music_name
        # Ringtone category ID
        self.music_type = music_type
        # Ringtone category name
        self.music_type_name = music_type_name
        # Ringtone URL
        self.music_url = music_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.music_id is not None:
            result['MusicId'] = self.music_id

        if self.music_name is not None:
            result['MusicName'] = self.music_name

        if self.music_type is not None:
            result['MusicType'] = self.music_type

        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name

        if self.music_url is not None:
            result['MusicUrl'] = self.music_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')

        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')

        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')

        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')

        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')

        return self

