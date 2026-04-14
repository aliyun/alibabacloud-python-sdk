# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class RegistryConfig(DaraModel):
    def __init__(
        self,
        auth_config: main_models.RegistryAuthConfig = None,
        cert_config: main_models.RegistryCertConfig = None,
        network_config: main_models.RegistryNetworkConfig = None,
    ):
        # 镜像仓库的认证配置信息
        self.auth_config = auth_config
        # 镜像仓库的证书配置信息
        self.cert_config = cert_config
        # 镜像仓库的网络配置信息
        self.network_config = network_config

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cert_config:
            self.cert_config.validate()
        if self.network_config:
            self.network_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()

        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()

        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = main_models.RegistryAuthConfig()
            self.auth_config = temp_model.from_map(m.get('authConfig'))

        if m.get('certConfig') is not None:
            temp_model = main_models.RegistryCertConfig()
            self.cert_config = temp_model.from_map(m.get('certConfig'))

        if m.get('networkConfig') is not None:
            temp_model = main_models.RegistryNetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        return self

