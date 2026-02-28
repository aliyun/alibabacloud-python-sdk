# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstancesByNcdRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        max_ncd: int = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The parameter that specifies the instance type.
        # 
        # Valid value:
        # 
        # *   node: Lingjun node.
        # *   lni: lingjun network interface controller.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # Maximum network communication distance
        # 
        # This parameter is required.
        self.max_ncd = max_ncd
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_ncd is not None:
            result['MaxNcd'] = self.max_ncd

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxNcd') is not None:
            self.max_ncd = m.get('MaxNcd')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

