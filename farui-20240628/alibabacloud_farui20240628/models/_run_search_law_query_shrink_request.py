# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunSearchLawQueryShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        filter_condition_shrink: str = None,
        page_param_shrink: str = None,
        query: str = None,
        query_keywords_shrink: str = None,
        thread_shrink: str = None,
    ):
        self.app_id = app_id
        self.filter_condition_shrink = filter_condition_shrink
        self.page_param_shrink = page_param_shrink
        # This parameter is required.
        self.query = query
        self.query_keywords_shrink = query_keywords_shrink
        self.thread_shrink = thread_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.filter_condition_shrink is not None:
            result['filterCondition'] = self.filter_condition_shrink

        if self.page_param_shrink is not None:
            result['pageParam'] = self.page_param_shrink

        if self.query is not None:
            result['query'] = self.query

        if self.query_keywords_shrink is not None:
            result['queryKeywords'] = self.query_keywords_shrink

        if self.thread_shrink is not None:
            result['thread'] = self.thread_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('filterCondition') is not None:
            self.filter_condition_shrink = m.get('filterCondition')

        if m.get('pageParam') is not None:
            self.page_param_shrink = m.get('pageParam')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('queryKeywords') is not None:
            self.query_keywords_shrink = m.get('queryKeywords')

        if m.get('thread') is not None:
            self.thread_shrink = m.get('thread')

        return self

