# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloneDBInstanceRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        dbinstance_id: str = None,
        src_db_instance_name: str = None,
    ):
        # This parameter is required.
        self.backup_id = backup_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.src_db_instance_name = src_db_instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.src_db_instance_name is not None:
            result['SrcDbInstanceName'] = self.src_db_instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('SrcDbInstanceName') is not None:
            self.src_db_instance_name = m.get('SrcDbInstanceName')

        return self

