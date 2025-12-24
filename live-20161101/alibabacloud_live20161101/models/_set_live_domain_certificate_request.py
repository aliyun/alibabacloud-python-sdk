# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveDomainCertificateRequest(DaraModel):
    def __init__(
        self,
        cert_name: str = None,
        cert_type: str = None,
        domain_name: str = None,
        force_set: str = None,
        owner_id: int = None,
        sslpri: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
        security_token: str = None,
    ):
        # The certificate name.
        self.cert_name = cert_name
        # The certificate type. Valid values:
        # 
        # *   **upload**: a custom certificate
        # *   **cas**: a certificate that is purchased from Certificate Management Service
        # *   **free**: a free certificate (for testing)
        self.cert_type = cert_type
        # The domain name that is secured by the certificate. The domain name uses `HTTPS`-based acceleration.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies whether to check the certificate name for duplicates. A value of 1 indicates that the system does not perform the check and overwrites the information about the certificate that has the same name. Set the value to **1**.
        self.force_set = force_set
        self.owner_id = owner_id
        # The private key.
        # 
        # >  This parameter is required only if you set the SSLProtocol parameter to on.
        self.sslpri = sslpri
        # Specifies whether to enable the HTTPS certificate. Valid values:
        # 
        # *   **on**. If you set this parameter to **on**, you must also specify the SSLPub and SSLPri parameters.
        # *   **off**. This is the default value.
        # 
        # This parameter is required.
        self.sslprotocol = sslprotocol
        # The public key.
        # 
        # >  This parameter is required only if you set the SSLProtocol parameter to on.
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

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.force_set is not None:
            result['ForceSet'] = self.force_set

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

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ForceSet') is not None:
            self.force_set = m.get('ForceSet')

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

