# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterCaCertificateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sn: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The serial number of the registered CA certificate. The serial number is the unique identifier of a CA certificate.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sn is not None:
            result['Sn'] = self.sn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        return self

