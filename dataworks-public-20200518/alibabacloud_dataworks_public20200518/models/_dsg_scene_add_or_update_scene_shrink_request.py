# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgSceneAddOrUpdateSceneShrinkRequest(DaraModel):
    def __init__(
        self,
        scenes_shrink: str = None,
    ):
        # The information about the level-2 data masking scenario.
        # 
        # This parameter is required.
        self.scenes_shrink = scenes_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scenes_shrink is not None:
            result['scenes'] = self.scenes_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scenes') is not None:
            self.scenes_shrink = m.get('scenes')

        return self

