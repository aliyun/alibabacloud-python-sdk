# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class UpdateTodoTaskRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.UpdateTodoTaskRequestTenantContext = None,
        description: str = None,
        done: bool = None,
        due_time: int = None,
        executor_ids: List[str] = None,
        participant_ids: List[str] = None,
        subject: str = None,
        task_id: str = None,
    ):
        self.tenant_context = tenant_context
        self.description = description
        self.done = done
        self.due_time = due_time
        self.executor_ids = executor_ids
        self.participant_ids = participant_ids
        self.subject = subject
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.done is not None:
            result['done'] = self.done

        if self.due_time is not None:
            result['dueTime'] = self.due_time

        if self.executor_ids is not None:
            result['executorIds'] = self.executor_ids

        if self.participant_ids is not None:
            result['participantIds'] = self.participant_ids

        if self.subject is not None:
            result['subject'] = self.subject

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.UpdateTodoTaskRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('done') is not None:
            self.done = m.get('done')

        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')

        if m.get('executorIds') is not None:
            self.executor_ids = m.get('executorIds')

        if m.get('participantIds') is not None:
            self.participant_ids = m.get('participantIds')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class UpdateTodoTaskRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

