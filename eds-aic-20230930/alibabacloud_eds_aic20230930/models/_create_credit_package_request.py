# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCreditPackageRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        credit_amount: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
    ):
        # Whether to enable auto-payment. Valid values:
        # 
        # - **true**: Enables auto-payment. Make sure that your account has a sufficient balance.
        # 
        # - **false** (Default): Creates an unpaid order.
        # 
        # > If your account has an insufficient balance, you can set this parameter to false. This generates an unpaid order. You can then pay for the order in the Wuying Cloud Phone management console.
        self.auto_pay = auto_pay
        # The number of credits.
        self.credit_amount = credit_amount
        # The subscription duration. The PeriodUnit parameter specifies the unit for the duration.
        self.period = period
        # The unit of the subscription duration.
        # Valid values:
        # 
        # - **Month**: The period is measured in months.
        # 
        # - **Year**: The period is measured in years.
        self.period_unit = period_unit
        # The promotion ID.
        self.promotion_id = promotion_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

