# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ProtocolConfiguration(DaraModel):
    def __init__(
        self,
        protocol_settings: List[main_models.ProtocolSettings] = None,
        type: str = None,
    ):
        # 详细的协议配置信息
        self.protocol_settings = protocol_settings
        self.type = type

    def validate(self):
        if self.protocol_settings:
            for v1 in self.protocol_settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['protocolSettings'] = []
        if self.protocol_settings is not None:
            for k1 in self.protocol_settings:
                result['protocolSettings'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.protocol_settings = []
        if m.get('protocolSettings') is not None:
            for k1 in m.get('protocolSettings'):
                temp_model = main_models.ProtocolSettings()
                self.protocol_settings.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

