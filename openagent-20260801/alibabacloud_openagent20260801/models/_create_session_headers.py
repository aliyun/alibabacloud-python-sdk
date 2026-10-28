# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateSessionHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_open_agent_idempotency_key: str = None,
    ):
        self.common_headers = common_headers
        # The request idempotency key. Use the same value and the same business parameters when retrying the same request.
        self.x_open_agent_idempotency_key = x_open_agent_idempotency_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.x_open_agent_idempotency_key is not None:
            result['X-OpenAgent-Idempotency-Key'] = self.x_open_agent_idempotency_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('X-OpenAgent-Idempotency-Key') is not None:
            self.x_open_agent_idempotency_key = m.get('X-OpenAgent-Idempotency-Key')

        return self

