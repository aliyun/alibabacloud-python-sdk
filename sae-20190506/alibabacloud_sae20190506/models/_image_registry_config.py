# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ImageRegistryConfig(DaraModel):
    def __init__(
        self,
        auth_config: main_models.RegistryAuthenticationConfig = None,
        cert_config: main_models.RegistryCertificateConfig = None,
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
            result['AuthConfig'] = self.auth_config.to_map()

        if self.cert_config is not None:
            result['CertConfig'] = self.cert_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConfig') is not None:
            temp_model = main_models.RegistryAuthenticationConfig()
            self.auth_config = temp_model.from_map(m.get('AuthConfig'))

        if m.get('CertConfig') is not None:
            temp_model = main_models.RegistryCertificateConfig()
            self.cert_config = temp_model.from_map(m.get('CertConfig'))

        return self

