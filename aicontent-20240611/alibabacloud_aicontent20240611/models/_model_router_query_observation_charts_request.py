# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryObservationChartsRequest(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        client_id: int = None,
        end_time: str = None,
        member_user_ids: str = None,
        model_id: int = None,
        start_time: str = None,
        time_range: str = None,
    ):
        # The API key ID used to filter results.
        self.api_key_id = api_key_id
        # The client ID used to filter results.
        self.client_id = client_id
        # The custom end time.
        self.end_time = end_time
        # Optional. Filters by member IDs. Separate multiple IDs with commas. If this parameter is not specified, the department and all its members are included. If an empty value is specified, only the department is included without members.
        self.member_user_ids = member_user_ids
        # The model ID used to filter results.
        self.model_id = model_id
        # The custom start time.
        self.start_time = start_time
        # The time range for the query. Valid values: 1h, 6h, 24h, 7d, and 30d.
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

        if self.member_user_ids is not None:
            result['memberUserIds'] = self.member_user_ids

        if self.model_id is not None:
            result['modelId'] = self.model_id

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

        if m.get('memberUserIds') is not None:
            self.member_user_ids = m.get('memberUserIds')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

