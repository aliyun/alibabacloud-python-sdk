# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunDocIntroductionRequest(DaraModel):
    def __init__(
        self,
        clean_cache: bool = None,
        doc_id: str = None,
        introduction_prompt: str = None,
        key_point_prompt: str = None,
        model_name: str = None,
        session_id: str = None,
        summary_prompt: str = None,
        workspace_id: str = None,
        reference_content: str = None,
    ):
        self.clean_cache = clean_cache
        # This parameter is required.
        self.doc_id = doc_id
        self.introduction_prompt = introduction_prompt
        self.key_point_prompt = key_point_prompt
        self.model_name = model_name
        # This parameter is required.
        self.session_id = session_id
        self.summary_prompt = summary_prompt
        # This parameter is required.
        self.workspace_id = workspace_id
        self.reference_content = reference_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clean_cache is not None:
            result['CleanCache'] = self.clean_cache

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.introduction_prompt is not None:
            result['IntroductionPrompt'] = self.introduction_prompt

        if self.key_point_prompt is not None:
            result['KeyPointPrompt'] = self.key_point_prompt

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.summary_prompt is not None:
            result['SummaryPrompt'] = self.summary_prompt

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.reference_content is not None:
            result['referenceContent'] = self.reference_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleanCache') is not None:
            self.clean_cache = m.get('CleanCache')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('IntroductionPrompt') is not None:
            self.introduction_prompt = m.get('IntroductionPrompt')

        if m.get('KeyPointPrompt') is not None:
            self.key_point_prompt = m.get('KeyPointPrompt')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SummaryPrompt') is not None:
            self.summary_prompt = m.get('SummaryPrompt')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('referenceContent') is not None:
            self.reference_content = m.get('referenceContent')

        return self

