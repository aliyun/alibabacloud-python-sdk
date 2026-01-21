# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMonitorGroupRequest(DaraModel):
    def __init__(
        self,
        contact_groups: str = None,
        group_id: str = None,
        group_name: str = None,
        region_id: str = None,
    ):
        # The alert groups that can receive alert notifications for the application group.
        self.contact_groups = contact_groups
        # The ID of the application group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the application group.
        self.group_name = group_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

