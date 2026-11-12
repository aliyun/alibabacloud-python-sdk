# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestoreApplicationByBackupSetRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        backup_set_id: str = None,
        region_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The application type.
        self.application_type = application_type
        # The ID of the backup set used to restore the application. This parameter is required. If it is not provided, the API returns InvalidBackupSetID.NotFound (404).
        self.backup_set_id = backup_set_id
        # The region ID of the application.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

