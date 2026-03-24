# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushObjectCacheResponseBody(DaraModel):
    def __init__(
        self,
        push_task_id: str = None,
        request_id: str = None,
    ):
        # The ID of the prefetch task. If multiple tasks are returned, the IDs are separated by commas (,). The task IDs are merged based on the following rules:
        # 
        # *   If the tasks are set for the same accelerated domain name, submitted within the same second, and prefetch content from URLs instead of directories, the tasks IDs are merged into the same task ID (RushTaskId).
        # *   If the number of tasks that are set for the same accelerated domain name, submitted within the same second, and prefetch content from URLs instead of directories exceeds 500, every 500 task IDs are merged into the same task ID (RushTaskId).
        self.push_task_id = push_task_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.push_task_id is not None:
            result['PushTaskId'] = self.push_task_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushTaskId') is not None:
            self.push_task_id = m.get('PushTaskId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

