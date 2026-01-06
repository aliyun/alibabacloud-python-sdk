# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCompactionServiceSwitchRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        enable_compaction_service: bool = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable the remote build feature.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is required.
        self.enable_compaction_service = enable_compaction_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enable_compaction_service is not None:
            result['EnableCompactionService'] = self.enable_compaction_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EnableCompactionService') is not None:
            self.enable_compaction_service = m.get('EnableCompactionService')

        return self

