# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RequestContents(DaraModel):
    def __init__(
        self,
        main_text: bool = None,
        markdown_text: bool = None,
        rerank_score: bool = None,
        rich_main_body: bool = None,
        summary: bool = None,
    ):
        self.main_text = main_text
        self.markdown_text = markdown_text
        self.rerank_score = rerank_score
        self.rich_main_body = rich_main_body
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.main_text is not None:
            result['mainText'] = self.main_text

        if self.markdown_text is not None:
            result['markdownText'] = self.markdown_text

        if self.rerank_score is not None:
            result['rerankScore'] = self.rerank_score

        if self.rich_main_body is not None:
            result['richMainBody'] = self.rich_main_body

        if self.summary is not None:
            result['summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mainText') is not None:
            self.main_text = m.get('mainText')

        if m.get('markdownText') is not None:
            self.markdown_text = m.get('markdownText')

        if m.get('rerankScore') is not None:
            self.rerank_score = m.get('rerankScore')

        if m.get('richMainBody') is not None:
            self.rich_main_body = m.get('richMainBody')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        return self

