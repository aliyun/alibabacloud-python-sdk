# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDNAFilesRequest(DaraModel):
    def __init__(
        self,
        dbid: str = None,
        owner_account: str = None,
        owner_id: int = None,
        primary_keys: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the media fingerprint library from which you want to delete files.
        # 
        # This parameter is required.
        self.dbid = dbid
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The primary key values of the files that you want to delete. Separate multiple values with commas (,). You can delete up to 50 files at a time.
        # 
        # This parameter is required.
        self.primary_keys = primary_keys
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbid is not None:
            result['DBId'] = self.dbid

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.primary_keys is not None:
            result['PrimaryKeys'] = self.primary_keys

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBId') is not None:
            self.dbid = m.get('DBId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrimaryKeys') is not None:
            self.primary_keys = m.get('PrimaryKeys')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

