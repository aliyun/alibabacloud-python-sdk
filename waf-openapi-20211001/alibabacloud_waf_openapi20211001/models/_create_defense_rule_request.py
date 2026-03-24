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
        # The protection scenario for the rule.
        # 
        # When **DefenseType** is **template**, valid values are:
        # 
        # - **waf_group**: basic protection.
        # 
        # - **waf_base**: new version of Web core protection.
        # 
        # - **antiscan**: scan protection.
        # 
        # - **ip_blacklist**: IP blacklist.
        # 
        # - **custom_acl**: custom rules.
        # 
        # - **whitelist**: whitelist.
        # 
        # - **region_block**: location blacklist.
        # 
        # - **custom_response**: legacy custom response.
        # 
        # - **cc**: HTTP flood protection.
        # 
        # - **tamperproof**: webpage tamper protection.
        # 
        # - **dlp**: data leak prevention.
        # 
        # - **spike_throttle**: peak traffic throttling.
        # 
        # When **DefenseType** is **resource**, valid values are:
        # 
        # - **account_identifier**: account extraction.
        # 
        # - **custom_response**: new version of custom response.
        # 
        # - **waf_codec**: decoding.
        # 
        # When **DefenseType** is **global**, valid values are:
        # 
        # - **regular_custom**: custom regex.
        # 
        # - **address_book**: address book.
        # 
        # - **custom_response**: new version of custom response.
        # 
        # > For globally configured custom responses, users can reference them under protected objects or rules. When referenced at different levels, the effective logic follows this order: rule level > protected object level > default page.
        # 
        # This parameter is required.
        self.defense_scene = defense_scene
        # The type of the protection rule. Valid values:
        # 
        # - **template** (default): template-based protection rules.
        # 
        # - **resource**: rules applied at the protected object level.
        # 
        # - **global**: global-level rules.
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
        # The protected object associated with the rule.
        # 
        # > Provide this parameter only when **DefenseType** is **resource**.
        self.resource = resource
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The rule configuration content, specified as a JSON string.
        # 
        # > The specific parameters vary based on the specified **DefenseType** (**DefenseScene**). For details, see **Protection Rule Parameter Descriptions**.
        # 
        # This parameter is required.
        self.rules = rules
        # The ID of the protection template to which the rule belongs.
        # 
        # > Provide this parameter only when **DefenseType** is **template**.
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

