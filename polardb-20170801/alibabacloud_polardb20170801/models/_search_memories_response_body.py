# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class SearchMemoriesResponseBody(DaraModel):
    def __init__(
        self,
        page: str = None,
        page_size: str = None,
        request_id: str = None,
        results: List[main_models.SearchMemoriesResponseBodyResults] = None,
        total: str = None,
        total_pages: str = None,
    ):
        self.page = page
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of results.
        self.results = results
        self.total = total
        self.total_pages = total_pages

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.SearchMemoriesResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class SearchMemoriesResponseBodyResults(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        memory: str = None,
        memory_agent_id: str = None,
        memory_user_id: str = None,
        metadata: str = None,
        score: str = None,
        update_time: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The memory ID.
        self.id = id
        # The memory content.
        self.memory = memory
        # The agent to which the memory belongs.
        self.memory_agent_id = memory_agent_id
        # The user to whom the memory belongs.
        self.memory_user_id = memory_user_id
        # The metadata.
        self.metadata = metadata
        # The score.
        self.score = score
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.memory_agent_id is not None:
            result['MemoryAgentId'] = self.memory_agent_id

        if self.memory_user_id is not None:
            result['MemoryUserId'] = self.memory_user_id

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.score is not None:
            result['Score'] = self.score

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MemoryAgentId') is not None:
            self.memory_agent_id = m.get('MemoryAgentId')

        if m.get('MemoryUserId') is not None:
            self.memory_user_id = m.get('MemoryUserId')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

