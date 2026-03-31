# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDefenseTemplateValidGroupsRequest(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        group_name: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        template_id: int = None,
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
        # 
        # This parameter is required.
        self.defense_scene = defense_scene
        # The name of the protected object group that you want to query.
        self.group_name = group_name
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
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
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The ID of the protection template.
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

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

