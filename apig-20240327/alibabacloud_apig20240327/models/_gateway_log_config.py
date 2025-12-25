# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GatewayLogConfig(DaraModel):
    def __init__(
        self,
        sls_config: main_models.GatewayLogConfigSlsConfig = None,
    ):
        self.sls_config = sls_config

    def validate(self):
        if self.sls_config:
            self.sls_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sls_config is not None:
            result['slsConfig'] = self.sls_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('slsConfig') is not None:
            temp_model = main_models.GatewayLogConfigSlsConfig()
            self.sls_config = temp_model.from_map(m.get('slsConfig'))

        return self

class GatewayLogConfigSlsConfig(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        return self

