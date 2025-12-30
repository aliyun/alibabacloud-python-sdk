# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMainDomainNameResponseBody(DaraModel):
    def __init__(
        self,
        domain_level: int = None,
        domain_name: str = None,
        rr: str = None,
        request_id: str = None,
    ):
        # The level of the entered domain name.
        self.domain_level = domain_level
        # The domain name.
        self.domain_name = domain_name
        # The hostname.
        self.rr = rr
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_level is not None:
            result['DomainLevel'] = self.domain_level

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.rr is not None:
            result['RR'] = self.rr

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainLevel') is not None:
            self.domain_level = m.get('DomainLevel')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RR') is not None:
            self.rr = m.get('RR')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

