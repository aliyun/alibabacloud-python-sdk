# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGatewayQuotaRuleSubjectUsageRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        filter_failed_requests: bool = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # The end time for querying consumption record details, in UNIX timestamp format (seconds). If only this parameter is specified, the system automatically calculates startTime based on the rule cycle.
        self.end_time = end_time
        # Specifies whether to filter out zero values.
        self.filter_failed_requests = filter_failed_requests
        # The page number of the detailed consumption (request) records of the subject within the cycle.
        self.page_number = page_number
        # The number of detailed consumption (request) records per page for the subject within the cycle. Maximum value: 10.
        self.page_size = page_size
        # The start time for querying consumption record details, in UNIX timestamp format (seconds). If only this parameter is specified, the system automatically calculates endTime based on the rule cycle.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.filter_failed_requests is not None:
            result['filterFailedRequests'] = self.filter_failed_requests

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('filterFailedRequests') is not None:
            self.filter_failed_requests = m.get('filterFailedRequests')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

