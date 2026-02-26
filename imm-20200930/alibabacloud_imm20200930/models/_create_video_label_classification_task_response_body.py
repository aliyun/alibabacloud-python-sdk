# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVideoLabelClassificationTaskResponseBody(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The event ID of the current task. You can use [EventBridge](https://www.alibabacloud.com/en/product/eventbridge) to query the ID and obtain the task information notification.
        self.event_id = event_id
        # The request ID.
        self.request_id = request_id
        # The ID of the current task. You can call the [GetTask](~~GetTask~~) operation to view the task information or the [GetVideoLabelClassificationResult](https://help.aliyun.com/document_detail/478224.html) operation to obtain the result of the video label detection task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

