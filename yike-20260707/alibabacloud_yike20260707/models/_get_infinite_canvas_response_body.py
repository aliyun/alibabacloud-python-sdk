# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetInfiniteCanvasResponseBody(DaraModel):
    def __init__(
        self,
        infinite_canvas: main_models.GetInfiniteCanvasResponseBodyInfiniteCanvas = None,
        request_id: str = None,
    ):
        # The infinite canvas details.
        self.infinite_canvas = infinite_canvas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.infinite_canvas:
            self.infinite_canvas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.infinite_canvas is not None:
            result['InfiniteCanvas'] = self.infinite_canvas.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfiniteCanvas') is not None:
            temp_model = main_models.GetInfiniteCanvasResponseBodyInfiniteCanvas()
            self.infinite_canvas = temp_model.from_map(m.get('InfiniteCanvas'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInfiniteCanvasResponseBodyInfiniteCanvas(DaraModel):
    def __init__(
        self,
        canvas_id: str = None,
        cover_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        thumbnail: str = None,
        title: str = None,
    ):
        # The ID of the infinite canvas.
        self.canvas_id = canvas_id
        # The cover URL.
        self.cover_url = cover_url
        # The creation time in UTC.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The thumbnail URL.
        self.thumbnail = thumbnail
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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanvasId') is not None:
            self.canvas_id = m.get('CanvasId')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

