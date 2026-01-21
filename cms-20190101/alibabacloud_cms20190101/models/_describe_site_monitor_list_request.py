# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSiteMonitorListRequest(DaraModel):
    def __init__(
        self,
        agent_group: str = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
        region_id: str = None,
        task_id: str = None,
        task_state: str = None,
        task_type: str = None,
    ):
        # Task network type. Valid values:
        # 
        # - PC: Cable Network
        # 
        # - MOBILE: Mobile Cellular Network
        # 
        # - FC: Alibaba Cloud VPC Network
        self.agent_group = agent_group
        # The keyword to be matched.
        # 
        # >  You can search for tasks by name or address. Fuzzy search is supported.
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page = page
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        self.region_id = region_id
        # The ID of the site monitoring task.
        self.task_id = task_id
        # The task status. Valid values:
        # 
        # *   1: The task is enabled.
        # *   2: The task is disabled.
        self.task_state = task_state
        # The protocol that is used by the site monitoring task. Valid values: HTTP, PING, TCP, UDP, DNS, SMTP, POP3, and FTP.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_group is not None:
            result['AgentGroup'] = self.agent_group

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentGroup') is not None:
            self.agent_group = m.get('AgentGroup')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

