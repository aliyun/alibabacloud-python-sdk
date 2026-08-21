# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetVodDomainCertificateRequest(DaraModel):
    def __init__(
        self,
        cert_name: str = None,
        domain_name: str = None,
        owner_id: int = None,
        sslpri: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        security_token: str = None,
    ):
        # The certificate name.
        self.cert_name = cert_name
        # The accelerated domain name to which the certificate belongs. The domain name must be of the HTTPS acceleration type.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # The content of the private key. If you do not enable the certificate, you do not need to enter this parameter. If you configure a certificate, enter the private key content.
        self.sslpri = sslpri
        # Specifies whether to enable the HTTPS certificate. Valid values:
        # 
        # - **on**: enabled.
        # - **off** (default): disabled.
        # 
        # This parameter is required.
        self.sslprotocol = sslprotocol
        # The content of the security certificate. If you do not enable the certificate, you do not need to enter this parameter. If you configure a certificate, enter the certificate content.
        self.sslpub = sslpub
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri

        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol

        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')

        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')

        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

