# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMemoryResponseBody(DaraModel):
    def __init__(
        self,
        memory_id: str = None,
        request_id: str = None,
    ):
        # The long-term memory ID.
        # > Store this value properly. It is required for all subsequent API operations related to this long-term memory.
        # >.
        self.memory_id = memory_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory_id is not None:
            result['memoryId'] = self.memory_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

