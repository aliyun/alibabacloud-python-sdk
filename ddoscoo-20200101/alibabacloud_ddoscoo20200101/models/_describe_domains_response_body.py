# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: List[str] = None,
        request_id: str = None,
    ):
        # An array consisting of details of the domain name for which the forwarding rules are configured.
        self.domains = domains
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domains is not None:
            result['Domains'] = self.domains

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

