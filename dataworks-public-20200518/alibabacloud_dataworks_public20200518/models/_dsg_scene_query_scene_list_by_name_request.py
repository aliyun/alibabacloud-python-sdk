# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgSceneQuerySceneListByNameRequest(DaraModel):
    def __init__(
        self,
        scene_name: str = None,
    ):
        # The name of the data masking scenario. A fuzzy match is performed in the platform based on a keyword to search for the data masking scenario.
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        return self

