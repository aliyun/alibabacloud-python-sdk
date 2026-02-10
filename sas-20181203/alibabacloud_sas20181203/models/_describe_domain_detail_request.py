# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainDetailRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        source_ip: str = None,
    ):
        # The domain name or the name of website that you want to query.
        # 
        # >  Fuzzy match is not supported. You must enter a complete domain name or a website.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

