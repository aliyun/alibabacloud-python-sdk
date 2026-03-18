# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMaintainableTimeRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        maintainable_time_period: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.maintainable_time_period = maintainable_time_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.maintainable_time_period is not None:
            result['MaintainableTimePeriod'] = self.maintainable_time_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaintainableTimePeriod') is not None:
            self.maintainable_time_period = m.get('MaintainableTimePeriod')

        return self

