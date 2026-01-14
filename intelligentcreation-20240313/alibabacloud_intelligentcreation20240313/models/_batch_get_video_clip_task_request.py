# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchGetVideoClipTaskRequest(DaraModel):
    def __init__(
        self,
        task_id_list: List[str] = None,
    ):
        self.task_id_list = task_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id_list is not None:
            result['taskIdList'] = self.task_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskIdList') is not None:
            self.task_id_list = m.get('taskIdList')

        return self

