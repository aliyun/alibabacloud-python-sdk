# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloseWorkflowTodosResponseBody(DaraModel):
    def __init__(
        self,
        cancelled_count: int = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        source_workflow_id: str = None,
    ):
        # The number of closed to-do items. The value is 0 for idempotent repeated calls.
        self.cancelled_count = cancelled_count
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The error description.
        self.message = message
        # The request tracking ID.
        self.request_id = request_id
        # The workflow ID, returned as provided.
        self.source_workflow_id = source_workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancelled_count is not None:
            result['cancelledCount'] = self.cancelled_count

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source_workflow_id is not None:
            result['sourceWorkflowId'] = self.source_workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancelledCount') is not None:
            self.cancelled_count = m.get('cancelledCount')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sourceWorkflowId') is not None:
            self.source_workflow_id = m.get('sourceWorkflowId')

        return self

