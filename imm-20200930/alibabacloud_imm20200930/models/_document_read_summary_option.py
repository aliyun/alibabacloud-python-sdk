# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DocumentReadSummaryOption(DaraModel):
    def __init__(
        self,
        chapter_summarize: bool = None,
        chapter_summarize_option: main_models.DocumentChapterSummarizeOption = None,
        summarize: bool = None,
    ):
        # Specifies whether to extract the chapter-level summary of the article.
        self.chapter_summarize = chapter_summarize
        # The chapter-level summary options for the article.
        self.chapter_summarize_option = chapter_summarize_option
        # Specifies whether to extract the article summary.
        self.summarize = summarize

    def validate(self):
        if self.chapter_summarize_option:
            self.chapter_summarize_option.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chapter_summarize is not None:
            result['ChapterSummarize'] = self.chapter_summarize

        if self.chapter_summarize_option is not None:
            result['ChapterSummarizeOption'] = self.chapter_summarize_option.to_map()

        if self.summarize is not None:
            result['Summarize'] = self.summarize

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChapterSummarize') is not None:
            self.chapter_summarize = m.get('ChapterSummarize')

        if m.get('ChapterSummarizeOption') is not None:
            temp_model = main_models.DocumentChapterSummarizeOption()
            self.chapter_summarize_option = temp_model.from_map(m.get('ChapterSummarizeOption'))

        if m.get('Summarize') is not None:
            self.summarize = m.get('Summarize')

        return self

