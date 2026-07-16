# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMainDomainNameResponseBody(DaraModel):
    def __init__(
        self,
        domain_level: int = None,
        main_domain_name: str = None,
        rr: str = None,
        request_id: str = None,
    ):
        # The level of the domain name.
        self.domain_level = domain_level
        # The root domain name.
        self.main_domain_name = main_domain_name
        # The host record.
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

        if self.main_domain_name is not None:
            result['MainDomainName'] = self.main_domain_name

        if self.rr is not None:
            result['RR'] = self.rr

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainLevel') is not None:
            self.domain_level = m.get('DomainLevel')

        if m.get('MainDomainName') is not None:
            self.main_domain_name = m.get('MainDomainName')

        if m.get('RR') is not None:
            self.rr = m.get('RR')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

