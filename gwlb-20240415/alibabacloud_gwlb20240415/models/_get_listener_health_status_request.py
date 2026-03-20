# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gwlb20240415 import models as main_models
from darabonba.model import DaraModel

class GetListenerHealthStatusRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.GetListenerHealthStatusRequestFilter] = None,
        listener_id: str = None,
        max_results: int = None,
        next_token: str = None,
        skip: int = None,
    ):
        # The filter conditions. You can specify at most 20 filter conditions.
        self.filter = filter
        # The listener ID.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The number of entries per page. Valid values: 1 to 1000. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The number of entries to be skipped in the call.
        self.skip = skip

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.skip is not None:
            result['Skip'] = self.skip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.GetListenerHealthStatusRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        return self

class GetListenerHealthStatusRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        values: List[str] = None,
    ):
        # The filter condition name. You can filter by one or more filter condition names. The URL must meet the following requirements:
        # 
        # *   **Status**: the health status.
        # *   **ReasonCode**: the cause of an unhealthy server.
        # *   **ServerId**: the ID of the backend server.
        # *   **ServerIp**: the IP address of the backend server.
        self.name = name
        # The filter condition values. You can specify at most 20 condition values.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

