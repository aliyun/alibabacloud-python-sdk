# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchMemoriesRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        create_time_begin: str = None,
        create_time_end: str = None,
        memory_agent_id: str = None,
        memory_id: str = None,
        memory_user_id: str = None,
        page: int = None,
        page_size: int = None,
        query: str = None,
        top_k: str = None,
    ):
        # The application ID. Example: pa-**************. The application must be of the mem0 type. When you create the application by calling CreateApplication, set ApplicationType to mem0. If you call this operation on a non-mem0 application, the IncorrectDBInstanceEngine (403) error is returned.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The start time for memory creation.
        self.create_time_begin = create_time_begin
        # The end time for memory creation.
        self.create_time_end = create_time_end
        # The ID of the memory agent.
        self.memory_agent_id = memory_agent_id
        # The memory ID. If you specify this parameter, the complete change history of the memory is queried.
        self.memory_id = memory_id
        # The ID of the memory user.
        self.memory_user_id = memory_user_id
        # The page number.
        self.page = page
        # The number of records to display on each page.
        self.page_size = page_size
        # The search query.
        self.query = query
        # The number of top results to return.
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.create_time_begin is not None:
            result['CreateTimeBegin'] = self.create_time_begin

        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.memory_agent_id is not None:
            result['MemoryAgentId'] = self.memory_agent_id

        if self.memory_id is not None:
            result['MemoryId'] = self.memory_id

        if self.memory_user_id is not None:
            result['MemoryUserId'] = self.memory_user_id

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.top_k is not None:
            result['TopK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('CreateTimeBegin') is not None:
            self.create_time_begin = m.get('CreateTimeBegin')

        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('MemoryAgentId') is not None:
            self.memory_agent_id = m.get('MemoryAgentId')

        if m.get('MemoryId') is not None:
            self.memory_id = m.get('MemoryId')

        if m.get('MemoryUserId') is not None:
            self.memory_user_id = m.get('MemoryUserId')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

