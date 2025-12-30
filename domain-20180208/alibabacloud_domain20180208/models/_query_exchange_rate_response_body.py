# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryExchangeRateResponseBody(DaraModel):
    def __init__(
        self,
        exchange_rate: float = None,
        request_id: str = None,
    ):
        self.exchange_rate = exchange_rate
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exchange_rate is not None:
            result['ExchangeRate'] = self.exchange_rate

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExchangeRate') is not None:
            self.exchange_rate = m.get('ExchangeRate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

