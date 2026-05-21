# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteTempFileTasksRequest(DaraModel):
    def __init__(
        self,
        temp_file_task_ids: List[str] = None,
    ):
        self.temp_file_task_ids = temp_file_task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.temp_file_task_ids is not None:
            result['TempFileTaskIds'] = self.temp_file_task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TempFileTaskIds') is not None:
            self.temp_file_task_ids = m.get('TempFileTaskIds')

        return self

