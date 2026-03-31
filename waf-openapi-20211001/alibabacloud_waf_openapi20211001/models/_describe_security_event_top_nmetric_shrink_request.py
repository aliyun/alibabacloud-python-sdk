# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecurityEventTopNMetricShrinkRequest(DaraModel):
    def __init__(
        self,
        filter_shrink: str = None,
        instance_id: str = None,
        limit: int = None,
        metric: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The filter conditions for the query. Multiple conditions are evaluated by using a logical AND.
        # 
        # This parameter is required.
        self.filter_shrink = filter_shrink
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstanceInfo](https://help.aliyun.com/document_detail/140857.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of data entries that can be returned. Data entries are sorted in descending order before they are returned. Maximum value: 10.
        # 
        # This parameter is required.
        self.limit = limit
        # The metric whose top N data entries you want to return. The following metrics are supported:
        # 
        # >  For more information about attack requests, see the "Operation description" section of this topic.
        # 
        # *   real_client_ip: The system aggregates the source IP addresses of attack requests to collect statistics, sorts the statistical results in descending order, and returns top N data entries.
        # *   http_user_agent: The system aggregates the User-Agent header field of attack requests to collect statistics, sorts the statistical results in descending order, and returns top N data entries.
        # *   matched_host: The system aggregates the protected objects that are matched by attack requests to collect statistics, sorts the statistical results in descending order, and returns top N data entries.
        # *   remote_region_id: The system aggregates the countries to which the source IP addresses of attack requests belong to collect statistics, sorts the statistical results in descending order, and returns top N data entries.
        # *   request_path: The system aggregates the URLs of attack requests to collect statistics, sorts the statistical results in descending order, and returns top N data entries. The URLs exclude query strings.
        # *   block_defense_scene: The system aggregates the protection modules that block attack requests to collect statistics, sorts the statistical results in descending order, and returns top N data entries. The requests match protection rules whose actions are not set to Monitor.
        # *   defense_scene: The system aggregates the protection modules that are matched by attack requests to collect statistics, sorts the statistical results in descending order, and returns top N data entries.
        # *   defense_scene_rule_id: The system returns the IDs of top N protection rules that are matched by attack requests and also the related protection modules. Only protection rules whose actions are not set to Monitor are counted. The system returns the value in the following format:\\
        #     `{ "Attribute": "waf_base", "Value": 140, "Name": "111034" }`
        # *   defense_scene_with_rule_id: The system returns the IDs of top N protection rules that are matched by attack requests and also the related protection modules. The IDs and protection modules are connected by using hyphens (-). Protection rules whose actions are set to Monitor and Block are counted. The system returns the value in the following format:\\
        #     `{ "Attribute": "", "Value": 1, "Name": "120075-waf_base" }`
        # *   defense_scene_top_rule_id: The system returns top N matched protection rules of a specific protection module. You can specify Conditions in Filter to configure filter conditions. For example, you can use the following condition to query top N matched protection rules of the custom rule module:\\
        #     `{ "Key": "defense_scene_map", "OpValue": "contain", "Values": "custom_acl" }`
        # *   defense_scene_rule_type: The system returns top N matched protection rules of the core web protection module. This metric is supported only by the core web protection module because only this module supports subtypes of protection rules. You must specify Conditions in Filter to configure filter conditions. Example:\\
        #     `{ "Key": "defense_scene", "OpValue": "eq", "Values": "waf_base" }`
        # 
        # This parameter is required.
        self.metric = metric
        # The region ID of the WAF instance. Valid values:
        # 
        # *   **cn-hangzhou**: The Chinese mainland.
        # *   **ap-southeast-1**: Outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

