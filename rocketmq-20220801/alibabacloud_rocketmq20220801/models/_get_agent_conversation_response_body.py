# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetAgentConversationResponseBody(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        created_at: str = None,
        current_run_status: str = None,
        id: str = None,
        pending_tool: Any = None,
        scenario_id: str = None,
        title: str = None,
        updated_at: str = None,
    ):
        self.conversation_id = conversation_id
        self.created_at = created_at
        self.current_run_status = current_run_status
        self.id = id
        self.pending_tool = pending_tool
        self.scenario_id = scenario_id
        self.title = title
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.current_run_status is not None:
            result['currentRunStatus'] = self.current_run_status

        if self.id is not None:
            result['id'] = self.id

        if self.pending_tool is not None:
            result['pendingTool'] = self.pending_tool

        if self.scenario_id is not None:
            result['scenarioId'] = self.scenario_id

        if self.title is not None:
            result['title'] = self.title

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('currentRunStatus') is not None:
            self.current_run_status = m.get('currentRunStatus')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('pendingTool') is not None:
            self.pending_tool = m.get('pendingTool')

        if m.get('scenarioId') is not None:
            self.scenario_id = m.get('scenarioId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

