# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from darabonba.model import DaraModel

class ListPartitionsByNamesRequest(DaraModel):
    def __init__(
        self,
        specs: List[Dict[str, str]] = None,
    ):
        # 分区规格列表。
        self.specs = specs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.specs is not None:
            result['specs'] = self.specs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('specs') is not None:
            self.specs = m.get('specs')

        return self

