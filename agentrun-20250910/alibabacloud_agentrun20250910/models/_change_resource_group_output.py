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
            result['newResourceGroupId'] = self.new_resource_group_id

        if self.old_resource_group_id is not None:
            result['oldResourceGroupId'] = self.old_resource_group_id

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newResourceGroupId') is not None:
            self.new_resource_group_id = m.get('newResourceGroupId')

        if m.get('oldResourceGroupId') is not None:
            self.old_resource_group_id = m.get('oldResourceGroupId')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        return self

