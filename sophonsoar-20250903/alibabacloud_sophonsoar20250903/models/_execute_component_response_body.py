# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteComponentResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        run_result: str = None,
    ):
        self.request_id = request_id
        self.run_result = run_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.run_result is not None:
            result['RunResult'] = self.run_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunResult') is not None:
            self.run_result = m.get('RunResult')

        return self

