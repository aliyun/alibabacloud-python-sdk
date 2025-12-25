# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunBookIntroductionRequest(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        key_point_prompt: str = None,
        session_id: str = None,
        summary_prompt: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        self.key_point_prompt = key_point_prompt
        # This parameter is required.
        self.session_id = session_id
        self.summary_prompt = summary_prompt
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.key_point_prompt is not None:
            result['KeyPointPrompt'] = self.key_point_prompt

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.summary_prompt is not None:
            result['SummaryPrompt'] = self.summary_prompt

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('KeyPointPrompt') is not None:
            self.key_point_prompt = m.get('KeyPointPrompt')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SummaryPrompt') is not None:
            self.summary_prompt = m.get('SummaryPrompt')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

