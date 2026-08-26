# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamPushMetricDetailDataResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        next_page_token: str = None,
        page_size: int = None,
        request_id: str = None,
        start_time: str = None,
        stream_detail_data: main_models.DescribeLiveStreamPushMetricDetailDataResponseBodyStreamDetailData = None,
    ):
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range for the returned data. The time follows the ISO 8601 standard in the UTC time zone.
        # 
        # Format: YYYY-MM-DDThh:mm:ssZ.
        self.end_time = end_time
        # The paging query token. Each query returns a maximum of 5,000 rows of data. If the data to be queried exceeds 5,000 rows, the response includes the start index for the next query.
        # 
        # Pass this token in the request to continue querying data from the row after the last row returned in the previous query.
        self.next_page_token = next_page_token
        # The number of returned data rows.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the UTC time zone.
        # 
        # Format: YYYY-MM-DDThh:mm:ssZ.
        self.start_time = start_time
        self.stream_detail_data = stream_detail_data

    def validate(self):
        if self.stream_detail_data:
            self.stream_detail_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_detail_data is not None:
            result['StreamDetailData'] = self.stream_detail_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamDetailData') is not None:
            temp_model = main_models.DescribeLiveStreamPushMetricDetailDataResponseBodyStreamDetailData()
            self.stream_detail_data = temp_model.from_map(m.get('StreamDetailData'))

        return self

class DescribeLiveStreamPushMetricDetailDataResponseBodyStreamDetailData(DaraModel):
    def __init__(
        self,
        stream_data: List[main_models.DescribeLiveStreamPushMetricDetailDataResponseBodyStreamDetailDataStreamData] = None,
    ):
        self.stream_data = stream_data

    def validate(self):
        if self.stream_data:
            for v1 in self.stream_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StreamData'] = []
        if self.stream_data is not None:
            for k1 in self.stream_data:
                result['StreamData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream_data = []
        if m.get('StreamData') is not None:
            for k1 in m.get('StreamData'):
                temp_model = main_models.DescribeLiveStreamPushMetricDetailDataResponseBodyStreamDetailDataStreamData()
                self.stream_data.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamPushMetricDetailDataResponseBodyStreamDetailDataStreamData(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        req_bps: float = None,
        req_traffic: int = None,
        stream_name: str = None,
        time_stamp: str = None,
    ):
        self.app_name = app_name
        self.req_bps = req_bps
        self.req_traffic = req_traffic
        self.stream_name = stream_name
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.req_bps is not None:
            result['ReqBps'] = self.req_bps

        if self.req_traffic is not None:
            result['ReqTraffic'] = self.req_traffic

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ReqBps') is not None:
            self.req_bps = m.get('ReqBps')

        if m.get('ReqTraffic') is not None:
            self.req_traffic = m.get('ReqTraffic')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

