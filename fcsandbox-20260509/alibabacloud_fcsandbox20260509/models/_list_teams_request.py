# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTeamsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plan: str = None,
        resource_group_id: str = None,
        team_name: str = None,
    ):
        # The page number, starting from 1.
        self.page_number = page_number
        # The number of teams displayed per page.
        self.page_size = page_size
        # The subscription plan of the team. Valid values:
        # 
        # - eco
        # - std
        # - pro
        self.plan = plan
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The team name.
        self.team_name = team_name

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

        if self.plan is not None:
            result['plan'] = self.plan

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('plan') is not None:
            self.plan = m.get('plan')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        return self

