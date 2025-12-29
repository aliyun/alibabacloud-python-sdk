# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class QuerySceneListResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        results: List[main_models.QuerySceneListResponseBodyResults] = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.results = results
        self.status_code = status_code

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.QuerySceneListResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class QuerySceneListResponseBodyResults(DaraModel):
    def __init__(
        self,
        icon: str = None,
        scene_id: str = None,
        scene_name: str = None,
        scene_source: str = None,
        scene_state: int = None,
        scene_type: str = None,
        template_info_dtolist: List[main_models.QuerySceneListResponseBodyResultsTemplateInfoDTOList] = None,
        unavailable_reason: str = None,
    ):
        self.icon = icon
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.scene_source = scene_source
        self.scene_state = scene_state
        self.scene_type = scene_type
        self.template_info_dtolist = template_info_dtolist
        self.unavailable_reason = unavailable_reason

    def validate(self):
        if self.template_info_dtolist:
            for v1 in self.template_info_dtolist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icon is not None:
            result['Icon'] = self.icon

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.scene_source is not None:
            result['SceneSource'] = self.scene_source

        if self.scene_state is not None:
            result['SceneState'] = self.scene_state

        if self.scene_type is not None:
            result['SceneType'] = self.scene_type

        result['TemplateInfoDTOList'] = []
        if self.template_info_dtolist is not None:
            for k1 in self.template_info_dtolist:
                result['TemplateInfoDTOList'].append(k1.to_map() if k1 else None)

        if self.unavailable_reason is not None:
            result['UnavailableReason'] = self.unavailable_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('SceneSource') is not None:
            self.scene_source = m.get('SceneSource')

        if m.get('SceneState') is not None:
            self.scene_state = m.get('SceneState')

        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')

        self.template_info_dtolist = []
        if m.get('TemplateInfoDTOList') is not None:
            for k1 in m.get('TemplateInfoDTOList'):
                temp_model = main_models.QuerySceneListResponseBodyResultsTemplateInfoDTOList()
                self.template_info_dtolist.append(temp_model.from_map(k1))

        if m.get('UnavailableReason') is not None:
            self.unavailable_reason = m.get('UnavailableReason')

        return self

class QuerySceneListResponseBodyResultsTemplateInfoDTOList(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

