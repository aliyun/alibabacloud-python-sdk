# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBatchResultCountResponseBody(DaraModel):
    def __init__(
        self,
        batch_type: str = None,
        failed_count: int = None,
        reason: str = None,
        request_id: str = None,
        status: int = None,
        success_count: int = None,
        task_id: int = None,
        total_count: int = None,
    ):
        # The type of the batch operation.
        self.batch_type = batch_type
        # The total number of domain names or DNS records that failed to be processed.
        self.failed_count = failed_count
        # The cause of the execution failure.
        self.reason = reason
        # The request ID.
        self.request_id = request_id
        # The state of the task. Valid values:
        # 
        # *   **-1**: No task for importing domain names or DNS records is submitted.
        # *   **0**: The task is being processed.
        # *   **1**: The task is complete.
        # *   **2**: The task failed.
        self.status = status
        # The total number of domain names or DNS records that were processed.
        self.success_count = success_count
        # The ID of the last task.
        self.task_id = task_id
        # The total number of DNS records that were processed in batches.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

