# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CreateTodoResponseBody(DaraModel):
    def __init__(
        self,
        assignees: List[main_models.CreateTodoResponseBodyAssignees] = None,
        code: str = None,
        gmt_create: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        todo_id: str = None,
    ):
        # The list of assignees.
        self.assignees = assignees
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The creation time in ISO 8601 format with a time zone. This format differs from the UTC+8 format string used in the list and details.
        self.gmt_create = gmt_create
        # The error description.
        self.message = message
        # The request tracking ID.
        self.request_id = request_id
        # The status of the to-do item.
        self.status = status
        # The ID of the created to-do item.
        self.todo_id = todo_id

    def validate(self):
        if self.assignees:
            for v1 in self.assignees:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['assignees'] = []
        if self.assignees is not None:
            for k1 in self.assignees:
                result['assignees'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['code'] = self.code

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assignees = []
        if m.get('assignees') is not None:
            for k1 in m.get('assignees'):
                temp_model = main_models.CreateTodoResponseBodyAssignees()
                self.assignees.append(temp_model.from_map(k1))

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        return self

class CreateTodoResponseBodyAssignees(DaraModel):
    def __init__(
        self,
        assignee_user_id: str = None,
        status: str = None,
    ):
        # The user ID of the assignee.
        self.assignee_user_id = assignee_user_id
        # The processing status of the assignee.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assignee_user_id is not None:
            result['assigneeUserId'] = self.assignee_user_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assigneeUserId') is not None:
            self.assignee_user_id = m.get('assigneeUserId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

