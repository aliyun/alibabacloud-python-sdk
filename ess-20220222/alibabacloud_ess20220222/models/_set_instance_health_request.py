# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetInstanceHealthRequest(DaraModel):
    def __init__(
        self,
        health_status: str = None,
        instance_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        # The health status of the instance. Valid values:
        # 
        # *   Healthy: sets the instance as healthy.
        # *   Unhealthy: sets the instance as unhealthy.
        # 
        # This parameter is required.
        self.health_status = health_status
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        return self

