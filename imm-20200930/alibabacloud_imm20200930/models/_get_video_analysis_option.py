# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVideoAnalysisOption(DaraModel):
    def __init__(
        self,
        chapter_summary: bool = None,
        keyword: bool = None,
        ppt: bool = None,
        question: bool = None,
        summary: bool = None,
        transcript: bool = None,
        transcript_chapter_summary: bool = None,
        transcript_summary: bool = None,
    ):
        # Specifies whether to retrieve the chapter-based summary of the video.
        self.chapter_summary = chapter_summary
        # Specifies whether to retrieve keywords.
        self.keyword = keyword
        # Specifies whether to retrieve the PPT from the video. Default value: false.
        self.ppt = ppt
        # Specifies whether to retrieve the generated questions and corresponding answers.
        self.question = question
        # Specifies whether to retrieve the full-text summary.
        self.summary = summary
        # Specifies whether to retrieve the dialogue in the video. Default value: false.
        self.transcript = transcript
        # Specifies whether to retrieve the segmented summary generated from the dialogue in the video. Default value: false.
        self.transcript_chapter_summary = transcript_chapter_summary
        # Specifies whether to retrieve the summary generated from the dialogue in the video. Default value: false.
        self.transcript_summary = transcript_summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chapter_summary is not None:
            result['ChapterSummary'] = self.chapter_summary

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.ppt is not None:
            result['PPT'] = self.ppt

        if self.question is not None:
            result['Question'] = self.question

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.transcript is not None:
            result['Transcript'] = self.transcript

        if self.transcript_chapter_summary is not None:
            result['TranscriptChapterSummary'] = self.transcript_chapter_summary

        if self.transcript_summary is not None:
            result['TranscriptSummary'] = self.transcript_summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChapterSummary') is not None:
            self.chapter_summary = m.get('ChapterSummary')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PPT') is not None:
            self.ppt = m.get('PPT')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Transcript') is not None:
            self.transcript = m.get('Transcript')

        if m.get('TranscriptChapterSummary') is not None:
            self.transcript_chapter_summary = m.get('TranscriptChapterSummary')

        if m.get('TranscriptSummary') is not None:
            self.transcript_summary = m.get('TranscriptSummary')

        return self

