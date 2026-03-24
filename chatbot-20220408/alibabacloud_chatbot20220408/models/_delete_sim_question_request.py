# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSimQuestionRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        sim_question_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.sim_question_id = sim_question_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')

        return self

