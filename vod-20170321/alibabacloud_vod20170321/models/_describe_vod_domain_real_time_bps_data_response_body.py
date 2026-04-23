# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodDomainRealTimeBpsDataResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeVodDomainRealTimeBpsDataResponseBodyData = None,
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
            temp_model = main_models.DescribeVodDomainRealTimeBpsDataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVodDomainRealTimeBpsDataResponseBodyData(DaraModel):
    def __init__(
        self,
        bps_model: List[main_models.DescribeVodDomainRealTimeBpsDataResponseBodyDataBpsModel] = None,
    ):
        self.bps_model = bps_model

    def validate(self):
        if self.bps_model:
            for v1 in self.bps_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BpsModel'] = []
        if self.bps_model is not None:
            for k1 in self.bps_model:
                result['BpsModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bps_model = []
        if m.get('BpsModel') is not None:
            for k1 in m.get('BpsModel'):
                temp_model = main_models.DescribeVodDomainRealTimeBpsDataResponseBodyDataBpsModel()
                self.bps_model.append(temp_model.from_map(k1))

        return self

class DescribeVodDomainRealTimeBpsDataResponseBodyDataBpsModel(DaraModel):
    def __init__(
        self,
        bps: float = None,
        time_stamp: str = None,
    ):
        self.bps = bps
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps is not None:
            result['Bps'] = self.bps

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

