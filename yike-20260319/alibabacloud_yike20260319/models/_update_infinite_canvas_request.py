# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInfiniteCanvasRequest(DaraModel):
    def __init__(
        self,
        canvas_id: str = None,
        cover_url: str = None,
        title: str = None,
    ):
        # The ID of the infinite canvas.
        # 
        # This parameter is required.
        self.canvas_id = canvas_id
        # The cover URL.
        self.cover_url = cover_url
        # The title of the infinite canvas.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.canvas_id is not None:
            result['CanvasId'] = self.canvas_id

        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanvasId') is not None:
            self.canvas_id = m.get('CanvasId')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

