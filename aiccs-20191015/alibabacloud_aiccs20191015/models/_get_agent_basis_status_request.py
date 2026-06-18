# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetAgentBasisStatusRequest(DaraModel):
    def __init__(
        self,
        agent_ids: List[int] = None,
        current_page: int = None,
        dep_ids: List[int] = None,
        end_date: int = None,
        instance_id: str = None,
        page_size: int = None,
        start_date: int = None,
    ):
        # A list of agent IDs.
        self.agent_ids = agent_ids
        # The current page number. The value must be greater than **0**. Default value: **1**.
        self.current_page = current_page
        # A list of department IDs.
        self.dep_ids = dep_ids
        # End Datetime UNIX timestamp. Unit: milliseconds.
        self.end_date = end_date
        # The Artificial Intelligence Cloud Call Service (AICCS) instance ID.  
        # You can obtain it in the **Instance Management** section of the left-side navigation pane in the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries per page. The value must be greater than **0**. Default value: **20**.
        self.page_size = page_size
        # The UNIX timestamp of the start date. Unit: milliseconds.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

