# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListAlbumIsAddedResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.ListAlbumIsAddedResponseBodyResult] = None,
    ):
        # Status code
        self.code = code
        # Additional information
        self.message = message
        # Request ID
        self.request_id = request_id
        # Result
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
                temp_model = main_models.ListAlbumIsAddedResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListAlbumIsAddedResponseBodyResult(DaraModel):
    def __init__(
        self,
        album_id: str = None,
        is_added: str = None,
    ):
        # Album ID
        self.album_id = album_id
        # Whether it is subscribed
        self.is_added = is_added

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.album_id is not None:
            result['AlbumId'] = self.album_id

        if self.is_added is not None:
            result['IsAdded'] = self.is_added

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')

        if m.get('IsAdded') is not None:
            self.is_added = m.get('IsAdded')

        return self

