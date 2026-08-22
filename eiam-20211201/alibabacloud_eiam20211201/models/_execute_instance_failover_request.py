# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteInstanceFailoverRequest(DaraModel):
    def __init__(
        self,
        instance_failover_status: str = None,
        instance_id: str = None,
    ):
        # The failover status. Valid values:
        # - inactive: The primary instance is active.
        # - active: The replica instance is active.
        # 
        # This parameter is required.
        self.instance_failover_status = instance_failover_status
        # The replica instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_failover_status is not None:
            result['InstanceFailoverStatus'] = self.instance_failover_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceFailoverStatus') is not None:
            self.instance_failover_status = m.get('InstanceFailoverStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

