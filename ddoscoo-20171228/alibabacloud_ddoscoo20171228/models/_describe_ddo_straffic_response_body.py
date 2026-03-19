# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeDDoSTrafficResponseBody(DaraModel):
    def __init__(
        self,
        ddo_straffic_points: List[main_models.DescribeDDoSTrafficResponseBodyDDoSTrafficPoints] = None,
        defense_in_bytes: int = None,
        request_id: str = None,
        source_in_bytes: int = None,
    ):
        self.ddo_straffic_points = ddo_straffic_points
        self.defense_in_bytes = defense_in_bytes
        self.request_id = request_id
        self.source_in_bytes = source_in_bytes

    def validate(self):
        if self.ddo_straffic_points:
            for v1 in self.ddo_straffic_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DDoSTrafficPoints'] = []
        if self.ddo_straffic_points is not None:
            for k1 in self.ddo_straffic_points:
                result['DDoSTrafficPoints'].append(k1.to_map() if k1 else None)

        if self.defense_in_bytes is not None:
            result['DefenseInBytes'] = self.defense_in_bytes

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_in_bytes is not None:
            result['SourceInBytes'] = self.source_in_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ddo_straffic_points = []
        if m.get('DDoSTrafficPoints') is not None:
            for k1 in m.get('DDoSTrafficPoints'):
                temp_model = main_models.DescribeDDoSTrafficResponseBodyDDoSTrafficPoints()
                self.ddo_straffic_points.append(temp_model.from_map(k1))

        if m.get('DefenseInBytes') is not None:
            self.defense_in_bytes = m.get('DefenseInBytes')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceInBytes') is not None:
            self.source_in_bytes = m.get('SourceInBytes')

        return self

class DescribeDDoSTrafficResponseBodyDDoSTrafficPoints(DaraModel):
    def __init__(
        self,
        defense_max_in_bps: int = None,
        source_max_in_bps: int = None,
        time: int = None,
    ):
        self.defense_max_in_bps = defense_max_in_bps
        self.source_max_in_bps = source_max_in_bps
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_max_in_bps is not None:
            result['DefenseMaxInBps'] = self.defense_max_in_bps

        if self.source_max_in_bps is not None:
            result['SourceMaxInBps'] = self.source_max_in_bps

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseMaxInBps') is not None:
            self.defense_max_in_bps = m.get('DefenseMaxInBps')

        if m.get('SourceMaxInBps') is not None:
            self.source_max_in_bps = m.get('SourceMaxInBps')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

