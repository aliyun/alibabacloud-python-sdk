# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateDefenseTemplateRequest(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
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
        # The scenario in which you want to use the protection rule template. For more information, see the description of the **DefenseScene** parameter in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        # 
        # This parameter is required.
        self.defense_scene = defense_scene
        # The description of the protection rule template.
        self.description = description
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
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The name of the protection rule template.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The origin of the protection rule template that you want to create. Set the value to **custom**. The value specifies that the protection rule template is a custom template.
        # 
        # This parameter is required.
        self.template_origin = template_origin
        # The status of the protection rule template. Valid values:
        # 
        # *   **0:** disabled.
        # *   **1:** enabled.
        # 
        # This parameter is required.
        self.template_status = template_status
        # The type of the protection rule template. Valid values:
        # 
        # *   **user_default:** default template.
        # *   **user_custom:** custom template.
        # 
        # This parameter is required.
        self.template_type = template_type
        self.unbind_resource_groups = unbind_resource_groups
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

