# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260319 import models as main_models
from darabonba.model import DaraModel

class ListInfiniteCanvasesResponseBody(DaraModel):
    def __init__(
        self,
        canvas_list: List[main_models.ListInfiniteCanvasesResponseBodyCanvasList] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of infinite canvases.
        self.canvas_list = canvas_list
        # The current page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of infinite canvases.
        self.total_count = total_count

    def validate(self):
        if self.canvas_list:
            for v1 in self.canvas_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CanvasList'] = []
        if self.canvas_list is not None:
            for k1 in self.canvas_list:
                result['CanvasList'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.canvas_list = []
        if m.get('CanvasList') is not None:
            for k1 in m.get('CanvasList'):
                temp_model = main_models.ListInfiniteCanvasesResponseBodyCanvasList()
                self.canvas_list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInfiniteCanvasesResponseBodyCanvasList(DaraModel):
    def __init__(
        self,
        canvas_id: str = None,
        cover_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        thumbnail: str = None,
        title: str = None,
    ):
        # The infinite canvas ID.
        self.canvas_id = canvas_id
        # The cover URL.
        self.cover_url = cover_url
        # The creation time, in milliseconds.
        self.gmt_create = gmt_create
        # The last modification time.
        self.gmt_modified = gmt_modified
        # The thumbnail height, in px.
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

