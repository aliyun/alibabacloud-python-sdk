# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PackSceneRequest(DaraModel):
    def __init__(
        self,
        scene_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.scene_id = scene_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

