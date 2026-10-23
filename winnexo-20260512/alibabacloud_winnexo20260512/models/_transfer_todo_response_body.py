# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class TransferTodoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        targets: List[main_models.TransferTodoResponseBodyTargets] = None,
        todo_id: str = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The error description.
        self.message = message
        # The request tracking ID.
        self.request_id = request_id
        # The processing results for each target.
        self.targets = targets
        # The ID of the to-do task.
        self.todo_id = todo_id

    def validate(self):
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['targets'].append(k1.to_map() if k1 else None)

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.targets = []
        if m.get('targets') is not None:
            for k1 in m.get('targets'):
                temp_model = main_models.TransferTodoResponseBodyTargets()
                self.targets.append(temp_model.from_map(k1))

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        return self

class TransferTodoResponseBodyTargets(DaraModel):
    def __init__(
        self,
        result: str = None,
        user_id: str = None,
    ):
        # The processing result. Valid values: CREATED, REVIVED, and ALREADY_PENDING.
        self.result = result
        # The ID of the target user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['result'] = self.result

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

