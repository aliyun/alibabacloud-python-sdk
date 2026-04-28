# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListForwardStrategyBindingItemsRequest(DaraModel):
    def __init__(
        self,
        forward_ids: List[str] = None,
        item_type: str = None,
    ):
        # This parameter is required.
        self.forward_ids = forward_ids
        self.item_type = item_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_ids is not None:
            result['ForwardIds'] = self.forward_ids

        if self.item_type is not None:
            result['ItemType'] = self.item_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardIds') is not None:
            self.forward_ids = m.get('ForwardIds')

        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')

        return self

