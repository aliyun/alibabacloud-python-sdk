# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindVbrRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        smart_agid: str = None,
        smart_aguid: int = None,
        vbr_id: str = None,
        vbr_region_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the Smart Access Gateway instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The instance ID of the Smart Access Gateway instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The Alibaba Cloud account ID that owns the Smart Access Gateway instance.
        self.smart_aguid = smart_aguid
        # The instance ID of the virtual border routing instance to bind.
        # 
        # This parameter is required.
        self.vbr_id = vbr_id
        # The region ID of the virtual border router (VBR) to bind.
        # 
        # This parameter is required.
        self.vbr_region_id = vbr_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_aguid is not None:
            result['SmartAGUid'] = self.smart_aguid

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        if self.vbr_region_id is not None:
            result['VbrRegionId'] = self.vbr_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGUid') is not None:
            self.smart_aguid = m.get('SmartAGUid')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        if m.get('VbrRegionId') is not None:
            self.vbr_region_id = m.get('VbrRegionId')

        return self

