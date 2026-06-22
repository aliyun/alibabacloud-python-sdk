# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class VideoReadOption(DaraModel):
    def __init__(
        self,
        keyword: main_models.VideoReadKeywordOption = None,
        ppt: main_models.VideoReadPPTOption = None,
        question: main_models.VideoReadQuestionOption = None,
        summary: main_models.VideoReadSummaryOption = None,
    ):
        self.keyword = keyword
        self.ppt = ppt
        self.question = question
        self.summary = summary

    def validate(self):
        if self.keyword:
            self.keyword.validate()
        if self.ppt:
            self.ppt.validate()
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

        if self.ppt is not None:
            result['PPT'] = self.ppt.to_map()

        if self.question is not None:
            result['Question'] = self.question.to_map()

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            temp_model = main_models.VideoReadKeywordOption()
            self.keyword = temp_model.from_map(m.get('Keyword'))

        if m.get('PPT') is not None:
            temp_model = main_models.VideoReadPPTOption()
            self.ppt = temp_model.from_map(m.get('PPT'))

        if m.get('Question') is not None:
            temp_model = main_models.VideoReadQuestionOption()
            self.question = temp_model.from_map(m.get('Question'))

        if m.get('Summary') is not None:
            temp_model = main_models.VideoReadSummaryOption()
            self.summary = temp_model.from_map(m.get('Summary'))

        return self

