# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ReserveDomainRequest(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
        domain_name: str = None,
    ):
        self.channels = channels
        # This parameter is required.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

