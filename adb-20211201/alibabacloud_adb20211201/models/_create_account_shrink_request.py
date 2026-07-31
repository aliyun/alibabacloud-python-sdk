# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccountShrinkRequest(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        account_type: str = None,
        dbcluster_id: str = None,
        engine: str = None,
        ram_user_list_shrink: str = None,
    ):
        # The description of the account.
        # - Cannot start with `http://` or `https://`.
        # - Cannot exceed 256 characters in length.
        self.account_description = account_description
        # The name of the database account. The name must meet the following requirements:
        # - Starts with a lowercase letter and ends with a lowercase letter or digit.
        # - Contains only lowercase letters, digits, or underscores (_).
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the database account.
        # - Must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # - Special characters include: `!@#$%^&*()_+-=`
        # - Must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.account_password = account_password
        # The type of the account. Valid values:
        # - **Normal**: standard account.
        # - **Super**: privileged account.
        # 
        # This parameter is required.
        self.account_type = account_type
        # <props="china">The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The database engine. Valid values:
        # 
        # - **AnalyticDB** (default): AnalyticDB for MySQL engine.
        # - **Clickhouse**: wide table engine.
        self.engine = engine
        # The list of Alibaba Cloud Resource Access Management (RAM) user IDs to attach. Currently, only one RAM user can be attached.
        self.ram_user_list_shrink = ram_user_list_shrink

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

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.ram_user_list_shrink is not None:
            result['RamUserList'] = self.ram_user_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('RamUserList') is not None:
            self.ram_user_list_shrink = m.get('RamUserList')

        return self

