# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSqlConversionResultRequest(DaraModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        task_id: int = None,
    ):
        # The page number.
        self.page = page
        # The number of entries per page.
        self.size = size
        # The task ID that uniquely identifies a task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

