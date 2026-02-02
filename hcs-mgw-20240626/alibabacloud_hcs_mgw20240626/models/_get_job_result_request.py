# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobResultRequest(DaraModel):
    def __init__(
        self,
        runtime_id: int = None,
    ):
        # The execution ID of the task.
        # 
        # This parameter is required.
        self.runtime_id = runtime_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.runtime_id is not None:
            result['runtimeId'] = self.runtime_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('runtimeId') is not None:
            self.runtime_id = m.get('runtimeId')

        return self

