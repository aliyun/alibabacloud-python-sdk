# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHybridCloudClusterRuleRequest(DaraModel):
    def __init__(
        self,
        cluster_id: int = None,
        cluster_rule_resource_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        rule_config: str = None,
        rule_status: str = None,
        rule_type: str = None,
    ):
        # The ID of the hybrid cloud cluster.
        self.cluster_id = cluster_id
        self.cluster_rule_resource_id = cluster_rule_resource_id
        # The ID of the WAF instance.
        # 
        # >  You can call the DescribeInstanceInfo operation to query the ID of the WAF instance.[](~~140857~~)
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region of the WAF instance. Valid value:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: Outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The configuration of the rule.
        self.rule_config = rule_config
        # The status of the rule. Valid values:
        # 
        # *   **on**: enables the rule.
        # *   **off**: disables the rule.
        self.rule_status = rule_status
        # The type of the rule. Valid values:
        # 
        # *   **pullin**: The traffic redirection rule.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_rule_resource_id is not None:
            result['ClusterRuleResourceId'] = self.cluster_rule_resource_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterRuleResourceId') is not None:
            self.cluster_rule_resource_id = m.get('ClusterRuleResourceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('RuleConfig') is not None:
            self.rule_config = m.get('RuleConfig')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

