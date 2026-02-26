# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DocumentParseOption(DaraModel):
    def __init__(
        self,
        keyword: main_models.DocumentParseKeywordOption = None,
        narrator: main_models.DocumentParseNarratorOption = None,
        question: main_models.DocumentParseQuestionOption = None,
        summary: main_models.DocumentParseSummaryOption = None,
    ):
        self.keyword = keyword
        self.narrator = narrator
        self.question = question
        self.summary = summary

    def validate(self):
        if self.keyword:
            self.keyword.validate()
        if self.narrator:
            self.narrator.validate()
        if self.question:
            self.question.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword.to_map()

        if self.narrator is not None:
            result['Narrator'] = self.narrator.to_map()

        if self.question is not None:
            result['Question'] = self.question.to_map()

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            temp_model = main_models.DocumentParseKeywordOption()
            self.keyword = temp_model.from_map(m.get('Keyword'))

        if m.get('Narrator') is not None:
            temp_model = main_models.DocumentParseNarratorOption()
            self.narrator = temp_model.from_map(m.get('Narrator'))

        if m.get('Question') is not None:
            temp_model = main_models.DocumentParseQuestionOption()
            self.question = temp_model.from_map(m.get('Question'))

        if m.get('Summary') is not None:
            temp_model = main_models.DocumentParseSummaryOption()
            self.summary = temp_model.from_map(m.get('Summary'))

        return self

