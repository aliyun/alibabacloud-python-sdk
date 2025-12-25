# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class TlsCipherSuitesConfig(DaraModel):
    def __init__(
        self,
        config_type: str = None,
        tls_cipher_suite: List[main_models.TlsCipherSuitesConfigTlsCipherSuite] = None,
    ):
        self.config_type = config_type
        self.tls_cipher_suite = tls_cipher_suite

    def validate(self):
        if self.tls_cipher_suite:
            for v1 in self.tls_cipher_suite:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_type is not None:
            result['configType'] = self.config_type

        result['tlsCipherSuite'] = []
        if self.tls_cipher_suite is not None:
            for k1 in self.tls_cipher_suite:
                result['tlsCipherSuite'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        self.tls_cipher_suite = []
        if m.get('tlsCipherSuite') is not None:
            for k1 in m.get('tlsCipherSuite'):
                temp_model = main_models.TlsCipherSuitesConfigTlsCipherSuite()
                self.tls_cipher_suite.append(temp_model.from_map(k1))

        return self

class TlsCipherSuitesConfigTlsCipherSuite(DaraModel):
    def __init__(
        self,
        name: str = None,
        support_versions: List[str] = None,
    ):
        self.name = name
        self.support_versions = support_versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.support_versions is not None:
            result['supportVersions'] = self.support_versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('supportVersions') is not None:
            self.support_versions = m.get('supportVersions')

        return self

