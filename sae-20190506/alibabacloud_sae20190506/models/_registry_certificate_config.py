# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegistryCertificateConfig(DaraModel):
    def __init__(
        self,
        cert_base_64: str = None,
        insecure: bool = None,
    ):
        self.cert_base_64 = cert_base_64
        self.insecure = insecure

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_base_64 is not None:
            result['CertBase64'] = self.cert_base_64

        if self.insecure is not None:
            result['Insecure'] = self.insecure

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertBase64') is not None:
            self.cert_base_64 = m.get('CertBase64')

        if m.get('Insecure') is not None:
            self.insecure = m.get('Insecure')

        return self

