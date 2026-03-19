# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFullBackupSetDownloadRequest(DaraModel):
    def __init__(
        self,
        backup_set_data_format: str = None,
        backup_set_id: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The format of the downloaded full backup set. Valid values:
        # 
        # - **Native**
        # 
        # - **SQL**
        # 
        # - **CSV**
        # 
        # - **JSON**
        # 
        # > The default value is CSV.
        self.backup_set_data_format = backup_set_data_format
        # The ID of the full backup set.
        # 
        # This parameter is required.
        self.backup_set_id = backup_set_id
        # A client token used to ensure the idempotence of the request. This prevents the same request from being sent multiple times.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_data_format is not None:
            result['BackupSetDataFormat'] = self.backup_set_data_format

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetDataFormat') is not None:
            self.backup_set_data_format = m.get('BackupSetDataFormat')

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

