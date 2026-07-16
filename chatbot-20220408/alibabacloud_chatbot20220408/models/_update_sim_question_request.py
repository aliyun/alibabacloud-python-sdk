# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSimQuestionRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        sim_question_id: int = None,
        title: str = None,
    ):
        # The key of the workspace. If you do not specify this parameter, the default workspace is used. You can find the key on the Business Management page of your master account.
        self.agent_key = agent_key
        # The ID of the similar question that you want to update.
        # 
        # This parameter is required.
        self.sim_question_id = sim_question_id
        # The new title of the similar question. The title can be up to 120 characters long.
        # 
        # This parameter is required.
        self.title = title

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

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

