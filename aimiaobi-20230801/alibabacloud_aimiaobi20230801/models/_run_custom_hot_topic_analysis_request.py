# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunCustomHotTopicAnalysisRequest(DaraModel):
    def __init__(
        self,
        ask_user: str = None,
        force_analysis_exists_topic: bool = None,
        prompt: str = None,
        session_id: str = None,
        task_id: str = None,
        user_back: str = None,
        workspace_id: str = None,
    ):
        self.ask_user = ask_user
        self.force_analysis_exists_topic = force_analysis_exists_topic
        # This parameter is required.
        self.prompt = prompt
        self.session_id = session_id
        self.task_id = task_id
        self.user_back = user_back
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ask_user is not None:
            result['AskUser'] = self.ask_user

        if self.force_analysis_exists_topic is not None:
            result['ForceAnalysisExistsTopic'] = self.force_analysis_exists_topic

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.user_back is not None:
            result['UserBack'] = self.user_back

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AskUser') is not None:
            self.ask_user = m.get('AskUser')

        if m.get('ForceAnalysisExistsTopic') is not None:
            self.force_analysis_exists_topic = m.get('ForceAnalysisExistsTopic')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UserBack') is not None:
            self.user_back = m.get('UserBack')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

