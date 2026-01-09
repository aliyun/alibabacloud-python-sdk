# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class MLLabelParam(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        label_id: str = None,
        last_modify_time: int = None,
        name: str = None,
        settings: List[main_models.MLLabelParamSettings] = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.label_id = label_id
        self.last_modify_time = last_modify_time
        self.name = name
        self.settings = settings
        self.type = type

    def validate(self):
        if self.settings:
            for v1 in self.settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.label_id is not None:
            result['labelId'] = self.label_id

        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time

        if self.name is not None:
            result['name'] = self.name

        result['settings'] = []
        if self.settings is not None:
            for k1 in self.settings:
                result['settings'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')

        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.settings = []
        if m.get('settings') is not None:
            for k1 in m.get('settings'):
                temp_model = main_models.MLLabelParamSettings()
                self.settings.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class MLLabelParamSettings(DaraModel):
    def __init__(
        self,
        config: str = None,
        mode: str = None,
        type: str = None,
        version: str = None,
    ):
        self.config = config
        self.mode = mode
        self.type = type
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

        if self.mode is not None:
            result['mode'] = self.mode

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

