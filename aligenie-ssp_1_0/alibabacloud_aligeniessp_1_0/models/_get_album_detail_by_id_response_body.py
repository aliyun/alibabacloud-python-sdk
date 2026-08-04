# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetAlbumDetailByIdResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetAlbumDetailByIdResponseBodyResult = None,
    ):
        # Status code
        self.code = code
        # Additional information
        self.message = message
        # Request ID
        self.request_id = request_id
        # Album content
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
            temp_model = main_models.GetAlbumDetailByIdResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetAlbumDetailByIdResponseBodyResult(DaraModel):
    def __init__(
        self,
        album_content_list: List[main_models.GetAlbumDetailByIdResponseBodyResultAlbumContentList] = None,
        album_cover_url: str = None,
        album_description: str = None,
        album_id: str = None,
        album_title: str = None,
    ):
        # Album content list
        self.album_content_list = album_content_list
        # Album thumbnail
        self.album_cover_url = album_cover_url
        # Album Description
        self.album_description = album_description
        # Album ID
        self.album_id = album_id
        # Album Title
        self.album_title = album_title

    def validate(self):
        if self.album_content_list:
            for v1 in self.album_content_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlbumContentList'] = []
        if self.album_content_list is not None:
            for k1 in self.album_content_list:
                result['AlbumContentList'].append(k1.to_map() if k1 else None)

        if self.album_cover_url is not None:
            result['AlbumCoverUrl'] = self.album_cover_url

        if self.album_description is not None:
            result['AlbumDescription'] = self.album_description

        if self.album_id is not None:
            result['AlbumId'] = self.album_id

        if self.album_title is not None:
            result['AlbumTitle'] = self.album_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.album_content_list = []
        if m.get('AlbumContentList') is not None:
            for k1 in m.get('AlbumContentList'):
                temp_model = main_models.GetAlbumDetailByIdResponseBodyResultAlbumContentList()
                self.album_content_list.append(temp_model.from_map(k1))

        if m.get('AlbumCoverUrl') is not None:
            self.album_cover_url = m.get('AlbumCoverUrl')

        if m.get('AlbumDescription') is not None:
            self.album_description = m.get('AlbumDescription')

        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')

        if m.get('AlbumTitle') is not None:
            self.album_title = m.get('AlbumTitle')

        return self

class GetAlbumDetailByIdResponseBodyResultAlbumContentList(DaraModel):
    def __init__(
        self,
        duration: str = None,
        id: str = None,
        order_index: str = None,
        title: str = None,
    ):
        # Album content duration
        self.duration = duration
        # Album content ID
        self.id = id
        # Album content sorting
        self.order_index = order_index
        # Album content title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.id is not None:
            result['Id'] = self.id

        if self.order_index is not None:
            result['OrderIndex'] = self.order_index

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

