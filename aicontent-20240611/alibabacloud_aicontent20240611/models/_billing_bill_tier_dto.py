# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BillingBillTierDTO(DaraModel):
    def __init__(
        self,
        dim_values: str = None,
        payable_amount: float = None,
        values: str = None,
    ):
        self.dim_values = dim_values
        self.payable_amount = payable_amount
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dim_values is not None:
            result['dimValues'] = self.dim_values

        if self.payable_amount is not None:
            result['payableAmount'] = self.payable_amount

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dimValues') is not None:
            self.dim_values = m.get('dimValues')

        if m.get('payableAmount') is not None:
            self.payable_amount = m.get('payableAmount')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

