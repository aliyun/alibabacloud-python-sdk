# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetAccountPasswordRequest(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        dbcluster_id: str = None,
        engine: str = None,
        resource_group_name: str = None,
    ):
        # The description of the account.
        # - The description cannot start with `http://` or `https://`.
        # - The description must be 2 to 256 characters in length.
        self.account_description = account_description
        # The database account.
        # > You can call the [DescribeAccounts](https://help.aliyun.com/document_detail/612430.html) operation to query the database account information of a specified cluster, including the database account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the database account.
        # - The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # - The following special characters are supported: `!@#$%^&*()_+-=`
        # - The password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.account_password = account_password
        # <props="china">The ID of the cluster. The cluster can be an Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The database engine. Valid values:
        # 
        # - **AnalyticDB** (default): the AnalyticDB for MySQL engine.
        # - **Clickhouse**: the wide table engine.
        self.engine = engine
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

