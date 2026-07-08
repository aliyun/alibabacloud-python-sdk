# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachPolicyRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        policy_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the tag policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the object.
        # 
        # > If you use the Tag Policy feature in single-account mode, this parameter is optional. If you use the Tag Policy feature in multi-account mode, this parameter is required.
        self.target_id = target_id
        # The type of the object. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # > If you use the Tag Policy feature in single-account mode, this parameter is optional. If you use the Tag Policy feature in multi-account mode, this parameter is required. The value of this parameter is not case-sensitive.
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

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

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

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

