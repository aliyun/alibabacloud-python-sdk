# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindDBResourceGroupWithUserRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        group_user: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        self.group_name = group_name
        # The name of the database account.
        self.group_user = group_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_user is not None:
            result['GroupUser'] = self.group_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupUser') is not None:
            self.group_user = m.get('GroupUser')

        return self

