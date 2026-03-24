# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshObjectCachesResponseBody(DaraModel):
    def __init__(
        self,
        refresh_task_id: str = None,
        request_id: str = None,
    ):
        # The ID of the refresh task. If multiple tasks are returned, the task IDs are separated by commas (,). The task IDs are merged based on the following rules:
        # 
        # *   If the tasks are specified for the same accelerated domain name, submitted within the same second, and run to refresh content based on URLs instead of directories, the task IDs are merged into one task ID (RefreshTaskId).
        # *   If the number of tasks that are specified for the same accelerated domain name, submitted within the same second, and run to refresh content based on URLs instead of directories exceeds 2,000, every 2,000 task IDs are merged into one task ID (RefreshTaskId).
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

