# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateSavingsPlansInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        commodity_code: str = None,
        duration: str = None,
        effective_date: str = None,
        extend_map: Dict[str, str] = None,
        pay_mode: str = None,
        pool_value: str = None,
        pricing_cycle: str = None,
        region: str = None,
        spec_type: str = None,
        specification: str = None,
        type: str = None,
    ):
        self.auto_pay = auto_pay
        # This parameter is required.
        self.commodity_code = commodity_code
        # This parameter is required.
        self.duration = duration
        self.effective_date = effective_date
        self.extend_map = extend_map
        # This parameter is required.
        self.pay_mode = pay_mode
        # This parameter is required.
        self.pool_value = pool_value
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        self.region = region
        self.spec_type = spec_type
        self.specification = specification
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.effective_date is not None:
            result['EffectiveDate'] = self.effective_date

        if self.extend_map is not None:
            result['ExtendMap'] = self.extend_map

        if self.pay_mode is not None:
            result['PayMode'] = self.pay_mode

        if self.pool_value is not None:
            result['PoolValue'] = self.pool_value

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.region is not None:
            result['Region'] = self.region

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EffectiveDate') is not None:
            self.effective_date = m.get('EffectiveDate')

        if m.get('ExtendMap') is not None:
            self.extend_map = m.get('ExtendMap')

        if m.get('PayMode') is not None:
            self.pay_mode = m.get('PayMode')

        if m.get('PoolValue') is not None:
            self.pool_value = m.get('PoolValue')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

