# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMajorProtectionBlackIpRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        ip_list: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        rule_id: int = None,
        template_id: int = None,
    ):
        # The ID of the WAF instance.
        # 
        # > You can call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to obtain the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IP blacklist to delete. Custom IP addresses or CIDR blocks are supported, including both IPv4 and IPv6. Separate multiple IP addresses with commas (,).
        # For more information, see [Critical event protection](https://help.aliyun.com/document_detail/425591.html).
        # 
        # This parameter is required.
        self.ip_list = ip_list
        # The region where the WAF instance is deployed. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The ID of the IP blacklist rule for critical event protection.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The ID of the critical event protection scenario template.
        # 
        # > This parameter requires the ID of a protection template of the critical event protection type. You can create this type of template only after purchasing the critical event protection upgrade.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

