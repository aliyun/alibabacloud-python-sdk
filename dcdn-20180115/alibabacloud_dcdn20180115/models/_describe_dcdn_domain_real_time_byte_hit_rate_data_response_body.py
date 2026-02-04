# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainRealTimeByteHitRateDataResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData = None,
        request_id: str = None,
    ):
        # The list of byte hit ratios.
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
            temp_model = main_models.DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyData(DaraModel):
    def __init__(
        self,
        byte_hit_rate_data_model: List[main_models.DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel] = None,
    ):
        self.byte_hit_rate_data_model = byte_hit_rate_data_model

    def validate(self):
        if self.byte_hit_rate_data_model:
            for v1 in self.byte_hit_rate_data_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ByteHitRateDataModel'] = []
        if self.byte_hit_rate_data_model is not None:
            for k1 in self.byte_hit_rate_data_model:
                result['ByteHitRateDataModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.byte_hit_rate_data_model = []
        if m.get('ByteHitRateDataModel') is not None:
            for k1 in m.get('ByteHitRateDataModel'):
                temp_model = main_models.DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel()
                self.byte_hit_rate_data_model.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel(DaraModel):
    def __init__(
        self,
        byte_hit_rate: float = None,
        time_stamp: str = None,
    ):
        # The byte hit ratio.
        self.byte_hit_rate = byte_hit_rate
        # The timestamp of the data returned. The time follows the ISO 8601 standard. The time is displayed in UTC.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.byte_hit_rate is not None:
            result['ByteHitRate'] = self.byte_hit_rate

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByteHitRate') is not None:
            self.byte_hit_rate = m.get('ByteHitRate')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

