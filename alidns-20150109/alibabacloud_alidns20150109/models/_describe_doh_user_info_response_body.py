# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDohUserInfoResponseBody(DaraModel):
    def __init__(
        self,
        domain_count: int = None,
        pdns_id: int = None,
        request_id: str = None,
        sub_domain_count: int = None,
    ):
        # The number of accessed domains.
        self.domain_count = domain_count
        # The ID of the Alibaba Cloud public DNS user.
        self.pdns_id = pdns_id
        # The ID of the request.
        self.request_id = request_id
        # The number of accessed subdomains.
        self.sub_domain_count = sub_domain_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count

        if self.pdns_id is not None:
            result['PdnsId'] = self.pdns_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sub_domain_count is not None:
            result['SubDomainCount'] = self.sub_domain_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')

        if m.get('PdnsId') is not None:
            self.pdns_id = m.get('PdnsId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubDomainCount') is not None:
            self.sub_domain_count = m.get('SubDomainCount')

        return self

