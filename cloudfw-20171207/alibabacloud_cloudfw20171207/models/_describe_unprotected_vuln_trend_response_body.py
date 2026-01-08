# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeUnprotectedVulnTrendResponseBody(DaraModel):
    def __init__(
        self,
        cur_protected_cnt: int = None,
        cur_unprotected_cnt: int = None,
        data_list: List[main_models.DescribeUnprotectedVulnTrendResponseBodyDataList] = None,
        end_time: int = None,
        interval: int = None,
        request_id: str = None,
        start_time: int = None,
    ):
        self.cur_protected_cnt = cur_protected_cnt
        self.cur_unprotected_cnt = cur_unprotected_cnt
        self.data_list = data_list
        self.end_time = end_time
        self.interval = interval
        self.request_id = request_id
        self.start_time = start_time

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
        if self.cur_protected_cnt is not None:
            result['CurProtectedCnt'] = self.cur_protected_cnt

        if self.cur_unprotected_cnt is not None:
            result['CurUnprotectedCnt'] = self.cur_unprotected_cnt

        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurProtectedCnt') is not None:
            self.cur_protected_cnt = m.get('CurProtectedCnt')

        if m.get('CurUnprotectedCnt') is not None:
            self.cur_unprotected_cnt = m.get('CurUnprotectedCnt')

        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeUnprotectedVulnTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeUnprotectedVulnTrendResponseBodyDataList(DaraModel):
    def __init__(
        self,
        protected_vuln_cnt: int = None,
        time: int = None,
        unprotected_vuln_cnt: int = None,
    ):
        self.protected_vuln_cnt = protected_vuln_cnt
        self.time = time
        self.unprotected_vuln_cnt = unprotected_vuln_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protected_vuln_cnt is not None:
            result['ProtectedVulnCnt'] = self.protected_vuln_cnt

        if self.time is not None:
            result['Time'] = self.time

        if self.unprotected_vuln_cnt is not None:
            result['UnprotectedVulnCnt'] = self.unprotected_vuln_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectedVulnCnt') is not None:
            self.protected_vuln_cnt = m.get('ProtectedVulnCnt')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('UnprotectedVulnCnt') is not None:
            self.unprotected_vuln_cnt = m.get('UnprotectedVulnCnt')

        return self

