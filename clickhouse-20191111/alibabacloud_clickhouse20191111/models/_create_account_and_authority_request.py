# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccountAndAuthorityRequest(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        allow_databases: str = None,
        allow_dictionaries: str = None,
        dbcluster_id: str = None,
        ddl_authority: bool = None,
        dml_authority: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        total_databases: str = None,
        total_dictionaries: str = None,
    ):
        # The description of the database account.
        # 
        # - Cannot start with `http://` or `https://`.
        # 
        # - Must be 0 to 256 characters in length.
        self.account_description = account_description
        # The name of the database account.
        # 
        # - Must be unique within the cluster.
        # 
        # - Can contain only lowercase letters, digits, and underscores (_).
        # 
        # - Must start with a lowercase letter and end with a lowercase letter or a digit.
        # 
        # - Must be 2 to 64 characters in length.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password for the database account.
        # 
        # > - Must contain characters from at least three of the following types: uppercase letters, lowercase letters, digits, and special characters.
        # 
        # - The supported special characters are `!@#$%^&*()_+-=`.
        # 
        # - Must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.account_password = account_password
        # The databases to which the account has permissions. Separate multiple database names with commas (,).
        # 
        # This parameter is required.
        self.allow_databases = allow_databases
        # The dictionaries to which the account has permissions. Separate multiple dictionary names with commas (,).
        # 
        # This parameter is required.
        self.allow_dictionaries = allow_dictionaries
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to grant DDL permissions to the database account. Valid values:
        # 
        # - **true**: DDL operations are allowed.
        # 
        # - **false**: DDL operations are denied.
        # 
        # This parameter is required.
        self.ddl_authority = ddl_authority
        # Specifies the DML permissions for the database account. Valid values:
        # 
        # - **all**: read, write, and settings permissions.
        # 
        # - **readOnly,modify**: read and settings permissions.
        # 
        # This parameter is required.
        self.dml_authority = dml_authority
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/170875.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # All databases in the cluster. Separate multiple database names with commas (,).
        self.total_databases = total_databases
        # All dictionaries in the cluster. Separate multiple dictionary names with commas (,).
        self.total_dictionaries = total_dictionaries

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

        if self.allow_databases is not None:
            result['AllowDatabases'] = self.allow_databases

        if self.allow_dictionaries is not None:
            result['AllowDictionaries'] = self.allow_dictionaries

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.ddl_authority is not None:
            result['DdlAuthority'] = self.ddl_authority

        if self.dml_authority is not None:
            result['DmlAuthority'] = self.dml_authority

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.total_databases is not None:
            result['TotalDatabases'] = self.total_databases

        if self.total_dictionaries is not None:
            result['TotalDictionaries'] = self.total_dictionaries

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('AllowDatabases') is not None:
            self.allow_databases = m.get('AllowDatabases')

        if m.get('AllowDictionaries') is not None:
            self.allow_dictionaries = m.get('AllowDictionaries')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DdlAuthority') is not None:
            self.ddl_authority = m.get('DdlAuthority')

        if m.get('DmlAuthority') is not None:
            self.dml_authority = m.get('DmlAuthority')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TotalDatabases') is not None:
            self.total_databases = m.get('TotalDatabases')

        if m.get('TotalDictionaries') is not None:
            self.total_dictionaries = m.get('TotalDictionaries')

        return self

