# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QuerySceneListRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        scene_states: List[int] = None,
        scene_types: List[str] = None,
        template_info_ids: List[str] = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.scene_states = scene_states
        self.scene_types = scene_types
        self.template_info_ids = template_info_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.scene_states is not None:
            result['SceneStates'] = self.scene_states

        if self.scene_types is not None:
            result['SceneTypes'] = self.scene_types

        if self.template_info_ids is not None:
            result['TemplateInfoIds'] = self.template_info_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('SceneStates') is not None:
            self.scene_states = m.get('SceneStates')

        if m.get('SceneTypes') is not None:
            self.scene_types = m.get('SceneTypes')

        if m.get('TemplateInfoIds') is not None:
            self.template_info_ids = m.get('TemplateInfoIds')

        return self

