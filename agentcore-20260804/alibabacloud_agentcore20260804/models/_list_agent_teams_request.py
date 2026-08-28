# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListAgentTeamsRequest(DaraModel):
    def __init__(
        self,
        body: main_models.ListAgentTeamsRequestBody = None,
    ):
        # The request parameters for querying the agent team list.
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
            temp_model = main_models.ListAgentTeamsRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class ListAgentTeamsRequestBody(DaraModel):
    def __init__(
        self,
        agent_ids: List[str] = None,
    ):
        # The list of agent IDs for which to query team information.
        # 
        # This parameter is required.
        self.agent_ids = agent_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_ids is not None:
            result['agentIds'] = self.agent_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentIds') is not None:
            self.agent_ids = m.get('agentIds')

        return self

