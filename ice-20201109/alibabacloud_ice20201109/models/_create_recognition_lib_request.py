# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRecognitionLibRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        lib_description: str = None,
        lib_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The type of recognition algorithm. Valid values:
        # 
        # *   landmark
        # *   object
        # *   logo
        # *   face
        # *   label
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The description of the recognition library. Max length: 128 bytes.
        self.lib_description = lib_description
        # The name of the recognition library. Max length: 64 bytes.
        # 
        # This parameter is required.
        self.lib_name = lib_name
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

        if self.lib_description is not None:
            result['LibDescription'] = self.lib_description

        if self.lib_name is not None:
            result['LibName'] = self.lib_name

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

        if m.get('LibDescription') is not None:
            self.lib_description = m.get('LibDescription')

        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

