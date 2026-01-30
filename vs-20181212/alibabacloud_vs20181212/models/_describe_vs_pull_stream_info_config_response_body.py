# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsPullStreamInfoConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_app_record_list: main_models.DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList = None,
        request_id: str = None,
    ):
        self.live_app_record_list = live_app_record_list
        self.request_id = request_id

    def validate(self):
        if self.live_app_record_list:
            self.live_app_record_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_app_record_list is not None:
            result['LiveAppRecordList'] = self.live_app_record_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveAppRecordList') is not None:
            temp_model = main_models.DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList()
            self.live_app_record_list = temp_model.from_map(m.get('LiveAppRecordList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList(DaraModel):
    def __init__(
        self,
        live_app_record: List[main_models.DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord] = None,
    ):
        self.live_app_record = live_app_record

    def validate(self):
        if self.live_app_record:
            for v1 in self.live_app_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveAppRecord'] = []
        if self.live_app_record is not None:
            for k1 in self.live_app_record:
                result['LiveAppRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_app_record = []
        if m.get('LiveAppRecord') is not None:
            for k1 in m.get('LiveAppRecord'):
                temp_model = main_models.DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord()
                self.live_app_record.append(temp_model.from_map(k1))

        return self

class DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        source_url: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        self.app_name = app_name
        self.domain_name = domain_name
        self.end_time = end_time
        self.source_url = source_url
        self.start_time = start_time
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.source_url is not None:
            result['SourceUrl'] = self.source_url

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

