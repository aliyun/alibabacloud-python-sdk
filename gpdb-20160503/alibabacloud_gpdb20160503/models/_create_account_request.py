# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccountRequest(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        account_type: str = None,
        dbinstance_id: str = None,
        database_name: str = None,
        owner_id: int = None,
    ):
        # The description of the initial account.
        self.account_description = account_description
        # The name of the initial account.
        # 
        # *   The name can contain lowercase letters, digits, and underscores (_).
        # *   The name must start with a lowercase letter and end with a lowercase letter or a digit.
        # *   The name cannot start with gp.
        # *   The name must be 2 to 16 characters in length.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the initial account.
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   Special characters include `! @ # $ % ^ & * ( ) _ + - =`
        # *   The password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.account_password = account_password
        # The type of the initial account. Default value: Super, which specifies a privileged account. To create a standard account, set the value to Normal.
        self.account_type = account_type
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database_name = database_name
        self.owner_id = owner_id

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

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

