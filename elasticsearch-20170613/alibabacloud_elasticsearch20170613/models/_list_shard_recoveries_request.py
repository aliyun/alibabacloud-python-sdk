# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListShardRecoveriesRequest(DaraModel):
    def __init__(
        self,
        active_only: bool = None,
    ):
        # Specifies whether to display shard data recovery tracking information. Valid values:
        # 
        # - true: Displays only ongoing shard data recovery tracking information.
        # 
        # - false: Displays all shard data recovery tracking information.
        self.active_only = active_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_only is not None:
            result['activeOnly'] = self.active_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeOnly') is not None:
            self.active_only = m.get('activeOnly')

        return self

