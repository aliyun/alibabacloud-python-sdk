# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAICloudPhoneRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        bandwidth_package_id: str = None,
        biz_region_id: str = None,
        image_id: str = None,
        instance_group_name: str = None,
        instance_group_spec: str = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        promotion_id: str = None,
    ):
        # The quantity to purchase.
        # 
        # This parameter is required.
        self.amount = amount
        # Specifies whether to enable automatic payment.
        self.auto_pay = auto_pay
        # The bandwidth package ID.
        # 
        # This parameter is required.
        self.bandwidth_package_id = bandwidth_package_id
        # The region ID for the purchase.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The instance group name.
        # 
        # This parameter is required.
        self.instance_group_name = instance_group_name
        # The instance group specification. Valid values:
        # 
        # - STANDARD: standard.
        # - MEDIUM: advanced.
        # 
        # This parameter is required.
        self.instance_group_spec = instance_group_spec
        # The purchase duration.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the purchase duration.
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The policy group ID.
        self.policy_group_id = policy_group_id
        # The coupon ID.
        self.promotion_id = promotion_id

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

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name

        if self.instance_group_spec is not None:
            result['InstanceGroupSpec'] = self.instance_group_spec

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')

        if m.get('InstanceGroupSpec') is not None:
            self.instance_group_spec = m.get('InstanceGroupSpec')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

