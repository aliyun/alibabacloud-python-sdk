# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCResourcesModificationShrinkRequest(DaraModel):
    def __init__(
        self,
        conditionss_shrink: str = None,
        cores: int = None,
        destination_resource: str = None,
        instance_id: str = None,
        instance_type: str = None,
        memory: float = None,
        operation_type: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.conditionss_shrink = conditionss_shrink
        self.cores = cores
        # This parameter is required.
        self.destination_resource = destination_resource
        # This parameter is required.
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.memory = memory
        self.operation_type = operation_type
        # This parameter is required.
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conditionss_shrink is not None:
            result['Conditionss'] = self.conditionss_shrink

        if self.cores is not None:
            result['Cores'] = self.cores

        if self.destination_resource is not None:
            result['DestinationResource'] = self.destination_resource

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditionss') is not None:
            self.conditionss_shrink = m.get('Conditionss')

        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('DestinationResource') is not None:
            self.destination_resource = m.get('DestinationResource')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

