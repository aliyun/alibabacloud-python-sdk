# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class ListEgressProxyRuleGroupsResponseBody(DaraModel):
    def __init__(
        self,
        egress_proxy_rule_groups: List[main_models.ListEgressProxyRuleGroupsResponseBodyEgressProxyRuleGroups] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.egress_proxy_rule_groups = egress_proxy_rule_groups
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.egress_proxy_rule_groups:
            for v1 in self.egress_proxy_rule_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EgressProxyRuleGroups'] = []
        if self.egress_proxy_rule_groups is not None:
            for k1 in self.egress_proxy_rule_groups:
                result['EgressProxyRuleGroups'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.egress_proxy_rule_groups = []
        if m.get('EgressProxyRuleGroups') is not None:
            for k1 in m.get('EgressProxyRuleGroups'):
                temp_model = main_models.ListEgressProxyRuleGroupsResponseBodyEgressProxyRuleGroups()
                self.egress_proxy_rule_groups.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEgressProxyRuleGroupsResponseBodyEgressProxyRuleGroups(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        egress_proxy_ip_pool_id: str = None,
        egress_proxy_rule_group_id: str = None,
        egress_proxy_rule_group_name: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.ListEgressProxyRuleGroupsResponseBodyEgressProxyRuleGroupsTags] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.egress_proxy_ip_pool_id = egress_proxy_ip_pool_id
        self.egress_proxy_rule_group_id = egress_proxy_rule_group_id
        self.egress_proxy_rule_group_name = egress_proxy_rule_group_name
        self.resource_group_id = resource_group_id
        self.status = status
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_ip_pool_id is not None:
            result['EgressProxyIpPoolId'] = self.egress_proxy_ip_pool_id

        if self.egress_proxy_rule_group_id is not None:
            result['EgressProxyRuleGroupId'] = self.egress_proxy_rule_group_id

        if self.egress_proxy_rule_group_name is not None:
            result['EgressProxyRuleGroupName'] = self.egress_proxy_rule_group_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyIpPoolId') is not None:
            self.egress_proxy_ip_pool_id = m.get('EgressProxyIpPoolId')

        if m.get('EgressProxyRuleGroupId') is not None:
            self.egress_proxy_rule_group_id = m.get('EgressProxyRuleGroupId')

        if m.get('EgressProxyRuleGroupName') is not None:
            self.egress_proxy_rule_group_name = m.get('EgressProxyRuleGroupName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListEgressProxyRuleGroupsResponseBodyEgressProxyRuleGroupsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListEgressProxyRuleGroupsResponseBodyEgressProxyRuleGroupsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

