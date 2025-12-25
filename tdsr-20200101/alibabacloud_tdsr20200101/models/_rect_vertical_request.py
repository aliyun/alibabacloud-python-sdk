# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RectVerticalRequest(DaraModel):
    def __init__(
        self,
        count_detect_door: int = None,
        detect_door: bool = None,
        sub_scene_id: str = None,
        vertical_rect: str = None,
    ):
        self.count_detect_door = count_detect_door
        self.detect_door = detect_door
        # This parameter is required.
        self.sub_scene_id = sub_scene_id
        # This parameter is required.
        self.vertical_rect = vertical_rect

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count_detect_door is not None:
            result['CountDetectDoor'] = self.count_detect_door

        if self.detect_door is not None:
            result['DetectDoor'] = self.detect_door

        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id

        if self.vertical_rect is not None:
            result['VerticalRect'] = self.vertical_rect

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountDetectDoor') is not None:
            self.count_detect_door = m.get('CountDetectDoor')

        if m.get('DetectDoor') is not None:
            self.detect_door = m.get('DetectDoor')

        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')

        if m.get('VerticalRect') is not None:
            self.vertical_rect = m.get('VerticalRect')

        return self

