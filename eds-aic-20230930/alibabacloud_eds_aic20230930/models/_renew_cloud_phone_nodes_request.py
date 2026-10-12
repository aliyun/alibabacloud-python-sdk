# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RenewCloudPhoneNodesRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        node_ids: List[str] = None,
        paid_call_back_url: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Default value: false.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal.
        self.auto_renew = auto_renew
        # The list of cloud phone matrix IDs.
        self.node_ids = node_ids
        # The redirect URL for the payment success page.
        self.paid_call_back_url = paid_call_back_url
        # The subscription period. The unit is specified by PeriodUnit.
        # 
        # - If PeriodUnit is set to **year**, the only valid value is 1.
        # - If PeriodUnit is set to **month**, valid values are 1, 2, 3, and 6.
        self.period = period
        # The unit of the subscription period.
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

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.paid_call_back_url is not None:
            result['PaidCallBackUrl'] = self.paid_call_back_url

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

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('PaidCallBackUrl') is not None:
            self.paid_call_back_url = m.get('PaidCallBackUrl')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

