# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDcdnL2VipsResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        request_id: str = None,
        vips: List[str] = None,
    ):
        # The accelerated domain name.
        self.domain_name = domain_name
        # The ID of the request.
        self.request_id = request_id
        # The virtual IP addresses (VIPs).
        self.vips = vips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vips is not None:
            result['Vips'] = self.vips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Vips') is not None:
            self.vips = m.get('Vips')

        return self

