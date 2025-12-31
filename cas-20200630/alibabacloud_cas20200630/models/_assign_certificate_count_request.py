# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssignCertificateCountRequest(DaraModel):
    def __init__(
        self,
        cert_total_count: int = None,
        id: int = None,
    ):
        self.cert_total_count = cert_total_count
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_total_count is not None:
            result['CertTotalCount'] = self.cert_total_count

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertTotalCount') is not None:
            self.cert_total_count = m.get('CertTotalCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

