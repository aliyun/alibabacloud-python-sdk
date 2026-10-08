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
        check_policy: bool = None,
        dbinstance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The description of the account. The description must be 2 to 256 characters in length. It must start with a letter or a Chinese character and can contain digits, Chinese characters, letters, underscores (_), and hyphens (-).
        # >The description cannot start with `http://` or `https://`.
        self.account_description = account_description
        # The name of the database account.
        # 
        # > The name must be unique and can contain uppercase letters (supported only by MySQL), lowercase letters, digits, or underscores. For specific naming conventions, refer to the tutorials for each engine: [Create a MySQL account](https://help.aliyun.com/document_detail/96089.html), [Create a PostgreSQL account](https://help.aliyun.com/document_detail/96753.html), [Create a SQL Server account](https://help.aliyun.com/document_detail/95810.html), [Create a MariaDB account](https://help.aliyun.com/document_detail/97132.html).
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the database account.
        # > * The password must be 8 to 32 characters in length.
        # > * The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters (`!@#$%^&*()_+-=`).
        # 
        # This parameter is required.
        self.account_password = account_password
        # The type of the account. Valid values:
        # 
        # - **Normal** (default): standard account.
        # - **Super**: privileged account. You can create at most one privileged account per instance.
        # - **Sysadmin** (SQL Server instances only): database account with SA permissions. Before you create this account, check whether the instance meets the [prerequisites](https://help.aliyun.com/document_detail/170736.html).
        # - **GlobalRO** (SQL Server instances only): global read-only account. You can create at most two global read-only accounts per instance. The database engine version of the instance must be SQL Server 2016 or later, and the instance type must be dedicated or general-purpose.
        self.account_type = account_type
        # The [account password policy](https://help.aliyun.com/document_detail/2845728.html) for the SQL Server instance. Valid values:
        # - **true**: The policy is applied.
        # - **false**: The policy is not applied.
        # > - If you set this parameter to true, you must first [configure the SQL Server account password policy](https://help.aliyun.com/document_detail/2848317.html).
        # > - This parameter does not support SQL Server instances of the [shared instance type](https://help.aliyun.com/document_detail/57184.html), [2008 R2 edition](https://help.aliyun.com/document_detail/145468.html), or [serverless type](https://help.aliyun.com/document_detail/603466.html).
        self.check_policy = check_policy
        # The instance ID. You can call [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

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

        if self.check_policy is not None:
            result['CheckPolicy'] = self.check_policy

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if m.get('CheckPolicy') is not None:
            self.check_policy = m.get('CheckPolicy')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

