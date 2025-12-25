# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveHotspotTagListRequest(DaraModel):
    def __init__(
        self,
        hotspot_list_json: str = None,
        scene_id: str = None,
    ):
        # This parameter is required.
        self.hotspot_list_json = hotspot_list_json
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotspot_list_json is not None:
            result['HotspotListJson'] = self.hotspot_list_json

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotspotListJson') is not None:
            self.hotspot_list_json = m.get('HotspotListJson')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

