# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RoamClientUserRequest(DaraModel):
    def __init__(
        self,
        origin_region_id: str = None,
        origin_smart_agid: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        target_smart_agid: str = None,
        user_name: str = None,
    ):
        # The region ID of the SAG app instance.
        # 
        # This parameter is required.
        self.origin_region_id = origin_region_id
        # The ID of the source SAG app instance.
        # 
        # This parameter is required.
        self.origin_smart_agid = origin_smart_agid
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the SAG app instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the destination SAG app instance.
        # 
        # This parameter is required.
        self.target_smart_agid = target_smart_agid
        # The usernames of the client for which you want to enable roaming.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.origin_region_id is not None:
            result['OriginRegionId'] = self.origin_region_id

        if self.origin_smart_agid is not None:
            result['OriginSmartAGId'] = self.origin_smart_agid

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

        if self.target_smart_agid is not None:
            result['TargetSmartAGId'] = self.target_smart_agid

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginRegionId') is not None:
            self.origin_region_id = m.get('OriginRegionId')

        if m.get('OriginSmartAGId') is not None:
            self.origin_smart_agid = m.get('OriginSmartAGId')

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

        if m.get('TargetSmartAGId') is not None:
            self.target_smart_agid = m.get('TargetSmartAGId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

