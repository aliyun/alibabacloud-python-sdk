# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDefenseTemplatesRequest(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        defense_sub_scene: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource: str = None,
        resource_manager_resource_group_id: str = None,
        resource_type: str = None,
        template_id: int = None,
        template_ids: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The scenario in which the protection template is used.
        # 
        # *   **waf_group**: basic protection.
        # *   **antiscan**: scan protection.
        # *   **ip_blacklist**: IP address blacklist.
        # *   **custom_acl**: custom rule.
        # *   **whitelist**: whitelist.
        # *   **region_block**: region blacklist.
        # *   **custom_response**: custom response.
        # *   **cc**: HTTP flood protection.
        # *   **tamperproof**: website tamper-proofing.
        # *   **dlp**: data leakage prevention.
        self.defense_scene = defense_scene
        # The sub-scenario in which the protection template is used. Valid values:
        # 
        # *   **web**: bot management for website protection.
        # *   **app**: bot management for app protection.
        # *   **basic**: bot management for basic protection.
        self.defense_sub_scene = defense_sub_scene
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **20**.
        self.page_size = page_size
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The name of the protected object or protected object group.
        # 
        # >  If you specify ResourceType, you must specify this parameter.
        self.resource = resource
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The type of the protected resource. Valid values:
        # 
        # *   **single**: protected object. This is the default value.
        # *   **group**: protected object group.
        # 
        # >  If you specify Resource, you must specify this parameter.
        self.resource_type = resource_type
        # The ID of the protection template.
        self.template_id = template_id
        # The IDs of the protection templates that you want to query. Separate multiple template IDs with commas (,).
        self.template_ids = template_ids
        # The name of the protection template.
        self.template_name = template_name
        # The type of the protection template. Valid values:
        # 
        # *   **user_default**: default template.
        # *   **user_custom**: custom template.
        self.template_type = template_type

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('DefenseSubScene') is not None:
            self.defense_sub_scene = m.get('DefenseSubScene')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

