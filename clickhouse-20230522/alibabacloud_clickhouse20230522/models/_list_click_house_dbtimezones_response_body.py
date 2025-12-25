# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class ListClickHouseDBTimezonesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        time_zones: List[main_models.ListClickHouseDBTimezonesResponseBodyTimeZones] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.time_zones = time_zones

    def validate(self):
        if self.time_zones:
            for v1 in self.time_zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TimeZones'] = []
        if self.time_zones is not None:
            for k1 in self.time_zones:
                result['TimeZones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.time_zones = []
        if m.get('TimeZones') is not None:
            for k1 in m.get('TimeZones'):
                temp_model = main_models.ListClickHouseDBTimezonesResponseBodyTimeZones()
                self.time_zones.append(temp_model.from_map(k1))

        return self

class ListClickHouseDBTimezonesResponseBodyTimeZones(DaraModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

