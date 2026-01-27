# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigureBackupSetInfoRequest(DaraModel):
    def __init__(
        self,
        backup_method: str = None,
        backup_mode: str = None,
        backup_set_id: str = None,
        backup_set_name: str = None,
        backup_type: str = None,
        check_sum: str = None,
        client_token: str = None,
        data_source_id: str = None,
        extra_meta: str = None,
        region_code: str = None,
        region_id: str = None,
        upload_status: str = None,
    ):
        # This parameter is required.
        self.backup_method = backup_method
        # This parameter is required.
        self.backup_mode = backup_mode
        self.backup_set_id = backup_set_id
        # This parameter is required.
        self.backup_set_name = backup_set_name
        # This parameter is required.
        self.backup_type = backup_type
        self.check_sum = check_sum
        self.client_token = client_token
        # This parameter is required.
        self.data_source_id = data_source_id
        self.extra_meta = extra_meta
        # This parameter is required.
        self.region_code = region_code
        self.region_id = region_id
        # This parameter is required.
        self.upload_status = upload_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.backup_set_name is not None:
            result['BackupSetName'] = self.backup_set_name

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.check_sum is not None:
            result['CheckSum'] = self.check_sum

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.extra_meta is not None:
            result['ExtraMeta'] = self.extra_meta

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.upload_status is not None:
            result['UploadStatus'] = self.upload_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('BackupSetName') is not None:
            self.backup_set_name = m.get('BackupSetName')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('CheckSum') is not None:
            self.check_sum = m.get('CheckSum')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('ExtraMeta') is not None:
            self.extra_meta = m.get('ExtraMeta')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UploadStatus') is not None:
            self.upload_status = m.get('UploadStatus')

        return self

