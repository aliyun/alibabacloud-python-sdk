# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteForwardStrategyRequest(DaraModel):
    def __init__(
        self,
        forward_id: str = None,
    ):
        # The forwarding rule ID.
        # 
        # This parameter is required.
        self.forward_id = forward_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_id is not None:
            result['ForwardId'] = self.forward_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardId') is not None:
            self.forward_id = m.get('ForwardId')

        return self

