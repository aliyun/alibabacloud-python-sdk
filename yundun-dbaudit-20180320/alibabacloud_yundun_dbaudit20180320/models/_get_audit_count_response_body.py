# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAuditCountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_count: int = None,
        session_count: int = None,
        sql_count: int = None,
    ):
        self.request_id = request_id
        self.risk_count = risk_count
        self.session_count = session_count
        self.sql_count = sql_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')

        return self

