# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDifyEditionsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        data_region: str = None,
    ):
        self.client_token = client_token
        self.data_region = data_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.data_region is not None:
            result['DataRegion'] = self.data_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataRegion') is not None:
            self.data_region = m.get('DataRegion')

        return self

