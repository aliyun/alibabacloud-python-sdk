# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HiMarketAgentConfig(DaraModel):
    def __init__(
        self,
        agent_apiconfig: main_models.HiMarketAgentConfigAgentAPIConfig = None,
    ):
        self.agent_apiconfig = agent_apiconfig

    def validate(self):
        if self.agent_apiconfig:
            self.agent_apiconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_apiconfig is not None:
            result['agentAPIConfig'] = self.agent_apiconfig.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentAPIConfig') is not None:
            temp_model = main_models.HiMarketAgentConfigAgentAPIConfig()
            self.agent_apiconfig = temp_model.from_map(m.get('agentAPIConfig'))

        return self

class HiMarketAgentConfigAgentAPIConfig(DaraModel):
    def __init__(
        self,
        agent_protocols: List[str] = None,
        routes: List[main_models.HiMarketHttpRoute] = None,
    ):
        self.agent_protocols = agent_protocols
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
        if self.agent_protocols is not None:
            result['agentProtocols'] = self.agent_protocols

        result['routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['routes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentProtocols') is not None:
            self.agent_protocols = m.get('agentProtocols')

        self.routes = []
        if m.get('routes') is not None:
            for k1 in m.get('routes'):
                temp_model = main_models.HiMarketHttpRoute()
                self.routes.append(temp_model.from_map(k1))

        return self

