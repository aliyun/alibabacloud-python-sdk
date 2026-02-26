# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MemberAccountRequest(DaraModel):
    def __init__(
        self,
        shop_id: str = None,
    ):
        # This parameter is required.
        self.shop_id = shop_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.shop_id is not None:
            result['shopId'] = self.shop_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')

        return self

