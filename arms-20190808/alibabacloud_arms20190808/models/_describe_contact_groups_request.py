# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeContactGroupsRequest(DaraModel):
    def __init__(
        self,
        contact_group_name: str = None,
        group_ids: str = None,
        is_detail: bool = None,
        page: int = None,
        region_id: str = None,
        size: int = None,
    ):
        # The name of the alert contact group.
        self.contact_group_name = contact_group_name
        # The ID of the alert contact group.
        self.group_ids = group_ids
        # Specifies whether to return all the alert contacts in the queried alert contact group. Valid values:
        # 
        # *   `false`
        # *   `true`
        self.is_detail = is_detail
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page = page
        # The region ID.
        self.region_id = region_id
        # The number of alert contact groups displayed on each page.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail

        if self.page is not None:
            result['Page'] = self.page

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

