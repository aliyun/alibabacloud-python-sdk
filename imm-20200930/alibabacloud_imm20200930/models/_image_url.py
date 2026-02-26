# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageURL(DaraModel):
    def __init__(
        self,
        thumbnail: str = None,
        url: str = None,
    ):
        self.thumbnail = thumbnail
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

