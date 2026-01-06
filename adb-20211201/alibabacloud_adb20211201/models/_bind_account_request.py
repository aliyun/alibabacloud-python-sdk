# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindAccountRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
        ram_user: str = None,
    ):
        # The standard account of the cluster.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of the RAM user.
        # 
        # This parameter is required.
        self.ram_user = ram_user

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RamUser') is not None:
            self.ram_user = m.get('RamUser')

        return self

