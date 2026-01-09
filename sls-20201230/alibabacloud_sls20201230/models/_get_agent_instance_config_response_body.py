# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetAgentInstanceConfigResponseBody(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        config: str = None,
        config_type: str = None,
        create_time: int = None,
        gray_configs: List[main_models.AgentInstanceConfigGrayConfigs] = None,
        last_modify_time: int = None,
    ):
        self.attributes = attributes
        self.config = config
        self.config_type = config_type
        self.create_time = create_time
        self.gray_configs = gray_configs
        self.last_modify_time = last_modify_time

    def validate(self):
        if self.gray_configs:
            for v1 in self.gray_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.config is not None:
            result['config'] = self.config

        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.create_time is not None:
            result['createTime'] = self.create_time

        result['grayConfigs'] = []
        if self.gray_configs is not None:
            for k1 in self.gray_configs:
                result['grayConfigs'].append(k1.to_map() if k1 else None)

        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        self.gray_configs = []
        if m.get('grayConfigs') is not None:
            for k1 in m.get('grayConfigs'):
                temp_model = main_models.AgentInstanceConfigGrayConfigs()
                self.gray_configs.append(temp_model.from_map(k1))

        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')

        return self

