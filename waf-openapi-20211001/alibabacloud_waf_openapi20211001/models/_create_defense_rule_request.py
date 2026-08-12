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
        # The WAF protection scenario to create.
        # 
        # When the protection rule type **DefenseType** is set to **template**, valid values:
        # 
        # - **waf_group**: Basic Web Protection.
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
        # - **region_block**: Location Blacklist.
        # 
        # - **custom_response**: legacy custom response.
        # 
        # - **cc**: HTTP flood mitigation.
        # 
        # - **tamperproof**: web tamper proofing.
        # 
        # - **dlp**: information leak prevention.
        # 
        # - **spike_throttle**: peak traffic throttling.
        # 
        # - **bot_manager**: bot management.
        # 
        # 
        # When the protection rule type **DefenseType** is set to **resource**, valid values:
        # 
        # - **account_identifier**: account extraction.
        # 
        # - **custom_response**: new version of custom response.
        # 
        # - **waf_codec**: decoding.
        # 
        # - **websdk**: WebSDK integration.
        # 
        # When the protection rule type **DefenseType** is set to **global**, valid values:
        # 
        # - **regular_custom**: custom regular expression.
        # 
        # - **address_book**: address book.
        # 
        # - **custom_response**: new version of custom response.
        # >  The custom response in global configurations can be referenced by protected objects or rules. When custom response rules are referenced at different levels, the effective priority is: rule level > protected object level > default page.
        # 
        # This parameter is required.
        self.defense_scene = defense_scene
        # The type of the protection rule.
        self.defense_type = defense_type
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region where the WAF instance resides. Valid values:
        self.region_id = region_id
        # The protection object associated with the rule to create.
        self.resource = resource
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The rule configuration content, which is a JSON string constructed from a series of parameters.
        # >  The specific parameters vary depending on the **mitigation setting type** (**DefenseScene**) that you specify. For more information, refer to **Protection rule parameter description**.
        # 
        # This parameter is required.
        self.rules = rules
        # The ID of the protection template for which you want to create a protection rule.
        # > This parameter is required only when **DefenseType** is set to **template**.
        # > There is an upper limit on the number of rules that can be created in a protection template. For more information, see **Rule quantity limits**. If the number of rules has reached the upper limit, you can call the [CreateDefenseTemplate](https://help.aliyun.com/document_detail/461613.html) operation to create a new protection template. You can also call the [ModifyDefenseRule](https://help.aliyun.com/document_detail/461422.html) operation to modify an existing rule.
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

