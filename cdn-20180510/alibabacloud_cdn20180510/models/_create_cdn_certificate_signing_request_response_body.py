# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCdnCertificateSigningRequestResponseBody(DaraModel):
    def __init__(
        self,
        common_name: str = None,
        csr: str = None,
        pub_md_5: str = None,
        request_id: str = None,
    ):
        # The Common Name of the certificate.
        self.common_name = common_name
        # The content of the CSR file.
        self.csr = csr
        # The MD5 hash value of the certificate public key.
        self.pub_md_5 = pub_md_5
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.csr is not None:
            result['Csr'] = self.csr

        if self.pub_md_5 is not None:
            result['PubMd5'] = self.pub_md_5

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        if m.get('PubMd5') is not None:
            self.pub_md_5 = m.get('PubMd5')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

