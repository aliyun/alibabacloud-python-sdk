# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListProductAbilitiesResponseBody(DaraModel):
    def __init__(
        self,
        product_abilities: List[str] = None,
        request_id: str = None,
    ):
        # Products supported by the edge node.
        self.product_abilities = product_abilities
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_abilities is not None:
            result['ProductAbilities'] = self.product_abilities

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductAbilities') is not None:
            self.product_abilities = m.get('ProductAbilities')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

