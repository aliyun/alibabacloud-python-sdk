# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDomainRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        region_id: str = None,
        target_domain: str = None,
    ):
        # The new accelerated domain name.
        # 
        # Only primary domain names are supported, such as `example.net`.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
        self.region_id = region_id
        # The accelerated domain name to be modified.
        # 
        # This parameter is required.
        self.target_domain = target_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_domain is not None:
            result['TargetDomain'] = self.target_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetDomain') is not None:
            self.target_domain = m.get('TargetDomain')

        return self

