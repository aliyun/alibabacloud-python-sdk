# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBenchmarkTaskResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        region: str = None,
        request_id: str = None,
        task_name: str = None,
    ):
        # The returned message.
        self.message = message
        # The ID of the region where the stress testing task is performed.
        self.region = region
        # The request ID.
        self.request_id = request_id
        # The name of the stress testing task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.region is not None:
            result['Region'] = self.region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

