# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagTrafficTopNResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_top_n: List[main_models.DescribeSagTrafficTopNResponseBodyTrafficTopN] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the data transfer rate of the SAG instance.
        self.traffic_top_n = traffic_top_n

    def validate(self):
        if self.traffic_top_n:
            for v1 in self.traffic_top_n:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TrafficTopN'] = []
        if self.traffic_top_n is not None:
            for k1 in self.traffic_top_n:
                result['TrafficTopN'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.traffic_top_n = []
        if m.get('TrafficTopN') is not None:
            for k1 in m.get('TrafficTopN'):
                temp_model = main_models.DescribeSagTrafficTopNResponseBodyTrafficTopN()
                self.traffic_top_n.append(temp_model.from_map(k1))

        return self

class DescribeSagTrafficTopNResponseBodyTrafficTopN(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        region_id: str = None,
        traffic_rate: str = None,
    ):
        # The ID of the SAG instance.
        self.instance_id = instance_id
        # The name of the SAG instance.
        self.name = name
        # The ID of the region where the SAG instance is deployed.
        self.region_id = region_id
        # The data transfer rate of the SAG instance. Unit: bit/s
        self.traffic_rate = traffic_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.traffic_rate is not None:
            result['TrafficRate'] = self.traffic_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TrafficRate') is not None:
            self.traffic_rate = m.get('TrafficRate')

        return self

