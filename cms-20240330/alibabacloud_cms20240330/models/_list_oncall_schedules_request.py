# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListOncallSchedulesRequest(DaraModel):
    def __init__(
        self,
        oncall_schedule_ids: List[str] = None,
        oncall_schedule_name: str = None,
        page_number: int = None,
        page_size: int = None,
        workspace: str = None,
    ):
        self.oncall_schedule_ids = oncall_schedule_ids
        self.oncall_schedule_name = oncall_schedule_name
        self.page_number = page_number
        self.page_size = page_size
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oncall_schedule_ids is not None:
            result['oncallScheduleIds'] = self.oncall_schedule_ids

        if self.oncall_schedule_name is not None:
            result['oncallScheduleName'] = self.oncall_schedule_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oncallScheduleIds') is not None:
            self.oncall_schedule_ids = m.get('oncallScheduleIds')

        if m.get('oncallScheduleName') is not None:
            self.oncall_schedule_name = m.get('oncallScheduleName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

