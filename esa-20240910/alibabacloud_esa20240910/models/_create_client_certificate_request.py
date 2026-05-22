# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClientCertificateRequest(DaraModel):
    def __init__(
        self,
        csr: str = None,
        pkey_type: str = None,
        site_id: int = None,
        validity_days: int = None,
    ):
        # The certificate signing request (CSR).
        self.csr = csr
        # The type of the private key algorithm.
        self.pkey_type = pkey_type
        # The website ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The validity period of the certificate. Unit: day.
        # 
        # This parameter is required.
        self.validity_days = validity_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.csr is not None:
            result['CSR'] = self.csr

        if self.pkey_type is not None:
            result['PkeyType'] = self.pkey_type

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.validity_days is not None:
            result['ValidityDays'] = self.validity_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CSR') is not None:
            self.csr = m.get('CSR')

        if m.get('PkeyType') is not None:
            self.pkey_type = m.get('PkeyType')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('ValidityDays') is not None:
            self.validity_days = m.get('ValidityDays')

        return self

