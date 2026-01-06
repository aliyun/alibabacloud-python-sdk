# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserCertificateDetailRequest(DaraModel):
    def __init__(
        self,
        cert_filter: bool = None,
        cert_id: int = None,
    ):
        # Specifies whether to filter return results. Valid values: true and false. Default value: false. **true** specifies that the Cert, Key, EncryptCert, EncryptPrivateKey, SignCert, and SignPrivateKey parameters are not returned. **false** specifies that the parameters are returned.
        self.cert_filter = cert_filter
        # The ID of the certificate.
        # 
        # >  You can call the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation to query the ID.
        # 
        # This parameter is required.
        self.cert_id = cert_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_filter is not None:
            result['CertFilter'] = self.cert_filter

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertFilter') is not None:
            self.cert_filter = m.get('CertFilter')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        return self

