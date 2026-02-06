# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAuditHistoryRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        sort_by: str = None,
        video_id: str = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.page_no = page_no
        # The number of entries to return on each page. Default value: **10**. Maximum value: **100**.
        self.page_size = page_size
        # The sorting rule of the results. Valid values:
        # *   **CreationTime:Desc**: sorts the results based on the creation time in descending order. This is the default value.
        # *   **CreationTime:Asc**: sorts the results based on the creation time in ascending order.
        self.sort_by = sort_by
        # The ID of the video.
        # 
        # This parameter is required.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

