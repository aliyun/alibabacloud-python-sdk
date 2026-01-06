# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTodoTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        description: str = None,
        done: bool = None,
        due_time: int = None,
        executor_ids_shrink: str = None,
        participant_ids_shrink: str = None,
        subject: str = None,
        task_id: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        self.description = description
        self.done = done
        self.due_time = due_time
        self.executor_ids_shrink = executor_ids_shrink
        self.participant_ids_shrink = participant_ids_shrink
        self.subject = subject
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.description is not None:
            result['description'] = self.description

        if self.done is not None:
            result['done'] = self.done

        if self.due_time is not None:
            result['dueTime'] = self.due_time

        if self.executor_ids_shrink is not None:
            result['executorIds'] = self.executor_ids_shrink

        if self.participant_ids_shrink is not None:
            result['participantIds'] = self.participant_ids_shrink

        if self.subject is not None:
            result['subject'] = self.subject

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('done') is not None:
            self.done = m.get('done')

        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')

        if m.get('executorIds') is not None:
            self.executor_ids_shrink = m.get('executorIds')

        if m.get('participantIds') is not None:
            self.participant_ids_shrink = m.get('participantIds')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

