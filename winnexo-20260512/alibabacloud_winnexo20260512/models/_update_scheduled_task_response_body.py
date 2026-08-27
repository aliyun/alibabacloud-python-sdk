# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateScheduledTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        task_id: str = None,
        updated: bool = None,
    ):
        # The business status code. A value of 200 indicates success. A failure returns a backend error code (ERR.* or InvalidParameter.*).
        self.code = code
        # The error description. Empty when the request is successful.
        self.message = message
        # The request trace ID.
        self.request_id = request_id
        # The task ID (echoed back).
        self.task_id = task_id
        # Indicates whether an actual update was made.
        self.updated = updated

    def validate(self):
        pass

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

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

