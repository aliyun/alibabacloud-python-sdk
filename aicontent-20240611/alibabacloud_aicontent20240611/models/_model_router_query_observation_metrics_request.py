# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryObservationMetricsRequest(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        client_id: int = None,
        end_time: str = None,
        group_by: str = None,
        max_results: int = None,
        member_user_ids: str = None,
        model_id: int = None,
        need_total_count: bool = None,
        next_token: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_index: int = None,
        page_size: int = None,
        start_time: str = None,
        time_range: str = None,
    ):
        # The API key ID used to filter the results.
        self.api_key_id = api_key_id
        # The client ID used to filter the results.
        self.client_id = client_id
        # The custom end time.
        self.end_time = end_time
        # The field by which to group the results.
        self.group_by = group_by
        # The maximum number of results to return.
        self.max_results = max_results
        # Optional. Filters by member IDs. Separate multiple IDs with commas. If not specified, the department and all its members are included. If an empty value is specified, only the department is included without members.
        self.member_user_ids = member_user_ids
        # The model ID used to filter the results.
        self.model_id = model_id
        # Specifies whether to return the total count.
        self.need_total_count = need_total_count
        # The token for the next query. An empty value indicates the last page.
        self.next_token = next_token
        # The field by which to sort the results.
        self.order_by = order_by
        # The sort direction.
        self.order_direction = order_direction
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The custom start time.
        self.start_time = start_time
        # The time range for the query. Valid values: 1h, 6h, 24h, 7d, 30d.
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['apiKeyId'] = self.api_key_id

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.member_user_ids is not None:
            result['memberUserIds'] = self.member_user_ids

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.need_total_count is not None:
            result['needTotalCount'] = self.need_total_count

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyId') is not None:
            self.api_key_id = m.get('apiKeyId')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('memberUserIds') is not None:
            self.member_user_ids = m.get('memberUserIds')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('needTotalCount') is not None:
            self.need_total_count = m.get('needTotalCount')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

