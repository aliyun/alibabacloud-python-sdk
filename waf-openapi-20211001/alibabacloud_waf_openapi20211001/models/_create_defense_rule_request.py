# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDefenseRuleRequest(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        defense_type: str = None,
        dry_run: bool = None,
        instance_id: str = None,
        region_id: str = None,
        resource: str = None,
        resource_manager_resource_group_id: str = None,
        resource_type: str = None,
        rules: str = None,
        template_id: int = None,
    ):
        # The WAF protection scenario to be created.
        # 
        # Valid values when the protection rule type **DefenseType** is set to **template**:
        # 
        # - **waf_group**: basic protection.
        # - **waf_base**: new version of web core protection.
        # 
        # - **antiscan**: scan protection.
        # 
        # - **ip_blacklist**: IP blacklist.
        # 
        # - **custom_acl**: custom rules.
        # 
        # - **whitelist**: whitelist.
        # 
        # - **region_block**: area blocking.
        # 
        # - **custom_response**: custom response of the old version.
        # 
        # - **cc**: HTTP flood protection.
        # 
        # - **tamperproof**: web tamper-proofing.
        # 
        # - **dlp**: data leak prevention.
        # 
        # - **spike_throttle**: peak traffic throttling.
        # 
        # - **bot_manager**: bot management.
        # 
        # 
        # Valid values when the protection rule type **DefenseType** is set to **resource**:
        # 
        # -  **account_identifier**: account extraction.
        # 
        # - **custom_response**: custom response of the new version.
        # 
        # - **waf_codec**: decoding.
        # 
        # - **websdk**: WebSDK integration.
        # 
        # Valid values when the protection rule type **DefenseType** is set to **global**:
        # 
        # -  **regular_custom**: custom regular expressions.
        # 
        # - **address_book**: address book.
        # 
        # - **custom_response**: custom response of the new version.
        # > For globally configured custom responses, you can reference them under protected objects or rules. When custom response rules are referenced at different dimensions, the actual effective priority is: rule level > protected object level > default page.
        # 
        # This parameter is required.
        self.defense_scene = defense_scene
        # The type of the protection rule.
        self.defense_type = defense_type
        # Specifies whether to enable the dry run mode. If this parameter is not specified, a normal request is initiated. Valid values:
        # - **true**: initiates a dry run request. The system only checks whether the request meets the execution conditions and does not perform the operations specified in the request. If the dry run fails, the corresponding error code is returned. If the dry run succeeds, the error code Defense.Control.DryRunOperation is returned.
        # - **false**: initiates a normal request. The system performs the operations specified in the request after the check succeeds.
        self.dry_run = dry_run
        # Instance ID of the WAF instance.
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query instance ID of your WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The protected object corresponding to the created rule.
        # > This parameter is required only when **DefenseType** is set to **resource**.
        self.resource = resource
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The type of the protected target. This parameter applies to rules where **DefenseType** is set to **resource**. Valid values:
        # 
        # - **single** (default): a single protected object.
        # - **group**: a protection group.
        self.resource_type = resource_type
        # The rule configuration content, which is converted into a string in JSON format constructed by a series of parameters.
        # > The specific parameters involved vary depending on the specified **protection rule type** (**DefenseScene**). For more information, see **Protection rule parameter description**.
        # 
        # This parameter is required.
        self.rules = rules
        # The ID of the protection template for the protection rule to be created.
        # > This parameter is required only when **DefenseType** is set to **template**.
        # > The number of rules that can be created in a single protection template is limited. For more information, see **Rule quantity limits**. If the limit is reached, you can call the [CreateDefenseTemplate](https://help.aliyun.com/document_detail/461613.html) operation to create a new protection template, or call the [ModifyDefenseRule](https://help.aliyun.com/document_detail/461422.html) operation to modify an existing rule.
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

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

