# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLivePullStreamConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_app_record_list: main_models.DescribeLivePullStreamConfigResponseBodyLiveAppRecordList = None,
        request_id: str = None,
    ):
        # Details about the stream pulling configurations.
        self.live_app_record_list = live_app_record_list
        # The ID of the request.
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
            temp_model = main_models.DescribeLivePullStreamConfigResponseBodyLiveAppRecordList()
            self.live_app_record_list = temp_model.from_map(m.get('LiveAppRecordList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLivePullStreamConfigResponseBodyLiveAppRecordList(DaraModel):
    def __init__(
        self,
        live_app_record: List[main_models.DescribeLivePullStreamConfigResponseBodyLiveAppRecordListLiveAppRecord] = None,
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
                temp_model = main_models.DescribeLivePullStreamConfigResponseBodyLiveAppRecordListLiveAppRecord()
                self.live_app_record.append(temp_model.from_map(k1))

        return self

class DescribeLivePullStreamConfigResponseBodyLiveAppRecordListLiveAppRecord(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        source_url: str = None,
        source_using: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The main streaming domain.
        self.domain_name = domain_name
        # The end of the time range for which the configurations were queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The origin server of the live stream.
        self.source_url = source_url
        # The live stream origin server that you are using.
        self.source_using = source_using
        # The beginning of the time range for which the configurations were queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time
        # The name of the live stream.
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

        if self.source_using is not None:
            result['SourceUsing'] = self.source_using

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

        if m.get('SourceUsing') is not None:
            self.source_using = m.get('SourceUsing')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

