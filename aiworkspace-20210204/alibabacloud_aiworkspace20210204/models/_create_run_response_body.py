# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRunResponseBody(DaraModel):
    def __init__(
        self,
        run_id: str = None,
        request_id: str = None,
    ):
        # The run ID.
        self.run_id = run_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.run_id is not None:
            result['RunId'] = self.run_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

