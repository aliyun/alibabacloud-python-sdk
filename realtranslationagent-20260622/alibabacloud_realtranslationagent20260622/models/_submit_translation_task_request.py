# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_realtranslationagent20260622 import models as main_models
from darabonba.model import DaraModel

class SubmitTranslationTaskRequest(DaraModel):
    def __init__(
        self,
        apikey: str = None,
        base_task_id: str = None,
        config: main_models.SubmitTranslationTaskRequestConfig = None,
        custom_terms: List[main_models.SubmitTranslationTaskRequestCustomTerms] = None,
        task_id: str = None,
    ):
        self.apikey = apikey
        self.base_task_id = base_task_id
        # This parameter is required.
        self.config = config
        self.custom_terms = custom_terms
        self.task_id = task_id

    def validate(self):
        if self.config:
            self.config.validate()
        if self.custom_terms:
            for v1 in self.custom_terms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey is not None:
            result['APIKey'] = self.apikey

        if self.base_task_id is not None:
            result['BaseTaskId'] = self.base_task_id

        if self.config is not None:
            result['Config'] = self.config.to_map()

        result['CustomTerms'] = []
        if self.custom_terms is not None:
            for k1 in self.custom_terms:
                result['CustomTerms'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIKey') is not None:
            self.apikey = m.get('APIKey')

        if m.get('BaseTaskId') is not None:
            self.base_task_id = m.get('BaseTaskId')

        if m.get('Config') is not None:
            temp_model = main_models.SubmitTranslationTaskRequestConfig()
            self.config = temp_model.from_map(m.get('Config'))

        self.custom_terms = []
        if m.get('CustomTerms') is not None:
            for k1 in m.get('CustomTerms'):
                temp_model = main_models.SubmitTranslationTaskRequestCustomTerms()
                self.custom_terms.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class SubmitTranslationTaskRequestCustomTerms(DaraModel):
    def __init__(
        self,
        source_term: str = None,
        target_term: str = None,
    ):
        self.source_term = source_term
        self.target_term = target_term

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_term is not None:
            result['SourceTerm'] = self.source_term

        if self.target_term is not None:
            result['TargetTerm'] = self.target_term

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceTerm') is not None:
            self.source_term = m.get('SourceTerm')

        if m.get('TargetTerm') is not None:
            self.target_term = m.get('TargetTerm')

        return self

class SubmitTranslationTaskRequestConfig(DaraModel):
    def __init__(
        self,
        font: str = None,
        source_language: str = None,
        style: str = None,
        target_language: str = None,
    ):
        self.font = font
        # This parameter is required.
        self.source_language = source_language
        self.style = style
        # This parameter is required.
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.font is not None:
            result['Font'] = self.font

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.style is not None:
            result['Style'] = self.style

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('Style') is not None:
            self.style = m.get('Style')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        return self

