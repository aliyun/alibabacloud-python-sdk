# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ImportHotelConfigRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        import_hotel_config: main_models.ImportHotelConfigRequestImportHotelConfig = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.import_hotel_config = import_hotel_config

    def validate(self):
        if self.import_hotel_config:
            self.import_hotel_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.import_hotel_config is not None:
            result['ImportHotelConfig'] = self.import_hotel_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('ImportHotelConfig') is not None:
            temp_model = main_models.ImportHotelConfigRequestImportHotelConfig()
            self.import_hotel_config = temp_model.from_map(m.get('ImportHotelConfig'))

        return self

class ImportHotelConfigRequestImportHotelConfig(DaraModel):
    def __init__(
        self,
        rcu_custom_scenes: List[main_models.ImportHotelConfigRequestImportHotelConfigRcuCustomScenes] = None,
    ):
        self.rcu_custom_scenes = rcu_custom_scenes

    def validate(self):
        if self.rcu_custom_scenes:
            for v1 in self.rcu_custom_scenes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RcuCustomScenes'] = []
        if self.rcu_custom_scenes is not None:
            for k1 in self.rcu_custom_scenes:
                result['RcuCustomScenes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rcu_custom_scenes = []
        if m.get('RcuCustomScenes') is not None:
            for k1 in m.get('RcuCustomScenes'):
                temp_model = main_models.ImportHotelConfigRequestImportHotelConfigRcuCustomScenes()
                self.rcu_custom_scenes.append(temp_model.from_map(k1))

        return self

class ImportHotelConfigRequestImportHotelConfigRcuCustomScenes(DaraModel):
    def __init__(
        self,
        corpus_list: List[str] = None,
        description: str = None,
        icon: str = None,
        name: str = None,
        scene_id: str = None,
    ):
        # This parameter is required.
        self.corpus_list = corpus_list
        self.description = description
        self.icon = icon
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.scene_id = scene_id

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

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

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

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

