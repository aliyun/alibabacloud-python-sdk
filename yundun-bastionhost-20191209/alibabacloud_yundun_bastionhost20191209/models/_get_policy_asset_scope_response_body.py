# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetPolicyAssetScopeResponseBody(DaraModel):
    def __init__(
        self,
        asset_scope: main_models.GetPolicyAssetScopeResponseBodyAssetScope = None,
        request_id: str = None,
    ):
        # The assets to which the control policy applies.
        self.asset_scope = asset_scope
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.asset_scope:
            self.asset_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_scope is not None:
            result['AssetScope'] = self.asset_scope.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetScope') is not None:
            temp_model = main_models.GetPolicyAssetScopeResponseBodyAssetScope()
            self.asset_scope = temp_model.from_map(m.get('AssetScope'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPolicyAssetScopeResponseBodyAssetScope(DaraModel):
    def __init__(
        self,
        databases: List[main_models.GetPolicyAssetScopeResponseBodyAssetScopeDatabases] = None,
        host_groups: List[main_models.GetPolicyAssetScopeResponseBodyAssetScopeHostGroups] = None,
        hosts: List[main_models.GetPolicyAssetScopeResponseBodyAssetScopeHosts] = None,
        scope_type: str = None,
    ):
        # The databases and database accounts to which the control policy applies.
        self.databases = databases
        # The asset groups and asset accounts to which the control policy applies.
        self.host_groups = host_groups
        # The hosts and host accounts to which the control policy applies.
        self.hosts = hosts
        # The scope of assets to which the control policy applies.
        # 
        # *   If **All** is returned for this parameter, the control policy applies to all assets.
        # 
        # *   If no value is returned for this parameter, the control policy applies to the assets specified in the return values of Databases, HostGroups, and Hosts.
        self.scope_type = scope_type

    def validate(self):
        if self.databases:
            for v1 in self.databases:
                 if v1:
                    v1.validate()
        if self.host_groups:
            for v1 in self.host_groups:
                 if v1:
                    v1.validate()
        if self.hosts:
            for v1 in self.hosts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Databases'] = []
        if self.databases is not None:
            for k1 in self.databases:
                result['Databases'].append(k1.to_map() if k1 else None)

        result['HostGroups'] = []
        if self.host_groups is not None:
            for k1 in self.host_groups:
                result['HostGroups'].append(k1.to_map() if k1 else None)

        result['Hosts'] = []
        if self.hosts is not None:
            for k1 in self.hosts:
                result['Hosts'].append(k1.to_map() if k1 else None)

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k1 in m.get('Databases'):
                temp_model = main_models.GetPolicyAssetScopeResponseBodyAssetScopeDatabases()
                self.databases.append(temp_model.from_map(k1))

        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k1 in m.get('HostGroups'):
                temp_model = main_models.GetPolicyAssetScopeResponseBodyAssetScopeHostGroups()
                self.host_groups.append(temp_model.from_map(k1))

        self.hosts = []
        if m.get('Hosts') is not None:
            for k1 in m.get('Hosts'):
                temp_model = main_models.GetPolicyAssetScopeResponseBodyAssetScopeHosts()
                self.hosts.append(temp_model.from_map(k1))

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        return self

class GetPolicyAssetScopeResponseBodyAssetScopeHosts(DaraModel):
    def __init__(
        self,
        account_scope_type: str = None,
        host_account_ids: List[str] = None,
        host_id: str = None,
    ):
        # The scope of host accounts to which the control policy applies. Valid values:
        # 
        # *   **All**: The control policy applies to all accounts of the host.
        # *   **AccountId**: The control policy applies to specified accounts of the host.
        self.account_scope_type = account_scope_type
        # The host accounts to which the control policy applies.
        self.host_account_ids = host_account_ids
        # The host ID.
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_scope_type is not None:
            result['AccountScopeType'] = self.account_scope_type

        if self.host_account_ids is not None:
            result['HostAccountIds'] = self.host_account_ids

        if self.host_id is not None:
            result['HostId'] = self.host_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScopeType') is not None:
            self.account_scope_type = m.get('AccountScopeType')

        if m.get('HostAccountIds') is not None:
            self.host_account_ids = m.get('HostAccountIds')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        return self

class GetPolicyAssetScopeResponseBodyAssetScopeHostGroups(DaraModel):
    def __init__(
        self,
        account_names: List[str] = None,
        account_scope_type: str = None,
        host_group_id: str = None,
    ):
        # The asset accounts to which the control policy applies.
        self.account_names = account_names
        # The scope of asset accounts to which the control policy applies. Valid values:
        # 
        # *   **All**: The control policy applies to all accounts in the asset group.
        # *   **AccountName**: The control policy applies to specified accounts in the asset group.
        self.account_scope_type = account_scope_type
        # The asset group ID.
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_names is not None:
            result['AccountNames'] = self.account_names

        if self.account_scope_type is not None:
            result['AccountScopeType'] = self.account_scope_type

        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNames') is not None:
            self.account_names = m.get('AccountNames')

        if m.get('AccountScopeType') is not None:
            self.account_scope_type = m.get('AccountScopeType')

        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')

        return self

class GetPolicyAssetScopeResponseBodyAssetScopeDatabases(DaraModel):
    def __init__(
        self,
        account_scope_type: str = None,
        database_account_ids: List[str] = None,
        database_id: str = None,
    ):
        # The scope of database accounts to which the control policy applies. Valid values:
        # 
        # *   **All**: The control policy applies to all database accounts of the database.
        # *   **AccountId**: The control policy applies to specified database accounts of the database.
        self.account_scope_type = account_scope_type
        # The IDs of database accounts to which the control policy applies.
        self.database_account_ids = database_account_ids
        # The database ID.
        self.database_id = database_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_scope_type is not None:
            result['AccountScopeType'] = self.account_scope_type

        if self.database_account_ids is not None:
            result['DatabaseAccountIds'] = self.database_account_ids

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScopeType') is not None:
            self.account_scope_type = m.get('AccountScopeType')

        if m.get('DatabaseAccountIds') is not None:
            self.database_account_ids = m.get('DatabaseAccountIds')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        return self

