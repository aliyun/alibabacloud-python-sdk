# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDiagnoseReportRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        diagnose_type: str = None,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        report_ids: List[str] = None,
        resource_ids: List[str] = None,
        start_time: str = None,
        status: str = None,
    ):
        self.client_token = client_token
        self.diagnose_type = diagnose_type
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.report_ids = report_ids
        self.resource_ids = resource_ids
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.diagnose_type is not None:
            result['DiagnoseType'] = self.diagnose_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DiagnoseType') is not None:
            self.diagnose_type = m.get('DiagnoseType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

