# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDefenseRuleRequest(DaraModel):
    def __init__(
        self,
        defense_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource: str = None,
        resource_manager_resource_group_id: str = None,
        rule_id: int = None,
        template_id: int = None,
    ):
        # The type of the protection rule. Valid values:
        # 
        # - **template** (default): a protection rule template.
        # 
        # - **resource**: a rule for a protected object.
        # 
        # - **global**: a global rule.
        self.defense_type = defense_type
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The protected object to which the protection rule applies.
        # 
        # > This parameter is required only when **DefenseType** is set to **resource**.
        self.resource = resource
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The ID of the protection rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The ID of the protection rule template.
        # 
        # > This parameter is required only when **DefenseType** is set to **template**.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

