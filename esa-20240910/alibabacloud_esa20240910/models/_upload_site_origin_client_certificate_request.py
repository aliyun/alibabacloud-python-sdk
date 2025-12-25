# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadSiteOriginClientCertificateRequest(DaraModel):
    def __init__(
        self,
        certificate: str = None,
        name: str = None,
        private_key: str = None,
        site_id: int = None,
    ):
        # The certificate content.
        # 
        # This parameter is required.
        self.certificate = certificate
        # The certificate name.
        self.name = name
        # The private key of the certificate.
        # 
        # This parameter is required.
        self.private_key = private_key
        # Site ID.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.name is not None:
            result['Name'] = self.name

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

