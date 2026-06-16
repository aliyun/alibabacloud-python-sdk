# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMem0MemoriesShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        agent_id: str = None,
        app_id: str = None,
        context_store_id: str = None,
        metadata_shrink: str = None,
        org_id: str = None,
        project_id: str = None,
        run_id: str = None,
        user_id: str = None,
    ):
        self.agent_space = agent_space
        self.agent_id = agent_id
        self.app_id = app_id
        self.context_store_id = context_store_id
        self.metadata_shrink = metadata_shrink
        self.org_id = org_id
        self.project_id = project_id
        self.run_id = run_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.agent_id is not None:
            result['agent_id'] = self.agent_id

        if self.app_id is not None:
            result['app_id'] = self.app_id

        if self.context_store_id is not None:
            result['context_store_id'] = self.context_store_id

        if self.metadata_shrink is not None:
            result['metadata'] = self.metadata_shrink

        if self.org_id is not None:
            result['org_id'] = self.org_id

        if self.project_id is not None:
            result['project_id'] = self.project_id

        if self.run_id is not None:
            result['run_id'] = self.run_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')

        if m.get('context_store_id') is not None:
            self.context_store_id = m.get('context_store_id')

        if m.get('metadata') is not None:
            self.metadata_shrink = m.get('metadata')

        if m.get('org_id') is not None:
            self.org_id = m.get('org_id')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

