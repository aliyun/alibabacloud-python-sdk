# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class GetNetworkAvailableZonesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetNetworkAvailableZonesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            temp_model = main_models.GetNetworkAvailableZonesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNetworkAvailableZonesResponseBodyData(DaraModel):
    def __init__(
        self,
        region_id_list: List[str] = None,
        zone_id_list: List[str] = None,
    ):
        self.region_id_list = region_id_list
        self.zone_id_list = zone_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id_list is not None:
            result['RegionIdList'] = self.region_id_list

        if self.zone_id_list is not None:
            result['ZoneIdList'] = self.zone_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionIdList') is not None:
            self.region_id_list = m.get('RegionIdList')

        if m.get('ZoneIdList') is not None:
            self.zone_id_list = m.get('ZoneIdList')

        return self

