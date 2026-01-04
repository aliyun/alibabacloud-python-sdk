# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveUsersFromGroupRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
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
        # The account IDs. A maximum of 100 accounts can be removed from a group.
        # 
        # This parameter is required.
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

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

