# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CertInfo(DaraModel):
    def __init__(
        self,
        cert_body: str = None,
        cert_name: str = None,
        cert_privatekey: str = None,
    ):
        self.cert_body = cert_body
        self.cert_name = cert_name
        self.cert_privatekey = cert_privatekey

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_body is not None:
            result['cert_body'] = self.cert_body

        if self.cert_name is not None:
            result['cert_name'] = self.cert_name

        if self.cert_privatekey is not None:
            result['cert_privatekey'] = self.cert_privatekey

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_body') is not None:
            self.cert_body = m.get('cert_body')

        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')

        if m.get('cert_privatekey') is not None:
            self.cert_privatekey = m.get('cert_privatekey')

        return self

