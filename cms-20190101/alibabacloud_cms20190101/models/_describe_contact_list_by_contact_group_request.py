# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeContactListByContactGroupRequest(DaraModel):
    def __init__(
        self,
        contact_group_name: str = None,
        region_id: str = None,
    ):
        # The name of the alert contact group.
        # 
        # This parameter is required.
        self.contact_group_name = contact_group_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

