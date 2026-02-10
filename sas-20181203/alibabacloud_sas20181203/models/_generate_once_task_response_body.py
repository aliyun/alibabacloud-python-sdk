# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateOnceTaskResponseBody(DaraModel):
    def __init__(
        self,
        can_create: bool = None,
        collect_time: int = None,
        finish_count: int = None,
        last_task: str = None,
        request_id: str = None,
        task_id: str = None,
        total_count: int = None,
    ):
        # Indicates whether you can create more scan tasks. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # > By default, a maximum of 10 scan tasks can be running at the same time. If 10 image scan tasks are running, you cannot create a scan task by calling this operation. You must wait for at least one of the 10 existing scan tasks to complete before you can create a scan task.
        self.can_create = can_create
        # The collection time.
        self.collect_time = collect_time
        # The number of scan tasks that are complete.
        self.finish_count = finish_count
        # The ID of the last scan task.
        self.last_task = last_task
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The ID of the scan task.
        self.task_id = task_id
        # The total number of scan tasks.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_create is not None:
            result['CanCreate'] = self.can_create

        if self.collect_time is not None:
            result['CollectTime'] = self.collect_time

        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count

        if self.last_task is not None:
            result['LastTask'] = self.last_task

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanCreate') is not None:
            self.can_create = m.get('CanCreate')

        if m.get('CollectTime') is not None:
            self.collect_time = m.get('CollectTime')

        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')

        if m.get('LastTask') is not None:
            self.last_task = m.get('LastTask')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

