# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeClusterAddonsUpgradeStatusRequest(DaraModel):
    def __init__(
        self,
        component_ids: List[str] = None,
    ):
        # The list of component names.
        # 
        # This parameter is required.
        self.component_ids = component_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_ids is not None:
            result['componentIds'] = self.component_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentIds') is not None:
            self.component_ids = m.get('componentIds')

        return self

