# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAudioNoteRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        biz_id: str = None,
        file_path: str = None,
        llm_model_id: int = None,
    ):
        # The ID of the notes agent. Specify the ID of a published recording notes agent.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The custom task ID defined by the business side. This ID is used to associate external business records during callbacks or troubleshooting.
        self.biz_id = biz_id
        # The storage path of the recording file in OSS. Use the FilePath returned by the upload address retrieval operation.
        # 
        # This parameter is required.
        self.file_path = file_path
        # The ID of the LLM model used for notes inference. If this parameter is not specified, the default model configuration of the agent is used.
        self.llm_model_id = llm_model_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.llm_model_id is not None:
            result['LlmModelId'] = self.llm_model_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('LlmModelId') is not None:
            self.llm_model_id = m.get('LlmModelId')

        return self

