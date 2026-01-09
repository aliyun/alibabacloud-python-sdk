# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class UpdateAgentInstanceConfigRequest(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        config: str = None,
        gray_configs: List[main_models.AgentInstanceConfigGrayConfigs] = None,
    ):
        self.attributes = attributes
        # This parameter is required.
        self.config = config
        self.gray_configs = gray_configs

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

        result['grayConfigs'] = []
        if self.gray_configs is not None:
            for k1 in self.gray_configs:
                result['grayConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('config') is not None:
            self.config = m.get('config')

        self.gray_configs = []
        if m.get('grayConfigs') is not None:
            for k1 in m.get('grayConfigs'):
                temp_model = main_models.AgentInstanceConfigGrayConfigs()
                self.gray_configs.append(temp_model.from_map(k1))

        return self

