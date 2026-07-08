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
        # The query filter conditions. Multiple filter conditions are evaluated using a logical AND.
        # 
        # This parameter is required.
        self.filter_shrink = filter_shrink
        # The ID of the WAF instance.
        # 
        # > You can call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to query the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of data entries to return after the statistics are sorted in descending order. Maximum value: 10.
        # 
        # This parameter is required.
        self.limit = limit
        # Specifies the type of data to return. Different Metric values correspond to different data content. The following Metric values are supported by this API operation:
        # > The definition of "attack request" is described in the API operation description. The following descriptions reference this concept.
        # 
        # - real_client_ip: performs aggregation and sorting of the source IP addresses of attack requests in descending order, and returns the top N entries.
        # - http_user_agent: performs aggregation and sorting of the User-Agent values of attack requests in descending order, and returns the top N entries.
        # - matched_host: performs aggregation and sorting of the protected objects hit by attack requests in descending order, and returns the top N entries.
        # - remote_region_id: performs aggregation and sorting of the countries to which the source IP addresses of attack requests belong in descending order, and returns the top N entries.
        # - request_path: performs aggregation and sorting of the URLs (excluding query strings) of attack requests in descending order, and returns the top N entries.
        # - block_defense_scene: performs aggregation and sorting of the final action modules of blocked requests (whose action is not "monitor") in descending order, and returns the top N entries.
        # - defense_scene: performs aggregation and sorting of all protection modules hit by attack requests in descending order, and returns the top N entries.
        # - defense_scene_rule_id: queries the top rule IDs of hit non-monitor rules and the protection modules to which the rules belong. This query returns statistics only for non-monitor mode rules. The returned data format is as follows:<br>
        #  `{ "Attribute": "waf_base", "Value": 140, "Name": "111034" }`
        # - defense_scene_with_rule_id: returns the top N rule IDs ranked by the number of hit requests and the protection modules to which the rules belong, connected by "-". This query does not distinguish between rule actions and includes both monitor rules and block rules. The returned format is as follows:<br>
        #  `{ "Attribute": "",  "Value": 1,  "Name": "120075-waf_base" }`
        # - defense_scene_top_rule_id: queries the top rule hits of a specific protection module. Specify filter conditions in the Conditions field of Filter. For example, to query the top rule hits of the "custom ACL" module, set the Conditions field as follows:<br>
        #    `{ "Key": "defense_scene_map", "OpValue": "contain", "Values": "custom_acl" }`
        # - defense_scene_rule_type: queries the top hit rule types of the web core protection module. Only the web core protection module supports this query because only web core protection has rule child classes. Specify filter conditions in the Conditions field of Filter. The format is as follows:<br>
        # `    { "Key": "defense_scene", "OpValue": "eq", "Values": "waf_base" }`
        # 
        # This parameter is required.
        self.metric = metric
        # The region where the WAF instance is deployed. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The Alibaba Cloud resource group ID.
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

