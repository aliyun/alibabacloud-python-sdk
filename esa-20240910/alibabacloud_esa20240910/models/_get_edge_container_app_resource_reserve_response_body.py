# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetEdgeContainerAppResourceReserveResponseBody(DaraModel):
    def __init__(
        self,
        duration_time: str = None,
        enable: bool = None,
        forever: bool = None,
        request_id: str = None,
        reserve_set: List[main_models.GetEdgeContainerAppResourceReserveResponseBodyReserveSet] = None,
    ):
        self.duration_time = duration_time
        self.enable = enable
        self.forever = forever
        self.request_id = request_id
        self.reserve_set = reserve_set

    def validate(self):
        if self.reserve_set:
            for v1 in self.reserve_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration_time is not None:
            result['DurationTime'] = self.duration_time

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.forever is not None:
            result['Forever'] = self.forever

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ReserveSet'] = []
        if self.reserve_set is not None:
            for k1 in self.reserve_set:
                result['ReserveSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationTime') is not None:
            self.duration_time = m.get('DurationTime')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Forever') is not None:
            self.forever = m.get('Forever')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.reserve_set = []
        if m.get('ReserveSet') is not None:
            for k1 in m.get('ReserveSet'):
                temp_model = main_models.GetEdgeContainerAppResourceReserveResponseBodyReserveSet()
                self.reserve_set.append(temp_model.from_map(k1))

        return self

class GetEdgeContainerAppResourceReserveResponseBodyReserveSet(DaraModel):
    def __init__(
        self,
        isp: str = None,
        region: str = None,
        replicas: int = None,
    ):
        self.isp = isp
        self.region = region
        self.replicas = replicas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isp is not None:
            result['Isp'] = self.isp

        if self.region is not None:
            result['Region'] = self.region

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        return self

