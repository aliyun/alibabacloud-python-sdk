# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConnectableClustersRequest(DaraModel):
    def __init__(
        self,
        already_set_items: bool = None,
    ):
        # The ID of the instance that can communicate with each other.
        self.already_set_items = already_set_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_set_items is not None:
            result['alreadySetItems'] = self.already_set_items

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alreadySetItems') is not None:
            self.already_set_items = m.get('alreadySetItems')

        return self

