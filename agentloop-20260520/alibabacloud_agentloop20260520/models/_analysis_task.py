# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class AnalysisTask(DaraModel):
    def __init__(
        self,
        completed_at: int = None,
        created_at: int = None,
        error_code: str = None,
        error_message: str = None,
        report: Dict[str, Any] = None,
        selected_count: int = None,
        status: str = None,
        task_id: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The task completion time as a UNIX timestamp in milliseconds.
        self.completed_at = completed_at
        # The task creation time as a UNIX timestamp in milliseconds.
        self.created_at = created_at
        # The error code for the task failure.
        self.error_code = error_code
        # The error message for the task failure.
        self.error_message = error_message
        # The generated analysis report. This field is typically not returned by list operations.
        self.report = report
        # The number of evaluation details selected by the user.
        self.selected_count = selected_count
        # The task status. Valid values: PENDING, RUNNING, SUCCEEDED, PARTIAL_SUCCEEDED, and FAILED.
        self.status = status
        # The analysis task ID.
        self.task_id = task_id
        # The analysis task name.
        self.task_name = task_name
        # The analysis task type.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.report is not None:
            result['report'] = self.report

        if self.selected_count is not None:
            result['selectedCount'] = self.selected_count

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('report') is not None:
            self.report = m.get('report')

        if m.get('selectedCount') is not None:
            self.selected_count = m.get('selectedCount')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

