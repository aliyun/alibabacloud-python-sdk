# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindAccountShrinkRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
        ram_user: str = None,
        ram_user_list_shrink: str = None,
    ):
        # A standard database account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # ID of the cluster. Applies to Enterprise Edition, Basic Edition, or Data Lakehouse Edition clusters.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # ID of the Alibaba Cloud RAM user to bind.
        self.ram_user = ram_user
        # List of Alibaba Cloud RAM user IDs to bind. You can bind only one RAM user at a time. If you specify this parameter, the RamUser parameter is ignored.
        self.ram_user_list_shrink = ram_user_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.ram_user is not None:
            result['RamUser'] = self.ram_user

        if self.ram_user_list_shrink is not None:
            result['RamUserList'] = self.ram_user_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RamUser') is not None:
            self.ram_user = m.get('RamUser')

        if m.get('RamUserList') is not None:
            self.ram_user_list_shrink = m.get('RamUserList')

        return self

