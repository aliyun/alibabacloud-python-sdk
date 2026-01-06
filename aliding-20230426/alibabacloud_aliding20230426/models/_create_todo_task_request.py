# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateTodoTaskRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.CreateTodoTaskRequestTenantContext = None,
        action_list: List[main_models.CreateTodoTaskRequestActionList] = None,
        content_field_list: List[main_models.CreateTodoTaskRequestContentFieldList] = None,
        creator_id: str = None,
        description: str = None,
        detail_url: main_models.CreateTodoTaskRequestDetailUrl = None,
        due_time: int = None,
        executor_ids: List[str] = None,
        is_only_show_executor: bool = None,
        notify_configs: main_models.CreateTodoTaskRequestNotifyConfigs = None,
        operator_id: str = None,
        participant_ids: List[str] = None,
        priority: int = None,
        remind_notify_configs: main_models.CreateTodoTaskRequestRemindNotifyConfigs = None,
        reminder_time_stamp: int = None,
        source_id: str = None,
        subject: str = None,
    ):
        self.tenant_context = tenant_context
        self.action_list = action_list
        self.content_field_list = content_field_list
        self.creator_id = creator_id
        self.description = description
        self.detail_url = detail_url
        self.due_time = due_time
        self.executor_ids = executor_ids
        self.is_only_show_executor = is_only_show_executor
        self.notify_configs = notify_configs
        self.operator_id = operator_id
        self.participant_ids = participant_ids
        self.priority = priority
        self.remind_notify_configs = remind_notify_configs
        self.reminder_time_stamp = reminder_time_stamp
        self.source_id = source_id
        # This parameter is required.
        self.subject = subject

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()
        if self.action_list:
            for v1 in self.action_list:
                 if v1:
                    v1.validate()
        if self.content_field_list:
            for v1 in self.content_field_list:
                 if v1:
                    v1.validate()
        if self.detail_url:
            self.detail_url.validate()
        if self.notify_configs:
            self.notify_configs.validate()
        if self.remind_notify_configs:
            self.remind_notify_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        result['actionList'] = []
        if self.action_list is not None:
            for k1 in self.action_list:
                result['actionList'].append(k1.to_map() if k1 else None)

        result['contentFieldList'] = []
        if self.content_field_list is not None:
            for k1 in self.content_field_list:
                result['contentFieldList'].append(k1.to_map() if k1 else None)

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.description is not None:
            result['description'] = self.description

        if self.detail_url is not None:
            result['detailUrl'] = self.detail_url.to_map()

        if self.due_time is not None:
            result['dueTime'] = self.due_time

        if self.executor_ids is not None:
            result['executorIds'] = self.executor_ids

        if self.is_only_show_executor is not None:
            result['isOnlyShowExecutor'] = self.is_only_show_executor

        if self.notify_configs is not None:
            result['notifyConfigs'] = self.notify_configs.to_map()

        if self.operator_id is not None:
            result['operatorId'] = self.operator_id

        if self.participant_ids is not None:
            result['participantIds'] = self.participant_ids

        if self.priority is not None:
            result['priority'] = self.priority

        if self.remind_notify_configs is not None:
            result['remindNotifyConfigs'] = self.remind_notify_configs.to_map()

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
            temp_model = main_models.CreateTodoTaskRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        self.action_list = []
        if m.get('actionList') is not None:
            for k1 in m.get('actionList'):
                temp_model = main_models.CreateTodoTaskRequestActionList()
                self.action_list.append(temp_model.from_map(k1))

        self.content_field_list = []
        if m.get('contentFieldList') is not None:
            for k1 in m.get('contentFieldList'):
                temp_model = main_models.CreateTodoTaskRequestContentFieldList()
                self.content_field_list.append(temp_model.from_map(k1))

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('detailUrl') is not None:
            temp_model = main_models.CreateTodoTaskRequestDetailUrl()
            self.detail_url = temp_model.from_map(m.get('detailUrl'))

        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')

        if m.get('executorIds') is not None:
            self.executor_ids = m.get('executorIds')

        if m.get('isOnlyShowExecutor') is not None:
            self.is_only_show_executor = m.get('isOnlyShowExecutor')

        if m.get('notifyConfigs') is not None:
            temp_model = main_models.CreateTodoTaskRequestNotifyConfigs()
            self.notify_configs = temp_model.from_map(m.get('notifyConfigs'))

        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')

        if m.get('participantIds') is not None:
            self.participant_ids = m.get('participantIds')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('remindNotifyConfigs') is not None:
            temp_model = main_models.CreateTodoTaskRequestRemindNotifyConfigs()
            self.remind_notify_configs = temp_model.from_map(m.get('remindNotifyConfigs'))

        if m.get('reminderTimeStamp') is not None:
            self.reminder_time_stamp = m.get('reminderTimeStamp')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        return self

