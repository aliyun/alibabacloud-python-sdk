# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebCertConfig(DaraModel):
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
            result['CertName'] = self.cert_name

        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        return self

