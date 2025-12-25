# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDefenseRuleRequest(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        defense_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource: str = None,
        resource_manager_resource_group_id: str = None,
        rules: str = None,
        template_id: int = None,
    ):
        # The module to which the protection rule that you want to create belongs.
        # 
        # *   **waf_group:** the basic protection rule module.
        # *   **antiscan:** the scan protection module.
        # *   **ip_blacklist:** the IP address blacklist module.
        # *   **custom_acl:** the custom rule module.
        # *   **whitelist:** the whitelist module.
        # *   **region_block:** the region blacklist module.
        # *   **custom_response:** the custom response module.
        # *   **cc:** the HTTP flood protection module.
        # *   **tamperproof:** the website tamper-proofing module.
        # *   **dlp:** the data leakage prevention module.
        # 
        # This parameter is required.
        self.defense_scene = defense_scene
        self.defense_type = defense_type
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to obtain the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id
        self.resource = resource
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # This parameter is required.
        self.rules = rules
        # The ID of the rule template for which you want to create a protection rule.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

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

        if self.rules is not None:
            result['Rules'] = self.rules

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

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

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

