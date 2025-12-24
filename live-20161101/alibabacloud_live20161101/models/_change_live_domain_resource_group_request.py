# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeLiveDomainResourceGroupRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        new_resource_group_id: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The ingest domain or streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The ID of the resource group to which the domain name is moved.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        self.owner_id = owner_id
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

        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

