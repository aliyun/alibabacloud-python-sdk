# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeComfyTaskWaitingQueueResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        task_waiting_queue: main_models.DescribeComfyTaskWaitingQueueResponseBodyTaskWaitingQueue = None,
    ):
        # The status code. A value of 0 indicates success.
        self.code = code
        # The description.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The waiting queue information.
        self.task_waiting_queue = task_waiting_queue

    def validate(self):
        if self.task_waiting_queue:
            self.task_waiting_queue.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_waiting_queue is not None:
            result['TaskWaitingQueue'] = self.task_waiting_queue.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskWaitingQueue') is not None:
            temp_model = main_models.DescribeComfyTaskWaitingQueueResponseBodyTaskWaitingQueue()
            self.task_waiting_queue = temp_model.from_map(m.get('TaskWaitingQueue'))

        return self

class DescribeComfyTaskWaitingQueueResponseBodyTaskWaitingQueue(DaraModel):
    def __init__(
        self,
        waiting_count: int = None,
    ):
        # The number of waiting tasks.
        self.waiting_count = waiting_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.waiting_count is not None:
            result['WaitingCount'] = self.waiting_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WaitingCount') is not None:
            self.waiting_count = m.get('WaitingCount')

        return self

