# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SplitTrafficControlTargetRequest(DaraModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        set_points: List[int] = None,
        set_values: List[int] = None,
        time_points: List[int] = None,
    ):
        # The environment. Valid values:
        # 
        # - `Pre`: pre-production environment.
        # 
        # - `Prod`: production environment.
        self.environment = environment
        # The instance ID. For information about how to obtain the instance ID, see [ListInstances](https://help.aliyun.com/document_detail/2411819.html).
        self.instance_id = instance_id
        # This parameter is deprecated.
        self.set_points = set_points
        # The target values that correspond to the time intervals defined by the `TimePoints` parameter.
        self.set_values = set_values
        # The time points that define the traffic-splitting intervals.
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment is not None:
            result['Environment'] = self.environment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.set_points is not None:
            result['SetPoints'] = self.set_points

        if self.set_values is not None:
            result['SetValues'] = self.set_values

        if self.time_points is not None:
            result['TimePoints'] = self.time_points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SetPoints') is not None:
            self.set_points = m.get('SetPoints')

        if m.get('SetValues') is not None:
            self.set_values = m.get('SetValues')

        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')

        return self

