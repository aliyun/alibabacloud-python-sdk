# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DiscoverEventSourceShrinkRequest(DaraModel):
    def __init__(
        self,
        source_my_sqlparameters_shrink: str = None,
    ):
        self.source_my_sqlparameters_shrink = source_my_sqlparameters_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_my_sqlparameters_shrink is not None:
            result['SourceMySQLParameters'] = self.source_my_sqlparameters_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceMySQLParameters') is not None:
            self.source_my_sqlparameters_shrink = m.get('SourceMySQLParameters')

        return self

