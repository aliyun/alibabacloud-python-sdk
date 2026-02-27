# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeResourceGroupRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        new_resource_group_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # new resource group id
        self.new_resource_group_id = new_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.new_resource_group_id is not None:
            result['newResourceGroupId'] = self.new_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('newResourceGroupId') is not None:
            self.new_resource_group_id = m.get('newResourceGroupId')

        return self

