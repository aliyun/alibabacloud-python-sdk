# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetTestTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        test_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The ID of the test task. The unique identifier of a network test task.
        self.test_id = test_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.test_id is not None:
            result['TestId'] = self.test_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TestId') is not None:
            self.test_id = m.get('TestId')

        return self

