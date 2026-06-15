# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFeatureViewOnlineFeaturesShrinkRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        join_ids_shrink: str = None,
    ):
        self.config = config
        # The join IDs used to retrieve online features.
        # 
        # This parameter is required.
        self.join_ids_shrink = join_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.join_ids_shrink is not None:
            result['JoinIds'] = self.join_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('JoinIds') is not None:
            self.join_ids_shrink = m.get('JoinIds')

        return self

