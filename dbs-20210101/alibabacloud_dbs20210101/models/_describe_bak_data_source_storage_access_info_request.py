# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBakDataSourceStorageAccessInfoRequest(DaraModel):
    def __init__(
        self,
        backup_set_id: str = None,
        backup_type: str = None,
        client_token: str = None,
        data_source_id: str = None,
        duration_seconds: int = None,
        region_code: str = None,
        region_id: str = None,
        storage_type: str = None,
    ):
        # This parameter is required.
        self.backup_set_id = backup_set_id
        # This parameter is required.
        self.backup_type = backup_type
        self.client_token = client_token
        # This parameter is required.
        self.data_source_id = data_source_id
        self.duration_seconds = duration_seconds
        # This parameter is required.
        self.region_code = region_code
        self.region_id = region_id
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

