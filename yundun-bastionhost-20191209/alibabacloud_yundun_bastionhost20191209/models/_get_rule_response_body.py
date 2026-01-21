# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule: main_models.GetRuleResponseBodyRule = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned information about the authorization rule.
        self.rule = rule

    def validate(self):
        if self.rule:
            self.rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule is not None:
            result['Rule'] = self.rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rule') is not None:
            temp_model = main_models.GetRuleResponseBodyRule()
            self.rule = temp_model.from_map(m.get('Rule'))

        return self

class GetRuleResponseBodyRule(DaraModel):
    def __init__(
        self,
        comment: str = None,
        databases: List[main_models.GetRuleResponseBodyRuleDatabases] = None,
        effective_end_time: str = None,
        effective_start_time: str = None,
        host_groups: List[main_models.GetRuleResponseBodyRuleHostGroups] = None,
        hosts: List[main_models.GetRuleResponseBodyRuleHosts] = None,
        rule_id: str = None,
        rule_name: str = None,
        user_groups: List[main_models.GetRuleResponseBodyRuleUserGroups] = None,
        users: List[main_models.GetRuleResponseBodyRuleUsers] = None,
    ):
        # The remarks of the authorization rule.
        self.comment = comment
        # The databases on which permissions are granted by using the authorization rule.
        self.databases = databases
        # The end time of the validity period of the authorization rule. The value is a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time
        # The start time of the validity period of the authorization rule. The value is a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time
        # The asset groups on which permissions are granted by using the authorization rule.
        self.host_groups = host_groups
        # The information about the hosts that the policy authorizes users to manage.
        self.hosts = hosts
        # The ID of the authorization rule.
        self.rule_id = rule_id
        # The name of the authorization rule.
        self.rule_name = rule_name
        # The authorized user groups.
        self.user_groups = user_groups
        # The authorized users.
        self.users = users

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
        if self.user_groups:
            for v1 in self.user_groups:
                 if v1:
                    v1.validate()
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        result['Databases'] = []
        if self.databases is not None:
            for k1 in self.databases:
                result['Databases'].append(k1.to_map() if k1 else None)

        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time

        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time

        result['HostGroups'] = []
        if self.host_groups is not None:
            for k1 in self.host_groups:
                result['HostGroups'].append(k1.to_map() if k1 else None)

        result['Hosts'] = []
        if self.hosts is not None:
            for k1 in self.hosts:
                result['Hosts'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        result['UserGroups'] = []
        if self.user_groups is not None:
            for k1 in self.user_groups:
                result['UserGroups'].append(k1.to_map() if k1 else None)

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        self.databases = []
        if m.get('Databases') is not None:
            for k1 in m.get('Databases'):
                temp_model = main_models.GetRuleResponseBodyRuleDatabases()
                self.databases.append(temp_model.from_map(k1))

        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')

        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')

        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k1 in m.get('HostGroups'):
                temp_model = main_models.GetRuleResponseBodyRuleHostGroups()
                self.host_groups.append(temp_model.from_map(k1))

        self.hosts = []
        if m.get('Hosts') is not None:
            for k1 in m.get('Hosts'):
                temp_model = main_models.GetRuleResponseBodyRuleHosts()
                self.hosts.append(temp_model.from_map(k1))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k1 in m.get('UserGroups'):
                temp_model = main_models.GetRuleResponseBodyRuleUserGroups()
                self.user_groups.append(temp_model.from_map(k1))

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.GetRuleResponseBodyRuleUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class GetRuleResponseBodyRuleUsers(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The ID of the authorized user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetRuleResponseBodyRuleUserGroups(DaraModel):
    def __init__(
        self,
        user_group_id: str = None,
    ):
        # The ID of the authorized user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

class GetRuleResponseBodyRuleHosts(DaraModel):
    def __init__(
        self,
        host_accounts: List[main_models.GetRuleResponseBodyRuleHostsHostAccounts] = None,
        host_id: str = None,
    ):
        # The host accounts that the policy authorizes users to manage.
        self.host_accounts = host_accounts
        # The ID of the host that the policy authorizes users to manage.
        self.host_id = host_id

    def validate(self):
        if self.host_accounts:
            for v1 in self.host_accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k1 in self.host_accounts:
                result['HostAccounts'].append(k1.to_map() if k1 else None)

        if self.host_id is not None:
            result['HostId'] = self.host_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k1 in m.get('HostAccounts'):
                temp_model = main_models.GetRuleResponseBodyRuleHostsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k1))

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        return self

class GetRuleResponseBodyRuleHostsHostAccounts(DaraModel):
    def __init__(
        self,
        host_account_id: str = None,
    ):
        # The ID of the host account that the policy authorizes users to manage.
        self.host_account_id = host_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')

        return self

class GetRuleResponseBodyRuleHostGroups(DaraModel):
    def __init__(
        self,
        host_account_names: List[str] = None,
        host_group_id: str = None,
    ):
        # The asset accounts on which permissions are granted by using the authorization rule.
        self.host_account_names = host_account_names
        # The ID of the asset group that the policy authorizes users to manage.
        self.host_group_id = host_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_account_names is not None:
            result['HostAccountNames'] = self.host_account_names

        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountNames') is not None:
            self.host_account_names = m.get('HostAccountNames')

        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')

        return self

class GetRuleResponseBodyRuleDatabases(DaraModel):
    def __init__(
        self,
        database_accounts: List[main_models.GetRuleResponseBodyRuleDatabasesDatabaseAccounts] = None,
        database_id: str = None,
    ):
        # The database accounts on which permissions are granted by using the authorization rule.
        self.database_accounts = database_accounts
        # The ID of the database that the policy authorizes users to manage.
        self.database_id = database_id

    def validate(self):
        if self.database_accounts:
            for v1 in self.database_accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k1 in self.database_accounts:
                result['DatabaseAccounts'].append(k1.to_map() if k1 else None)

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k1 in m.get('DatabaseAccounts'):
                temp_model = main_models.GetRuleResponseBodyRuleDatabasesDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k1))

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        return self

class GetRuleResponseBodyRuleDatabasesDatabaseAccounts(DaraModel):
    def __init__(
        self,
        database_account_id: str = None,
    ):
        # The ID of the database account that the policy authorizes users to manage.
        self.database_account_id = database_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')

        return self

