# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCustinsResourceRequest(DaraModel):
    def __init__(
        self,
        adjust_deadline: str = None,
        dbinstance_id: str = None,
        increase_ratio: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        restore_original_specification: str = None,
        target_value: int = None,
    ):
        # The deadline for the modification.
        self.adjust_deadline = adjust_deadline
        # The instance ID. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/26232.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The increase rate in percentage.
        self.increase_ratio = increase_ratio
        self.resource_owner_id = resource_owner_id
        # The resource type.
        self.resource_type = resource_type
        # The original value. This parameter must be specified when the **ResourceType** parameter is set to **instance**.
        self.restore_original_specification = restore_original_specification
        # The target value. This parameter is available only if you set the ScalingRuleType parameter to TargetTrackingScalingRule or PredictiveScalingRule. The value must be greater than 0 and can contain up to three decimal places.
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjust_deadline is not None:
            result['AdjustDeadline'] = self.adjust_deadline

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.increase_ratio is not None:
            result['IncreaseRatio'] = self.increase_ratio

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.restore_original_specification is not None:
            result['RestoreOriginalSpecification'] = self.restore_original_specification

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustDeadline') is not None:
            self.adjust_deadline = m.get('AdjustDeadline')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('IncreaseRatio') is not None:
            self.increase_ratio = m.get('IncreaseRatio')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RestoreOriginalSpecification') is not None:
            self.restore_original_specification = m.get('RestoreOriginalSpecification')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

