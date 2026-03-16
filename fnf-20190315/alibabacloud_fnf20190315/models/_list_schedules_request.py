# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSchedulesRequest(DaraModel):
    def __init__(
        self,
        flow_name: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # The name of the flow that is associated with the time-based schedules. The name is unique within the region and cannot be modified after the flow is created. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The number of schedules that you want to query. Valid values: 1 to 1000.
        self.limit = limit
        # For the first query, you do not need to specify this parameter. The system uses the value of the **FlowName** parameter as the value of the **NextToken** parameter. When the query ends, no value is returned for this parameter.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

