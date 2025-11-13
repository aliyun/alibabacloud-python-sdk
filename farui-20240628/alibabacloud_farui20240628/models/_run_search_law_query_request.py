# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunSearchLawQueryRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        filter_condition: main_models.RunSearchLawQueryRequestFilterCondition = None,
        page_param: main_models.RunSearchLawQueryRequestPageParam = None,
        query: str = None,
        query_keywords: List[str] = None,
        thread: main_models.RunSearchLawQueryRequestThread = None,
    ):
        self.app_id = app_id
        self.filter_condition = filter_condition
        self.page_param = page_param
        # This parameter is required.
        self.query = query
        self.query_keywords = query_keywords
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

        if self.thread is not None:
            result['thread'] = self.thread.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('filterCondition') is not None:
            temp_model = main_models.RunSearchLawQueryRequestFilterCondition()
            self.filter_condition = temp_model.from_map(m.get('filterCondition'))

        if m.get('pageParam') is not None:
            temp_model = main_models.RunSearchLawQueryRequestPageParam()
            self.page_param = temp_model.from_map(m.get('pageParam'))

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('queryKeywords') is not None:
            self.query_keywords = m.get('queryKeywords')

        if m.get('thread') is not None:
            temp_model = main_models.RunSearchLawQueryRequestThread()
            self.thread = temp_model.from_map(m.get('thread'))

        return self

class RunSearchLawQueryRequestThread(DaraModel):
    def __init__(
        self,
        messages: List[main_models.RunSearchLawQueryRequestThreadMessages] = None,
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
                temp_model = main_models.RunSearchLawQueryRequestThreadMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class RunSearchLawQueryRequestThreadMessages(DaraModel):
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

class RunSearchLawQueryRequestPageParam(DaraModel):
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

class RunSearchLawQueryRequestFilterCondition(DaraModel):
    def __init__(
        self,
        law_name: str = None,
    ):
        self.law_name = law_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.law_name is not None:
            result['lawName'] = self.law_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lawName') is not None:
            self.law_name = m.get('lawName')

        return self

