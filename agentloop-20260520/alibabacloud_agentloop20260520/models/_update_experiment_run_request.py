# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateExperimentRunRequest(DaraModel):
    def __init__(
        self,
        completed_at: int = None,
        completed_tasks: int = None,
        executed_at: int = None,
        failed_tasks: int = None,
        record_name: str = None,
        status: str = None,
        total_tasks: int = None,
        client_token: str = None,
    ):
        # The experiment completion time. A millisecond-level UNIX timestamp.
        self.completed_at = completed_at
        # The number of completed tasks.
        self.completed_tasks = completed_tasks
        # The experiment execution time. A millisecond-level UNIX timestamp.
        self.executed_at = executed_at
        # The number of failed tasks.
        self.failed_tasks = failed_tasks
        # The experiment record name.
        self.record_name = record_name
        # The experiment record status. Set to cancelled to cancel execution.
        self.status = status
        # The total number of tasks.
        self.total_tasks = total_tasks
        # Optional.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.completed_tasks is not None:
            result['completedTasks'] = self.completed_tasks

        if self.executed_at is not None:
            result['executedAt'] = self.executed_at

        if self.failed_tasks is not None:
            result['failedTasks'] = self.failed_tasks

        if self.record_name is not None:
            result['recordName'] = self.record_name

        if self.status is not None:
            result['status'] = self.status

        if self.total_tasks is not None:
            result['totalTasks'] = self.total_tasks

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('completedTasks') is not None:
            self.completed_tasks = m.get('completedTasks')

        if m.get('executedAt') is not None:
            self.executed_at = m.get('executedAt')

        if m.get('failedTasks') is not None:
            self.failed_tasks = m.get('failedTasks')

        if m.get('recordName') is not None:
            self.record_name = m.get('recordName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalTasks') is not None:
            self.total_tasks = m.get('totalTasks')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

