# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBackupConfigRequest(DaraModel):
    def __init__(
        self,
        backup_config: str = None,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
    ):
        # Evidence backup configuration.
        self.backup_config = backup_config
        # Region ID.
        self.region_id = region_id
        # Resource type.
        self.resource_type = resource_type
        # Service code.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_config is not None:
            result['BackupConfig'] = self.backup_config

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupConfig') is not None:
            self.backup_config = m.get('BackupConfig')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        return self

