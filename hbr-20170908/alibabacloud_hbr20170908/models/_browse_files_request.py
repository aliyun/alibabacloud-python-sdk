# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BrowseFilesRequest(DaraModel):
    def __init__(
        self,
        absolute_path: str = None,
        client_id: str = None,
        edition: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
        restore_id: str = None,
        security_token: str = None,
        snapshot_hash: str = None,
        storage_class: str = None,
        token: str = None,
        vault_id: str = None,
    ):
        self.absolute_path = absolute_path
        self.client_id = client_id
        self.edition = edition
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.path = path
        self.restore_id = restore_id
        self.security_token = security_token
        self.snapshot_hash = snapshot_hash
        self.storage_class = storage_class
        self.token = token
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.absolute_path is not None:
            result['AbsolutePath'] = self.absolute_path

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path is not None:
            result['Path'] = self.path

        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.token is not None:
            result['Token'] = self.token

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbsolutePath') is not None:
            self.absolute_path = m.get('AbsolutePath')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

