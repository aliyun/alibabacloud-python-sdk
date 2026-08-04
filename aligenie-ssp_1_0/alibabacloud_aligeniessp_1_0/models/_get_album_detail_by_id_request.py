# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAlbumDetailByIdRequest(DaraModel):
    def __init__(
        self,
        album_id: str = None,
    ):
        # Album ID
        self.album_id = album_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.album_id is not None:
            result['AlbumId'] = self.album_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')

        return self

