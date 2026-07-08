# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunWritingShrinkRequest(DaraModel):
    def __init__(
        self,
        origin_session_id: str = None,
        prompt: str = None,
        reference_data_shrink: str = None,
        session_id: str = None,
        task_id: str = None,
        workspace_id: str = None,
        writing_config_shrink: str = None,
    ):
        # The ID of the original conversation to use for regeneration.
        self.origin_session_id = origin_session_id
        # The prompt.
        # 
        # This parameter is required.
        self.prompt = prompt
        # The reference article data for writing.
        self.reference_data_shrink = reference_data_shrink
        # The ID of a single-turn conversation.
        self.session_id = session_id
        # The ID of the task. You can reuse the same task ID in a multi-turn conversation.
        # 
        # > You do not need to specify TaskId. The system generates one automatically. If you use the same TaskId for multiple tasks, they are grouped into a single conversation.
        self.task_id = task_id
        # The unique ID of the Alibaba Cloud Model Studio workspace. For more information, see [Get a Workspace ID](https://help.aliyun.com/document_detail/2782167.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id
        # The writing configuration.
        self.writing_config_shrink = writing_config_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.writing_config_shrink is not None:
            result['WritingConfig'] = self.writing_config_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WritingConfig') is not None:
            self.writing_config_shrink = m.get('WritingConfig')

        return self

