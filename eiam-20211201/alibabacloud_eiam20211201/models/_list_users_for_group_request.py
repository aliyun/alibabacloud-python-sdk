# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListUsersForGroupRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        user_ids: List[str] = None,
    ):
        # The group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The account IDs. A maximum of 100 accounts can be queried.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

