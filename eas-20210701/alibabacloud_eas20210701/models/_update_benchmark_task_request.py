# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBenchmarkTaskRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The configuration parameters of the stress testing task. For more information, see **Table 1. base description table**. The target stress testing task must be in the Running state. You can call the DescribeBenchmarkTask operation to query the task status. If the task is in the Stopped state, you must first call the StartBenchmarkTask operation and wait until the task enters the Running state.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        return self

