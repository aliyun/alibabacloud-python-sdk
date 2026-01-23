# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRepoTagScanSummaryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        high_severity: int = None,
        is_success: bool = None,
        low_severity: int = None,
        medium_severity: int = None,
        request_id: str = None,
        total_severity: int = None,
        unknown_severity: int = None,
    ):
        # The number of medium-severity vulnerabilities.
        self.code = code
        # The number of low-severity vulnerabilities.
        self.high_severity = high_severity
        # The number of high-severity vulnerabilities.
        self.is_success = is_success
        self.low_severity = low_severity
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.medium_severity = medium_severity
        # The total number of vulnerabilities detected on images.
        self.request_id = request_id
        # The return value.
        self.total_severity = total_severity
        # The ID of the request.
        self.unknown_severity = unknown_severity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.high_severity is not None:
            result['HighSeverity'] = self.high_severity

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.low_severity is not None:
            result['LowSeverity'] = self.low_severity

        if self.medium_severity is not None:
            result['MediumSeverity'] = self.medium_severity

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_severity is not None:
            result['TotalSeverity'] = self.total_severity

        if self.unknown_severity is not None:
            result['UnknownSeverity'] = self.unknown_severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HighSeverity') is not None:
            self.high_severity = m.get('HighSeverity')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('LowSeverity') is not None:
            self.low_severity = m.get('LowSeverity')

        if m.get('MediumSeverity') is not None:
            self.medium_severity = m.get('MediumSeverity')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalSeverity') is not None:
            self.total_severity = m.get('TotalSeverity')

        if m.get('UnknownSeverity') is not None:
            self.unknown_severity = m.get('UnknownSeverity')

        return self

