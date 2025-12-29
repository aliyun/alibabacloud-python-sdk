# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class RunClusterCheckRequest(DaraModel):
    def __init__(
        self,
        options: Dict[str, str] = None,
        target: str = None,
        type: str = None,
    ):
        # The cluster check parameters.
        self.options = options
        # The check target.
        # 
        # If you set `type=NodePoolUpgrade`, you must set this parameter to the node pool ID. Otherwise, this parameter is optional.
        self.target = target
        # The check type.
        # 
        # Valid values:
        # 
        # *   ClusterMigrate: cluster migration.
        # *   MasterUpgrade: control plane upgrade.
        # *   NodePoolUpgrade: node pool upgrade.
        # *   ClusterUpgrade: cluster upgrade.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.options is not None:
            result['options'] = self.options

        if self.target is not None:
            result['target'] = self.target

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

