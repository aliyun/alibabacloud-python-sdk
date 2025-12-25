# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddRelativePositionRequest(DaraModel):
    def __init__(
        self,
        relative_position: str = None,
        scene_id: str = None,
    ):
        # This parameter is required.
        self.relative_position = relative_position
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.relative_position is not None:
            result['RelativePosition'] = self.relative_position

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelativePosition') is not None:
            self.relative_position = m.get('RelativePosition')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

