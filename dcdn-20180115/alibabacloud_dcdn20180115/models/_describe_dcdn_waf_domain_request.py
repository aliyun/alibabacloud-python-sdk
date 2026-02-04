# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnWafDomainRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The accelerated domain name. If you do not specify an accelerated domain name, all accelerated domain names are queried.
        self.domain_name = domain_name
        # The region where WAF is enabled.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. If you leave this parameter empty, the default resource group is used.
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

