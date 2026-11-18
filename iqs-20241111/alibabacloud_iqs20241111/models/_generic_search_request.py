# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GenericSearchRequest(DaraModel):
    def __init__(
        self,
        advanced_params: Dict[str, Any] = None,
        enable_rerank: bool = None,
        industry: str = None,
        page: int = None,
        query: str = None,
        return_main_text: bool = None,
        return_markdown_text: bool = None,
        return_rich_main_body: bool = None,
        return_summary: bool = None,
        session_id: str = None,
        time_range: str = None,
    ):
        # The advanced search parameters. Filters search results by the start and end dates of the webpage publication time. The date format is YYYY-MM-DD. This parameter takes precedence over timeRange.
        self.advanced_params = advanced_params
        # Specifies whether to rerank the search results. Default value: true.
        self.enable_rerank = enable_rerank
        # The industry. If specified, only site content restricted to the specified industries is recalled. Separate multiple industries with commas.
        self.industry = industry
        # The page number. The value starts from 1.
        self.page = page
        # The search keywords.
        # 
        # This parameter is required.
        self.query = query
        # Specifies whether to return the main text of the webpage. Default value: true.
        self.return_main_text = return_main_text
        # Specifies whether to return the webpage content in Markdown format. Default value: true.
        self.return_markdown_text = return_markdown_text
        # Specifies whether to return the full rich text body. Default value: false.
        self.return_rich_main_body = return_rich_main_body
        # Specifies whether to return the enhanced summary. Default value: true.
        self.return_summary = return_summary
        # The session ID for multi-turn interactions.
        self.session_id = session_id
        # The time range.
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_params is not None:
            result['advancedParams'] = self.advanced_params

        if self.enable_rerank is not None:
            result['enableRerank'] = self.enable_rerank

        if self.industry is not None:
            result['industry'] = self.industry

        if self.page is not None:
            result['page'] = self.page

        if self.query is not None:
            result['query'] = self.query

        if self.return_main_text is not None:
            result['returnMainText'] = self.return_main_text

        if self.return_markdown_text is not None:
            result['returnMarkdownText'] = self.return_markdown_text

        if self.return_rich_main_body is not None:
            result['returnRichMainBody'] = self.return_rich_main_body

        if self.return_summary is not None:
            result['returnSummary'] = self.return_summary

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advancedParams') is not None:
            self.advanced_params = m.get('advancedParams')

        if m.get('enableRerank') is not None:
            self.enable_rerank = m.get('enableRerank')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('returnMainText') is not None:
            self.return_main_text = m.get('returnMainText')

        if m.get('returnMarkdownText') is not None:
            self.return_markdown_text = m.get('returnMarkdownText')

        if m.get('returnRichMainBody') is not None:
            self.return_rich_main_body = m.get('returnRichMainBody')

        if m.get('returnSummary') is not None:
            self.return_summary = m.get('returnSummary')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

