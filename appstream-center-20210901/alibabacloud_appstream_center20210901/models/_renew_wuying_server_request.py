# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewWuyingServerRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        wuying_server_id: str = None,
    ):
        # Automatic payment.
        self.auto_pay = auto_pay
        # The renewal duration.
        self.period = period
        # The unit of the renewal time.
        # 
        # Valid values:
        # 
        # *   Month: month.
        # *   Year: year.
        self.period_unit = period_unit
        # The discount ID.
        self.promotion_id = promotion_id
        # The ID of the workstation.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')

        return self

