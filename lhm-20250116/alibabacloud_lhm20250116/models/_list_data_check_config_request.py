# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataCheckConfigRequest(DaraModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        src_table: str = None,
        task_id: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.src_table = src_table
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.src_table is not None:
            result['srcTable'] = self.src_table

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('srcTable') is not None:
            self.src_table = m.get('srcTable')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

