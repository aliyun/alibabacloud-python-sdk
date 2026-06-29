# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInspirationRequest(DaraModel):
    def __init__(
        self,
        amountspec: str = None,
        client_token: str = None,
        duration: int = None,
        extend: str = None,
        payment_type: str = None,
        pricing_cycle: str = None,
        quantity: int = None,
    ):
        # The resource plan specification.
        self.amountspec = amountspec
        # The idempotency token.
        self.client_token = client_token
        # The subscription duration.
        self.duration = duration
        # The extended information in JSON format.
        self.extend = extend
        # The payment type.
        self.payment_type = payment_type
        # The unit of the subscription duration. Valid values:
        # - Year: year.
        # - Month: month.
        # - Day: day.
        # - Hour: hour.
        self.pricing_cycle = pricing_cycle
        # The number of instances to purchase.
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amountspec is not None:
            result['Amountspec'] = self.amountspec

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

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amountspec') is not None:
            self.amountspec = m.get('Amountspec')

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

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        return self

