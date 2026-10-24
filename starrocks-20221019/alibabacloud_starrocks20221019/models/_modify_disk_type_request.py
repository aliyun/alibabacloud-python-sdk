# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDiskTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        instance_id: str = None,
        node_group_id: str = None,
        promotion_option_no: str = None,
        target_disk_type: str = None,
        target_performance_level: str = None,
    ):
        # Specifies whether to automatically pay for all products specified in the Products parameter. Valid values:
        # - true: Automatic payment.
        # - false: Manual payment.
        self.auto_pay = auto_pay
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The compute group ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # The coupon ID.
        self.promotion_option_no = promotion_option_no
        # The target disk type.
        # 
        # This parameter is required.
        self.target_disk_type = target_disk_type
        # The target disk performance.
        # 
        # This parameter is required.
        self.target_performance_level = target_performance_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.target_disk_type is not None:
            result['TargetDiskType'] = self.target_disk_type

        if self.target_performance_level is not None:
            result['TargetPerformanceLevel'] = self.target_performance_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('TargetDiskType') is not None:
            self.target_disk_type = m.get('TargetDiskType')

        if m.get('TargetPerformanceLevel') is not None:
            self.target_performance_level = m.get('TargetPerformanceLevel')

        return self

