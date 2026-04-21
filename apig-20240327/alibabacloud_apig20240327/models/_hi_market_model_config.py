# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HiMarketModelConfig(DaraModel):
    def __init__(
        self,
        model_apiconfig: main_models.HiMarketModelConfigModelAPIConfig = None,
    ):
        self.model_apiconfig = model_apiconfig

    def validate(self):
        if self.model_apiconfig:
            self.model_apiconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_apiconfig is not None:
            result['modelAPIConfig'] = self.model_apiconfig.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelAPIConfig') is not None:
            temp_model = main_models.HiMarketModelConfigModelAPIConfig()
            self.model_apiconfig = temp_model.from_map(m.get('modelAPIConfig'))

        return self

class HiMarketModelConfigModelAPIConfig(DaraModel):
    def __init__(
        self,
        ai_protocols: List[str] = None,
        model_category: str = None,
        routes: List[main_models.HiMarketHttpRoute] = None,
    ):
        self.ai_protocols = ai_protocols
        self.model_category = model_category
        self.routes = routes

    def validate(self):
        if self.routes:
            for v1 in self.routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_protocols is not None:
            result['aiProtocols'] = self.ai_protocols

        if self.model_category is not None:
            result['modelCategory'] = self.model_category

        result['routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['routes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiProtocols') is not None:
            self.ai_protocols = m.get('aiProtocols')

        if m.get('modelCategory') is not None:
            self.model_category = m.get('modelCategory')

        self.routes = []
        if m.get('routes') is not None:
            for k1 in m.get('routes'):
                temp_model = main_models.HiMarketHttpRoute()
                self.routes.append(temp_model.from_map(k1))

        return self

