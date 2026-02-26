# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocumentParseSummaryOption(DaraModel):
    def __init__(
        self,
        chapter_summarize: bool = None,
        summarize: bool = None,
    ):
        self.chapter_summarize = chapter_summarize
        self.summarize = summarize

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chapter_summarize is not None:
            result['ChapterSummarize'] = self.chapter_summarize

        if self.summarize is not None:
            result['Summarize'] = self.summarize

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChapterSummarize') is not None:
            self.chapter_summarize = m.get('ChapterSummarize')

        if m.get('Summarize') is not None:
            self.summarize = m.get('Summarize')

        return self

