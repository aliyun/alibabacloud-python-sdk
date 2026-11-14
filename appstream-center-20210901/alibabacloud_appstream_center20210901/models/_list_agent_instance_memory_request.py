# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAgentInstanceMemoryRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        biz_type: int = None,
        end_user_ids: List[str] = None,
        excluded_end_user_ids: List[str] = None,
        memory_statuses: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        search_keyword: str = None,
        search_type: str = None,
    ):
        # Filters results by the business platform to which the agent belongs. If this parameter is omitted, no restriction is applied to the business platform.
        self.agent_platform = agent_platform
        # Filters results by agent provider. If this parameter is omitted, the system queries providers that support memory management. `JVSCopilot` is not supported for memory management in this API operation.
        self.agent_provider = agent_provider
        # Filters results by business type code. If this parameter is omitted, no restriction is applied to the business type.
        self.biz_type = biz_type
        # The list of end user IDs to be included in the query results. Exact matching is applied. Maximum value: 200.
        self.end_user_ids = end_user_ids
        # The list of end user IDs to be excluded from the query results. Maximum value: 200. When used together with EndUserIds, these users are removed from the inclusion scope.
        self.excluded_end_user_ids = excluded_end_user_ids
        # Filters results by the memory switch configured for the instance.
        # - `ENABLED`: The instance memory switch is turned on.
        # - `DISABLED`: The instance memory switch is turned off.
        # If both values are passed, instances matching either status are returned.
        self.memory_statuses = memory_statuses
        # The page number. Pages start from 1. If this parameter is not specified or is set to 0, the first page is queried.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100. Default value: 100.
        self.page_size = page_size
        # The keyword used for inclusion matching. Use SearchType to specify the search field. If this parameter is left empty, no keyword filtering is applied.
        self.search_keyword = search_keyword
        # The scope of the keyword search. Default value: `ALL`.
        # - `ALL`: Searches resource IDs, resource names, runtime IDs, and end user IDs.
        # - `RESOURCE_ID`: Searches resource IDs.
        # - `RESOURCE_NAME`: Searches resource names.
        # - `RUNTIME_ID`: Searches runtime IDs.
        # - `END_USER_ID`: Searches end user IDs.
        self.search_type = search_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.excluded_end_user_ids is not None:
            result['ExcludedEndUserIds'] = self.excluded_end_user_ids

        if self.memory_statuses is not None:
            result['MemoryStatuses'] = self.memory_statuses

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_keyword is not None:
            result['SearchKeyword'] = self.search_keyword

        if self.search_type is not None:
            result['SearchType'] = self.search_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('ExcludedEndUserIds') is not None:
            self.excluded_end_user_ids = m.get('ExcludedEndUserIds')

        if m.get('MemoryStatuses') is not None:
            self.memory_statuses = m.get('MemoryStatuses')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKeyword') is not None:
            self.search_keyword = m.get('SearchKeyword')

        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')

        return self

