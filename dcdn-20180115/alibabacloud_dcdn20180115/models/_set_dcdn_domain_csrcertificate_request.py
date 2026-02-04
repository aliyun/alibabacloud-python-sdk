# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDcdnDomainCSRCertificateRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        server_certificate: str = None,
    ):
        # The domain name that is secured by the certificate. The domain name uses HTTPS acceleration.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The content of the certificate. The certificate must match the certificate signing request (CSR) created by calling the [CreateDcdnCertificateSigningRequest](https://help.aliyun.com/document_detail/144478.html) operation. Make sure that the certificate is in PEM format and its content is Base64-encoded and then encoded by encodeURIComponent.
        # 
        # This parameter is required.
        self.server_certificate = server_certificate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')

        return self

