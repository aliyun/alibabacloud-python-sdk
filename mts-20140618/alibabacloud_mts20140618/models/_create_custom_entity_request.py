# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomEntityRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        custom_entity_info: str = None,
        custom_entity_name: str = None,
        custom_group_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.algorithm = algorithm
        self.custom_entity_info = custom_entity_info
        # This parameter is required.
        self.custom_entity_name = custom_entity_name
        # This parameter is required.
        self.custom_group_id = custom_group_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.custom_entity_info is not None:
            result['CustomEntityInfo'] = self.custom_entity_info

        if self.custom_entity_name is not None:
            result['CustomEntityName'] = self.custom_entity_name

        if self.custom_group_id is not None:
            result['CustomGroupId'] = self.custom_group_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CustomEntityInfo') is not None:
            self.custom_entity_info = m.get('CustomEntityInfo')

        if m.get('CustomEntityName') is not None:
            self.custom_entity_name = m.get('CustomEntityName')

        if m.get('CustomGroupId') is not None:
            self.custom_group_id = m.get('CustomGroupId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

