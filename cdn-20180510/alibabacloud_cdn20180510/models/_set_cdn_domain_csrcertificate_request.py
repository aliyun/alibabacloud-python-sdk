# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCdnDomainCSRCertificateRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        server_certificate: str = None,
    ):
        # The accelerated domain name for which you want to configure an SSL certificate. The domain name must have HTTPS secure acceleration enabled.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The content of the certificate. The certificate must match the certificate signing request (CSR) created by calling the [CreateCdnCertificateSigningRequest](https://help.aliyun.com/document_detail/144478.html) operation. Make sure that the content of the certificate is encoded in Base64 and then encoded by encodeURIComponent.
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

