# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_anytrans20250707 import models as main_models
from darabonba.model import DaraModel

class TermEditRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        ext: main_models.TermEditRequestExt = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.ext = ext
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.target_language = target_language
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
        if self.action is not None:
            result['action'] = self.action

        if self.ext is not None:
            result['ext'] = self.ext.to_map()

        if self.scene is not None:
            result['scene'] = self.scene

        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language

        if self.target_language is not None:
            result['targetLanguage'] = self.target_language

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('ext') is not None:
            temp_model = main_models.TermEditRequestExt()
            self.ext = temp_model.from_map(m.get('ext'))

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')

        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class TermEditRequestExt(DaraModel):
    def __init__(
        self,
        param_map: Any = None,
        terms: List[main_models.TermEditRequestExtTerms] = None,
    ):
        self.param_map = param_map
        # This parameter is required.
        self.terms = terms

    def validate(self):
        if self.terms:
            for v1 in self.terms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_map is not None:
            result['paramMap'] = self.param_map

        result['terms'] = []
        if self.terms is not None:
            for k1 in self.terms:
                result['terms'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paramMap') is not None:
            self.param_map = m.get('paramMap')

        self.terms = []
        if m.get('terms') is not None:
            for k1 in m.get('terms'):
                temp_model = main_models.TermEditRequestExtTerms()
                self.terms.append(temp_model.from_map(k1))

        return self

class TermEditRequestExtTerms(DaraModel):
    def __init__(
        self,
        src: str = None,
        term_id: str = None,
        tgt: str = None,
    ):
        # This parameter is required.
        self.src = src
        self.term_id = term_id
        # This parameter is required.
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

        if self.term_id is not None:
            result['termId'] = self.term_id

        if self.tgt is not None:
            result['tgt'] = self.tgt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')

        if m.get('termId') is not None:
            self.term_id = m.get('termId')

        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')

        return self

