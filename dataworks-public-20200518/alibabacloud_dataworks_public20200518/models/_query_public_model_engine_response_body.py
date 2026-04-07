# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class QueryPublicModelEngineResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        return_value: List[Dict[str, Any]] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned information about objects.
        self.return_value = return_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.return_value is not None:
            result['ReturnValue'] = self.return_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ReturnValue') is not None:
            self.return_value = m.get('ReturnValue')

        return self

