# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyInstanceChargeTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        charge_type: str = None,
        instance_group_ids: List[str] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
    ):
        # Specifies whether to enable the auto-payment feature. Default value: false.
        self.auto_pay = auto_pay
        # Specifies whether to enable the auto-renewal feature. Default value: false.
        self.auto_renew = auto_renew
        # The billing method. Valid values:
        # 
        # >  Currently, this operation only allows you to change the billing method from **pay-as-you-go to subscription**.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The IDs of the instance groups.
        # 
        # This parameter is required.
        self.instance_group_ids = instance_group_ids
        # The subscription duration. The unit is specified by PeriodUnit. Valid values: 1 Month, 2 Months, 3 Months, 6 Months, and 1 Year.
        self.period = period
        # The unit of the subscription duration. Valid values:
        # 
        # *   **Month**
        # *   **Year**
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

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

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

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

