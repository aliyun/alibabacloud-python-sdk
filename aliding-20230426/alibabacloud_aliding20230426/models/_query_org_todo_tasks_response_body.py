# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryOrgTodoTasksResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        todo_cards: List[main_models.QueryOrgTodoTasksResponseBodyTodoCards] = None,
    ):
        self.next_token = next_token
        # requestId
        self.request_id = request_id
        self.todo_cards = todo_cards

    def validate(self):
        if self.todo_cards:
            for v1 in self.todo_cards:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['todoCards'] = []
        if self.todo_cards is not None:
            for k1 in self.todo_cards:
                result['todoCards'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.todo_cards = []
        if m.get('todoCards') is not None:
            for k1 in m.get('todoCards'):
                temp_model = main_models.QueryOrgTodoTasksResponseBodyTodoCards()
                self.todo_cards.append(temp_model.from_map(k1))

        return self

class QueryOrgTodoTasksResponseBodyTodoCards(DaraModel):
    def __init__(
        self,
        biz_tag: str = None,
        created_time: int = None,
        creator_id: str = None,
        detail_url: main_models.QueryOrgTodoTasksResponseBodyTodoCardsDetailUrl = None,
        due_time: int = None,
        is_done: bool = None,
        modified_time: int = None,
        priority: int = None,
        source_id: str = None,
        subject: str = None,
        task_id: str = None,
    ):
        self.biz_tag = biz_tag
        self.created_time = created_time
        self.creator_id = creator_id
        self.detail_url = detail_url
        self.due_time = due_time
        self.is_done = is_done
        self.modified_time = modified_time
        self.priority = priority
        self.source_id = source_id
        self.subject = subject
        self.task_id = task_id

    def validate(self):
        if self.detail_url:
            self.detail_url.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_tag is not None:
            result['bizTag'] = self.biz_tag

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.detail_url is not None:
            result['detailUrl'] = self.detail_url.to_map()

        if self.due_time is not None:
            result['dueTime'] = self.due_time

        if self.is_done is not None:
            result['isDone'] = self.is_done

        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.priority is not None:
            result['priority'] = self.priority

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.subject is not None:
            result['subject'] = self.subject

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizTag') is not None:
            self.biz_tag = m.get('bizTag')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('detailUrl') is not None:
            temp_model = main_models.QueryOrgTodoTasksResponseBodyTodoCardsDetailUrl()
            self.detail_url = temp_model.from_map(m.get('detailUrl'))

        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')

        if m.get('isDone') is not None:
            self.is_done = m.get('isDone')

        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class QueryOrgTodoTasksResponseBodyTodoCardsDetailUrl(DaraModel):
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

