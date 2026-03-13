# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyTripTaskExecuteRequest(DaraModel):
    def __init__(
        self,
        action_from: str = None,
        comment: str = None,
        task_action: str = None,
        task_id: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.action_from = action_from
        self.comment = comment
        # This parameter is required.
        self.task_action = task_action
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_from is not None:
            result['action_from'] = self.action_from

        if self.comment is not None:
            result['comment'] = self.comment

        if self.task_action is not None:
            result['task_action'] = self.task_action

        if self.task_id is not None:
            result['task_id'] = self.task_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_from') is not None:
            self.action_from = m.get('action_from')

        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('task_action') is not None:
            self.task_action = m.get('task_action')

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

