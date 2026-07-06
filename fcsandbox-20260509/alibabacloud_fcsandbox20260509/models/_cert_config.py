# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CertConfig(DaraModel):
    def __init__(
        self,
        cert_name: str = None,
        certificate: str = None,
        private_key: str = None,
    ):
        self.cert_name = cert_name
        self.certificate = certificate
        self.private_key = private_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_name is not None:
            result['certName'] = self.cert_name

        if self.certificate is not None:
            result['certificate'] = self.certificate

        if self.private_key is not None:
            result['privateKey'] = self.private_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certName') is not None:
            self.cert_name = m.get('certName')

        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')

        if m.get('privateKey') is not None:
            self.private_key = m.get('privateKey')

        return self

