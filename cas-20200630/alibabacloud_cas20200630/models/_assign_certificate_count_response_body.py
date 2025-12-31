# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssignCertificateCountResponseBody(DaraModel):
    def __init__(
        self,
        cert_count: int = None,
        current_year_free_cert_count: int = None,
        request_id: str = None,
    ):
        self.cert_count = cert_count
        self.current_year_free_cert_count = current_year_free_cert_count
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_count is not None:
            result['CertCount'] = self.cert_count

        if self.current_year_free_cert_count is not None:
            result['CurrentYearFreeCertCount'] = self.current_year_free_cert_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCount') is not None:
            self.cert_count = m.get('CertCount')

        if m.get('CurrentYearFreeCertCount') is not None:
            self.current_year_free_cert_count = m.get('CurrentYearFreeCertCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

