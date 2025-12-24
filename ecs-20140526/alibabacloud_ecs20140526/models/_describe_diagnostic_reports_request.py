# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDiagnosticReportsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        report_ids: List[str] = None,
        resource_ids: List[str] = None,
        severity: str = None,
        status: str = None,
    ):
        # The number of entries per page. Valid values: 1 to 100.
        # 
        # Default value:
        # 
        # *   If this parameter is left empty, the default value is 10.
        # *   If you set this parameter to a value that is greater than 100, the default value is 100.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of diagnostic reports.
        self.report_ids = report_ids
        # The IDs of resources. You can specify up to 100 resource IDs.
        self.resource_ids = resource_ids
        # The severity level of the diagnostic report. Valid values:
        # 
        # *   Unknown: The diagnostic did not start, failed to run, or unexpectedly exited without a diagnosis.
        # *   Normal: No exceptions were detected.
        # *   Info: Diagnostic information was recorded and may be related to exceptions.
        # *   Warn: Diagnostic information was recorded and may indicate exceptions.
        # *   Critical: Critical exceptions were detected.
        self.severity = severity
        # The status of the diagnostic report. Valid values:
        # 
        # *   InProgress
        # *   Failed
        # *   Finished
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

