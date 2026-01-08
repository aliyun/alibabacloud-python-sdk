# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeSdlEventDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sdl_event_detail_list: List[main_models.DescribeSdlEventDetailResponseBodySdlEventDetailList] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.sdl_event_detail_list = sdl_event_detail_list
        self.total_count = total_count

    def validate(self):
        if self.sdl_event_detail_list:
            for v1 in self.sdl_event_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SdlEventDetailList'] = []
        if self.sdl_event_detail_list is not None:
            for k1 in self.sdl_event_detail_list:
                result['SdlEventDetailList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sdl_event_detail_list = []
        if m.get('SdlEventDetailList') is not None:
            for k1 in m.get('SdlEventDetailList'):
                temp_model = main_models.DescribeSdlEventDetailResponseBodySdlEventDetailList()
                self.sdl_event_detail_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSdlEventDetailResponseBodySdlEventDetailList(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        sensitive_data_cnt: int = None,
        sensitive_level: str = None,
        sensitive_type: str = None,
        start_time: int = None,
    ):
        self.event_name = event_name
        self.sensitive_data_cnt = sensitive_data_cnt
        self.sensitive_level = sensitive_level
        self.sensitive_type = sensitive_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.sensitive_data_cnt is not None:
            result['SensitiveDataCnt'] = self.sensitive_data_cnt

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        if self.sensitive_type is not None:
            result['SensitiveType'] = self.sensitive_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('SensitiveDataCnt') is not None:
            self.sensitive_data_cnt = m.get('SensitiveDataCnt')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        if m.get('SensitiveType') is not None:
            self.sensitive_type = m.get('SensitiveType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

