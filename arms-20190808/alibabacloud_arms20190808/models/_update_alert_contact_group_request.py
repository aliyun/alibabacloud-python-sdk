# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAlertContactGroupRequest(DaraModel):
    def __init__(
        self,
        contact_group_id: int = None,
        contact_group_name: str = None,
        contact_ids: str = None,
        region_id: str = None,
    ):
        # The ID of the alert contact group.
        # 
        # This parameter is required.
        self.contact_group_id = contact_group_id
        # The name of the alert contact group.
        # 
        # This parameter is required.
        self.contact_group_name = contact_group_name
        # The ID of the alert contact.
        self.contact_ids = contact_ids
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id

        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')

        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

