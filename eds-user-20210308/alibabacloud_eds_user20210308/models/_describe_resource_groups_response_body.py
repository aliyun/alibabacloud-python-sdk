# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: List[main_models.DescribeResourceGroupsResponseBodyResourceGroup] = None,
        total_count: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The resource groups.
        self.resource_group = resource_group
        # The total number of resource groups.
        self.total_count = total_count

    def validate(self):
        if self.resource_group:
            for v1 in self.resource_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceGroup'] = []
        if self.resource_group is not None:
            for k1 in self.resource_group:
                result['ResourceGroup'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_group = []
        if m.get('ResourceGroup') is not None:
            for k1 in m.get('ResourceGroup'):
                temp_model = main_models.DescribeResourceGroupsResponseBodyResourceGroup()
                self.resource_group.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeResourceGroupsResponseBodyResourceGroup(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        app_rules: List[main_models.DescribeResourceGroupsResponseBodyResourceGroupAppRules] = None,
        auth_count: str = None,
        create_time: str = None,
        policies: List[main_models.DescribeResourceGroupsResponseBodyResourceGroupPolicies] = None,
        resource_count: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        timers: List[main_models.DescribeResourceGroupsResponseBodyResourceGroupTimers] = None,
    ):
        self.aliyun_resource_group_id = aliyun_resource_group_id
        self.app_rules = app_rules
        # The number of administrators that are authorized to access the resource group.
        self.auth_count = auth_count
        # The time when the resource group was created.
        self.create_time = create_time
        # >  The policy that is associated with the resource group.
        # 
        # *   The policy applies to cloud computers in the resource group. If multiple policies exist, they are enforced in order of priority.
        # 
        # *   If any of these cloud computers are already associated with other policies, the resource group\\"s policy takes precedence.
        self.policies = policies
        # The number of resources in the resource group.
        self.resource_count = resource_count
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The name of the resource group.
        self.resource_group_name = resource_group_name
        # >  The associated scheduled task.
        # 
        # *   The scheduled task applies to all cloud computers in the resource group. If any of these cloud computers are already associated with other scheduled tasks, the resource group\\"s scheduled task takes precedence.
        self.timers = timers

    def validate(self):
        if self.app_rules:
            for v1 in self.app_rules:
                 if v1:
                    v1.validate()
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()
        if self.timers:
            for v1 in self.timers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id

        result['AppRules'] = []
        if self.app_rules is not None:
            for k1 in self.app_rules:
                result['AppRules'].append(k1.to_map() if k1 else None)

        if self.auth_count is not None:
            result['AuthCount'] = self.auth_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        result['Timers'] = []
        if self.timers is not None:
            for k1 in self.timers:
                result['Timers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')

        self.app_rules = []
        if m.get('AppRules') is not None:
            for k1 in m.get('AppRules'):
                temp_model = main_models.DescribeResourceGroupsResponseBodyResourceGroupAppRules()
                self.app_rules.append(temp_model.from_map(k1))

        if m.get('AuthCount') is not None:
            self.auth_count = m.get('AuthCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribeResourceGroupsResponseBodyResourceGroupPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        self.timers = []
        if m.get('Timers') is not None:
            for k1 in m.get('Timers'):
                temp_model = main_models.DescribeResourceGroupsResponseBodyResourceGroupTimers()
                self.timers.append(temp_model.from_map(k1))

        return self

class DescribeResourceGroupsResponseBodyResourceGroupTimers(DaraModel):
    def __init__(
        self,
        bind_status: str = None,
        id: str = None,
        name: str = None,
        timer_status: str = None,
    ):
        self.bind_status = bind_status
        # The ID of the scheduled task.
        self.id = id
        # The name of the scheduled task.
        self.name = name
        self.timer_status = timer_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_status is not None:
            result['BindStatus'] = self.bind_status

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.timer_status is not None:
            result['TimerStatus'] = self.timer_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindStatus') is not None:
            self.bind_status = m.get('BindStatus')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TimerStatus') is not None:
            self.timer_status = m.get('TimerStatus')

        return self

class DescribeResourceGroupsResponseBodyResourceGroupPolicies(DaraModel):
    def __init__(
        self,
        id: str = None,
        is_default: bool = None,
        name: str = None,
    ):
        # The policy ID.
        self.id = id
        # Specifies whether to use the default policy.
        self.is_default = is_default
        # The policy name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeResourceGroupsResponseBodyResourceGroupAppRules(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: int = None,
    ):
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

