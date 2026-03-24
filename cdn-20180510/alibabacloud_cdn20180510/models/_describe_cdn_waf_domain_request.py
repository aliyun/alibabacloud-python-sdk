# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCdnWafDomainRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The domain name that you want to query.
        # 
        # You can specify only one domain name in each request. You have three options to configure this parameter:
        # 
        # *   Specify an exact domain name. For example, if you set this parameter to example.com, configuration information of example.com is queried.
        # *   Specify a keyword. For example, if you set this parameter to example, configuration information about all domain names that contain example is queried.
        # *   Leave this parameter empty. If this parameter is left empty, all accelerated domain names for which WAF is configured are queried.
        self.domain_name = domain_name
        # The region where WAF is enabled. Valid values:
        # 
        # *   **cn-hangzhou**: inside the Chinese mainland
        # *   **ap-southeast-1**: outside the Chinese mainland
        # 
        # > ap-southeast-1 includes Hong Kong (China), Macao (China), Taiwan (China), and other countries and regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

