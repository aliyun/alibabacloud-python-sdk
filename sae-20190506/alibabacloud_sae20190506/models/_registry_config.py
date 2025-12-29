# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class RegistryConfig(DaraModel):
    def __init__(
        self,
        auth_config: main_models.RegistryAuthConfig = None,
        cert_config: main_models.RegistryCertConfig = None,
    ):
        self.auth_config = auth_config
        self.cert_config = cert_config

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cert_config:
            self.cert_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()

        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = main_models.RegistryAuthConfig()
            self.auth_config = temp_model.from_map(m.get('authConfig'))

        if m.get('certConfig') is not None:
            temp_model = main_models.RegistryCertConfig()
            self.cert_config = temp_model.from_map(m.get('certConfig'))

        return self

