# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchCreateMetaEntitiesShrinkRequest(DaraModel):
    def __init__(
        self,
        entities_shrink: str = None,
    ):
        # An entity list. You can create up to five entities in a batch. All entities in the batch must have the same `EntityType`.
        # 
        # This parameter is required.
        self.entities_shrink = entities_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entities_shrink is not None:
            result['Entities'] = self.entities_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entities') is not None:
            self.entities_shrink = m.get('Entities')

        return self

