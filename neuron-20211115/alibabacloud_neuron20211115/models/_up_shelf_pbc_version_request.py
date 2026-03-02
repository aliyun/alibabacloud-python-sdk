# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpShelfPbcVersionRequest(DaraModel):
    def __init__(
        self,
        market_id: int = None,
    ):
        # This parameter is required.
        self.market_id = market_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.market_id is not None:
            result['marketId'] = self.market_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        return self

