# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateAgentSpecRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateAgentSpecRequestBody = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateAgentSpecRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class CreateAgentSpecRequestBody(DaraModel):
    def __init__(
        self,
        agent_spec_name: str = None,
        target_version: str = None,
    ):
        # The unique name of the AgentSpec.
        # 
        # This parameter is required.
        self.agent_spec_name = agent_spec_name
        # The draft version number. If not specified, the default value is 0.0.1.
        self.target_version = target_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_spec_name is not None:
            result['agentSpecName'] = self.agent_spec_name

        if self.target_version is not None:
            result['targetVersion'] = self.target_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpecName') is not None:
            self.agent_spec_name = m.get('agentSpecName')

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        return self

