# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentBasisStatusShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_ids_shrink: str = None,
        current_page: int = None,
        dep_ids_shrink: str = None,
        end_date: int = None,
        instance_id: str = None,
        page_size: int = None,
        start_date: int = None,
    ):
        self.agent_ids_shrink = agent_ids_shrink
        self.current_page = current_page
        self.dep_ids_shrink = dep_ids_shrink
        self.end_date = end_date
        # This parameter is required.
        self.instance_id = instance_id
        self.page_size = page_size
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink

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
            self.agent_ids_shrink = m.get('AgentIds')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

