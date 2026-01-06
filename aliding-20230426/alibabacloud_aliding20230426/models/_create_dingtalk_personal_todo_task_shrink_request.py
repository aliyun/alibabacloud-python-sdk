# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDingtalkPersonalTodoTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        due_time: int = None,
        executor_ids_shrink: str = None,
        notify_configs_shrink: str = None,
        participant_ids_shrink: str = None,
        subject: str = None,
        tenant_context_shrink: str = None,
        user_token: str = None,
    ):
        self.description = description
        self.due_time = due_time
        # This parameter is required.
        self.executor_ids_shrink = executor_ids_shrink
        self.notify_configs_shrink = notify_configs_shrink
        self.participant_ids_shrink = participant_ids_shrink
        # This parameter is required.
        self.subject = subject
        self.tenant_context_shrink = tenant_context_shrink
        self.user_token = user_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.due_time is not None:
            result['DueTime'] = self.due_time

        if self.executor_ids_shrink is not None:
            result['ExecutorIds'] = self.executor_ids_shrink

        if self.notify_configs_shrink is not None:
            result['NotifyConfigs'] = self.notify_configs_shrink

        if self.participant_ids_shrink is not None:
            result['ParticipantIds'] = self.participant_ids_shrink

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.user_token is not None:
            result['UserToken'] = self.user_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')

        if m.get('ExecutorIds') is not None:
            self.executor_ids_shrink = m.get('ExecutorIds')

        if m.get('NotifyConfigs') is not None:
            self.notify_configs_shrink = m.get('NotifyConfigs')

        if m.get('ParticipantIds') is not None:
            self.participant_ids_shrink = m.get('ParticipantIds')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('UserToken') is not None:
            self.user_token = m.get('UserToken')

        return self

