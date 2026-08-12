# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyChargeTypeRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        billing_instance_ids: str = None,
        duration: str = None,
        instance_id: str = None,
        pricing_cycle: str = None,
        promotion_option_no: str = None,
    ):
        # Whether to enable auto-renewal. This parameter takes effect only when payType is PrePaid. Default: disabled.
        self.auto_renew = auto_renew
        # List of billing instance IDs that require renewal. Separate multiple IDs with commas.
        self.billing_instance_ids = billing_instance_ids
        # Subscription duration. This parameter takes effect only when payType is PrePaid.
        self.duration = duration
        # Cluster ID
        self.instance_id = instance_id
        # Subscription duration unit:
        # 
        # - Month
        # 
        # - Year
        # 
        # This parameter takes effect only when payType is PrePaid.
        self.pricing_cycle = pricing_cycle
        # Coupon ID.
        self.promotion_option_no = promotion_option_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.billing_instance_ids is not None:
            result['BillingInstanceIds'] = self.billing_instance_ids

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BillingInstanceIds') is not None:
            self.billing_instance_ids = m.get('BillingInstanceIds')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        return self

