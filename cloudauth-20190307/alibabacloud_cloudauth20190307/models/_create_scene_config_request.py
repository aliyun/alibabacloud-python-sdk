# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSceneConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        scene_id: int = None,
        type: str = None,
    ):
        # Intention authentication configuration, as a JSON string.
        # 
        # This parameter is required.
        self.config = config
        # Scene ID.
        # 
        # This parameter is required.
        self.scene_id = scene_id
        # Configuration type.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.scene_id is not None:
            result['sceneId'] = self.scene_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

