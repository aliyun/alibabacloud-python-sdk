# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegistryCertConfig(DaraModel):
    def __init__(
        self,
        insecure: bool = None,
        root_ca_cert_base_64: str = None,
    ):
        self.insecure = insecure
        self.root_ca_cert_base_64 = root_ca_cert_base_64

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.insecure is not None:
            result['insecure'] = self.insecure

        if self.root_ca_cert_base_64 is not None:
            result['rootCaCertBase64'] = self.root_ca_cert_base_64

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('insecure') is not None:
            self.insecure = m.get('insecure')

        if m.get('rootCaCertBase64') is not None:
            self.root_ca_cert_base_64 = m.get('rootCaCertBase64')

        return self

