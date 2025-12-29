# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSceneConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        id: int = None,
        scene_id: int = None,
    ):
        # Scene configuration information, in JSON format. For the specific structure definition, please refer to more information about the configuration.
        # 
        # This parameter is required.
        self.config = config
        # Willingness configuration ID.
        # 
        # This parameter is required.
        self.id = id
        # Selected authentication scene.
        # 
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.id is not None:
            result['id'] = self.id

        if self.scene_id is not None:
            result['sceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')

        return self

