# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGatewayQuotaRuleSubjectUsageExportTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        end_time: int = None,
        filter_failed_requests: bool = None,
        format: str = None,
        start_time: int = None,
    ):
        self.client_token = client_token
        self.end_time = end_time
        self.filter_failed_requests = filter_failed_requests
        self.format = format
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.filter_failed_requests is not None:
            result['filterFailedRequests'] = self.filter_failed_requests

        if self.format is not None:
            result['format'] = self.format

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('filterFailedRequests') is not None:
            self.filter_failed_requests = m.get('filterFailedRequests')

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

