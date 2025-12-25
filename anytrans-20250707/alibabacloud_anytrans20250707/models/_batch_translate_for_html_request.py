# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_anytrans20250707 import models as main_models
from darabonba.model import DaraModel

class BatchTranslateForHtmlRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        ext: main_models.BatchTranslateForHtmlRequestExt = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: Dict[str, Any] = None,
        workspace_id: str = None,
    ):
        self.app_name = app_name
        self.ext = ext
        self.format = format
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
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
        if self.app_name is not None:
            result['appName'] = self.app_name

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
        if m.get('appName') is not None:
            self.app_name = m.get('appName')

        if m.get('ext') is not None:
            temp_model = main_models.BatchTranslateForHtmlRequestExt()
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

class BatchTranslateForHtmlRequestExt(DaraModel):
    def __init__(
        self,
        config: main_models.BatchTranslateForHtmlRequestExtConfig = None,
        domain_hint: str = None,
        examples: List[main_models.BatchTranslateForHtmlRequestExtExamples] = None,
        sensitives: List[str] = None,
        terminologies: List[main_models.BatchTranslateForHtmlRequestExtTerminologies] = None,
        text_transform: main_models.BatchTranslateForHtmlRequestExtTextTransform = None,
    ):
        self.config = config
        self.domain_hint = domain_hint
        self.examples = examples
        self.sensitives = sensitives
        self.terminologies = terminologies
        self.text_transform = text_transform

    def validate(self):
        if self.config:
            self.config.validate()
        if self.examples:
            for v1 in self.examples:
                 if v1:
                    v1.validate()
        if self.terminologies:
            for v1 in self.terminologies:
                 if v1:
                    v1.validate()
        if self.text_transform:
            self.text_transform.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.domain_hint is not None:
            result['domainHint'] = self.domain_hint

        result['examples'] = []
        if self.examples is not None:
            for k1 in self.examples:
                result['examples'].append(k1.to_map() if k1 else None)

        if self.sensitives is not None:
            result['sensitives'] = self.sensitives

        result['terminologies'] = []
        if self.terminologies is not None:
            for k1 in self.terminologies:
                result['terminologies'].append(k1.to_map() if k1 else None)

        if self.text_transform is not None:
            result['textTransform'] = self.text_transform.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.BatchTranslateForHtmlRequestExtConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('domainHint') is not None:
            self.domain_hint = m.get('domainHint')

        self.examples = []
        if m.get('examples') is not None:
            for k1 in m.get('examples'):
                temp_model = main_models.BatchTranslateForHtmlRequestExtExamples()
                self.examples.append(temp_model.from_map(k1))

        if m.get('sensitives') is not None:
            self.sensitives = m.get('sensitives')

        self.terminologies = []
        if m.get('terminologies') is not None:
            for k1 in m.get('terminologies'):
                temp_model = main_models.BatchTranslateForHtmlRequestExtTerminologies()
                self.terminologies.append(temp_model.from_map(k1))

        if m.get('textTransform') is not None:
            temp_model = main_models.BatchTranslateForHtmlRequestExtTextTransform()
            self.text_transform = temp_model.from_map(m.get('textTransform'))

        return self

class BatchTranslateForHtmlRequestExtTextTransform(DaraModel):
    def __init__(
        self,
        to_lower: bool = None,
        to_title: bool = None,
        to_upper: bool = None,
    ):
        self.to_lower = to_lower
        self.to_title = to_title
        self.to_upper = to_upper

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.to_lower is not None:
            result['toLower'] = self.to_lower

        if self.to_title is not None:
            result['toTitle'] = self.to_title

        if self.to_upper is not None:
            result['toUpper'] = self.to_upper

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('toLower') is not None:
            self.to_lower = m.get('toLower')

        if m.get('toTitle') is not None:
            self.to_title = m.get('toTitle')

        if m.get('toUpper') is not None:
            self.to_upper = m.get('toUpper')

        return self

class BatchTranslateForHtmlRequestExtTerminologies(DaraModel):
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

class BatchTranslateForHtmlRequestExtExamples(DaraModel):
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

class BatchTranslateForHtmlRequestExtConfig(DaraModel):
    def __init__(
        self,
        skip_csi_check: bool = None,
    ):
        self.skip_csi_check = skip_csi_check

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skip_csi_check is not None:
            result['skipCsiCheck'] = self.skip_csi_check

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('skipCsiCheck') is not None:
            self.skip_csi_check = m.get('skipCsiCheck')

        return self

