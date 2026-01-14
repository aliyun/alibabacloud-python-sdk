# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewAppInstanceRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        client_token: str = None,
        duration: int = None,
        extend: str = None,
        payment_type: str = None,
        pricing_cycle: str = None,
    ):
        self.biz_id = biz_id
        self.client_token = client_token
        self.duration = duration
        self.extend = extend
        self.payment_type = payment_type
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        return self

