# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PurchaseRatePlanRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        channel: str = None,
        charge_type: str = None,
        coverage: str = None,
        period: int = None,
        plan_code: str = None,
        plan_name: str = None,
        site_name: str = None,
        type: str = None,
    ):
        # The number of plans to purchase.
        self.amount = amount
        # Specifies whether to enable automatic payment.
        # Set this parameter to true when you directly call this operation.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # - true: Auto-renewal is enabled.
        # - false: Auto-renewal is disabled.
        self.auto_renew = auto_renew
        # The channel field.
        self.channel = channel
        # The billing method. Valid values:
        # - PREPAY: subscription.
        # - POSTPAY: pay-as-you-go.
        # Set this parameter to PREPAY when you directly call this operation.
        self.charge_type = charge_type
        # The acceleration region. Valid values:
        # - domestic: the Chinese mainland only.
        # - global: global.
        # - overseas: global (excluding the Chinese mainland).
        self.coverage = coverage
        # The purchase period, in months.
        # This parameter is required when you directly call this operation.
        self.period = period
        # The plan code.
        # 
        # China site
        # 
        # - Free Edition: entranceplan
        # - Basic: basicplan
        # - Standard: standardplan
        # - Premium: advancedplan
        # 
        # International site
        # 
        # - Entrance: entranceplan
        # - Pro: standardplan
        # - Premium: advancedpla.
        self.plan_code = plan_code
        # The plan name.
        # 
        # China site
        # 
        # - Free Edition: entranceplan
        # - Basic: basic
        # - Standard: medium
        # - Premium: high
        # 
        # International site
        # 
        # - Entrance: entranceplan_intl
        # - Pro: basicplan_intl
        # - Premium: vipplan_intl
        # 
        # > Note: For Enterprise Edition plans, the plan name is provided after backend configuration.
        self.plan_name = plan_name
        # The site name.
        self.site_name = site_name
        # The site access type. Valid values:
        # - NS: NS access.
        # - CNAME: CNAME access.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.coverage is not None:
            result['Coverage'] = self.coverage

        if self.period is not None:
            result['Period'] = self.period

        if self.plan_code is not None:
            result['PlanCode'] = self.plan_code

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PlanCode') is not None:
            self.plan_code = m.get('PlanCode')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

