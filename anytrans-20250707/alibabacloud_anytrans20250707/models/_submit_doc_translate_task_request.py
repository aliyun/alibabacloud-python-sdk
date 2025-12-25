# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_anytrans20250707 import models as main_models
from darabonba.model import DaraModel

class SubmitDocTranslateTaskRequest(DaraModel):
    def __init__(
        self,
        ext: main_models.SubmitDocTranslateTaskRequestExt = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext = ext
        self.format = format
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        self.target_language = target_language
        # This parameter is required.
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
            temp_model = main_models.SubmitDocTranslateTaskRequestExt()
            self.ext = temp_model.from_map(m.get('ext'))

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

class SubmitDocTranslateTaskRequestExt(DaraModel):
    def __init__(
        self,
        config: main_models.SubmitDocTranslateTaskRequestExtConfig = None,
        domain_hint: str = None,
        param_map: Any = None,
        terminologies: List[main_models.SubmitDocTranslateTaskRequestExtTerminologies] = None,
    ):
        self.config = config
        self.domain_hint = domain_hint
        self.param_map = param_map
        self.terminologies = terminologies

    def validate(self):
        if self.config:
            self.config.validate()
        if self.terminologies:
            for v1 in self.terminologies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.domain_hint is not None:
            result['domainHint'] = self.domain_hint

        if self.param_map is not None:
            result['paramMap'] = self.param_map

        result['terminologies'] = []
        if self.terminologies is not None:
            for k1 in self.terminologies:
                result['terminologies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.SubmitDocTranslateTaskRequestExtConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('domainHint') is not None:
            self.domain_hint = m.get('domainHint')

        if m.get('paramMap') is not None:
            self.param_map = m.get('paramMap')

        self.terminologies = []
        if m.get('terminologies') is not None:
            for k1 in m.get('terminologies'):
                temp_model = main_models.SubmitDocTranslateTaskRequestExtTerminologies()
                self.terminologies.append(temp_model.from_map(k1))

        return self

class SubmitDocTranslateTaskRequestExtTerminologies(DaraModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.src is not None:
            result['src'] = self.src

        if self.tgt is not None:
            result['tgt'] = self.tgt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')

        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')

        return self

class SubmitDocTranslateTaskRequestExtConfig(DaraModel):
    def __init__(
        self,
        skip_img_trans: bool = None,
    ):
        self.skip_img_trans = skip_img_trans

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skip_img_trans is not None:
            result['skipImgTrans'] = self.skip_img_trans

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('skipImgTrans') is not None:
            self.skip_img_trans = m.get('skipImgTrans')

        return self

