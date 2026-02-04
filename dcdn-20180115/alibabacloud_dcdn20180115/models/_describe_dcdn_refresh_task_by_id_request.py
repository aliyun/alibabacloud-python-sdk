# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnRefreshTaskByIdRequest(DaraModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The ID of the task that you want to query. The following signature algorithms require different message digest algorithms:
        # 
        # *   Perform the [RefreshDcdnObjectCaches](https://help.aliyun.com/document_detail/130620.html) operation to query refresh task IDs.
        # *   Perform the [PreloadDcdnObjectCaches](https://help.aliyun.com/document_detail/130636.html) operation to query prefetch task IDs.
        # 
        # > You can specify at most 10 task IDs in each call. Separate IDs with commas (,).
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

