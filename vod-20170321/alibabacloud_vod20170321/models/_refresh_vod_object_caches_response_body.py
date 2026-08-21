# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshVodObjectCachesResponseBody(DaraModel):
    def __init__(
        self,
        refresh_task_id: str = None,
        request_id: str = None,
    ):
        # The ID of the purge task. Multiple task IDs are separated by commas (,).
        # The returned purge task IDs are merged based on the following rules:
        # 
        # Purge tasks (at URL granularity) submitted for the same domain name within the same second are merged into a single RefreshTaskId.
        # If purge tasks (at URL granularity) submitted for the same domain name within the same second exceed 2,000, they are merged into one RefreshTaskId per 2,000 tasks.
        self.refresh_task_id = refresh_task_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.refresh_task_id is not None:
            result['RefreshTaskId'] = self.refresh_task_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshTaskId') is not None:
            self.refresh_task_id = m.get('RefreshTaskId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

