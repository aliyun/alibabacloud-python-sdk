# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateDefenseTemplateRequest(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        defense_sub_scene: str = None,
        description: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        template_name: str = None,
        template_origin: str = None,
        template_status: int = None,
        template_type: str = None,
        unbind_resource_groups: List[str] = None,
        unbind_resources: List[str] = None,
    ):
        # The protection scenario. For more information, see the **DefenseScene** parameter of the [CreateDefenseRule](https://help.aliyun.com/document_detail/461421.html) operation.
        # 
        # This parameter is required.
        self.defense_scene = defense_scene
        self.defense_sub_scene = defense_sub_scene
        # The description of the protection template.
        # 
        # - **bot_custom_acl**: Represents the protection template for advanced custom rules in bot management.
        self.description = description
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to get the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region where the WAF instance is deployed. Valid values:
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # - **cn-hangzhou**: Represents the Chinese mainland.
        # 
        # - **ap-southeast-1**: Represents regions outside the Chinese mainland.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The name of the protection template. The name must be 1 to 255 characters long and can contain letters, digits, Chinese characters, underscores (_), periods (.), and hyphens (-).
        # 
        # > The names of templates for the same protection scenario (**DefenseScene**) must be unique.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The origin of the protection template. The value must be **custom**.
        # 
        # This parameter is required.
        self.template_origin = template_origin
        # Indicates whether the protection template is enabled. Valid values:
        # 
        # - **0**: Disabled.
        # 
        # - **1**: Enabled.
        # 
        # This parameter is required.
        self.template_status = template_status
        # The type of the protection template. Valid values:
        # 
        # - **user_default**: The user\\"s default template.
        # 
        # - **user_custom**: A user-defined template.
        # 
        # This parameter is required.
        self.template_type = template_type
        # The protected objects to unbind when you create a default template. Use the [**"XX1","XX2",...**] format.
        # 
        # > This parameter takes effect only when you create a **default template** (**TemplateType** is set to **user_default**).
        self.unbind_resource_groups = unbind_resource_groups
        # The ID of the Alibaba Cloud resource group.
        self.unbind_resources = unbind_resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        if self.defense_sub_scene is not None:
            result['DefenseSubScene'] = self.defense_sub_scene

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_origin is not None:
            result['TemplateOrigin'] = self.template_origin

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.unbind_resource_groups is not None:
            result['UnbindResourceGroups'] = self.unbind_resource_groups

        if self.unbind_resources is not None:
            result['UnbindResources'] = self.unbind_resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('DefenseSubScene') is not None:
            self.defense_sub_scene = m.get('DefenseSubScene')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateOrigin') is not None:
            self.template_origin = m.get('TemplateOrigin')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('UnbindResourceGroups') is not None:
            self.unbind_resource_groups = m.get('UnbindResourceGroups')

        if m.get('UnbindResources') is not None:
            self.unbind_resources = m.get('UnbindResources')

        return self

