# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IncreaseNodeGroup(DaraModel):
    def __init__(
        self,
        description: str = None,
        node_count: int = None,
        node_group_id: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        v_switch_id: str = None,
    ):
        # 描述。
        self.description = description
        # 节点数量。
        # 
        # This parameter is required.
        self.node_count = node_count
        # 节点组ID。
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # 付费时长。
        self.payment_duration = payment_duration
        # 付费时长单位。
        self.payment_duration_unit = payment_duration_unit
        # 虚拟机交换机ID。
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration

        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')

        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

