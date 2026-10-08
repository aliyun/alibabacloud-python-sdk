# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWhitelistTemplateRequest(DaraModel):
    def __init__(
        self,
        ip_whitelist: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
        template_name: str = None,
    ):
        # The IP whitelist of the instance. Separate multiple IP addresses with commas (,). IP addresses cannot be duplicated. The following two formats are supported:
        # 
        # - IP address format, such as 10.23.XX.XX.
        # - CIDR format, such as 10.23.XX.XX/24 (Classless Inter-Domain Routing, where 24 indicates the prefix length, with a value range of 1 to 32).
        # 
        # > Each instance supports a maximum of 1,000 IP addresses or CIDR blocks. The total number of IP addresses or CIDR blocks across all IP whitelist groups cannot exceed 1,000. If you have a large number of IP addresses, merge them into CIDR blocks, such as 10.23.XX.XX/24.
        # 
        # This parameter is required.
        self.ip_whitelist = ip_whitelist
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/26243.html) to query the region ID.
        self.region_id = region_id
        # The resource group ID. For more information about resource groups, see What is a resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The whitelist template ID.
        # This parameter is required for modify and delete operations. You can call DescribeAllWhitelistTemplate to obtain the template ID.
        self.template_id = template_id
        # The whitelist template name. Specify this parameter when creating a template. The name cannot be modified after creation, must be unique within the same account, and must start with a letter. You can call DescribeWhitelistTemplate to obtain the template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

