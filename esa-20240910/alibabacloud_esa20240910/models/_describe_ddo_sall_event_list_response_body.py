# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeDDoSAllEventListResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeDDoSAllEventListResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        site_id: int = None,
        total_count: int = None,
    ):
        # The DDoS attack events.
        self.data_list = data_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The website ID.
        self.site_id = site_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeDDoSAllEventListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDDoSAllEventListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        bps: int = None,
        coverage: str = None,
        cps: int = None,
        end_time: str = None,
        event_id: str = None,
        event_result: str = None,
        event_type: str = None,
        pps: int = None,
        qps: int = None,
        start_time: str = None,
        target: str = None,
        target_id: str = None,
    ):
        # The peak of volumetric attacks. Unit: bit/s.
        self.bps = bps
        self.coverage = coverage
        # The peak of connection flood attacks. Unit: connections per seconds (CPS).
        self.cps = cps
        # The time when the DDoS attack ends.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The attack event ID.
        self.event_id = event_id
        self.event_result = event_result
        # The type of DDoS attacks that was queried. Valid values:
        # 
        # *   **web-cc**: web resource exhaustion attacks.
        # *   **cc**: connection flood attacks.
        # *   **traffic**: volumetric attacks.
        self.event_type = event_type
        # The peak of volumetric attacks. Unit: packets per second (PPS).
        self.pps = pps
        # The peak QPS of web resource exhaustion attacks.
        self.qps = qps
        # The time when the DDoS attack starts.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The attack target.
        self.target = target
        # The ID of the web resource exhaustion attack target.
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps is not None:
            result['Bps'] = self.bps

        if self.coverage is not None:
            result['Coverage'] = self.coverage

        if self.cps is not None:
            result['Cps'] = self.cps

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_result is not None:
            result['EventResult'] = self.event_result

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.pps is not None:
            result['Pps'] = self.pps

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.target is not None:
            result['Target'] = self.target

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventResult') is not None:
            self.event_result = m.get('EventResult')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        return self

