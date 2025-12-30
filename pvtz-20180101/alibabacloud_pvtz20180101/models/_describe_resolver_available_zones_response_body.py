# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeResolverAvailableZonesResponseBody(DaraModel):
    def __init__(
        self,
        available_zones: List[main_models.DescribeResolverAvailableZonesResponseBodyAvailableZones] = None,
        request_id: str = None,
    ):
        # The queried zones.
        self.available_zones = available_zones
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.available_zones:
            for v1 in self.available_zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableZones'] = []
        if self.available_zones is not None:
            for k1 in self.available_zones:
                result['AvailableZones'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zones = []
        if m.get('AvailableZones') is not None:
            for k1 in m.get('AvailableZones'):
                temp_model = main_models.DescribeResolverAvailableZonesResponseBodyAvailableZones()
                self.available_zones.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeResolverAvailableZonesResponseBodyAvailableZones(DaraModel):
    def __init__(
        self,
        az_id: str = None,
        status: str = None,
    ):
        # The zone ID.
        self.az_id = az_id
        # The state of resources in the zone. Valid values:
        # 
        # *   NORMAL: The resources are in the normal state.
        # *   SOLD_OUT: The resources are sold out.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.az_id is not None:
            result['AzId'] = self.az_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzId') is not None:
            self.az_id = m.get('AzId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

