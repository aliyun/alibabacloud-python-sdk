# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCClusterConfigRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        temporary_duration_minutes: int = None,
        vpc_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The validity period of the temporary kubeconfig file. Unit: minutes. Valid values: 15 to 4320.
        # 
        # >  If you do not specify this parameter, the system specifies a longer validity period. The validity period is returned in the `expiration` parameter.
        self.temporary_duration_minutes = temporary_duration_minutes
        # The virtual private cloud (VPC) ID.
        # 
        # >  This is a reserved parameter.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.temporary_duration_minutes is not None:
            result['TemporaryDurationMinutes'] = self.temporary_duration_minutes

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemporaryDurationMinutes') is not None:
            self.temporary_duration_minutes = m.get('TemporaryDurationMinutes')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

