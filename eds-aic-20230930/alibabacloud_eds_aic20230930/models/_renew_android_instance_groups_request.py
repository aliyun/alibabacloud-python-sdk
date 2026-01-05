# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RenewAndroidInstanceGroupsRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        instance_group_ids: List[str] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
    ):
        # Specifies whether to enable the auto-payment feature.
        # 
        # Valid values:
        # 
        # *   true: enables the auto-payment feature. Ensure your account has sufficient balance to use this feature.
        # *   false: disables the auto-payment feature. You need to manually complete the payment process.
        self.auto_pay = auto_pay
        # The IDs of the instance groups.
        self.instance_group_ids = instance_group_ids
        # The duration of the renewal, measured in units defined by PeriodUnit.
        self.period = period
        # The unit of the renewal duration. Default value: Month.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        self.period_unit = period_unit
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

        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids

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

        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

