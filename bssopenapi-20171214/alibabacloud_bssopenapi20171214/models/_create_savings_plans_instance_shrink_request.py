# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSavingsPlansInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        commodity_code: str = None,
        duration: str = None,
        effective_date: str = None,
        extend_map_shrink: str = None,
        pay_mode: str = None,
        pool_value: str = None,
        pricing_cycle: str = None,
        region: str = None,
        spec_type: str = None,
        specification: str = None,
        type: str = None,
    ):
        self.auto_pay = auto_pay
        # The code of the service.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The service duration. This parameter is used together with the PricingCycle parameter.
        # 
        # This parameter is required.
        self.duration = duration
        # The time when the savings plan takes effect. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.effective_date = effective_date
        # The extended parameters.
        self.extend_map_shrink = extend_map_shrink
        # The payment mode. Valid values:
        # 
        # *   total: all upfront
        # *   half: partial upfront
        # *   zero: no upfront
        # 
        # This parameter is required.
        self.pay_mode = pay_mode
        # The contracted amount. unit: CNY
        # 
        # This parameter is required.
        self.pool_value = pool_value
        # The unit of the subscription duration. This parameter is used together with Duration. Valid values:
        # 
        # *   Year
        # *   Month
        # 
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # The ID of the region in which you create the savings plan. You must specify this parameter if the Type parameter is not set to universal.
        self.region = region
        # The specification type. This parameter is used together with the Specification parameter. You must specify this parameter if the Type parameter is not set to universal. Valid values:
        # 
        # *   group: specification group
        # *   family: specification family
        self.spec_type = spec_type
        # The specifications of the savings plan. This parameter is used together with the SpecType parameter.
        self.specification = specification
        # The type of the savings plan. Valid values:
        # 
        # *   universal: general-purpose type
        # *   ecs: Elastic Compute Service (ECS) compute type
        # *   elasticy: elastic type
        # 
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

        if self.extend_map_shrink is not None:
            result['ExtendMap'] = self.extend_map_shrink

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
            self.extend_map_shrink = m.get('ExtendMap')

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

