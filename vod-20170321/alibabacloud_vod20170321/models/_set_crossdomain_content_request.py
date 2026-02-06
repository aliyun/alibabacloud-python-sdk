# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCrossdomainContentRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        owner_account: str = None,
        owner_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        resource_real_owner_id: str = None,
        storage_location: str = None,
    ):
        # The content of the cross-domain policy file. The file must be in the XML format and can contain up to 2,048 characters.
        # 
        # This parameter is required.
        self.content = content
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the resource owner.
        self.resource_real_owner_id = resource_real_owner_id
        # The URL of the Object Storage Service (OSS) bucket.
        # 
        # This parameter is required.
        self.storage_location = storage_location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        return self

