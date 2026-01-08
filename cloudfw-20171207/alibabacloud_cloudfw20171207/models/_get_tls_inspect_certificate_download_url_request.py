# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTlsInspectCertificateDownloadUrlRequest(DaraModel):
    def __init__(
        self,
        ca_cert_id: str = None,
    ):
        # This parameter is required.
        self.ca_cert_id = ca_cert_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_cert_id is not None:
            result['CaCertId'] = self.ca_cert_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCertId') is not None:
            self.ca_cert_id = m.get('CaCertId')

        return self

