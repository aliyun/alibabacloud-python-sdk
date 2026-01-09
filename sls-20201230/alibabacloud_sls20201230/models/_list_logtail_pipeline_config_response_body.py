# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListLogtailPipelineConfigResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[str] = None,
        count: int = None,
        total: int = None,
    ):
        # The Logtail pipeline configurations that are returned on the current page.
        self.configs = configs
        # The number of Logtail pipeline configurations that are returned on the current page.
        self.count = count
        # The total number of Logtail pipeline configurations in the current project.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configs is not None:
            result['configs'] = self.configs

        if self.count is not None:
            result['count'] = self.count

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configs') is not None:
            self.configs = m.get('configs')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

