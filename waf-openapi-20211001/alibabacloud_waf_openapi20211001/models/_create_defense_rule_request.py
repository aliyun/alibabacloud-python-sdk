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
        # The scenario to which the protection rule is applied.
        # 
        # If **DefenseType** is set to **template**, valid values are:
        # 
        # - **waf_group**: basic protection.
        # 
        # - **waf_base**: web core protection.
        # 
        # - **antiscan**: scan protection.
        # 
        # - **ip_blacklist**: IP address blacklist.
        # 
        # - **custom_acl**: custom rule.
        # 
        # - **whitelist**: whitelist.
        # 
        # - **region_block**: geo-blocking.
        # 
        # - **custom_response**: custom response.
        # 
        # - **cc**: HTTP flood protection.
        # 
        # - **tamperproof**: webpage tamper-proofing.
        # 
        # - **dlp**: data leakage prevention.
        # 
        # - **spike_throttle**: rate limiting for bursts of traffic.
        # 
        # - **bot_manager**: bot management.
        # 
        # If **DefenseType** is set to **resource**, valid values are:
        # 
        # - **account_identifier**: account identification.
        # 
        # - **custom_response**: custom response.
        # 
        # - **waf_codec**: decoding.
        # 
        # If **DefenseType** is set to **global**, valid values are:
        # 
        # - **regular_custom**: custom regular expression.
        # 
        # - **address_book**: address book.
        # 
        # - **custom_response**: custom response.
        # 
        # > You can apply a global custom response to a protected object or a rule. If you configure custom response rules at different levels, the rule with the finest-grained scope takes precedence. The priority is as follows: rule > protected object > default page.
        # 
        # This parameter is required.
        self.defense_scene = defense_scene
        # The type of the protection rule. Valid values:
        # 
        # - **template** (default): a template-based protection rule.
        # 
        # - **resource**: a rule for a specific protected object.
        # 
        # - **global**: a global protection rule.
        self.defense_type = defense_type
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to get the ID of your WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region where the WAF instance is deployed. Valid values:
        # 
        # - **cn-hangzhou**: Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The protected object to which the rule applies.
        # 
        # > This parameter is required only when **DefenseType** is set to **resource**.
        self.resource = resource
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The details of the protection rule. This value is a JSON string.
        # 
        # > The parameters in the JSON string vary based on the value of **DefenseScene**. For more information, see **Protection rule parameters**.
        # 
        # This parameter is required.
        self.rules = rules
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

