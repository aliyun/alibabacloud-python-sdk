# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTlsInspectCertificateDownloadUrlResponseBody(DaraModel):
    def __init__(
        self,
        ca_cert_id: str = None,
        download_url: str = None,
        request_id: str = None,
    ):
        self.ca_cert_id = ca_cert_id
        self.download_url = download_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_cert_id is not None:
            result['CaCertId'] = self.ca_cert_id

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCertId') is not None:
            self.ca_cert_id = m.get('CaCertId')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

