# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyWebAreaBlockRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        regions: List[str] = None,
        resource_group_id: str = None,
    ):
        # The domain name for which you want to configure geo-blocking.
        # 
        # > The domain name must have a website forwarding rule configured. You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # The list of regions to block.
        # 
        # > If you do not set this parameter, the Location Blacklist (domain-specific) feature is shutdown.
        self.regions = regions
        # The ID of the resource group to which the Anti-DDoS Pro or Anti-DDoS Premium instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.regions is not None:
            result['Regions'] = self.regions

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Regions') is not None:
            self.regions = m.get('Regions')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

