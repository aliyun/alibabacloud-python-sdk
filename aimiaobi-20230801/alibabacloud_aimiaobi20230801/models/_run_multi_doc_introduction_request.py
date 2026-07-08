# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunMultiDocIntroductionRequest(DaraModel):
    def __init__(
        self,
        doc_ids: List[str] = None,
        key_point_prompt: str = None,
        model_name: str = None,
        session_id: str = None,
        summary_prompt: str = None,
        workspace_id: str = None,
    ):
        # Array of document IDs.
        # 
        # This parameter is required.
        self.doc_ids = doc_ids
        # Custom prompt for key points.
        self.key_point_prompt = key_point_prompt
        # Name of the custom model to use.
        self.model_name = model_name
        # Session ID.
        # 
        # This parameter is required.
        self.session_id = session_id
        # Custom prompt for the summary.
        self.summary_prompt = summary_prompt
        # Unique identifier of the Alibaba Cloud Model Studio workspace. To get this ID, see [Get the workspace ID](https://help.aliyun.com/document_detail/2782167.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_ids is not None:
            result['DocIds'] = self.doc_ids

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocIds') is not None:
            self.doc_ids = m.get('DocIds')

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

        return self

