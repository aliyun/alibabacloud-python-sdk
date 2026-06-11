# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSubTasksRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        root_task_id: str = None,
        task_type: str = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.root_task_id = root_task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.root_task_id is not None:
            result['RootTaskId'] = self.root_task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RootTaskId') is not None:
            self.root_task_id = m.get('RootTaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

