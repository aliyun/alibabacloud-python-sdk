# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeRTSNativeSDKPlayFailStatusResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        end_time: str = None,
        play_fail_status: List[main_models.DescribeRTSNativeSDKPlayFailStatusResponseBodyPlayFailStatus] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The time granularity.
        self.data_interval = data_interval
        # The end of the time range for which the data was queried.
        self.end_time = end_time
        # The number of error status codes at each interval.
        self.play_fail_status = play_fail_status
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range for which the data was queried.
        self.start_time = start_time

    def validate(self):
        if self.play_fail_status:
            for v1 in self.play_fail_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['PlayFailStatus'] = []
        if self.play_fail_status is not None:
            for k1 in self.play_fail_status:
                result['PlayFailStatus'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.play_fail_status = []
        if m.get('PlayFailStatus') is not None:
            for k1 in m.get('PlayFailStatus'):
                temp_model = main_models.DescribeRTSNativeSDKPlayFailStatusResponseBodyPlayFailStatus()
                self.play_fail_status.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeRTSNativeSDKPlayFailStatusResponseBodyPlayFailStatus(DaraModel):
    def __init__(
        self,
        time_stamp: str = None,
        v_20001: str = None,
        v_20002: str = None,
        v_20011: str = None,
        v_20012: str = None,
        v_20013: str = None,
        v_20052: str = None,
    ):
        # The timestamp of the returned data.
        self.time_stamp = time_stamp
        # The status code that indicates failed DNS resolution.
        self.v_20001 = v_20001
        # The status code that indicates failed authentication.
        self.v_20002 = v_20002
        # The status code that indicates a connection signaling timeout.
        self.v_20011 = v_20011
        # The status code that indicates a subscription signaling error.
        self.v_20012 = v_20012
        # The status code indicating that the stream to subscribe to does not exist.
        self.v_20013 = v_20013
        # The status code that indicates a media packet collection timeout.
        self.v_20052 = v_20052

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.v_20001 is not None:
            result['V20001'] = self.v_20001

        if self.v_20002 is not None:
            result['V20002'] = self.v_20002

        if self.v_20011 is not None:
            result['V20011'] = self.v_20011

        if self.v_20012 is not None:
            result['V20012'] = self.v_20012

        if self.v_20013 is not None:
            result['V20013'] = self.v_20013

        if self.v_20052 is not None:
            result['V20052'] = self.v_20052

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('V20001') is not None:
            self.v_20001 = m.get('V20001')

        if m.get('V20002') is not None:
            self.v_20002 = m.get('V20002')

        if m.get('V20011') is not None:
            self.v_20011 = m.get('V20011')

        if m.get('V20012') is not None:
            self.v_20012 = m.get('V20012')

        if m.get('V20013') is not None:
            self.v_20013 = m.get('V20013')

        if m.get('V20052') is not None:
            self.v_20052 = m.get('V20052')

        return self

