# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePrivateRAGServiceResponseBody(DaraModel):
    def __init__(
        self,
        ca_cert: str = None,
        request_id: str = None,
    ):
        self.ca_cert = ca_cert
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_cert is not None:
            result['CaCert'] = self.ca_cert

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCert') is not None:
            self.ca_cert = m.get('CaCert')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

