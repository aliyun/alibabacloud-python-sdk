# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class PolicyConfig(DaraModel):
    def __init__(
        self,
        ai_fallback_config: main_models.AiFallbackConfig = None,
        enable: bool = None,
        type: str = None,
    ):
        self.ai_fallback_config = ai_fallback_config
        self.enable = enable
        self.type = type

    def validate(self):
        if self.ai_fallback_config:
            self.ai_fallback_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_fallback_config is not None:
            result['aiFallbackConfig'] = self.ai_fallback_config.to_map()

        if self.enable is not None:
            result['enable'] = self.enable

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiFallbackConfig') is not None:
            temp_model = main_models.AiFallbackConfig()
            self.ai_fallback_config = temp_model.from_map(m.get('aiFallbackConfig'))

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

