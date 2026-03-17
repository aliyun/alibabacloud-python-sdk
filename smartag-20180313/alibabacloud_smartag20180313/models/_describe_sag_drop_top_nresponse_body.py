# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagDropTopNResponseBody(DaraModel):
    def __init__(
        self,
        drop_top_n: List[main_models.DescribeSagDropTopNResponseBodyDropTopN] = None,
        request_id: str = None,
    ):
        # The information about packets dropped by the SAG instance.
        self.drop_top_n = drop_top_n
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.drop_top_n:
            for v1 in self.drop_top_n:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DropTopN'] = []
        if self.drop_top_n is not None:
            for k1 in self.drop_top_n:
                result['DropTopN'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.drop_top_n = []
        if m.get('DropTopN') is not None:
            for k1 in m.get('DropTopN'):
                temp_model = main_models.DescribeSagDropTopNResponseBodyDropTopN()
                self.drop_top_n.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSagDropTopNResponseBodyDropTopN(DaraModel):
    def __init__(
        self,
        drop_rate: str = None,
        instance_id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The packet loss rate of the SAG instance. Unit: packets per second (PPS).
        self.drop_rate = drop_rate
        # The ID of the SAG instance.
        self.instance_id = instance_id
        # The name of the SAG instance.
        self.name = name
        # The ID of the region where the SAG instance is deployed.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drop_rate is not None:
            result['DropRate'] = self.drop_rate

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DropRate') is not None:
            self.drop_rate = m.get('DropRate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

