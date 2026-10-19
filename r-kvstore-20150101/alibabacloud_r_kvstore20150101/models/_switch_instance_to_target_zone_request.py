# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchInstanceToTargetZoneRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: str = None,
        switch_type: str = None,
        target_zone_id: str = None,
    ):
        # Instance ID of the instance. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) operation to query instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the child node in a cluster instance.
        # 
        # > If you do not specify this parameter, all shards are switched to the destination zone.
        self.node_id = node_id
        # The switch mode. Valid values:
        # * **ReliabilityPriority** (default): Reliability priority. A primary/secondary switchover is performed only when data synchronization between the primary and secondary nodes has no latency. This ensures that no data is lost. However, in scenarios with a large write volume and continuous synchronization latency, the switchover may fail.
        # * **AvailablePriority**: Availability priority. A primary/secondary switchover is performed immediately regardless of the synchronization latency between the primary and secondary nodes. A small amount of data may be lost.
        # 
        # > Select a switch mode based on your business requirements for data and services.
        self.switch_type = switch_type
        # The ID of the destination zone.
        # 
        # This parameter is required.
        self.target_zone_id = target_zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.switch_type is not None:
            result['SwitchType'] = self.switch_type

        if self.target_zone_id is not None:
            result['TargetZoneId'] = self.target_zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('SwitchType') is not None:
            self.switch_type = m.get('SwitchType')

        if m.get('TargetZoneId') is not None:
            self.target_zone_id = m.get('TargetZoneId')

        return self

