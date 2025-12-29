# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySceneListShrinkRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        scene_states_shrink: str = None,
        scene_types_shrink: str = None,
        template_info_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.scene_states_shrink = scene_states_shrink
        self.scene_types_shrink = scene_types_shrink
        self.template_info_ids_shrink = template_info_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.scene_states_shrink is not None:
            result['SceneStates'] = self.scene_states_shrink

        if self.scene_types_shrink is not None:
            result['SceneTypes'] = self.scene_types_shrink

        if self.template_info_ids_shrink is not None:
            result['TemplateInfoIds'] = self.template_info_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('SceneStates') is not None:
            self.scene_states_shrink = m.get('SceneStates')

        if m.get('SceneTypes') is not None:
            self.scene_types_shrink = m.get('SceneTypes')

        if m.get('TemplateInfoIds') is not None:
            self.template_info_ids_shrink = m.get('TemplateInfoIds')

        return self

