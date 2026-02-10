# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIdcProbeScanResultListRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        current_page: int = None,
        found_end_time: int = None,
        found_start_time: int = None,
        logical_exp: str = None,
        page_size: int = None,
        status: str = None,
    ):
        # The search conditions for assets. This parameter is in the JSON format. The value is case-sensitive.
        # 
        # >  A search condition can be the instance ID, instance name, VPC ID, region, or public IP address. You can call the [DescribeIdcAssetCriteria](https://help.aliyun.com/document_detail/2842671.html) operation to query supported search conditions.
        self.criteria = criteria
        # The page number.
        self.current_page = current_page
        # The end time of the scan.
        self.found_end_time = found_end_time
        # The start time of the scan.
        self.found_start_time = found_start_time
        # The logical operator that combines multiple search conditions. Valid values:
        # 
        # *   **OR******
        # *   **AND******
        self.logical_exp = logical_exp
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The statuses of the corresponding probes. Separate multiple values with commas (,). Valid values:
        # 
        # *   **0**: The probe is valid.
        # *   **1**: The probe is ignored.
        # *   **2**: The probe is invalid.
        # *   **3**: The probe expired.
        # *   **4**: The probe does not exist.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.found_end_time is not None:
            result['FoundEndTime'] = self.found_end_time

        if self.found_start_time is not None:
            result['FoundStartTime'] = self.found_start_time

        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FoundEndTime') is not None:
            self.found_end_time = m.get('FoundEndTime')

        if m.get('FoundStartTime') is not None:
            self.found_start_time = m.get('FoundStartTime')

        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

