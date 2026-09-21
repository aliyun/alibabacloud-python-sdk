# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyCertificateRequest(DaraModel):
    def __init__(
        self,
        alg_type: str = None,
        domains: str = None,
        site_id: int = None,
        type: str = None,
    ):
        # The algorithm type.
        self.alg_type = alg_type
        # The list of domain names, separated by commas.
        # 
        # This parameter is required.
        self.domains = domains
        # The site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The certificate type. Valid values:
        # - lets_encrypt: Let\\"s Encrypt certificate.
        # - digicert_single: DigiCert single-domain certificate.
        # - digicert_wildcard: DigiCert wildcard domain certificate.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alg_type is not None:
            result['AlgType'] = self.alg_type

        if self.domains is not None:
            result['Domains'] = self.domains

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgType') is not None:
            self.alg_type = m.get('AlgType')

        if m.get('Domains') is not None:
            self.domains = m.get('Domains')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

