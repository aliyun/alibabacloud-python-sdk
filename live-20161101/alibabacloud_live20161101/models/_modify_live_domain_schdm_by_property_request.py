# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLiveDomainSchdmByPropertyRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        property: str = None,
        region_id: str = None,
    ):
        # The domain name for which you want to modify the acceleration region.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # The acceleration region that you want to set. {"coverage":"overseas"} specifies regions outside the Chinese mainland. Valid values of coverage:
        # 
        # *   domestic: regions in the Chinese mainland.
        # *   overseas: regions outside the Chinese mainland.
        # *   global: regions in and outside the Chinese mainland.
        # 
        # This parameter is required.
        self.property = property
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.property is not None:
            result['Property'] = self.property

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

