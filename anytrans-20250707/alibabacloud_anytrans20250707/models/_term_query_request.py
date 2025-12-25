# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_anytrans20250707 import models as main_models
from darabonba.model import DaraModel

class TermQueryRequest(DaraModel):
    def __init__(
        self,
        ext: main_models.TermQueryRequestExt = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext = ext
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.target_language = target_language
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['ext'] = self.ext.to_map()

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
            temp_model = main_models.TermQueryRequestExt()
            self.ext = temp_model.from_map(m.get('ext'))

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

class TermQueryRequestExt(DaraModel):
    def __init__(
        self,
        param_map: Any = None,
    ):
        self.param_map = param_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_map is not None:
            result['paramMap'] = self.param_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paramMap') is not None:
            self.param_map = m.get('paramMap')

        return self

