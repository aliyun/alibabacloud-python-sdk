# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeACLProtectTrendResponseBody(DaraModel):
    def __init__(
        self,
        in_protect_cnt: int = None,
        inter_vpcprotect_cnt: int = None,
        interval: int = None,
        out_protect_cnt: int = None,
        request_id: str = None,
        total_protect_cnt: int = None,
        trend_list: List[main_models.DescribeACLProtectTrendResponseBodyTrendList] = None,
    ):
        # The number of internal requests that are blocked by the ACL feature.
        self.in_protect_cnt = in_protect_cnt
        # This parameter is deprecated.
        self.inter_vpcprotect_cnt = inter_vpcprotect_cnt
        # The interval for returning data. Unit: seconds.
        self.interval = interval
        # The number of external requests that are blocked by the ACL feature.
        self.out_protect_cnt = out_protect_cnt
        # The request ID.
        self.request_id = request_id
        # The total number of requests that are blocked by the ACL feature.
        self.total_protect_cnt = total_protect_cnt
        # The statistics on the requests that are blocked by the ACL feature.
        self.trend_list = trend_list

    def validate(self):
        if self.trend_list:
            for v1 in self.trend_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.in_protect_cnt is not None:
            result['InProtectCnt'] = self.in_protect_cnt

        if self.inter_vpcprotect_cnt is not None:
            result['InterVPCProtectCnt'] = self.inter_vpcprotect_cnt

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.out_protect_cnt is not None:
            result['OutProtectCnt'] = self.out_protect_cnt

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_protect_cnt is not None:
            result['TotalProtectCnt'] = self.total_protect_cnt

        result['TrendList'] = []
        if self.trend_list is not None:
            for k1 in self.trend_list:
                result['TrendList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InProtectCnt') is not None:
            self.in_protect_cnt = m.get('InProtectCnt')

        if m.get('InterVPCProtectCnt') is not None:
            self.inter_vpcprotect_cnt = m.get('InterVPCProtectCnt')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OutProtectCnt') is not None:
            self.out_protect_cnt = m.get('OutProtectCnt')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalProtectCnt') is not None:
            self.total_protect_cnt = m.get('TotalProtectCnt')

        self.trend_list = []
        if m.get('TrendList') is not None:
            for k1 in m.get('TrendList'):
                temp_model = main_models.DescribeACLProtectTrendResponseBodyTrendList()
                self.trend_list.append(temp_model.from_map(k1))

        return self

class DescribeACLProtectTrendResponseBodyTrendList(DaraModel):
    def __init__(
        self,
        protect_cnt: int = None,
        time: int = None,
    ):
        # The number of requests that are blocked by ACL on the current day.
        self.protect_cnt = protect_cnt
        # The UNIX timestamp at midnight (00:00:00) of each day, which indicates the date of the current day. Unit: seconds.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protect_cnt is not None:
            result['ProtectCnt'] = self.protect_cnt

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectCnt') is not None:
            self.protect_cnt = m.get('ProtectCnt')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

