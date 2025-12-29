# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class QuerySceneConfigsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scene_configs: List[main_models.QuerySceneConfigsResponseBodySceneConfigs] = None,
    ):
        # ID of this request.
        self.request_id = request_id
        # Willingness configuration list.
        self.scene_configs = scene_configs

    def validate(self):
        if self.scene_configs:
            for v1 in self.scene_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['sceneConfigs'] = []
        if self.scene_configs is not None:
            for k1 in self.scene_configs:
                result['sceneConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scene_configs = []
        if m.get('sceneConfigs') is not None:
            for k1 in m.get('sceneConfigs'):
                temp_model = main_models.QuerySceneConfigsResponseBodySceneConfigs()
                self.scene_configs.append(temp_model.from_map(k1))

        return self

class QuerySceneConfigsResponseBodySceneConfigs(DaraModel):
    def __init__(
        self,
        config: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        scene_id: int = None,
        type: str = None,
        version: int = None,
    ):
        # Specific configuration content, in JSON string format.
        self.config = config
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Configuration ID.
        self.id = id
        # Scene ID.
        self.scene_id = scene_id
        # Configuration type.
        self.type = type
        # Scene configuration version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.scene_id is not None:
            result['sceneId'] = self.scene_id

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

