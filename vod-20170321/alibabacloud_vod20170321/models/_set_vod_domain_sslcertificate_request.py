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
        # The certificate ID.
        self.cert_id = cert_id
        # The certificate name.
        self.cert_name = cert_name
        # The certificate region. Valid values:
        # - **ap-southeast-1** (Singapore)
        # - **cn-hangzhou** (Hangzhou)
        # 
        # Default value: **cn-hangzhou**.
        self.cert_region = cert_region
        # The certificate type. Valid values:
        # 
        # - **upload**: an uploaded certificate.
        # - **cas**: a certificate from SSL Certificates Service.
        self.cert_type = cert_type
        # The accelerated domain name for ApsaraVideo VOD.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies whether to distribute the certificate in a canary release environment. Valid values:
        # 
        # - **staging**: distributes the certificate in a canary release environment.
        # 
        # If this parameter is not specified or set to any other value, the certificate is formally distributed.
        self.env = env
        self.owner_id = owner_id
        # The content of the private key. If you do not enable the certificate, you do not need to specify this parameter. If you configure a certificate, enter the private key content.
        self.sslpri = sslpri
        # Specifies whether to enable the HTTPS certificate. Valid values:
        # 
        # - **on**: Enabled.
        # - **off**: Disabled.
        # 
        # This parameter is required.
        self.sslprotocol = sslprotocol
        # The content of the security certificate. If you do not enable the certificate, you do not need to specify this parameter. If you configure a certificate, enter the certificate content.
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

