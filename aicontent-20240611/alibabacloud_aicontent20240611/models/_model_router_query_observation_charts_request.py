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
        model_id: int = None,
        start_time: str = None,
        time_range: str = None,
    ):
        # The API key ID to use as a filter.
        self.api_key_id = api_key_id
        # The client ID to use as a filter.
        self.client_id = client_id
        # The end time of the custom time range, in ISO 8601 UTC format. If specified, `startTime` must also be provided.
        self.end_time = end_time
        # The model ID to use as a filter.
        self.model_id = model_id
        # The start time of the custom time range, in ISO 8601 UTC format. If specified, `endTime` must also be provided.
        self.start_time = start_time
        # The time range for the query. Valid values are `1h`, `6h`, `24h`, `7d`, and `30d`. This parameter is mutually exclusive with `startTime` and `endTime`.
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

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

