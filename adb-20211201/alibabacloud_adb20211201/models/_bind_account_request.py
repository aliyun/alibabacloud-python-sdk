# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BindAccountRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
        ram_user: str = None,
        ram_user_list: List[str] = None,
    ):
        # The standard database account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # <props="china">The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of the Alibaba Cloud RAM user to bind.
        self.ram_user = ram_user
        # The list of IDs of the Alibaba Cloud RAM users to bind. Currently, only one RAM user can be bound. If you specify this parameter, the RamUser parameter does not take effect.
        self.ram_user_list = ram_user_list

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

        if self.ram_user_list is not None:
            result['RamUserList'] = self.ram_user_list

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
            self.ram_user_list = m.get('RamUserList')

        return self

