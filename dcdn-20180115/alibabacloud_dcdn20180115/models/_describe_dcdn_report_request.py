# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnReportRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        domain_name: str = None,
        end_time: str = None,
        http_code: str = None,
        is_overseas: str = None,
        report_id: int = None,
        start_time: str = None,
    ):
        # The region. You can call the [DescribeDcdnRegionAndIsp](https://help.aliyun.com/document_detail/207199.html) operation to query regions.
        # 
        # *   If you do not specify a region, data in all regions is queried.
        # *   If you specify a region, data in the specified region is returned. You can specify one or more regions. Separate regions with commas (,).
        self.area = area
        # The domain names that you want to query. Separate domain names with commas (,).
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: HTTP 2xx status codes
        # *   **3xx**: HTTP 3xx status codes
        # *   **4xx**: HTTP 4xx status codes
        # *   **5xx**: HTTP 5xx status codes
        # 
        # If you do not specify an HTTP status code, data for all preceding HTTP status codes is queried.
        self.http_code = http_code
        # Specify whether the region is outside the Chinese mainland. Valid values:
        # 
        # *   **1**: outside the Chinese mainland
        # *   **0**: inside the Chinese mainland
        self.is_overseas = is_overseas
        # The ID of the operations report that you want to query. You can enter only one ID in each call. You can call the [DescribeDcdnSubList](https://help.aliyun.com/document_detail/270075.html) operation to query report IDs.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.is_overseas is not None:
            result['IsOverseas'] = self.is_overseas

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('IsOverseas') is not None:
            self.is_overseas = m.get('IsOverseas')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

