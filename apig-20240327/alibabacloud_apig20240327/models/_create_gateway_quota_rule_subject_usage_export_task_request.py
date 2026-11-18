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
        # The optional token used for request idempotency. It can be up to 128 bytes in length after leading and trailing whitespaces are removed. We recommend that you use ASCII characters.
        # 
        # When the same user retries with the same token and identical request parameters in the current region, the existing task is reused and its current status is returned. If the same token corresponds to different parameters, a parameter error is returned. The compared parameters include gatewayId, ruleId, subjectId, filterFailedRequests, format, and whether startTime and endTime are passed and their values. Omitting the time is not equivalent to explicitly passing 0.
        # 
        # Reusing a task does not recalculate the time range or regenerate the file. When you need to re-export data (including when the original task fails or the file expires), use a new token.
        self.client_token = client_token
        # The end time of the export time range. Use a non-negative Unix timestamp in seconds. This time is exclusive.
        # 
        # If only endTime is specified, one rule period is deduced forward from this time as the startTime. If neither is specified, the end time is the task creation time. If both are specified, endTime must be greater than or equal to startTime, and the span cannot exceed one rule period.
        self.end_time = end_time
        # Specifies whether to export only consumption details with valid usage. Default value: false.
        # 
        # - false: Does not filter records by usage.
        # - true: Filters out records with zero usage based on the token or credit metering dimension of the rule, and retains only records with usage.
        self.filter_failed_requests = filter_failed_requests
        # The format of the exported file. Currently, only CSV_GZIP is supported. If omitted or an empty string is passed, this format is used by default. The file is a GZIP-compressed CSV file named `{taskId}.csv.gz` and must be decompressed before reading.
        self.format = format
        # The start time of the export time range. Use a non-negative Unix timestamp in seconds. This time is inclusive.
        # 
        # - If neither startTime nor endTime is specified: The start point of the current rule epoch to the node creation time is used.
        # - If only startTime is specified: One rule epoch is deduced backward from this time as the endTime.
        # - If both are specified: endTime must be greater than or equal to startTime, and the span cannot exceed one rule epoch.
        # 
        # The actual export start point is also limited by the rule creation time, rule reset, or the effective start point of purge history records. You can confirm this by querying the effectiveWindowStart returned by the node.
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

