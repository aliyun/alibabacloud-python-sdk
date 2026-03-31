# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDefenseResourceTemplatesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        resource: str = None,
        resource_manager_resource_group_id: str = None,
        resource_type: str = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_type: str = None,
        template_name: str = None,
    ):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The name of the protected object or protected object group that you want to query.
        # 
        # This parameter is required.
        self.resource = resource
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The type of the protected resource. Valid values:
        # 
        # *   **single**: protected object. This is the default value.
        # *   **group**: protected object group.
        self.resource_type = resource_type
        # The ID of the protection rule.
        self.rule_id = rule_id
        # The name of the rule.
        self.rule_name = rule_name
        # The type of the protection rule. Valid values:
        # 
        # *   **defense**: defense rule. This is the default value.
        # *   **whitelist**: whitelist rule.
        self.rule_type = rule_type
        # The name of the protection rule template.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

