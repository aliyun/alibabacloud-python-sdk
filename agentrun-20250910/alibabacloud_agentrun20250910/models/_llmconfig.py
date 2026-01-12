# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class LLMConfig(DaraModel):
    def __init__(
        self,
        config: main_models.LLMConfigConfig = None,
        model_service_name: str = None,
    ):
        self.config = config
        self.model_service_name = model_service_name

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.model_service_name is not None:
            result['modelServiceName'] = self.model_service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.LLMConfigConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('modelServiceName') is not None:
            self.model_service_name = m.get('modelServiceName')

        return self

class LLMConfigConfig(DaraModel):
    def __init__(
        self,
        model: str = None,
    ):
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['model'] = self.model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model') is not None:
            self.model = m.get('model')

        return self