class CreateTodoTaskRequestRemindNotifyConfigs(DaraModel):
    def __init__(
        self,
        ding_notify: str = None,
        send_todo_apn: str = None,
    ):
        self.ding_notify = ding_notify
        self.send_todo_apn = send_todo_apn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ding_notify is not None:
            result['dingNotify'] = self.ding_notify

        if self.send_todo_apn is not None:
            result['sendTodoApn'] = self.send_todo_apn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingNotify') is not None:
            self.ding_notify = m.get('dingNotify')

        if m.get('sendTodoApn') is not None:
            self.send_todo_apn = m.get('sendTodoApn')

        return self

class CreateTodoTaskRequestNotifyConfigs(DaraModel):
    def __init__(
        self,
        ding_notify: str = None,
        send_assistant_chat: str = None,
        send_todo_apn: str = None,
    ):
        self.ding_notify = ding_notify
        self.send_assistant_chat = send_assistant_chat
        self.send_todo_apn = send_todo_apn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ding_notify is not None:
            result['dingNotify'] = self.ding_notify

        if self.send_assistant_chat is not None:
            result['sendAssistantChat'] = self.send_assistant_chat

        if self.send_todo_apn is not None:
            result['sendTodoApn'] = self.send_todo_apn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingNotify') is not None:
            self.ding_notify = m.get('dingNotify')

        if m.get('sendAssistantChat') is not None:
            self.send_assistant_chat = m.get('sendAssistantChat')

        if m.get('sendTodoApn') is not None:
            self.send_todo_apn = m.get('sendTodoApn')

        return self

class CreateTodoTaskRequestDetailUrl(DaraModel):
    def __init__(
        self,
        app_url: str = None,
        pc_url: str = None,
    ):
        self.app_url = app_url
        self.pc_url = pc_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_url is not None:
            result['appUrl'] = self.app_url

        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appUrl') is not None:
            self.app_url = m.get('appUrl')

        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')

        return self

class CreateTodoTaskRequestContentFieldList(DaraModel):
    def __init__(
        self,
        field_key: str = None,
        field_value: str = None,
    ):
        # fieldKey
        self.field_key = field_key
        # fieldValue
        self.field_value = field_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_key is not None:
            result['fieldKey'] = self.field_key

        if self.field_value is not None:
            result['fieldValue'] = self.field_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldKey') is not None:
            self.field_key = m.get('fieldKey')

        if m.get('fieldValue') is not None:
            self.field_value = m.get('fieldValue')

        return self

class CreateTodoTaskRequestActionList(DaraModel):
    def __init__(
        self,
        action_key: str = None,
        action_type: int = None,
        button_style_type: int = None,
        param: main_models.CreateTodoTaskRequestActionListParam = None,
        pc_url: str = None,
        title: str = None,
        url: str = None,
    ):
        self.action_key = action_key
        self.action_type = action_type
        self.button_style_type = button_style_type
        self.param = param
        self.pc_url = pc_url
        self.title = title
        self.url = url

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_key is not None:
            result['actionKey'] = self.action_key

        if self.action_type is not None:
            result['actionType'] = self.action_type

        if self.button_style_type is not None:
            result['buttonStyleType'] = self.button_style_type

        if self.param is not None:
            result['param'] = self.param.to_map()

        if self.pc_url is not None:
            result['pcUrl'] = self.pc_url

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionKey') is not None:
            self.action_key = m.get('actionKey')

        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')

        if m.get('buttonStyleType') is not None:
            self.button_style_type = m.get('buttonStyleType')

        if m.get('param') is not None:
            temp_model = main_models.CreateTodoTaskRequestActionListParam()
            self.param = temp_model.from_map(m.get('param'))

        if m.get('pcUrl') is not None:
            self.pc_url = m.get('pcUrl')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class CreateTodoTaskRequestActionListParam(DaraModel):
    def __init__(
        self,
        body: str = None,
        header: Dict[str, str] = None,
    ):
        self.body = body
        self.header = header

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.header is not None:
            result['header'] = self.header

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('header') is not None:
            self.header = m.get('header')

        return self

class CreateTodoTaskRequestTenantContext(DaraModel):
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

