# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeRtcUserCntDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_cnt_data_per_interval: main_models.DescribeRtcUserCntDataResponseBodyUserCntDataPerInterval = None,
    ):
        self.request_id = request_id
        self.user_cnt_data_per_interval = user_cnt_data_per_interval

    def validate(self):
        if self.user_cnt_data_per_interval:
            self.user_cnt_data_per_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_cnt_data_per_interval is not None:
            result['UserCntDataPerInterval'] = self.user_cnt_data_per_interval.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserCntDataPerInterval') is not None:
            temp_model = main_models.DescribeRtcUserCntDataResponseBodyUserCntDataPerInterval()
            self.user_cnt_data_per_interval = temp_model.from_map(m.get('UserCntDataPerInterval'))

        return self

class DescribeRtcUserCntDataResponseBodyUserCntDataPerInterval(DaraModel):
    def __init__(
        self,
        user_cnt_module: List[main_models.DescribeRtcUserCntDataResponseBodyUserCntDataPerIntervalUserCntModule] = None,
    ):
        self.user_cnt_module = user_cnt_module

    def validate(self):
        if self.user_cnt_module:
            for v1 in self.user_cnt_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserCntModule'] = []
        if self.user_cnt_module is not None:
            for k1 in self.user_cnt_module:
                result['UserCntModule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_cnt_module = []
        if m.get('UserCntModule') is not None:
            for k1 in m.get('UserCntModule'):
                temp_model = main_models.DescribeRtcUserCntDataResponseBodyUserCntDataPerIntervalUserCntModule()
                self.user_cnt_module.append(temp_model.from_map(k1))

        return self

class DescribeRtcUserCntDataResponseBodyUserCntDataPerIntervalUserCntModule(DaraModel):
    def __init__(
        self,
        active_user_cnt: int = None,
        time_stamp: str = None,
    ):
        self.active_user_cnt = active_user_cnt
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_user_cnt is not None:
            result['ActiveUserCnt'] = self.active_user_cnt

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveUserCnt') is not None:
            self.active_user_cnt = m.get('ActiveUserCnt')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

