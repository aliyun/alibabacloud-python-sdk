# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodDomainRealTimeReqHitRateDataResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeVodDomainRealTimeReqHitRateDataResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeVodDomainRealTimeReqHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVodDomainRealTimeReqHitRateDataResponseBodyData(DaraModel):
    def __init__(
        self,
        req_hit_rate_data_model: List[main_models.DescribeVodDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel] = None,
    ):
        self.req_hit_rate_data_model = req_hit_rate_data_model

    def validate(self):
        if self.req_hit_rate_data_model:
            for v1 in self.req_hit_rate_data_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReqHitRateDataModel'] = []
        if self.req_hit_rate_data_model is not None:
            for k1 in self.req_hit_rate_data_model:
                result['ReqHitRateDataModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.req_hit_rate_data_model = []
        if m.get('ReqHitRateDataModel') is not None:
            for k1 in m.get('ReqHitRateDataModel'):
                temp_model = main_models.DescribeVodDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel()
                self.req_hit_rate_data_model.append(temp_model.from_map(k1))

        return self

class DescribeVodDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel(DaraModel):
    def __init__(
        self,
        req_hit_rate: float = None,
        time_stamp: str = None,
    ):
        self.req_hit_rate = req_hit_rate
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.req_hit_rate is not None:
            result['ReqHitRate'] = self.req_hit_rate

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqHitRate') is not None:
            self.req_hit_rate = m.get('ReqHitRate')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

