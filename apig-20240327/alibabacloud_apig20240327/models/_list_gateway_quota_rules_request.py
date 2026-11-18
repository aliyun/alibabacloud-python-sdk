# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewayQuotaRulesRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        rule_status: str = None,
        subject_name_like: str = None,
    ):
        # The keyword in the rule name used for fuzzy matching.
        self.keyword = keyword
        # The maximum number of entries to return in a single call. This parameter is not supported.
        self.max_results = max_results
        # The pagination token. This parameter is not supported.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The status of the rule. Valid values: enabled and disabled. If you do not specify this parameter, all rules are queried.
        self.rule_status = rule_status
        # The keyword in the name of the associated subject for fuzzy matching based on the consumer or consumer group name.
        self.subject_name_like = subject_name_like

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.rule_status is not None:
            result['ruleStatus'] = self.rule_status

        if self.subject_name_like is not None:
            result['subjectNameLike'] = self.subject_name_like

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('ruleStatus') is not None:
            self.rule_status = m.get('ruleStatus')

        if m.get('subjectNameLike') is not None:
            self.subject_name_like = m.get('subjectNameLike')

        return self

