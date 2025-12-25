# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLayoutDataRequest(DaraModel):
    def __init__(
        self,
        layout_data: str = None,
        sub_scene_id: str = None,
    ):
        # This parameter is required.
        self.layout_data = layout_data
        # This parameter is required.
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.layout_data is not None:
            result['LayoutData'] = self.layout_data

        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutData') is not None:
            self.layout_data = m.get('LayoutData')

        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')

        return self

