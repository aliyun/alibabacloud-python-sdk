# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConnQuestionRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        conn_question_id: int = None,
        outline_id: int = None,
    ):
        # The key of the workspace. If this parameter is not specified, the default workspace is accessed. You can obtain the key on the business management page of the Alibaba Cloud account.
        self.agent_key = agent_key
        # The ID of the associated knowledge.
        # 
        # This parameter is required.
        self.conn_question_id = conn_question_id
        # The ID of the association.
        # 
        # This parameter is required.
        self.outline_id = outline_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.conn_question_id is not None:
            result['ConnQuestionId'] = self.conn_question_id

        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('ConnQuestionId') is not None:
            self.conn_question_id = m.get('ConnQuestionId')

        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')

        return self

