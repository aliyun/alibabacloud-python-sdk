# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchAlertContactGroupRequest(DaraModel):
    def __init__(
        self,
        contact_group_ids: str = None,
        contact_group_name: str = None,
        contact_id: int = None,
        contact_name: str = None,
        is_detail: bool = None,
        region_id: str = None,
    ):
        self.contact_group_ids = contact_group_ids
        self.contact_group_name = contact_group_name
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.is_detail = is_detail
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids

        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')

        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

