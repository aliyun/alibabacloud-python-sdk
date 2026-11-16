# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataStepPriceMapValue(DaraModel):
    def __init__(
        self,
        currency: str = None,
        deduct_cycle_type: str = None,
        left_close: bool = None,
        max: str = None,
        min: str = None,
        price_value: str = None,
        price_value_type: str = None,
        right_close: bool = None,
        step_price_value: str = None,
    ):
        self.currency = currency
        self.deduct_cycle_type = deduct_cycle_type
        self.left_close = left_close
        self.max = max
        self.min = min
        self.price_value = price_value
        self.price_value_type = price_value_type
        self.right_close = right_close
        self.step_price_value = step_price_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.deduct_cycle_type is not None:
            result['DeductCycleType'] = self.deduct_cycle_type

        if self.left_close is not None:
            result['LeftClose'] = self.left_close

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.price_value is not None:
            result['PriceValue'] = self.price_value

        if self.price_value_type is not None:
            result['PriceValueType'] = self.price_value_type

        if self.right_close is not None:
            result['RightClose'] = self.right_close

        if self.step_price_value is not None:
            result['StepPriceValue'] = self.step_price_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeductCycleType') is not None:
            self.deduct_cycle_type = m.get('DeductCycleType')

        if m.get('LeftClose') is not None:
            self.left_close = m.get('LeftClose')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('PriceValue') is not None:
            self.price_value = m.get('PriceValue')

        if m.get('PriceValueType') is not None:
            self.price_value_type = m.get('PriceValueType')

        if m.get('RightClose') is not None:
            self.right_close = m.get('RightClose')

        if m.get('StepPriceValue') is not None:
            self.step_price_value = m.get('StepPriceValue')

        return self

