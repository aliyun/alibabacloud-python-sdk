# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class GetDocumentAnalysisOption(DaraModel):
    def __init__(
        self,
        chapter_summary: bool = None,
        chapter_summary_option: main_models.DocumentChapterSummarizeOption = None,
        images: bool = None,
        keyword: bool = None,
        layouts: bool = None,
        narrator: bool = None,
        question: bool = None,
        summary: bool = None,
    ):
        # Specifies whether to generate summaries for each chapter. Set to `true` to enable this feature. Use `ChapterSummaryOption` to configure detailed options. Defaults to `false`.
        self.chapter_summary = chapter_summary
        self.chapter_summary_option = chapter_summary_option
        # Specifies whether to analyze each image within the document. Set to `true` to enable this feature. Defaults to `false`.
        self.images = images
        # Specifies whether to extract keywords from the document. Set to `true` to enable this feature. Defaults to `false`.
        self.keyword = keyword
        # Specifies whether to analyze the document layout. Set to `true` to enable this feature. Defaults to `false`.
        self.layouts = layouts
        # Specifies whether to identify the narrator in the document. Set to `true` to enable this feature. Defaults to `false`.
        self.narrator = narrator
        # Specifies whether to generate questions based on the document content. Set to `true` to enable this feature. Defaults to `false`.
        self.question = question
        # Specifies whether to generate a summary for the document. Set to `true` to enable this feature. Defaults to `false`.
        self.summary = summary

    def validate(self):
        if self.chapter_summary_option:
            self.chapter_summary_option.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chapter_summary is not None:
            result['ChapterSummary'] = self.chapter_summary

        if self.chapter_summary_option is not None:
            result['ChapterSummaryOption'] = self.chapter_summary_option.to_map()

        if self.images is not None:
            result['Images'] = self.images

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.layouts is not None:
            result['Layouts'] = self.layouts

        if self.narrator is not None:
            result['Narrator'] = self.narrator

        if self.question is not None:
            result['Question'] = self.question

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChapterSummary') is not None:
            self.chapter_summary = m.get('ChapterSummary')

        if m.get('ChapterSummaryOption') is not None:
            temp_model = main_models.DocumentChapterSummarizeOption()
            self.chapter_summary_option = temp_model.from_map(m.get('ChapterSummaryOption'))

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Layouts') is not None:
            self.layouts = m.get('Layouts')

        if m.get('Narrator') is not None:
            self.narrator = m.get('Narrator')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

