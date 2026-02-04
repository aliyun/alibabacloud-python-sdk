# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnDomainPropertyResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        protocol: str = None,
        request_id: str = None,
    ):
        # The accelerated domain name.
        self.domain_name = domain_name
        # The protocol. Valid values:
        # 
        # *   **udp**
        # *   **tcp**
        self.protocol = protocol
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

