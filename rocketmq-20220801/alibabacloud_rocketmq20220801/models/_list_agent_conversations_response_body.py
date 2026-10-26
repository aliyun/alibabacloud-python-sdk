# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListAgentConversationsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAgentConversationsResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListAgentConversationsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

class ListAgentConversationsResponseBodyData(DaraModel):
    def __init__(
        self,
        access: Any = None,
        agent: Any = None,
        analysis_coverage: Any = None,
        conversation_id: str = None,
        created_at: str = None,
        created_by: str = None,
        current_run_status: str = None,
        edit_monitor_id: str = None,
        id: str = None,
        owner: Any = None,
        project: Any = None,
        scenario_id: str = None,
        share_scope: str = None,
        source_session_id: str = None,
        tagging: Any = None,
        title: str = None,
        tool_call_count: int = None,
        updated_at: str = None,
        used_skills: List[str] = None,
    ):
        self.access = access
        self.agent = agent
        self.analysis_coverage = analysis_coverage
        self.conversation_id = conversation_id
        self.created_at = created_at
        self.created_by = created_by
        self.current_run_status = current_run_status
        self.edit_monitor_id = edit_monitor_id
        self.id = id
        self.owner = owner
        self.project = project
        self.scenario_id = scenario_id
        self.share_scope = share_scope
        self.source_session_id = source_session_id
        self.tagging = tagging
        self.title = title
        self.tool_call_count = tool_call_count
        self.updated_at = updated_at
        self.used_skills = used_skills

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access is not None:
            result['access'] = self.access

        if self.agent is not None:
            result['agent'] = self.agent

        if self.analysis_coverage is not None:
            result['analysisCoverage'] = self.analysis_coverage

        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.current_run_status is not None:
            result['currentRunStatus'] = self.current_run_status

        if self.edit_monitor_id is not None:
            result['editMonitorId'] = self.edit_monitor_id

        if self.id is not None:
            result['id'] = self.id

        if self.owner is not None:
            result['owner'] = self.owner

        if self.project is not None:
            result['project'] = self.project

        if self.scenario_id is not None:
            result['scenarioId'] = self.scenario_id

        if self.share_scope is not None:
            result['shareScope'] = self.share_scope

        if self.source_session_id is not None:
            result['sourceSessionId'] = self.source_session_id

        if self.tagging is not None:
            result['tagging'] = self.tagging

        if self.title is not None:
            result['title'] = self.title

        if self.tool_call_count is not None:
            result['toolCallCount'] = self.tool_call_count

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.used_skills is not None:
            result['usedSkills'] = self.used_skills

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access') is not None:
            self.access = m.get('access')

        if m.get('agent') is not None:
            self.agent = m.get('agent')

        if m.get('analysisCoverage') is not None:
            self.analysis_coverage = m.get('analysisCoverage')

        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('currentRunStatus') is not None:
            self.current_run_status = m.get('currentRunStatus')

        if m.get('editMonitorId') is not None:
            self.edit_monitor_id = m.get('editMonitorId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('scenarioId') is not None:
            self.scenario_id = m.get('scenarioId')

        if m.get('shareScope') is not None:
            self.share_scope = m.get('shareScope')

        if m.get('sourceSessionId') is not None:
            self.source_session_id = m.get('sourceSessionId')

        if m.get('tagging') is not None:
            self.tagging = m.get('tagging')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('toolCallCount') is not None:
            self.tool_call_count = m.get('toolCallCount')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('usedSkills') is not None:
            self.used_skills = m.get('usedSkills')

        return self

