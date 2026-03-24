# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCdnDomainSMCertificateRequest(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        domain_name: str = None,
        owner_id: int = None,
        sslprotocol: str = None,
        security_token: str = None,
    ):
        # The ID of the SM certificate that you want to configure. The identifier of the certificate. The value is Certificate ID-cn-hangzhou. For example, if the certificate ID is 123, set the value of this parameter to 123-cn-hangzhou.
        # 
        # This parameter is required.
        self.cert_identifier = cert_identifier
        # The accelerated domain name for which you want to configure the SM certificate.
        # 
        # > The domain name must use HTTPS acceleration.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # Specifies whether to enable the SSL certificate. Valid values:
        # 
        # *   **on**
        # *   **off**
        # 
        # This parameter is required.
        self.sslprotocol = sslprotocol
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

