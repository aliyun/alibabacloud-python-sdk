# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisasterDowngradeRequest(DaraModel):
    def __init__(
        self,
        downgrade_instance_id: str = None,
        instance_id: str = None,
    ):
        # The instance ID to be downgraded.
        # 
        # This parameter is required.
        self.downgrade_instance_id = downgrade_instance_id
        # The ID of the ApsaraMQ for MQTT (MSMQ) instance.
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
        if self.downgrade_instance_id is not None:
            result['DowngradeInstanceId'] = self.downgrade_instance_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DowngradeInstanceId') is not None:
            self.downgrade_instance_id = m.get('DowngradeInstanceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

