# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantSagInstanceToVbrRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        smart_agid: str = None,
        vbr_instance_id: str = None,
        vbr_region_id: str = None,
        vbr_uid: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the SAG instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The ID of the VBR.
        # 
        # This parameter is required.
        self.vbr_instance_id = vbr_instance_id
        # The ID of the region where the VBR is deployed.
        # 
        # This parameter is required.
        self.vbr_region_id = vbr_region_id
        # The user ID (UID) of the account to which the VBR belongs.
        # 
        # This parameter is required.
        self.vbr_uid = vbr_uid

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

        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id

        if self.vbr_region_id is not None:
            result['VbrRegionId'] = self.vbr_region_id

        if self.vbr_uid is not None:
            result['VbrUid'] = self.vbr_uid

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

        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')

        if m.get('VbrRegionId') is not None:
            self.vbr_region_id = m.get('VbrRegionId')

        if m.get('VbrUid') is not None:
            self.vbr_uid = m.get('VbrUid')

        return self

