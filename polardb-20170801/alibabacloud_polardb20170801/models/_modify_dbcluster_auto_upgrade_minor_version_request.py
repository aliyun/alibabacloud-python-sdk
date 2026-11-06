# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterAutoUpgradeMinorVersionRequest(DaraModel):
    def __init__(
        self,
        auto_upgrade_minor_version: str = None,
        dbcluster_id: str = None,
    ):
        # The minor engine version update policy. Valid values: Auto: automatic update. Manual: manual update.
        # 
        # This parameter is required.
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        # The ID of the PolarDB cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_upgrade_minor_version is not None:
            result['AutoUpgradeMinorVersion'] = self.auto_upgrade_minor_version

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpgradeMinorVersion') is not None:
            self.auto_upgrade_minor_version = m.get('AutoUpgradeMinorVersion')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        return self

