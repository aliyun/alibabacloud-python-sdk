# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ListMigrationZonesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        zone_list: List[main_models.ListMigrationZonesResponseBodyZoneList] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.zone_list = zone_list

    def validate(self):
        if self.zone_list:
            for v1 in self.zone_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['zoneList'] = []
        if self.zone_list is not None:
            for k1 in self.zone_list:
                result['zoneList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.zone_list = []
        if m.get('zoneList') is not None:
            for k1 in m.get('zoneList'):
                temp_model = main_models.ListMigrationZonesResponseBodyZoneList()
                self.zone_list.append(temp_model.from_map(k1))

        return self

class ListMigrationZonesResponseBodyZoneList(DaraModel):
    def __init__(
        self,
        available: bool = None,
        zone_id: str = None,
    ):
        self.available = available
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['available'] = self.available

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('available') is not None:
            self.available = m.get('available')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

