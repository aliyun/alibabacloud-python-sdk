# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSceneConfigRequest(DaraModel):
    def __init__(
        self,
        scene_config_id: int = None,
    ):
        # ID of the intent authentication configuration.
        # 
        # This parameter is required.
        self.scene_config_id = scene_config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene_config_id is not None:
            result['sceneConfigId'] = self.scene_config_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneConfigId') is not None:
            self.scene_config_id = m.get('sceneConfigId')

        return self

