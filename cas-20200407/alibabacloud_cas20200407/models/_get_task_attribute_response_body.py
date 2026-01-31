# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTaskAttributeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_message: str = None,
        task_status: str = None,
    ):
        self.request_id = request_id
        self.task_message = task_message
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_message is not None:
            result['TaskMessage'] = self.task_message

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskMessage') is not None:
            self.task_message = m.get('TaskMessage')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

