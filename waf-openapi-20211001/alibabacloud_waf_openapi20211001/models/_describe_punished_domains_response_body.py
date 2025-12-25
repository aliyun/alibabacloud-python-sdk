# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePunishedDomainsResponseBody(DaraModel):
    def __init__(
        self,
        punished_domains: List[str] = None,
        request_id: str = None,
    ):
        # The domain names that are penalized for failing to obtain an ICP filing.
        self.punished_domains = punished_domains
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.punished_domains is not None:
            result['PunishedDomains'] = self.punished_domains

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PunishedDomains') is not None:
            self.punished_domains = m.get('PunishedDomains')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

