# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class UpdateEdgeContainerAppResourceReserveResponseBody(DaraModel):
    def __init__(
        self,
        duration_time: str = None,
        enable: bool = None,
        forever: bool = None,
        request_id: str = None,
        reserve_set: List[main_models.UpdateEdgeContainerAppResourceReserveResponseBodyReserveSet] = None,
    ):
        # The end time of the reservation. The input time is UTC. It takes +8 hours to enter Beijing time. For example, if the current time is 2006-01-02 06:04:05, you need to enter "2006-01-02T14:04:05Z".
        self.duration_time = duration_time
        # Whether to enable resource reservation.
        self.enable = enable
        # Enable Permanent Incremental Backup
        self.forever = forever
        # The request ID.
        self.request_id = request_id
        # Reserved resource list.
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
                temp_model = main_models.UpdateEdgeContainerAppResourceReserveResponseBodyReserveSet()
                self.reserve_set.append(temp_model.from_map(k1))

        return self

class UpdateEdgeContainerAppResourceReserveResponseBodyReserveSet(DaraModel):
    def __init__(
        self,
        isp: str = None,
        region: str = None,
        replicas: int = None,
    ):
        # The ISP. The following types are supported. You do not need to enter the ISP in regions outside the Chinese mainland:
        # 
        # *   China Mobile: cmcc
        # *   China Telecom: chinanet
        # *   China Unicom: unicom
        self.isp = isp
        # Information about the region. The Chinese mainland supports the input of regions and special administrative regions, and the regions outside the Chinese mainland support the input of countries. The following is the corresponding parameter mapping:
        # 
        # Chinese mainland:
        # 
        # *   East China: huadong
        # *   South China: huanan
        # *   Central China: huazhong
        # *   North China: huabei
        # *   Northwest China: xibei
        # *   Southwest China: xinan
        # *   Northeast China: dongbei
        # 
        # Special Administrative Regions and overseas:
        # 
        # *   Taiwan, China: tw
        # *   Macau, China: mo
        # *   Hong Kong, China: hk
        # *   Japan: jp
        # *   United States: us
        # *   Thailand: th
        # *   Korea: kr
        # *   Russia: ru
        # *   Singapore: sg
        # *   France: fr
        # *   Spain: es
        # *   Italy: it
        # *   Sweden: se
        # *   UAE: ae
        # *   Indonesia: id
        # *   Chile: cl
        # *   Philippines: ph
        # *   Malaysia: my
        # *   Vietnam: vn
        # *   Argentina: AR
        # *   Australia: au
        # *   Brazil: br
        # *   Colombia: co
        # *   Germany: de
        # *   UK: GB
        # *   Peru: pe
        # *   Saudi Arabia: sa
        # *   Netherlands: nl
        # *   South Africa: za
        self.region = region
        # The number of container replicas.
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

