# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ModifyRuleRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        databases: List[main_models.ModifyRuleRequestDatabases] = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        host_groups: List[main_models.ModifyRuleRequestHostGroups] = None,
        hosts: List[main_models.ModifyRuleRequestHosts] = None,
        instance_id: str = None,
        region_id: str = None,
        rule_id: str = None,
        rule_name: str = None,
        user_group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # The new remarks of the authorization rule. It can be up to 500 characters in length.
        self.comment = comment
        # The databases and database accounts that a user associated with the modified rule can manage.
        self.databases = databases
        # The end time of the new validity period of the authorization rule. The value is a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time
        # The start time of the new validity period of the authorization rule. The value is a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time
        # The asset groups and asset accounts that a user associated with the modified rule can manage.
        self.host_groups = host_groups
        # An array that consists of the host IDs and host account IDs with which the modified authorization rule is associated.
        self.hosts = hosts
        # The ID of the bastion host whose authorization rule you want to modify.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the bastion host to which the authorization rule to modify belongs.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the authorization rule to modify.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The new name of the authorization rule. The name must be 1 to 128 characters in length and can contain periods (.), underscores (_), hyphens (-), single quotation marks (\\"), and spaces. It cannot start with a special character.
        self.rule_name = rule_name
        # The IDs of the user groups with which the modified authorization rule is associated.
        self.user_group_ids = user_group_ids
        # The IDs of the users with whom the modified authorization rule is associated.
        self.user_ids = user_ids

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        self.databases = []
        if m.get('Databases') is not None:
            for k1 in m.get('Databases'):
                temp_model = main_models.ModifyRuleRequestDatabases()
                self.databases.append(temp_model.from_map(k1))

        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')

        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')

        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k1 in m.get('HostGroups'):
                temp_model = main_models.ModifyRuleRequestHostGroups()
                self.host_groups.append(temp_model.from_map(k1))

        self.hosts = []
        if m.get('Hosts') is not None:
            for k1 in m.get('Hosts'):
                temp_model = main_models.ModifyRuleRequestHosts()
                self.hosts.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

class ModifyRuleRequestHosts(DaraModel):
    def __init__(
        self,
        host_account_ids: List[str] = None,
        host_id: str = None,
    ):
        # The host account IDs.
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
        if self.host_account_ids is not None:
            result['HostAccountIds'] = self.host_account_ids

        if self.host_id is not None:
            result['HostId'] = self.host_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountIds') is not None:
            self.host_account_ids = m.get('HostAccountIds')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        return self

class ModifyRuleRequestHostGroups(DaraModel):
    def __init__(
        self,
        host_account_names: List[str] = None,
        host_group_id: str = None,
    ):
        # The names of the asset accounts.
        self.host_account_names = host_account_names
        # The asset group ID.
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

class ModifyRuleRequestDatabases(DaraModel):
    def __init__(
        self,
        database_account_ids: List[str] = None,
        database_id: str = None,
    ):
        # The database account IDs.
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
        if self.database_account_ids is not None:
            result['DatabaseAccountIds'] = self.database_account_ids

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountIds') is not None:
            self.database_account_ids = m.get('DatabaseAccountIds')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        return self

