# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RenewMobileAgentPackageRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        client_token: str = None,
        mobile_agent_package_ids: List[str] = None,
        paid_callback_url: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **true**: Automatic payment is enabled. Make sure that your account balance is sufficient.
        # - **false** (default): Only an order is generated. No payment is made.
        # 
        # 
        # 
        # 
        # > If your payment method has an insufficient balance, set this parameter to false. An unpaid order is generated, and you can log on to the Elastic Cloud Phone console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Default value: false.
        self.auto_renew = auto_renew
        # The idempotence key.
        self.client_token = client_token
        # The list of resource plan IDs.
        self.mobile_agent_package_ids = mobile_agent_package_ids
        # The redirect URL after a successful payment.
        self.paid_callback_url = paid_callback_url
        # The duration for which you want to purchase the resource. The unit is specified by `PeriodUnit`.
        self.period = period
        # The unit of the duration for which you want to purchase the resource.
        # 
        # Valid values:
        # - **Month**: month.
        # - **Year**: year.
        self.period_unit = period_unit
        # The ID of the promotional campaign.
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

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.mobile_agent_package_ids is not None:
            result['MobileAgentPackageIds'] = self.mobile_agent_package_ids

        if self.paid_callback_url is not None:
            result['PaidCallbackUrl'] = self.paid_callback_url

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

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('MobileAgentPackageIds') is not None:
            self.mobile_agent_package_ids = m.get('MobileAgentPackageIds')

        if m.get('PaidCallbackUrl') is not None:
            self.paid_callback_url = m.get('PaidCallbackUrl')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

