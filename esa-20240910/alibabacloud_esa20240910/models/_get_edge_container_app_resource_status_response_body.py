# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetEdgeContainerAppResourceStatusResponseBody(DaraModel):
    def __init__(
        self,
        regions: List[main_models.GetEdgeContainerAppResourceStatusResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # Queries the regions of deployment.
        self.regions = regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for v1 in self.regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['Regions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k1 in m.get('Regions'):
                temp_model = main_models.GetEdgeContainerAppResourceStatusResponseBodyRegions()
                self.regions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetEdgeContainerAppResourceStatusResponseBodyRegions(DaraModel):
    def __init__(
        self,
        is_offline: bool = None,
        is_staging: bool = None,
        isp: str = None,
        ready: int = None,
        region: str = None,
        total: int = None,
    ):
        # Whether smooth offline is being used.
        self.is_offline = is_offline
        # Whether it is a test environment.
        self.is_staging = is_staging
        # Supported ISPs are as follows. The parameter is left empty for regions outside the Chinese mainland. ISP:
        # 
        # *   China Mobile: cmcc
        # *   China Telecom: chinanet
        # *   China Unicom: unicom
        self.isp = isp
        # The number of ready replicas.
        self.ready = ready
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
        # Special Administrative Regions and Overseas:
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
        # The number of replicas that are deployed.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_offline is not None:
            result['IsOffline'] = self.is_offline

        if self.is_staging is not None:
            result['IsStaging'] = self.is_staging

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.ready is not None:
            result['Ready'] = self.ready

        if self.region is not None:
            result['Region'] = self.region

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsOffline') is not None:
            self.is_offline = m.get('IsOffline')

        if m.get('IsStaging') is not None:
            self.is_staging = m.get('IsStaging')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Ready') is not None:
            self.ready = m.get('Ready')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

