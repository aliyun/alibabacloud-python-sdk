# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCloudNotesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        end_ts: int = None,
        page_no: int = None,
        page_size: int = None,
        start_ts: int = None,
        task_ids: List[str] = None,
    ):
        # APP ID。
        # 
        # This parameter is required.
        self.app_id = app_id
        self.channel_id = channel_id
        self.end_ts = end_ts
        self.page_no = page_no
        self.page_size = page_size
        self.start_ts = start_ts
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        return self

