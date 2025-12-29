# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class CreateRcuSceneRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        scene_id: str = None,
        scene_relation_ext_dto: main_models.CreateRcuSceneRequestSceneRelationExtDTO = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.scene_id = scene_id
        # This parameter is required.
        self.scene_relation_ext_dto = scene_relation_ext_dto

    def validate(self):
        if self.scene_relation_ext_dto:
            self.scene_relation_ext_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_relation_ext_dto is not None:
            result['SceneRelationExtDTO'] = self.scene_relation_ext_dto.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneRelationExtDTO') is not None:
            temp_model = main_models.CreateRcuSceneRequestSceneRelationExtDTO()
            self.scene_relation_ext_dto = temp_model.from_map(m.get('SceneRelationExtDTO'))

        return self

class CreateRcuSceneRequestSceneRelationExtDTO(DaraModel):
    def __init__(
        self,
        corpus_list: List[str] = None,
        description: str = None,
        icon: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.corpus_list = corpus_list
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.icon = icon
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corpus_list is not None:
            result['CorpusList'] = self.corpus_list

        if self.description is not None:
            result['Description'] = self.description

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpusList') is not None:
            self.corpus_list = m.get('CorpusList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

