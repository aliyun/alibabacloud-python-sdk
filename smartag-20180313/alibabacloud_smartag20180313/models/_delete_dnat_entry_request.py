# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDnatEntryRequest(DaraModel):
    def __init__(
        self,
        dnat_entry_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sag_id: str = None,
    ):
        # The ID of the DNAT entry.
        # 
        # This parameter is required.
        self.dnat_entry_id = dnat_entry_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the SAG instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the SAG instance.
        # 
        # >  Only SAG instances used to manage SAG devices support DNAT.
        # 
        # This parameter is required.
        self.sag_id = sag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dnat_entry_id is not None:
            result['DnatEntryId'] = self.dnat_entry_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sag_id is not None:
            result['SagId'] = self.sag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnatEntryId') is not None:
            self.dnat_entry_id = m.get('DnatEntryId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SagId') is not None:
            self.sag_id = m.get('SagId')

        return self

