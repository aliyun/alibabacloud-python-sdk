# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateOptimizeRunRequest(DaraModel):
    def __init__(
        self,
        extra: Dict[str, Any] = None,
        status: str = None,
        client_token: str = None,
    ):
        # The extra parameters. To retry a failed artifact application, set application.action to retry and do not specify status. Do not specify this field when canceling a run.
        self.extra = extra
        # The status. Only Cancelled is supported when canceling a run. The execution status is maintained by the server. Do not specify this field when retrying an artifact application.
        self.status = status
        # The idempotency token.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['extra'] = self.extra

        if self.status is not None:
            result['status'] = self.status

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

