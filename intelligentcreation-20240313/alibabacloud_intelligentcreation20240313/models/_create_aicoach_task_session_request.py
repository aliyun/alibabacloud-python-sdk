# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAICoachTaskSessionRequest(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        uid: str = None,
    ):
        self.task_id = task_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

