# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateTodoTaskResponseBody(DaraModel):
    def __init__(
        self,
        biz_tag: str = None,
        content_field_list: List[main_models.CreateTodoTaskResponseBodyContentFieldList] = None,
        created_time: int = None,
        creator_id: str = None,
        description: str = None,
        detail_url: main_models.CreateTodoTaskResponseBodyDetailUrl = None,
        done: bool = None,
        due_time: int = None,
        executor_ids: List[str] = None,
        finish_time: int = None,
        id: str = None,
        is_only_show_executor: bool = None,
        modified_time: int = None,
        modifier_id: str = None,
        notify_configs: main_models.CreateTodoTaskResponseBodyNotifyConfigs = None,
        participant_ids: List[str] = None,
        priority: int = None,
        request_id: str = None,
        source: str = None,
        source_id: str = None,
        start_time: int = None,
        subject: str = None,
    ):
        self.biz_tag = biz_tag
        self.content_field_list = content_field_list
        self.created_time = created_time
        self.creator_id = creator_id
        self.description = description
        self.detail_url = detail_url
        self.done = done
        self.due_time = due_time
        self.executor_ids = executor_ids
        self.finish_time = finish_time
        self.id = id
        self.is_only_show_executor = is_only_show_executor
        self.modified_time = modified_time
        self.modifier_id = modifier_id
        self.notify_configs = notify_configs
        self.participant_ids = participant_ids
        self.priority = priority
        # requestId
        self.request_id = request_id
        self.source = source
        self.source_id = source_id
        self.start_time = start_time
        self.subject = subject

    def validate(self):
        if self.content_field_list:
            for v1 in self.content_field_list:
                 if v1:
                    v1.validate()
        if self.detail_url:
            self.detail_url.validate()
        if self.notify_configs:
            self.notify_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_tag is not None:
            result['bizTag'] = self.biz_tag

        result['contentFieldList'] = []
        if self.content_field_list is not None:
            for k1 in self.content_field_list:
                result['contentFieldList'].append(k1.to_map() if k1 else None)

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.description is not None:
            result['description'] = self.description

        if self.detail_url is not None:
            result['detailUrl'] = self.detail_url.to_map()

        if self.done is not None:
            result['done'] = self.done

        if self.due_time is not None:
            result['dueTime'] = self.due_time

        if self.executor_ids is not None:
            result['executorIds'] = self.executor_ids

        if self.finish_time is not None:
            result['finishTime'] = self.finish_time

        if self.id is not None:
            result['id'] = self.id

        if self.is_only_show_executor is not None:
            result['isOnlyShowExecutor'] = self.is_only_show_executor

        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.modifier_id is not None:
            result['modifierId'] = self.modifier_id

        if self.notify_configs is not None:
            result['notifyConfigs'] = self.notify_configs.to_map()

        if self.participant_ids is not None:
            result['participantIds'] = self.participant_ids

        if self.priority is not None:
            result['priority'] = self.priority

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source is not None:
            result['source'] = self.source

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.subject is not None:
            result['subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizTag') is not None:
            self.biz_tag = m.get('bizTag')

        self.content_field_list = []
        if m.get('contentFieldList') is not None:
            for k1 in m.get('contentFieldList'):
                temp_model = main_models.CreateTodoTaskResponseBodyContentFieldList()
                self.content_field_list.append(temp_model.from_map(k1))

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('detailUrl') is not None:
            temp_model = main_models.CreateTodoTaskResponseBodyDetailUrl()
            self.detail_url = temp_model.from_map(m.get('detailUrl'))

        if m.get('done') is not None:
            self.done = m.get('done')

        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')

        if m.get('executorIds') is not None:
            self.executor_ids = m.get('executorIds')

        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isOnlyShowExecutor') is not None:
            self.is_only_show_executor = m.get('isOnlyShowExecutor')

        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('modifierId') is not None:
            self.modifier_id = m.get('modifierId')

        if m.get('notifyConfigs') is not None:
            temp_model = main_models.CreateTodoTaskResponseBodyNotifyConfigs()
            self.notify_configs = temp_model.from_map(m.get('notifyConfigs'))

        if m.get('participantIds') is not None:
            self.participant_ids = m.get('participantIds')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        return self

class CreateTodoTaskResponseBodyNotifyConfigs(DaraModel):
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
            result['dingNotify'] = self.ding_notify

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingNotify') is not None:
            self.ding_notify = m.get('dingNotify')

        return self

class CreateTodoTaskResponseBodyDetailUrl(DaraModel):
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

class CreateTodoTaskResponseBodyContentFieldList(DaraModel):
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

