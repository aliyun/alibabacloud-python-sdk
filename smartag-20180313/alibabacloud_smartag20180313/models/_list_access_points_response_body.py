# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class ListAccessPointsResponseBody(DaraModel):
    def __init__(
        self,
        access_points: List[main_models.ListAccessPointsResponseBodyAccessPoints] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the access point.
        self.access_points = access_points
        # The ID of the request.
        self.request_id = request_id
        # The total number of access points.
        self.total_count = total_count

    def validate(self):
        if self.access_points:
            for v1 in self.access_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessPoints'] = []
        if self.access_points is not None:
            for k1 in self.access_points:
                result['AccessPoints'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_points = []
        if m.get('AccessPoints') is not None:
            for k1 in m.get('AccessPoints'):
                temp_model = main_models.ListAccessPointsResponseBodyAccessPoints()
                self.access_points.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAccessPointsResponseBodyAccessPoints(DaraModel):
    def __init__(
        self,
        access_point_id: int = None,
        active_smart_agcount: int = None,
        inactive_smart_agcount: int = None,
        latitude: str = None,
        longitude: str = None,
    ):
        # The ID of the access point.
        self.access_point_id = access_point_id
        # The number of available SAG instances in the access point.
        self.active_smart_agcount = active_smart_agcount
        # The number of offline SAG instances in the access point.
        self.inactive_smart_agcount = inactive_smart_agcount
        # The latitude of the access point.
        self.latitude = latitude
        # The longitude of the access point.
        self.longitude = longitude

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.active_smart_agcount is not None:
            result['ActiveSmartAGCount'] = self.active_smart_agcount

        if self.inactive_smart_agcount is not None:
            result['InactiveSmartAGCount'] = self.inactive_smart_agcount

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('ActiveSmartAGCount') is not None:
            self.active_smart_agcount = m.get('ActiveSmartAGCount')

        if m.get('InactiveSmartAGCount') is not None:
            self.inactive_smart_agcount = m.get('InactiveSmartAGCount')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        return self

