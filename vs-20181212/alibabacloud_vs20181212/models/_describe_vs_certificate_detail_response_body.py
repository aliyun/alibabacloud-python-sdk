# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVsCertificateDetailResponseBody(DaraModel):
    def __init__(
        self,
        cert: str = None,
        cert_id: int = None,
        cert_name: str = None,
        key: str = None,
        request_id: str = None,
    ):
        self.cert = cert
        self.cert_id = cert_id
        self.cert_name = cert_name
        self.key = key
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert is not None:
            result['Cert'] = self.cert

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.key is not None:
            result['Key'] = self.key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

