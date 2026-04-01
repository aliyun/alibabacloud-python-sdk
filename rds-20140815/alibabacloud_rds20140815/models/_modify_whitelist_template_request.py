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
        # The IP addresses in an IP address whitelist. Separate multiple IP addresses with commas (,). Each IP address in the IP address whitelist must be unique. The entries in the IP address whitelist must be in one of the following formats:
        # 
        # *   IP addresses, such as 10.23.XX.XX.
        # *   CIDR blocks, such as 10.23.XX.XX/24. In this example, 24 indicates that the prefix of the CIDR block is 24-bit in length. You can replace 24 with a value that ranges from 1 to 32.
        # 
        # > : A maximum of 1,000 IP addresses or CIDR blocks can be added for each instance. If you want to add a large number of IP addresses, we recommend that you merge them into CIDR blocks, such as 10.23.XX.XX/24.
        # 
        # This parameter is required.
        self.ip_whitelist = ip_whitelist
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/26243.html) operation to query the most recent zone list.
        self.region_id = region_id
        # The resource group ID. For more information about resource groups, see related documentation.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the whitelist template. This parameter is required when you modify or delete a whitelist. You can call the DescribeAllWhitelistTemplate operation to obtain the ID of the whitelist.
        self.template_id = template_id
        # The name of the IP whitelist. This parameter is required when you create a whitelist. The value of this parameter cannot be modified after the whitelist is created. The value must be unique to an Alibaba Cloud account and start with a letter. You can call the DescribeWhitelistTemplate operation to obtain the name of the whitelist.
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

