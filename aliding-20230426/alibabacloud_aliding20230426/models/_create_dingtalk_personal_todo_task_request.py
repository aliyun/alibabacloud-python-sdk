# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateDingtalkPersonalTodoTaskRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        due_time: int = None,
        executor_ids: List[str] = None,
        notify_configs: main_models.CreateDingtalkPersonalTodoTaskRequestNotifyConfigs = None,
        participant_ids: List[str] = None,
        subject: str = None,
        tenant_context: main_models.CreateDingtalkPersonalTodoTaskRequestTenantContext = None,
        user_token: str = None,
    ):
        self.description = description
        self.due_time = due_time
        # This parameter is required.
        self.executor_ids = executor_ids
        self.notify_configs = notify_configs
        self.participant_ids = participant_ids
        # This parameter is required.
        self.subject = subject
        self.tenant_context = tenant_context
        self.user_token = user_token

    def validate(self):
        if self.notify_configs:
            self.notify_configs.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.due_time is not None:
            result['DueTime'] = self.due_time

        if self.executor_ids is not None:
            result['ExecutorIds'] = self.executor_ids

        if self.notify_configs is not None:
            result['NotifyConfigs'] = self.notify_configs.to_map()

        if self.participant_ids is not None:
            result['ParticipantIds'] = self.participant_ids

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

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
            self.executor_ids = m.get('ExecutorIds')

        if m.get('NotifyConfigs') is not None:
            temp_model = main_models.CreateDingtalkPersonalTodoTaskRequestNotifyConfigs()
            self.notify_configs = temp_model.from_map(m.get('NotifyConfigs'))

        if m.get('ParticipantIds') is not None:
            self.participant_ids = m.get('ParticipantIds')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('TenantContext') is not None:
            temp_model = main_models.CreateDingtalkPersonalTodoTaskRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('UserToken') is not None:
            self.user_token = m.get('UserToken')

        return self

class CreateDingtalkPersonalTodoTaskRequestTenantContext(DaraModel):
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

class CreateDingtalkPersonalTodoTaskRequestNotifyConfigs(DaraModel):
    def __init__(
        self,
        ding_notify: str = None,
    ):
        self.ding_notify = ding_notify

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ding_notify is not None:
            result['DingNotify'] = self.ding_notify

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingNotify') is not None:
            self.ding_notify = m.get('DingNotify')

        return self

