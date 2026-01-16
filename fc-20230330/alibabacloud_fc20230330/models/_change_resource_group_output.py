# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeResourceGroupOutput(DaraModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        old_resource_group_id: str = None,
        resource_id: str = None,
    ):
        self.new_resource_group_id = new_resource_group_id
        self.old_resource_group_id = old_resource_group_id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id

        if self.old_resource_group_id is not None:
            result['OldResourceGroupId'] = self.old_resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')

        if m.get('OldResourceGroupId') is not None:
            self.old_resource_group_id = m.get('OldResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

