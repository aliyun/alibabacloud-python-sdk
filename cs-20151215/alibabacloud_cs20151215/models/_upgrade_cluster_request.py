# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class UpgradeClusterRequest(DaraModel):
    def __init__(
        self,
        component_name: str = None,
        master_only: bool = None,
        next_version: str = None,
        rolling_policy: main_models.UpgradeClusterRequestRollingPolicy = None,
        version: str = None,
    ):
        # This parameter is deprecated. No need to pass values.
        self.component_name = component_name
        # Specifies whether to upgrade only master nodes. Valid values:
        # 
        # *   true: upgrades master nodes only.
        # *   false: upgrades both master and worker nodes.
        self.master_only = master_only
        # The target Kubernetes version for cluster upgrade.
        self.next_version = next_version
        # The rolling update configuration.
        self.rolling_policy = rolling_policy
        # This parameter is deprecated. Use next_version to specify the upgrade target Kubernetes version.
        self.version = version

    def validate(self):
        if self.rolling_policy:
            self.rolling_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_name is not None:
            result['component_name'] = self.component_name

        if self.master_only is not None:
            result['master_only'] = self.master_only

        if self.next_version is not None:
            result['next_version'] = self.next_version

        if self.rolling_policy is not None:
            result['rolling_policy'] = self.rolling_policy.to_map()

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('component_name') is not None:
            self.component_name = m.get('component_name')

        if m.get('master_only') is not None:
            self.master_only = m.get('master_only')

        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')

        if m.get('rolling_policy') is not None:
            temp_model = main_models.UpgradeClusterRequestRollingPolicy()
            self.rolling_policy = temp_model.from_map(m.get('rolling_policy'))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class UpgradeClusterRequestRollingPolicy(DaraModel):
    def __init__(
        self,
        max_parallelism: int = None,
    ):
        # The maximum number of nodes concurrently upgraded per batch.
        self.max_parallelism = max_parallelism

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_parallelism is not None:
            result['max_parallelism'] = self.max_parallelism

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('max_parallelism') is not None:
            self.max_parallelism = m.get('max_parallelism')

        return self

