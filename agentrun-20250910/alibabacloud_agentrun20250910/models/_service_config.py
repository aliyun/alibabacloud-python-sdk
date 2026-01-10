# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ServiceConfig(DaraModel):
    def __init__(
        self,
        ai_service_config: main_models.AiServiceConfig = None,
        name: str = None,
    ):
        self.ai_service_config = ai_service_config
        self.name = name

    def validate(self):
        if self.ai_service_config:
            self.ai_service_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_service_config is not None:
            result['aiServiceConfig'] = self.ai_service_config.to_map()

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiServiceConfig') is not None:
            temp_model = main_models.AiServiceConfig()
            self.ai_service_config = temp_model.from_map(m.get('aiServiceConfig'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

