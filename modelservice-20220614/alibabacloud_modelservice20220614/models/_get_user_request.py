# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserRequest(DaraModel):
    def __init__(
        self,
        scene_type: str = None,
    ):
        self.scene_type = scene_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')

        return self

