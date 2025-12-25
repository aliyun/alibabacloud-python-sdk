# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountsResponseBody(DaraModel):
    def __init__(
        self,
        accounts: main_models.DescribeAccountsResponseBodyAccounts = None,
        page_number: int = None,
        request_id: str = None,
        resource_group_id: str = None,
        system_admin_account_first_activation_time: str = None,
        system_admin_account_status: str = None,
        total_record_count: int = None,
    ):
        # The information about the account.
        self.accounts = accounts
        # The page number.
        self.page_number = page_number
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The first time when the system admin account was enabled. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # >  This parameter is returned only for instances that run SQL Server.
        self.system_admin_account_first_activation_time = system_admin_account_first_activation_time
        # Indicates whether the system admin account was enabled. Valid values:
        # 
        # *   **true**: The system admin account was enabled.
        # *   **false**: The system admin account was disabled.
        # 
        # >  The [system admin account](https://help.aliyun.com/document_detail/170736.html) is supported only for the instances that run SQL Server. If the instance runs SQL Server, a value is returned for this parameter. If the instance runs a different database engine, no value is returned for this parameter.
        self.system_admin_account_status = system_admin_account_status
        # The total number of entries that are returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.system_admin_account_first_activation_time is not None:
            result['SystemAdminAccountFirstActivationTime'] = self.system_admin_account_first_activation_time

        if self.system_admin_account_status is not None:
            result['SystemAdminAccountStatus'] = self.system_admin_account_status

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m.get('Accounts'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SystemAdminAccountFirstActivationTime') is not None:
            self.system_admin_account_first_activation_time = m.get('SystemAdminAccountFirstActivationTime')

        if m.get('SystemAdminAccountStatus') is not None:
            self.system_admin_account_status = m.get('SystemAdminAccountStatus')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeAccountsResponseBodyAccounts(DaraModel):
    def __init__(
        self,
        dbinstance_account: List[main_models.DescribeAccountsResponseBodyAccountsDBInstanceAccount] = None,
    ):
        self.dbinstance_account = dbinstance_account

    def validate(self):
        if self.dbinstance_account:
            for v1 in self.dbinstance_account:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceAccount'] = []
        if self.dbinstance_account is not None:
            for k1 in self.dbinstance_account:
                result['DBInstanceAccount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_account = []
        if m.get('DBInstanceAccount') is not None:
            for k1 in m.get('DBInstanceAccount'):
                temp_model = main_models.DescribeAccountsResponseBodyAccountsDBInstanceAccount()
                self.dbinstance_account.append(temp_model.from_map(k1))

        return self

class DescribeAccountsResponseBodyAccountsDBInstanceAccount(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_status: str = None,
        account_type: str = None,
        bypass_rls: str = None,
        check_policy: bool = None,
        create_db: str = None,
        create_role: str = None,
        dbinstance_id: str = None,
        database_privileges: main_models.DescribeAccountsResponseBodyAccountsDBInstanceAccountDatabasePrivileges = None,
        password_expire_time: str = None,
        priv_exceeded: str = None,
        replication: str = None,
        valid_until: str = None,
    ):
        # The description of the account.
        self.account_description = account_description
        # The name of the database account.
        self.account_name = account_name
        # The status of the account. Valid values:
        # 
        # *   **Unavailable**
        # *   **Available**
        self.account_status = account_status
        # The type of the account. Valid values:
        # 
        # *   **Normal**: standard account
        # *   **Super**: privileged account
        # *   **Sysadmin**: system admin account, which is supported only for instances running SQL Server
        self.account_type = account_type
        # Indicates whether the account has the row-level security (RLS) permissions. Valid values:
        # 
        # *   **t**: The account has the RLS permissions.
        # *   **f**: The account does not have the RLS permissions.
        # 
        # >  This parameter is returned only for instances that run PostgreSQL.
        self.bypass_rls = bypass_rls
        # Indicates whether the password policy is applied.
        # 
        # >  This parameter is returned only for instances that run SQL Server.
        self.check_policy = check_policy
        # Indicates whether the account has the permissions to create databases. Valid values:
        # 
        # *   **t**: The account has the permissions to create databases.
        # *   **f**: The account does not have the permissions to create databases.
        # 
        # >  This parameter is returned only for instances that run PostgreSQL.
        self.create_db = create_db
        # Indicates whether the account has the permissions to create roles. Valid values:
        # 
        # *   **t**: The account has the permissions to create roles.
        # *   **f**: The account does not have the permissions to create roles.
        # 
        # >  This parameter is returned only for instances that run PostgreSQL.
        self.create_role = create_role
        # The ID of the instance to which the account belongs.
        self.dbinstance_id = dbinstance_id
        # The details about the permissions that are granted to the account.
        self.database_privileges = database_privileges
        # The expiration time of the password.
        # 
        # >  This parameter is returned only for instances that run SQL Server.
        self.password_expire_time = password_expire_time
        # Indicates whether the number of databases that are managed by the account exceeds the upper limit. Valid values:
        # 
        # *   **1**: The number of databases that are managed by the account exceeds the upper limit.
        # *   **0**: The number of databases that are managed by the account does not exceed the upper limit.
        self.priv_exceeded = priv_exceeded
        # Indicates whether the account has the replication permissions. Valid values:
        # 
        # *   **t**: The account has the replication permissions.
        # *   **f**: The account does not have the replication permissions.
        # 
        # >  This parameter is returned only for instances that run PostgreSQL.
        self.replication = replication
        # The expiration time of the password. Valid values:
        # 
        # *   **infinity**: The password never expires.
        # *   **Empty**: The expiration time is not specified.
        # *   **Actual expiration time**: in the format of *yyyy-MM-dd*T*HH:mm:ss*Z in UTC. Example: 2022-10-01T00:00:00Z.
        # 
        # >  This parameter is returned only for instances that run PostgreSQL.
        self.valid_until = valid_until

    def validate(self):
        if self.database_privileges:
            self.database_privileges.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.bypass_rls is not None:
            result['BypassRLS'] = self.bypass_rls

        if self.check_policy is not None:
            result['CheckPolicy'] = self.check_policy

        if self.create_db is not None:
            result['CreateDB'] = self.create_db

        if self.create_role is not None:
            result['CreateRole'] = self.create_role

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.database_privileges is not None:
            result['DatabasePrivileges'] = self.database_privileges.to_map()

        if self.password_expire_time is not None:
            result['PasswordExpireTime'] = self.password_expire_time

        if self.priv_exceeded is not None:
            result['PrivExceeded'] = self.priv_exceeded

        if self.replication is not None:
            result['Replication'] = self.replication

        if self.valid_until is not None:
            result['ValidUntil'] = self.valid_until

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('BypassRLS') is not None:
            self.bypass_rls = m.get('BypassRLS')

        if m.get('CheckPolicy') is not None:
            self.check_policy = m.get('CheckPolicy')

        if m.get('CreateDB') is not None:
            self.create_db = m.get('CreateDB')

        if m.get('CreateRole') is not None:
            self.create_role = m.get('CreateRole')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DatabasePrivileges') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccountsDBInstanceAccountDatabasePrivileges()
            self.database_privileges = temp_model.from_map(m.get('DatabasePrivileges'))

        if m.get('PasswordExpireTime') is not None:
            self.password_expire_time = m.get('PasswordExpireTime')

        if m.get('PrivExceeded') is not None:
            self.priv_exceeded = m.get('PrivExceeded')

        if m.get('Replication') is not None:
            self.replication = m.get('Replication')

        if m.get('ValidUntil') is not None:
            self.valid_until = m.get('ValidUntil')

        return self

class DescribeAccountsResponseBodyAccountsDBInstanceAccountDatabasePrivileges(DaraModel):
    def __init__(
        self,
        database_privilege: List[main_models.DescribeAccountsResponseBodyAccountsDBInstanceAccountDatabasePrivilegesDatabasePrivilege] = None,
    ):
        self.database_privilege = database_privilege

    def validate(self):
        if self.database_privilege:
            for v1 in self.database_privilege:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatabasePrivilege'] = []
        if self.database_privilege is not None:
            for k1 in self.database_privilege:
                result['DatabasePrivilege'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_privilege = []
        if m.get('DatabasePrivilege') is not None:
            for k1 in m.get('DatabasePrivilege'):
                temp_model = main_models.DescribeAccountsResponseBodyAccountsDBInstanceAccountDatabasePrivilegesDatabasePrivilege()
                self.database_privilege.append(temp_model.from_map(k1))

        return self

class DescribeAccountsResponseBodyAccountsDBInstanceAccountDatabasePrivilegesDatabasePrivilege(DaraModel):
    def __init__(
        self,
        account_privilege: str = None,
        account_privilege_detail: str = None,
        dbname: str = None,
    ):
        # The type of the permissions. Valid values:
        # 
        # *   **ReadWrite**: read and write permissions.
        # *   **ReadOnly**: read-only permissions.
        # *   **DDLOnly**: DDL-only permissions.
        # *   **DMLOnly**: DML-only permissions.
        # *   **Custom**: custom permissions. You can modify the permissions of the account by using SQL commands.
        self.account_privilege = account_privilege
        # The permissions that are granted to the account. For more information, see [Account permissions](https://help.aliyun.com/document_detail/146395.html).
        self.account_privilege_detail = account_privilege_detail
        # The name of the database.
        self.dbname = dbname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege

        if self.account_privilege_detail is not None:
            result['AccountPrivilegeDetail'] = self.account_privilege_detail

        if self.dbname is not None:
            result['DBName'] = self.dbname

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('AccountPrivilegeDetail') is not None:
            self.account_privilege_detail = m.get('AccountPrivilegeDetail')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        return self

