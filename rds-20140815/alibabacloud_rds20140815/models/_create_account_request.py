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
        # The description of the account. The value must be 2 to 256 characters in length. The value can contain letters, digits, underscores (_), and hyphens (-), and must start with a letter.
        # 
        # > : The name cannot start with http:// or https://.
        self.account_description = account_description
        # The name of the database account.
        # 
        # 
        # *   The name must be unique.
        # 
        # *   The name can contain lowercase letters, digits, and underscores (_). For MySQL databases, the name can contain uppercase letters.
        # 
        # *   The name must start with a letter and end with a letter or digit.
        # 
        # *   For MySQL databases, the name of the privileged account cannot be the same as that of the standard account. For example, if the name of the privileged account is `Test1`, the name of the standard account cannot be `test1`.
        # 
        # *   The length of the value must meet the following requirements:
        # 
        #     *   If the instance runs MySQL 5.7 or MySQL 8.0, the value must be 2 to 32 characters in length.
        #     *   If the instance runs MySQL 5.6, the value must be 2 to 16 characters in length.
        #     *   If the instance runs SQL Server, the value must be 2 to 64 characters in length.
        #     *   If the instance runs PostgreSQL with cloud disks, the value must be 2 to 63 characters in length.
        #     *   If the instance runs PostgreSQL with local disks, the value must be 2 to 16 characters in length.
        #     *   If the instance runs MariaDB, the value must be 2 to 16 characters in length.
        # 
        # *   For more information about invalid characters, see [Forbidden keywords](https://help.aliyun.com/document_detail/26317.html).
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the account.
        #  
        # 
        # *   The value must be 8 to 32 characters in length.
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # 
        # *   Special characters include `! @ # $ % ^ & * ( ) _ + - =`
        # 
        # This parameter is required.
        self.account_password = account_password
        # The account type. Valid values:
        # 
        # *   **Normal** (default): standard account.
        # *   **Super**: privileged account.
        # *   **Sysadmin**: system admin account. The account type is available only for ApsaraDB RDS for SQL Server instances.
        # 
        # Before you create a system admin account, check whether the instance meets all prerequisites. For more information, see [Create a system admin account](https://help.aliyun.com/document_detail/170736.html).
        self.account_type = account_type
        # Specifies whether to use a password policy.
        # 
        # > 
        # 
        # *   This parameter is available only for ApsaraDB RDS for SQL Server instances that do not belong to the shared instance family and do not run SQL Server 2008 R2.
        # 
        # *   Before you call this operation, you must configure a password policy for the account of your instance. For more information, see [Configure a password policy for the account of an ApsaraDB RDS for SQL Server instance](https://help.aliyun.com/document_detail/2848317.html).
        self.check_policy = check_policy
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
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

