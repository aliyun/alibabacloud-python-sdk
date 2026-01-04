# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListGroupsRequest(DaraModel):
    def __init__(
        self,
        group_external_id: str = None,
        group_ids: List[str] = None,
        group_name: str = None,
        group_name_starts_with: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The external ID of the group.
        self.group_external_id = group_external_id
        # The group IDs.
        self.group_ids = group_ids
        # The name of the group. If you specify this parameter, the query is based on an exact match.
        self.group_name = group_name
        # The prefix of the group name. If you specify this parameter, the query follows the leftmost matching principle.
        self.group_name_starts_with = group_name_starts_with
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_external_id is not None:
            result['GroupExternalId'] = self.group_external_id

        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_name_starts_with is not None:
            result['GroupNameStartsWith'] = self.group_name_starts_with

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupExternalId') is not None:
            self.group_external_id = m.get('GroupExternalId')

        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupNameStartsWith') is not None:
            self.group_name_starts_with = m.get('GroupNameStartsWith')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

