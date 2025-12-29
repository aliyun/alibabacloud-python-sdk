# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ModifyNodePoolNodeConfigRequest(DaraModel):
    def __init__(
        self,
        containerd_config: main_models.ContainerdConfig = None,
        kubelet_config: main_models.KubeletConfig = None,
        os_config: main_models.ModifyNodePoolNodeConfigRequestOsConfig = None,
        rolling_policy: main_models.ModifyNodePoolNodeConfigRequestRollingPolicy = None,
    ):
        # The containerd runtime configuration.
        self.containerd_config = containerd_config
        # The kubelet configurations.
        self.kubelet_config = kubelet_config
        # The OS configuration.
        self.os_config = os_config
        # The rolling policy configuration.
        self.rolling_policy = rolling_policy

    def validate(self):
        if self.containerd_config:
            self.containerd_config.validate()
        if self.kubelet_config:
            self.kubelet_config.validate()
        if self.os_config:
            self.os_config.validate()
        if self.rolling_policy:
            self.rolling_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.containerd_config is not None:
            result['containerd_config'] = self.containerd_config.to_map()

        if self.kubelet_config is not None:
            result['kubelet_config'] = self.kubelet_config.to_map()

        if self.os_config is not None:
            result['os_config'] = self.os_config.to_map()

        if self.rolling_policy is not None:
            result['rolling_policy'] = self.rolling_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containerd_config') is not None:
            temp_model = main_models.ContainerdConfig()
            self.containerd_config = temp_model.from_map(m.get('containerd_config'))

        if m.get('kubelet_config') is not None:
            temp_model = main_models.KubeletConfig()
            self.kubelet_config = temp_model.from_map(m.get('kubelet_config'))

        if m.get('os_config') is not None:
            temp_model = main_models.ModifyNodePoolNodeConfigRequestOsConfig()
            self.os_config = temp_model.from_map(m.get('os_config'))

        if m.get('rolling_policy') is not None:
            temp_model = main_models.ModifyNodePoolNodeConfigRequestRollingPolicy()
            self.rolling_policy = temp_model.from_map(m.get('rolling_policy'))

        return self

class ModifyNodePoolNodeConfigRequestRollingPolicy(DaraModel):
    def __init__(
        self,
        max_parallelism: int = None,
    ):
        # The maximum number of unavailable nodes.
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

class ModifyNodePoolNodeConfigRequestOsConfig(DaraModel):
    def __init__(
        self,
        hugepage: main_models.Hugepage = None,
        sysctl: Dict[str, Any] = None,
    ):
        self.hugepage = hugepage
        # The sysctl configuration.
        self.sysctl = sysctl

    def validate(self):
        if self.hugepage:
            self.hugepage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hugepage is not None:
            result['hugepage'] = self.hugepage.to_map()

        if self.sysctl is not None:
            result['sysctl'] = self.sysctl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hugepage') is not None:
            temp_model = main_models.Hugepage()
            self.hugepage = temp_model.from_map(m.get('hugepage'))

        if m.get('sysctl') is not None:
            self.sysctl = m.get('sysctl')

        return self

