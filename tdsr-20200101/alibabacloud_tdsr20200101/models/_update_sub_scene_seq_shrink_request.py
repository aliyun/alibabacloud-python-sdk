# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSubSceneSeqShrinkRequest(DaraModel):
    def __init__(
        self,
        scene_id: str = None,
        sort_sub_scene_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.scene_id = scene_id
        # This parameter is required.
        self.sort_sub_scene_ids_shrink = sort_sub_scene_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.sort_sub_scene_ids_shrink is not None:
            result['SortSubSceneIds'] = self.sort_sub_scene_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SortSubSceneIds') is not None:
            self.sort_sub_scene_ids_shrink = m.get('SortSubSceneIds')

        return self

