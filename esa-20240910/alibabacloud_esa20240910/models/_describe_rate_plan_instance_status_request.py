# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRatePlanInstanceStatusRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_owner: int = None,
    ):
        # The instance ID. You can obtain the ID by calling the [ListUserRatePlanInstances](~~ListUserRatePlanInstances~~) operation.
        self.instance_id = instance_id
        self.resource_owner = resource_owner

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')

        return self

