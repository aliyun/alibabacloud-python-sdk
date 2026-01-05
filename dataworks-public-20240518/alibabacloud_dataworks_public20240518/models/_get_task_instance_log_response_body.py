# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTaskInstanceLogResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_instance_log: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The run log of the instance.
        self.task_instance_log = task_instance_log

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_instance_log is not None:
            result['TaskInstanceLog'] = self.task_instance_log

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskInstanceLog') is not None:
            self.task_instance_log = m.get('TaskInstanceLog')

        return self

