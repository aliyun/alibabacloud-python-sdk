# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryModifyDiskTypePriceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_group_id: str = None,
        promotion_option_no: str = None,
        target_disk_type: str = None,
        target_performance_level: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.node_group_id = node_group_id
        self.promotion_option_no = promotion_option_no
        # This parameter is required.
        self.target_disk_type = target_disk_type
        # This parameter is required.
        self.target_performance_level = target_performance_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

