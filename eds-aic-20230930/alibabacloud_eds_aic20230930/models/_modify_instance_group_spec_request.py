# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyInstanceGroupSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        instance_group_ids: List[str] = None,
        instance_group_spec: str = None,
        promotion_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **true**: Automatic payment is enabled. Make sure that your account balance is sufficient.
        # - **false** (default): Only generates an order without deducting fees.
        # 
        # 
        # 
        # 
        # > If your payment method balance is insufficient, set this parameter to false. An unpaid order is generated, and you can log on to the Cloud Phone console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # The list of instance group IDs.
        self.instance_group_ids = instance_group_ids
        # The instance group specification. You can call [DescribeSpec](~~DescribeSpec~~) to query the specifications available for purchase for cloud phones.
        # 
        # This parameter is required.
        self.instance_group_spec = instance_group_spec
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

        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids

        if self.instance_group_spec is not None:
            result['InstanceGroupSpec'] = self.instance_group_spec

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')

        if m.get('InstanceGroupSpec') is not None:
            self.instance_group_spec = m.get('InstanceGroupSpec')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

