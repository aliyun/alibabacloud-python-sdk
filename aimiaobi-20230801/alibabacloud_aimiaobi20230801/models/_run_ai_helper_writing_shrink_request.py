# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunAiHelperWritingShrinkRequest(DaraModel):
    def __init__(
        self,
        distribute_writing: bool = None,
        prompt: str = None,
        prompt_mode: str = None,
        workspace_id: str = None,
        writing_params_shrink: str = None,
        writing_scene: str = None,
        writing_style: str = None,
    ):
        # Specifies whether to generate the text step by step.
        self.distribute_writing = distribute_writing
        # The prompt, which specifies the subject for the AI to write about.
        # 
        # This parameter is required.
        self.prompt = prompt
        # The prompt pattern. For example, PE indicates the advanced pattern and Template indicates the template pattern.
        self.prompt_mode = prompt_mode
        # The [workspace](https://help.aliyun.com/document_detail/2782167.html) ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id
        # The writing parameters from the previous form, specified as key-value pairs.
        self.writing_params_shrink = writing_params_shrink
        # The writing scenario. Valid values: government, media, market, office, and custom.
        # 
        # This parameter is required.
        self.writing_scene = writing_scene
        # The unique key for the writing style. Call the [ListWritingStyles](https://help.aliyun.com/document_detail/2922609.html) operation to get a list of styles for the specified scenario.
        # 
        # This parameter is required.
        self.writing_style = writing_style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distribute_writing is not None:
            result['DistributeWriting'] = self.distribute_writing

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.prompt_mode is not None:
            result['PromptMode'] = self.prompt_mode

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.writing_params_shrink is not None:
            result['WritingParams'] = self.writing_params_shrink

        if self.writing_scene is not None:
            result['WritingScene'] = self.writing_scene

        if self.writing_style is not None:
            result['WritingStyle'] = self.writing_style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributeWriting') is not None:
            self.distribute_writing = m.get('DistributeWriting')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('PromptMode') is not None:
            self.prompt_mode = m.get('PromptMode')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WritingParams') is not None:
            self.writing_params_shrink = m.get('WritingParams')

        if m.get('WritingScene') is not None:
            self.writing_scene = m.get('WritingScene')

        if m.get('WritingStyle') is not None:
            self.writing_style = m.get('WritingStyle')

        return self

