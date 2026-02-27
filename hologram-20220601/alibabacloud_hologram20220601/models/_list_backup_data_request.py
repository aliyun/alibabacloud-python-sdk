# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBackupDataRequest(DaraModel):
    def __init__(
        self,
        backup_type: str = None,
        instance_id: str = None,
    ):
        # The backup type. Specific backup data is filtered based on the type. If you leave this parameter empty, all backup data is returned.
        # 
        # Valid values:
        # 
        # *   redundant_remote
        # *   remote
        # *   redundant
        # *   full_remote
        # *   local
        # *   full
        self.backup_type = backup_type
        # The instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_type is not None:
            result['backupType'] = self.backup_type

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backupType') is not None:
            self.backup_type = m.get('backupType')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        return self

