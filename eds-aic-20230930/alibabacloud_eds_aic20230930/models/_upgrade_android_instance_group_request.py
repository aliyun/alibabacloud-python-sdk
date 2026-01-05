# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeAndroidInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        increase_number_of_instance: int = None,
        instance_group_id: str = None,
        promotion_id: str = None,
    ):
        # Specifies whether to enable the auto-payment feature.
        # 
        # Valid values:
        # 
        # *   true: enables the auto-payment feature. Make sure that your Alibaba Cloud account has sufficient balance.
        # *   false: disables the auto-payment feature. You need to manually complete the payment process.
        self.auto_pay = auto_pay
        # The number of instances that you want to increase.
        self.increase_number_of_instance = increase_number_of_instance
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
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

        if self.increase_number_of_instance is not None:
            result['IncreaseNumberOfInstance'] = self.increase_number_of_instance

        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('IncreaseNumberOfInstance') is not None:
            self.increase_number_of_instance = m.get('IncreaseNumberOfInstance')

        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

