# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCreditPackageRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        channel_cookie: str = None,
        credit_amount: str = None,
        package_amount: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **true**: enables automatic payment. Make sure that your account balance is sufficient.
        # - **false** (default): generates an unpaid order without deducting fees.
        # 
        # > If the balance of your payment method is insufficient, you can change the Settings of this parameter to false to generate an unpaid order. Then, you can log on to the WUYING Cloud Phone console to complete the payment.
        self.auto_pay = auto_pay
        # The channel cookie. This parameter is passed through to the sales system when you place an order.
        self.channel_cookie = channel_cookie
        # The number of credits.
        self.credit_amount = credit_amount
        # The number of credit packages to purchase.
        self.package_amount = package_amount
        # The subscription period of the resource. The unit is specified by PeriodUnit.
        self.period = period
        # The unit of the subscription period. Valid values:
        # - **Month**: months.
        # - **Year**: years.
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
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.channel_cookie is not None:
            result['ChannelCookie'] = self.channel_cookie

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
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ChannelCookie') is not None:
            self.channel_cookie = m.get('ChannelCookie')

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

