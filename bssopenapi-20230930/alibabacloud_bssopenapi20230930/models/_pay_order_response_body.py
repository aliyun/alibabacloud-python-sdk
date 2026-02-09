# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class PayOrderResponseBody(DaraModel):
    def __init__(
        self,
        metadata: Any = None,
        order_id: int = None,
        pay_status: int = None,
        payer_id: int = None,
        request_id: str = None,
    ):
        self.metadata = metadata
        self.order_id = order_id
        self.pay_status = pay_status
        self.payer_id = payer_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status

        if self.payer_id is not None:
            result['PayerId'] = self.payer_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')

        if m.get('PayerId') is not None:
            self.payer_id = m.get('PayerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

