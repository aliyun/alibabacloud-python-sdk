# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PutLogStoreConfigRequest(DaraModel):
    def __init__(
        self,
        client_ip_headers: List[str] = None,
    ):
        self.client_ip_headers = client_ip_headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip_headers is not None:
            result['clientIpHeaders'] = self.client_ip_headers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientIpHeaders') is not None:
            self.client_ip_headers = m.get('clientIpHeaders')

        return self

