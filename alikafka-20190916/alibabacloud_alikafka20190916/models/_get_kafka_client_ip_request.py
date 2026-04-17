# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKafkaClientIpRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        group: str = None,
        instance_id: str = None,
        region_id: str = None,
        start_time: int = None,
        topic: str = None,
        type: str = None,
    ):
        # The end of the time range to query.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the consumer group.
        # 
        # >  This parameter is required only if you set Type to byGroup.
        self.group = group
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The topic name.
        # 
        # > 
        # 
        # *   This parameter is required only if you set Type to byTopic.
        self.topic = topic
        # The query method that you want to use to query the client IP addresses. Valid values:
        # 
        # *   byInstance: queries the IP addresses of the clients that are connected to the instance within a specific period of time.
        # *   byTopic: queries the IP addresses of the clients that are connected to a specific topic on the instance within a specific period of time.
        # *   byGroup: queries the IP addresses of the clients that are connected to a specific group on the instance within a specific period of time.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group is not None:
            result['Group'] = self.group

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

