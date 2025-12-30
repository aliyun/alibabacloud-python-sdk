# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class RunAgentRequest(DaraModel):
    def __init__(
        self,
        bot_id: str = None,
        model_id: str = None,
        stream: bool = None,
        thread_id: str = None,
        use_draft: bool = None,
        user_content: str = None,
        user_inputs: Dict[str, Any] = None,
        version_id: str = None,
    ):
        # This parameter is required.
        self.bot_id = bot_id
        self.model_id = model_id
        self.stream = stream
        self.thread_id = thread_id
        self.use_draft = use_draft
        # This parameter is required.
        self.user_content = user_content
        self.user_inputs = user_inputs
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_id is not None:
            result['botId'] = self.bot_id

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.stream is not None:
            result['stream'] = self.stream

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        if self.use_draft is not None:
            result['useDraft'] = self.use_draft

        if self.user_content is not None:
            result['userContent'] = self.user_content

        if self.user_inputs is not None:
            result['userInputs'] = self.user_inputs

        if self.version_id is not None:
            result['versionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('botId') is not None:
            self.bot_id = m.get('botId')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        if m.get('useDraft') is not None:
            self.use_draft = m.get('useDraft')

        if m.get('userContent') is not None:
            self.user_content = m.get('userContent')

        if m.get('userInputs') is not None:
            self.user_inputs = m.get('userInputs')

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        return self

