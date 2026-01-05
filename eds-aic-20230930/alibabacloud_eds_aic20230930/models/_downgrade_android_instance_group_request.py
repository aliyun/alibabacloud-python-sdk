# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DowngradeAndroidInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        auto_pay: bool = None,
        instance_group_id: str = None,
    ):
        # The IDs of the cloud phone instances that you want to delete.
        self.android_instance_ids = android_instance_ids
        # Specifies whether to enable the auto-payment feature. Default value: false.
        # 
        # Valid values:
        # 
        # *   true: enables the auto-payment feature. Ensure your account has sufficient balance to use this feature.
        # *   false: disables the auto-payment feature. This requires manual payment each time you place an order.
        self.auto_pay = auto_pay
        # The ID of the instance group.
        # 
        # This parameter is required.
        self.instance_group_id = instance_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')

        return self

