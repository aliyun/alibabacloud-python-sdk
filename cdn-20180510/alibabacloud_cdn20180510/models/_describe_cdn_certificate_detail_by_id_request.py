# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCdnCertificateDetailByIdRequest(DaraModel):
    def __init__(
        self,
        cert_id: str = None,
        cert_region: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the certificate.
        # 
        # This parameter is required.
        self.cert_id = cert_id
        # The region of the certificate. Valid values:
        # 
        # *   **ap-southeast-1**: Singapore
        # *   **cn-hangzhou**: China (Hangzhou)
        # 
        # Default value: **cn-hangzhou**
        self.cert_region = cert_region
        self.owner_id = owner_id
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

        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

