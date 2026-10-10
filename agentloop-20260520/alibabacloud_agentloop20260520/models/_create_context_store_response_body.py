# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateContextStoreResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        strategy_version: int = None,
    ):
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        self.strategy_version = strategy_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.strategy_version is not None:
            result['strategyVersion'] = self.strategy_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('strategyVersion') is not None:
            self.strategy_version = m.get('strategyVersion')

        return self

