# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTodoTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        action_list_shrink: str = None,
        content_field_list_shrink: str = None,
        creator_id: str = None,
        description: str = None,
        detail_url_shrink: str = None,
        due_time: int = None,
        executor_ids_shrink: str = None,
        is_only_show_executor: bool = None,
        notify_configs_shrink: str = None,
        operator_id: str = None,
        participant_ids_shrink: str = None,
        priority: int = None,
        remind_notify_configs_shrink: str = None,
        reminder_time_stamp: int = None,
        source_id: str = None,
        subject: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        self.action_list_shrink = action_list_shrink
        self.content_field_list_shrink = content_field_list_shrink
        self.creator_id = creator_id
        self.description = description
        self.detail_url_shrink = detail_url_shrink
        self.due_time = due_time
        self.executor_ids_shrink = executor_ids_shrink
        self.is_only_show_executor = is_only_show_executor
        self.notify_configs_shrink = notify_configs_shrink
        self.operator_id = operator_id
        self.participant_ids_shrink = participant_ids_shrink
        self.priority = priority
        self.remind_notify_configs_shrink = remind_notify_configs_shrink
        self.reminder_time_stamp = reminder_time_stamp
        self.source_id = source_id
        # This parameter is required.
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.action_list_shrink is not None:
            result['actionList'] = self.action_list_shrink

        if self.content_field_list_shrink is not None:
            result['contentFieldList'] = self.content_field_list_shrink

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.description is not None:
            result['description'] = self.description

        if self.detail_url_shrink is not None:
            result['detailUrl'] = self.detail_url_shrink

        if self.due_time is not None:
            result['dueTime'] = self.due_time

        if self.executor_ids_shrink is not None:
            result['executorIds'] = self.executor_ids_shrink

        if self.is_only_show_executor is not None:
            result['isOnlyShowExecutor'] = self.is_only_show_executor

        if self.notify_configs_shrink is not None:
            result['notifyConfigs'] = self.notify_configs_shrink

        if self.operator_id is not None:
            result['operatorId'] = self.operator_id

        if self.participant_ids_shrink is not None:
            result['participantIds'] = self.participant_ids_shrink

        if self.priority is not None:
            result['priority'] = self.priority

        if self.remind_notify_configs_shrink is not None:
            result['remindNotifyConfigs'] = self.remind_notify_configs_shrink

        if self.reminder_time_stamp is not None:
            result['reminderTimeStamp'] = self.reminder_time_stamp

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.subject is not None:
            result['subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('actionList') is not None:
            self.action_list_shrink = m.get('actionList')

        if m.get('contentFieldList') is not None:
            self.content_field_list_shrink = m.get('contentFieldList')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('detailUrl') is not None:
            self.detail_url_shrink = m.get('detailUrl')

        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')

        if m.get('executorIds') is not None:
            self.executor_ids_shrink = m.get('executorIds')

        if m.get('isOnlyShowExecutor') is not None:
            self.is_only_show_executor = m.get('isOnlyShowExecutor')

        if m.get('notifyConfigs') is not None:
            self.notify_configs_shrink = m.get('notifyConfigs')

        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')

        if m.get('participantIds') is not None:
            self.participant_ids_shrink = m.get('participantIds')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('remindNotifyConfigs') is not None:
            self.remind_notify_configs_shrink = m.get('remindNotifyConfigs')

        if m.get('reminderTimeStamp') is not None:
            self.reminder_time_stamp = m.get('reminderTimeStamp')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        return self

