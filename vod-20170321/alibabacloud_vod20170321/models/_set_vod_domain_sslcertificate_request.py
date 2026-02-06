# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetVodDomainSSLCertificateRequest(DaraModel):
    def __init__(
        self,
        cert_id: int = None,
        cert_name: str = None,
        cert_region: str = None,
        cert_type: str = None,
        domain_name: str = None,
        env: str = None,
        owner_id: int = None,
        sslpri: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        security_token: str = None,
    ):
        # The ID of the certificate.
        self.cert_id = cert_id
        # The name of the certificate.
        self.cert_name = cert_name
        # The region of the certificate. Valid values:
        # 
        # *   **ap-southeast-1**: Singapore
        # *   **cn-hangzhou**: China (Hangzhou)
        # 
        # Default value: **cn-hangzhou**
        self.cert_region = cert_region
        # The type of the certificate.
        # 
        # *   **upload**: a user-uploaded SSL certificate.
        # *   **cas**: a certificate that is acquired through Certificate Management Service.
        self.cert_type = cert_type
        # VOD acceleration domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies whether the certificate is issued in canary releases. If you set this parameter to **staging**, the certificate is issued in canary releases. If you do not specify this parameter or set this parameter to other values, the certificate is officially issued.
        self.env = env
        self.owner_id = owner_id
        # The private key. This parameter is required only if you enable the certificate.
        self.sslpri = sslpri
        # Specifies whether to enable the SSL certificate. Default value: off. Valid values:
        # 
        # *   **on**
        # *   **off**
        # 
        # This parameter is required.
        self.sslprotocol = sslprotocol
        # The content of the certificate. This parameter is required only if you enable the SSL certificate.
        self.sslpub = sslpub
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.env is not None:
            result['Env'] = self.env

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
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

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

