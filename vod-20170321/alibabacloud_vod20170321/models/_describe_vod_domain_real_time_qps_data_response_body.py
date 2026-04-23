# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodDomainRealTimeQpsDataResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeVodDomainRealTimeQpsDataResponseBodyData = None,
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
            temp_model = main_models.DescribeVodDomainRealTimeQpsDataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVodDomainRealTimeQpsDataResponseBodyData(DaraModel):
    def __init__(
        self,
        qps_model: List[main_models.DescribeVodDomainRealTimeQpsDataResponseBodyDataQpsModel] = None,
    ):
        self.qps_model = qps_model

    def validate(self):
        if self.qps_model:
            for v1 in self.qps_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QpsModel'] = []
        if self.qps_model is not None:
            for k1 in self.qps_model:
                result['QpsModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.qps_model = []
        if m.get('QpsModel') is not None:
            for k1 in m.get('QpsModel'):
                temp_model = main_models.DescribeVodDomainRealTimeQpsDataResponseBodyDataQpsModel()
                self.qps_model.append(temp_model.from_map(k1))

        return self

class DescribeVodDomainRealTimeQpsDataResponseBodyDataQpsModel(DaraModel):
    def __init__(
        self,
        qps: float = None,
        time_stamp: str = None,
    ):
        self.qps = qps
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.qps is not None:
            result['Qps'] = self.qps

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

