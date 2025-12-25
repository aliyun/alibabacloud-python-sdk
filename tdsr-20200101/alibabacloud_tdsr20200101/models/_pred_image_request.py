# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PredImageRequest(DaraModel):
    def __init__(
        self,
        correct_vertical: bool = None,
        count_detect_door: int = None,
        detect_door: bool = None,
        sub_scene_id: str = None,
    ):
        # This parameter is required.
        self.correct_vertical = correct_vertical
        self.count_detect_door = count_detect_door
        # This parameter is required.
        self.detect_door = detect_door
        # This parameter is required.
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.correct_vertical is not None:
            result['CorrectVertical'] = self.correct_vertical

        if self.count_detect_door is not None:
            result['CountDetectDoor'] = self.count_detect_door

        if self.detect_door is not None:
            result['DetectDoor'] = self.detect_door

        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorrectVertical') is not None:
            self.correct_vertical = m.get('CorrectVertical')

        if m.get('CountDetectDoor') is not None:
            self.count_detect_door = m.get('CountDetectDoor')

        if m.get('DetectDoor') is not None:
            self.detect_door = m.get('DetectDoor')

        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')

        return self

