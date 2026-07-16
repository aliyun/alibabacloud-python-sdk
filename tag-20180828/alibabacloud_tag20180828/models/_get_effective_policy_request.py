# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetEffectivePolicyRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        tag_keys: List[str] = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. Only `cn-shanghai` is supported.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.tag_keys = tag_keys
        # The ID of the target object.
        # 
        # > This parameter is optional in Single-Account Mode and required in Multi-Account Mode.
        self.target_id = target_id
        # The type of the target object. Valid values:
        # 
        # - USER: queries the effective policy for the current logon account. This value applies only to Single-Account Mode.
        # 
        # - ROOT: queries the effective policy for the Root Folder in a Resource Directory. This value applies only to Multi-Account Mode.
        # 
        # - FOLDER: queries the effective policy for a Folder in a Resource Directory. This value applies only to Multi-Account Mode.
        # 
        # - ACCOUNT: queries the effective policy for a Member in a Resource Directory. This value applies only to Multi-Account Mode.
        # 
        # > This parameter is optional in Single-Account Mode and required in Multi-Account Mode. The value is case-insensitive.
        self.target_type = target_type

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

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

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

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

