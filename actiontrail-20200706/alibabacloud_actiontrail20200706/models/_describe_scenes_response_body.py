# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class DescribeScenesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scene_list: List[main_models.DescribeScenesResponseBodySceneList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of scenarios.
        self.scene_list = scene_list

    def validate(self):
        if self.scene_list:
            for v1 in self.scene_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SceneList'] = []
        if self.scene_list is not None:
            for k1 in self.scene_list:
                result['SceneList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scene_list = []
        if m.get('SceneList') is not None:
            for k1 in m.get('SceneList'):
                temp_model = main_models.DescribeScenesResponseBodySceneList()
                self.scene_list.append(temp_model.from_map(k1))

        return self

class DescribeScenesResponseBodySceneList(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        scene_id: str = None,
        token: str = None,
        type: str = None,
    ):
        # The description of the scenario.
        self.description = description
        # The name of the scenario.
        self.name = name
        # The ID of the scenario.
        self.scene_id = scene_id
        # The identifier for the scenario category.
        self.token = token
        # The type of the scenario.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.token is not None:
            result['Token'] = self.token

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

