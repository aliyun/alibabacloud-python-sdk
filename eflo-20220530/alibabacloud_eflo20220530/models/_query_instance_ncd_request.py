# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryInstanceNcdRequest(DaraModel):
    def __init__(
        self,
        instance_id_1: str = None,
        instance_id_2: str = None,
        instance_type: str = None,
        region_id: str = None,
    ):
        # Instance 1ID
        # 
        # This parameter is required.
        self.instance_id_1 = instance_id_1
        # Instance 2ID
        # 
        # This parameter is required.
        self.instance_id_2 = instance_id_2
        # The parameter that specifies the instance type.
        # 
        # Valid value:
        # 
        # *   node: Lingjun node.
        # *   lni: lingjun network interface controller.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id_1 is not None:
            result['InstanceId1'] = self.instance_id_1

        if self.instance_id_2 is not None:
            result['InstanceId2'] = self.instance_id_2

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId1') is not None:
            self.instance_id_1 = m.get('InstanceId1')

        if m.get('InstanceId2') is not None:
            self.instance_id_2 = m.get('InstanceId2')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

