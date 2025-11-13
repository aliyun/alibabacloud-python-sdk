# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunSearchCaseFullTextRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        filter_condition: main_models.RunSearchCaseFullTextRequestFilterCondition = None,
        page_param: main_models.RunSearchCaseFullTextRequestPageParam = None,
        query: str = None,
        query_keywords: List[str] = None,
        refer_level: str = None,
        sort_key_and_direction: Dict[str, str] = None,
        thread: main_models.RunSearchCaseFullTextRequestThread = None,
    ):
        self.app_id = app_id
        self.filter_condition = filter_condition
        # This parameter is required.
        self.page_param = page_param
        # This parameter is required.
        self.query = query
        self.query_keywords = query_keywords
        self.refer_level = refer_level
        self.sort_key_and_direction = sort_key_and_direction
        self.thread = thread

    def validate(self):
        if self.filter_condition:
            self.filter_condition.validate()
        if self.page_param:
            self.page_param.validate()
        if self.thread:
            self.thread.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.filter_condition is not None:
            result['filterCondition'] = self.filter_condition.to_map()

        if self.page_param is not None:
            result['pageParam'] = self.page_param.to_map()

        if self.query is not None:
            result['query'] = self.query

        if self.query_keywords is not None:
            result['queryKeywords'] = self.query_keywords

        if self.refer_level is not None:
            result['referLevel'] = self.refer_level

        if self.sort_key_and_direction is not None:
            result['sortKeyAndDirection'] = self.sort_key_and_direction

        if self.thread is not None:
            result['thread'] = self.thread.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('filterCondition') is not None:
            temp_model = main_models.RunSearchCaseFullTextRequestFilterCondition()
            self.filter_condition = temp_model.from_map(m.get('filterCondition'))

        if m.get('pageParam') is not None:
            temp_model = main_models.RunSearchCaseFullTextRequestPageParam()
            self.page_param = temp_model.from_map(m.get('pageParam'))

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('queryKeywords') is not None:
            self.query_keywords = m.get('queryKeywords')

        if m.get('referLevel') is not None:
            self.refer_level = m.get('referLevel')

        if m.get('sortKeyAndDirection') is not None:
            self.sort_key_and_direction = m.get('sortKeyAndDirection')

        if m.get('thread') is not None:
            temp_model = main_models.RunSearchCaseFullTextRequestThread()
            self.thread = temp_model.from_map(m.get('thread'))

        return self

class RunSearchCaseFullTextRequestThread(DaraModel):
    def __init__(
        self,
        messages: List[main_models.RunSearchCaseFullTextRequestThreadMessages] = None,
    ):
        self.messages = messages

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.RunSearchCaseFullTextRequestThreadMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class RunSearchCaseFullTextRequestThreadMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

class RunSearchCaseFullTextRequestPageParam(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

class RunSearchCaseFullTextRequestFilterCondition(DaraModel):
    def __init__(
        self,
        case_no: str = None,
        case_title: str = None,
    ):
        self.case_no = case_no
        self.case_title = case_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_no is not None:
            result['caseNo'] = self.case_no

        if self.case_title is not None:
            result['caseTitle'] = self.case_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseNo') is not None:
            self.case_no = m.get('caseNo')

        if m.get('caseTitle') is not None:
            self.case_title = m.get('caseTitle')

        return self

