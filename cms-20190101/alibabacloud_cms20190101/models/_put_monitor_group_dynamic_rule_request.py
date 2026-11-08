# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutMonitorGroupDynamicRuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        group_id: int = None,
        group_rules: List[main_models.PutMonitorGroupDynamicRuleRequestGroupRules] = None,
        is_async: bool = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        # Specifies whether to only precheck this request. Valid values:
        # - **true**: sends a check request. No security group is associated with the instance. The check items include whether required parameters are specified, the request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # - **false** (default): sends a normal request. If the check succeeds, an HTTP 2xx status code is returned and the operation is directly performed.
        self.dry_run = dry_run
        # The ID of the application group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # None.
        # 
        # This parameter is required.
        self.group_rules = group_rules
        # The mode for creating the dynamic matching rule. Valid values:
        # 
        # - true: Asynchronous creation.
        # - false (default): Synchronous creation.
        self.is_async = is_async
        self.region_id = region_id

    def validate(self):
        if self.group_rules:
            for v1 in self.group_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        result['GroupRules'] = []
        if self.group_rules is not None:
            for k1 in self.group_rules:
                result['GroupRules'].append(k1.to_map() if k1 else None)

        if self.is_async is not None:
            result['IsAsync'] = self.is_async

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        self.group_rules = []
        if m.get('GroupRules') is not None:
            for k1 in m.get('GroupRules'):
                temp_model = main_models.PutMonitorGroupDynamicRuleRequestGroupRules()
                self.group_rules.append(temp_model.from_map(k1))

        if m.get('IsAsync') is not None:
            self.is_async = m.get('IsAsync')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class PutMonitorGroupDynamicRuleRequestGroupRules(DaraModel):
    def __init__(
        self,
        category: str = None,
        filter_relation: str = None,
        filters: List[main_models.PutMonitorGroupDynamicRuleRequestGroupRulesFilters] = None,
    ):
        # The type of Alibaba Cloud service for the dynamic alert rule. Valid values of N: 1 to 3. Valid values:
        # 
        # - ecs: Elastic Compute Service (ECS) server.
        # 
        # - rds: relational database.
        # 
        # - slb: load balancing.
        # 
        # This parameter is required.
        self.category = category
        # The combination condition for dynamic matching rules. Valid values of N: 1 to 3. Valid values:
        # 
        # - and: Only instances that meet all matching rules are automatically added to the application group.
        # 
        # - or: Instances that meet any matching rule are automatically added to the application group.
        # 
        # This parameter is required.
        self.filter_relation = filter_relation
        # None.
        # 
        # This parameter is required.
        self.filters = filters

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.filter_relation is not None:
            result['FilterRelation'] = self.filter_relation

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('FilterRelation') is not None:
            self.filter_relation = m.get('FilterRelation')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.PutMonitorGroupDynamicRuleRequestGroupRulesFilters()
                self.filters.append(temp_model.from_map(k1))

        return self

class PutMonitorGroupDynamicRuleRequestGroupRulesFilters(DaraModel):
    def __init__(
        self,
        function: str = None,
        name: str = None,
        value: str = None,
    ):
        # The filter condition for instances. Valid values of N: 1 to 3. Valid values:
        # - contains: Contains.
        # - notContains: Does not contain.
        # - startWith: Prefix.
        # - endWith: Suffix.
        # 
        # This parameter is required.
        self.function = function
        # The field name for instance matching. Valid values of N: 1 to 3.
        # 
        # Currently, only the hostname is supported, such as hostName.
        # 
        # This parameter is required.
        self.name = name
        # The value that meets the matching condition. Valid values of N: 1 to 3.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

