# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitHtmlTranslateTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        ext_shrink: str = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext_shrink = ext_shrink
        self.format = format
        self.scene = scene
        self.source_language = source_language
        self.target_language = target_language
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_shrink is not None:
            result['ext'] = self.ext_shrink

        if self.format is not None:
            result['format'] = self.format

        if self.scene is not None:
            result['scene'] = self.scene

        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language

        if self.target_language is not None:
            result['targetLanguage'] = self.target_language

        if self.text is not None:
            result['text'] = self.text

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            self.ext_shrink = m.get('ext')

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')

        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

