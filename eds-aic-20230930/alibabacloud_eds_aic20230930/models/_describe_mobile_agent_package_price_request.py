# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMobileAgentPackagePriceRequest(DaraModel):
    def __init__(
        self,
        amount: str = None,
        biz_region_id: str = None,
        credit_amount: int = None,
        mobile_agent_package_spec: str = None,
        period: str = None,
        period_unit: str = None,
        promotion_id: str = None,
    ):
        self.amount = amount
        self.biz_region_id = biz_region_id
        self.credit_amount = credit_amount
        self.mobile_agent_package_spec = mobile_agent_package_spec
        self.period = period
        self.period_unit = period_unit
        self.promotion_id = promotion_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount

        if self.mobile_agent_package_spec is not None:
            result['MobileAgentPackageSpec'] = self.mobile_agent_package_spec

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')

        if m.get('MobileAgentPackageSpec') is not None:
            self.mobile_agent_package_spec = m.get('MobileAgentPackageSpec')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

