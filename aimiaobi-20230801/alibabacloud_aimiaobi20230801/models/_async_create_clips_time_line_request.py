# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsyncCreateClipsTimeLineRequest(DaraModel):
    def __init__(
        self,
        additional_content: str = None,
        custom_content: str = None,
        no_ref_video: bool = None,
        process_prompt: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        self.additional_content = additional_content
        self.custom_content = custom_content
        self.no_ref_video = no_ref_video
        self.process_prompt = process_prompt
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_content is not None:
            result['AdditionalContent'] = self.additional_content

        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content

        if self.no_ref_video is not None:
            result['NoRefVideo'] = self.no_ref_video

        if self.process_prompt is not None:
            result['ProcessPrompt'] = self.process_prompt

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalContent') is not None:
            self.additional_content = m.get('AdditionalContent')

        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')

        if m.get('NoRefVideo') is not None:
            self.no_ref_video = m.get('NoRefVideo')

        if m.get('ProcessPrompt') is not None:
            self.process_prompt = m.get('ProcessPrompt')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

