# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class TracingConfig(DaraModel):
    def __init__(
        self,
        jaeger_config: main_models.JaegerConfig = None,
        params: Any = None,
        type: str = None,
    ):
        self.jaeger_config = jaeger_config
        self.params = params
        self.type = type

    def validate(self):
        if self.jaeger_config:
            self.jaeger_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jaeger_config is not None:
            result['jaegerConfig'] = self.jaeger_config.to_map()

        if self.params is not None:
            result['params'] = self.params

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jaegerConfig') is not None:
            temp_model = main_models.JaegerConfig()
            self.jaeger_config = temp_model.from_map(m.get('jaegerConfig'))

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

