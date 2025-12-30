# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNetTestResultRequest(DaraModel):
    def __init__(
        self,
        test_id: str = None,
    ):
        # The ID of the test task. The unique identifier of a network test task.
        self.test_id = test_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.test_id is not None:
            result['TestId'] = self.test_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TestId') is not None:
            self.test_id = m.get('TestId')

        return self

