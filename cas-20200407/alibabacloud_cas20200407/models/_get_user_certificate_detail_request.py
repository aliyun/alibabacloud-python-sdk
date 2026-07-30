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
        # Specifies whether to filter certificate content. If set to **true**, the Cert, Key, EncryptCert, EncryptPrivateKey, SignCert, and SignPrivateKey fields are not returned. If set to **false**, these fields are returned. Default value: false.
        self.cert_filter = cert_filter
        # The certificate ID.
        # > You can obtain this ID by calling [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html).
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

