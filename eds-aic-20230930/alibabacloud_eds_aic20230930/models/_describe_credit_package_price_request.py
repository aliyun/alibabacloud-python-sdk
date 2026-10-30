# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCreditPackagePriceRequest(DaraModel):
    def __init__(
        self,
        credit_amount: int = None,
        package_amount: str = None,
        period: str = None,
        period_unit: str = None,
        promotion_id: str = None,
    ):
        # The number of credits.
        self.credit_amount = credit_amount
        # The number of credit boost packages to purchase. Valid values: 1 to 99.
        self.package_amount = package_amount
        # The subscription period of the resource. The unit is specified by PeriodUnit. Valid values: 3 months, 6 months, and 1 year.
        self.period = period
        # The billing time unit of the subscription Billable methods. Valid values:
        # - **Year**: year
        # - **Month** (default): month
        self.period_unit = period_unit
        # The ID of the promotion.
        self.promotion_id = promotion_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount

        if self.package_amount is not None:
            result['PackageAmount'] = self.package_amount

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')

        if m.get('PackageAmount') is not None:
            self.package_amount = m.get('PackageAmount')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

