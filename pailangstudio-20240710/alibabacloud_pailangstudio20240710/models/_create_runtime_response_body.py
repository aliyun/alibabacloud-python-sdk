# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRuntimeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        runtime_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Runtime ID.
        self.runtime_id = runtime_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        return self

