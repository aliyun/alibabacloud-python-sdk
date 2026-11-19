# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class CreateAccountRequest(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        character_type: str = None,
        dbinstance_id: str = None,
        dbname: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        roles: List[main_models.CreateAccountRequestRoles] = None,
    ):
        # The account description.
        # 
        # - Regular expression: `^[a-zA-Z一-龥][a-zA-Z一-龥0-9_.-]{1,255}$`. The description must start with an English letter or Chinese character, followed by English letters, Chinese characters, digits, underscores (_), periods (.), or hyphens (-). The length must be 2 to 256 characters.
        # - If the description is invalid, InvalidAccountDescription.Malformed is returned.
        self.account_description = account_description
        # The account name.
        # - Regular expression: `^[a-z]+[a-z0-9|_]*[a-z0-9]+$`. The name must start with a lowercase letter, end with a lowercase letter or digit, and can contain lowercase letters, digits, and underscores (_). The length must be 2 to 16 characters.
        # - The reserved name `root` (case-insensitive, built-in system account) cannot be used.
        # - The name cannot start with `__cloud` (reserved prefix for system accounts).
        # - If the name is invalid, `InvalidAccountName.Malformed` is returned.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The account password.
        # - The length must be 8 to 32 characters. It can contain uppercase letters, lowercase letters, digits, and the following special characters: `!@#$%^&*()_+-=`.
        # - The password must contain at least **three** of the following four character types: uppercase letters, lowercase letters, digits, and special characters.
        # - If the password is invalid, `InvalidAccountPassword.Malformed` is returned.
        # 
        # 
        # > For information about how to handle special characters, see [How do I resolve the connection failure caused by special characters in the account name or password of a connection string?](https://help.aliyun.com/document_detail/471568.html)
        # 
        # This parameter is required.
        self.account_password = account_password
        # The account type.<br>Valid values:<br>- `normal`: replica set account. For a replica set instance, any value is processed as `normal`.<br>- `cs`: sharded cluster ConfigServer account.<br>- `db`: sharded cluster Shard direct connection account. For a sharded cluster instance, any value other than `cs` is processed as `db`.<br>Default value: `db`.
        self.character_type = character_type
        # The instance ID. For a sharded cluster instance, specify the sharded cluster ID. Account operations are executed from the perspective of the ConfigServer.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database to which the account belongs (authentication database).<br>
        # Default value: `admin`.<br>Rules: If this parameter is left empty, the request is allowed and the downstream system processes it as `admin`. If this parameter is specified, the length must be 1 to 63 characters. The value cannot contain `/`, `\\`, `.`, spaces, `"`, or `$`, and cannot be `local`. Otherwise, `InvalidParameter` is returned.
        self.dbname = dbname
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of authorization roles for the account. **Required for replica set and ConfigServer (cs) accounts**. **Prohibited for sharded cluster Shard direct connection (db) accounts**.
        # - **Globally prohibited** (returns `InvalidRoles.NotAllowed`): `root`, `clusterAdmin`, `hostManager`, `clusterManager`, `__system`, `__queryableBackup`, and `restore`.
        # - **Can be authorized to any database (including admin)**: `read`, `userAdmin`, and `enableSharding`.
        # - **Can only be authorized to non-admin databases** (returns `InvalidRoles.InvalidDB` if authorized to admin): `readWrite`, `dbAdmin`, and `dbOwner`.
        # - **Can only be authorized to the admin database**: `readAnyDatabase`, `readWriteAnyDatabase`, `userAdminAnyDatabase`, `dbAdminAnyDatabase`, `clusterMonitor`, `backup`, and `alibabaCloudAdmin`. (`alibabaCloudAdmin` is supported only for instances with kernel version 4.4 or later. For earlier versions, `InvalidRoles.NotAllowed` is returned.)
        # - **Custom roles**: Roles other than the preceding ones are considered custom roles and must already exist in the instance (you can query them by calling DescribeAccountRoles). Otherwise, `InvalidRoles.NotFound` is returned. `Roles.N.DBName` must be the same as the database where the role is defined. Otherwise, `InvalidRoles.DBNotMatch` is returned.
        # - If `Roles` is missing as a whole, `MissingRoles` is returned. If `Roles.N.Role` and `Roles.N.DBName` do not appear in pairs, `InvalidRoles.Malformed` is returned. If `Roles` is passed for a sharded cluster Shard direct connection account, `InvalidRoles.NotSupported` is returned.
        self.roles = roles

    def validate(self):
        if self.roles:
            for v1 in self.roles:
                 if v1:
                    v1.validate()

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

        if self.character_type is not None:
            result['CharacterType'] = self.character_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Roles'] = []
        if self.roles is not None:
            for k1 in self.roles:
                result['Roles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.roles = []
        if m.get('Roles') is not None:
            for k1 in m.get('Roles'):
                temp_model = main_models.CreateAccountRequestRoles()
                self.roles.append(temp_model.from_map(k1))

        return self



class CreateAccountRequestRoles(DaraModel):
    def __init__(
        self,
        dbname: str = None,
        role: str = None,
    ):
        # The database to which the account belongs (authentication database).<br>
        # Default value: `admin`.<br>Rules: If this parameter is left empty, the request is allowed and the downstream system processes it as `admin`. If this parameter is specified, the length must be 1 to 63 characters. The value cannot contain `/`, `\\`, `.`, spaces, `"`, or `$`, and cannot be `local`. Otherwise, `InvalidParameter` is returned.
        self.dbname = dbname
        # The role name. It can be a built-in role or a custom role created on the instance. For value rules, see [Roles parameter description](https://www.alibabacloud.com/help/en/mongodb/manage-database-accounts-through-the-console).
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

