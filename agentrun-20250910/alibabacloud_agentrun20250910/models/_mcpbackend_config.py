# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class MCPBackendConfig(DaraModel):
    def __init__(
        self,
        scene: str = None,
        services: List[main_models.MCPServiceConfig] = None,
    ):
        self.scene = scene
        self.services = services

    def validate(self):
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene is not None:
            result['scene'] = self.scene

        result['services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['services'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')

        self.services = []
        if m.get('services') is not None:
            for k1 in m.get('services'):
                temp_model = main_models.MCPServiceConfig()
                self.services.append(temp_model.from_map(k1))

        return self

