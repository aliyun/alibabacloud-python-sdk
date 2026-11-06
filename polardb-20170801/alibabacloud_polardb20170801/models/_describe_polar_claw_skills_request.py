# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarClawSkillsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # Specifies the agent workspace perspective. If this parameter is specified, the Disabled and AvailableToAgent fields are returned based on the specified agent. If this parameter is not specified, the default agent is used.
        self.agent_id = agent_id
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The page number. The value must be an integer greater than 0 and less than or equal to the maximum value of the Integer data type.
        self.page_number = page_number
        # The number of entries per page. Valid values: 30, 50, and 100. Default value: 30.
        self.page_size = page_size
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query all available regions for the current account, including region IDs.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

