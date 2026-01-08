# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeSdlEventSdListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sdl_event_sensitive_data_list: List[main_models.DescribeSdlEventSdListResponseBodySdlEventSensitiveDataList] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.sdl_event_sensitive_data_list = sdl_event_sensitive_data_list
        self.total_count = total_count

    def validate(self):
        if self.sdl_event_sensitive_data_list:
            for v1 in self.sdl_event_sensitive_data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SdlEventSensitiveDataList'] = []
        if self.sdl_event_sensitive_data_list is not None:
            for k1 in self.sdl_event_sensitive_data_list:
                result['SdlEventSensitiveDataList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sdl_event_sensitive_data_list = []
        if m.get('SdlEventSensitiveDataList') is not None:
            for k1 in m.get('SdlEventSensitiveDataList'):
                temp_model = main_models.DescribeSdlEventSdListResponseBodySdlEventSensitiveDataList()
                self.sdl_event_sensitive_data_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSdlEventSdListResponseBodySdlEventSensitiveDataList(DaraModel):
    def __init__(
        self,
        sensitive_data: str = None,
        sensitive_data_cnt: int = None,
        sensitive_level: str = None,
        sensitive_type: str = None,
        src_ip: str = None,
        start_time: int = None,
    ):
        self.sensitive_data = sensitive_data
        self.sensitive_data_cnt = sensitive_data_cnt
        self.sensitive_level = sensitive_level
        self.sensitive_type = sensitive_type
        self.src_ip = src_ip
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sensitive_data is not None:
            result['SensitiveData'] = self.sensitive_data

        if self.sensitive_data_cnt is not None:
            result['SensitiveDataCnt'] = self.sensitive_data_cnt

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        if self.sensitive_type is not None:
            result['SensitiveType'] = self.sensitive_type

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SensitiveData') is not None:
            self.sensitive_data = m.get('SensitiveData')

        if m.get('SensitiveDataCnt') is not None:
            self.sensitive_data_cnt = m.get('SensitiveDataCnt')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        if m.get('SensitiveType') is not None:
            self.sensitive_type = m.get('SensitiveType')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

