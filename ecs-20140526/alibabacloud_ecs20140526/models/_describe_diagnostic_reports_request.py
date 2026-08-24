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
        # The maximum number of entries per page for paging. Maximum value: 100.
        # 
        # Default value:
        # 
        # - If this parameter is not set, the default value is 10.
        # - If the value you set is greater than 100, the default value is 100.
        self.max_results = max_results
        # The pagination token. Set this parameter to the `NextToken` value returned in the previous call. You do not need to set this parameter for the first request.
        self.next_token = next_token
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of diagnostic report IDs.
        self.report_ids = report_ids
        # The list of resource IDs. A maximum of 100 IDs are supported.
        self.resource_ids = resource_ids
        # The severity level. Valid values:
        # 
        # - Unknown: The initial state, which indicates that the diagnosis has not started or the diagnosis process exited abnormally. No diagnostic conclusion is available.
        # - Normal: The diagnosis is normal and no issues are found.
        # - Info: Related information is available and may be associated with an exception.
        # - Warn: Related information is available and may cause an exception.
        # - Critical: A critical exception exists.
        self.severity = severity
        # The report status. Valid values:
        # 
        # - InProgress: The diagnosis is in progress.
        # - Failed: The diagnosis failed.
        # - Finished: The diagnosis is complete.
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

