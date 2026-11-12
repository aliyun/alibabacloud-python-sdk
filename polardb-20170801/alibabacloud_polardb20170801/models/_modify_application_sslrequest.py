# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApplicationSSLRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        ca_pem: str = None,
        cert_pem: str = None,
        key_pem: str = None,
        ssl_enabled: bool = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The server certificate chain in PEM format. This parameter is optional.
        self.ca_pem = ca_pem
        # The server certificate in PEM format. This parameter is provided when you use a bring-your-own (BYO) certificate. It must match KeyPem and override the instance connection domain name. This parameter is allowed only when CA SSL is enabled for the instance.
        self.cert_pem = cert_pem
        # The server private key in PEM format. PKCS#1, PKCS#8, and EC SEC1 formats are supported.
        self.key_pem = key_pem
        # Specifies whether SSL is enabled.
        # 
        # This parameter is required.
        self.ssl_enabled = ssl_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.ca_pem is not None:
            result['CaPem'] = self.ca_pem

        if self.cert_pem is not None:
            result['CertPem'] = self.cert_pem

        if self.key_pem is not None:
            result['KeyPem'] = self.key_pem

        if self.ssl_enabled is not None:
            result['SslEnabled'] = self.ssl_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('CaPem') is not None:
            self.ca_pem = m.get('CaPem')

        if m.get('CertPem') is not None:
            self.cert_pem = m.get('CertPem')

        if m.get('KeyPem') is not None:
            self.key_pem = m.get('KeyPem')

        if m.get('SslEnabled') is not None:
            self.ssl_enabled = m.get('SslEnabled')

        return self

